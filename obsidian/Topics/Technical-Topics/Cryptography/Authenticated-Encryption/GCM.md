──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*Galois/Counter Mode (GCM)* is an *AEAD* mode of operation of symmetric-key, block-cipher algorithm(s), specified in [1].

*Note:* The underlying block-cipher algorithm must have a block-size, `B`, of 128-bits (e.g., AES), and a key-size of at least 128-bits.
### Primitive(s)
---
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
Y(0) = 0

FOR i FROM 0 TO (LEN(X)/B):
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
### The Algorithm
---

## References
---
[1] Galois/Counter Mode (GCM) and GMAC, SP 800-38D, NIST.