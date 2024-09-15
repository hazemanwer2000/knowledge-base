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
* `X` - Bit string
* `S` - Integer, where `S <= LEN(X)`

And output(s),
* `X'` - Bit string, where `LEN(X) == LEN(X')` 

Then, it shall be defined as,
```
A = MSB(X, LEN(X) - S)
B = (LSB(X, S) + 1) MOD (2^S)

X' = CONCAT(A, B)
```
#### `MUL`
---
Let `MUL(X, Y)` be a function, with input(s),
* `X` - Bit string, where `LEN(X) == B`
* `Y` - Bit string, where `LEN(Y) == B`

And output(s),
* `O` - Bit string, where `LEN(O) == B`

Then, it shall be defined as,
```
...
```
### The Algorithm
---

## References
---
[1] Galois/Counter Mode (GCM) and GMAC, SP 800-38D, NIST.