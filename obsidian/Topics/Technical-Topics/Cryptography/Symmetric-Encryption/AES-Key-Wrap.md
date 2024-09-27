──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AES Key-Wrap* algorithm, as specified in [1], is a cryptographic algorithm, based on *AES*, that is meant to secure (i.e., provide authenticity and confidentiality) data, usually a session-key, for secure transmission over an insecure channel.

*Note:* Input data must be a multiple, `N`, of `B/2`, where `B` is the AES block-size in bit(s), with `N >= 2`.
### Initialization Vector
---
A default Initialization Vector (IV) is specified in [1] as `B/2`-sized, and consisting of consecutive `0xA6` byte(s).
### `WRAP`
---
The following pseudo-code specifies the `WRAP` function.

```
A = IV

FOR i FROM 1 TO N
	R[i] = P[i]

FOR j FROM 0 TO 5
	FOR i FROM 1 TO N
		D = CIPH(K, CONCAT(A, R[i]))
		t = (N * j) + i
		A = MSB(B/2, D) ^ t
		R[i] = LSB(B/2, D)

C[0] = A

FOR i FROM 1 TO N
	C[i] = R[i]
```
### `UNWRAP`
---
The following pseudo-code specifies the `UNWRAP` function.

```
A = C[0]

FOR i FROM 1 TO N
	R[i] = C[i]

FOR j FROM 5 TO 0
	FOR i FROM N TO 1
		t = (N * j) + i
		D = INVCIPH(K, CONCAT((A ^ t), R[i]))
		A = MSB(B/2, D)
		R[i] = LSB(B/2, D)

IF A == IV
	FOR i FROM 1 TO N
		P[i] = R[i]
ELSE
	"Authentication Error!"
```
## References
---
[1] Advanced Encryption Standard (AES) Key Wrap Algorithm, RFC 3394