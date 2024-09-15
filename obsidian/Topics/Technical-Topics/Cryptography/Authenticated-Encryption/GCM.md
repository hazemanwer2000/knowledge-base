──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*Galois/Counter Mode (GCM)* is an *AEAD* mode of operation of symmetric-key, block-cipher algorithm(s), specified in [1].

*Note:* The underlying block-cipher algorithm must have a block-size, `B`, of 128-bits (e.g., AES), and a key-size of at least 128-bits.
### Primitive(s)
---
#### Generic Primitive(s)
---
##### `LEN`
---
Let `LEN(X)` be a function, with bit-string `X` as input, it shall yield the length of `X` in bit(s). 
##### `MSB`
---
Let `MSB(X, N)` be a function, with `X` bit-string and `N` integer as input, it shall yield the most-significant `N` bit(s) of `X`.
##### `LSB`
---
Let `LSB(X, N)` be a function, with `X` bit-string and `N` integer as input, it shall yield the least-significant `N` bit(s) of `X`.
##### `CONCAT`
---
Let `CONCAT(X, ...)` be a function, with an arbitrary number of bit-string(s) as input, it shall yield the concatenation of all input bit-string(s).
##### `CEIL`
---
Let `CEIL(X)` be a function, with `X` floating value as input, it round-up `X`, to the next integer value, and yield that value. 
##### `ZPAD`
---
Let `ZPAD(X, B)` be a function, with `X` bit-string and `B` integer as input, it shall zero-pad `X`, until its length is a multiple of `B`, and yield that value.
##### `BITSTR`
---
Let `BITSTR(I, S)` be a function, with `I` value and `B` integer(s) as input, it shall assert `I` as a bit-string of size `S`.
#### `INC`
---
Let `INC(X, S)` be a function, with input(s),
* `X` - Bit-string
* `S` - Integer, where `S <= LEN(X)`

And output(s),
* `X'` - Bit-string, where `LEN(X) == LEN(X')` 

Then, it shall be defined as,
```
A = MSB(X, LEN(X) - S)
B = (LSB(X, S) + 1) MOD (2^S)

X' = CONCAT(A, B)
```
#### `MUL`
---
Let `MUL(X, Y)` be a function, with input(s),
* `X` - Bit-string, where `LEN(X) == B`
* `Y` - Bit-string, where `LEN(Y) == B`

And output(s),
* `W` - Bit-string, where `LEN(W) == B`

Then, it shall be defined as,
```
R' = 0b11100001
R = R' << (B - LEN(R'))

Z(0) = 0
V(0) = Y

FOR i FROM 0 TO (B-1) DO
	IF BIT(X, i) == 0
		Z(i+1) = Z(i)
	ELSE
		Z(i+1) = Z(i) XOR V(i)
		
	IF BIT(V(i), 0) == 0
		V(i+1) = V(i) >> 1
	ELSE
		V(i+1) = (V(I) >> 1) XOR R

W = Z(B)
```
#### `GHASH`
---
Let `GHASH(X, H)` be a function, with input(s),
* `X` - Bit-string, where `LEN(X)` is a multiple of `B`
* `H` - Bit-string, where `LEN(H) == B`

And output(s),
* `W` - Bit-string, where `LEN(W) == B`

Then, it shall be defined as,
```
N = LEN(X)/B

Y(0) = 0

FOR i FROM 0 TO (N-1):
	Y(i+1) = MUL(Y(i) XOR X(i), H)

W = Y(B)
```

Its definition may be visualized, as shown below.

![[GCM-GHASH.png|350]]``
#### `GCTR`
---
Let `GCTR(X, K, IV)` be a function, with input(s),
* `X` - Bit-string, of arbitrary length
* `K` - Cipher-Key
* `IV` - Bit-string, where `LEN(IV) == B`

And output(s),
* `X'` - Bit-string, where `LEN(X') == LEN(X)`

Then, it shall be defined as,
```
N = CEIL(LEN(X)/B)

	# Constructing the counter.

C(0) = IV

FOR i FROM 1 TO (N-1):
	C(i) = INC(C(i-1), 32)

	# Encrypting the payload.

FOR i FROM 0 TO (N-2):
	X'(i) = X(i) XOR CIPH(K, C(i))

X'(N-1) = X(N-1) XOR MSB(
	CIPH(K, C(N-1)),
	LEN(X(N-1))
)
```
### The Algorithm
---
#### `GCM`
---
Let `GCM(X, A, K, IV, TLEN)` be a function, with input(s),
* `X` - Bit-string (confidential), of arbitrary length
* `A` - Bit-string (non-confidential), of arbitrary length
* `K` - Cipher-key
* `IV` - Bit-string, of arbitrary length
* `TLEN` - *MAC* Truncation Length, where `TLEN <= B`

And output(s),
* `X'` - Bit-string, where `LEN(X') == LEN(X)`
* `T` - Bit-string (*MAC*), where `LEN(T) == TLEN`

Then, it shall be defined as,
```
H = CIPH(K, 0)

	# Encrypting the (confidential) data.

IF LEN(IV) == 96
	J = CONCAT(IV, BITSTR(1, 32))
ELSE
	J = GHASH(CONCAT(
		ZPAD(IV, B),
		BITSTR(LEN(IV), B)
	), H)

C = GCTR(X, K, INC(J, 32))

	# Calculating the MAC.

S = GHASH(CONCAT(
	ZPAD(A, B),
	ZPAD(C, B),
	BITSTR(LEN(A), B/2),
	BITSTR(LEN(C), B/2)
), H)

T = MSB(GCTR(S, J), TLEN)
```
## References
---
[1] Galois/Counter Mode (GCM) and GMAC, SP 800-38D, NIST.