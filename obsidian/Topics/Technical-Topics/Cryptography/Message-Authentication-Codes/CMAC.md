──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
## Content
---
*CMAC*, as defined in [1], is a method for generating *Message Authentication Codes (MAC)* using a symmetric-key, block-cipher algorithm (e.g., AES). Alternatively, *CMAC* is viewed as an authentication mode of operation of the respective algorithm.

*Note:* *CMAC* uses the same key as the respective algorithm.

*Note:* *CMAC* does not uses *forward cipher function*, $CIPH_K$, of the respective algorithm. It does not employ the *inverse cipher function*, $CIPH_K^{-1}$.
### The Algorithm
---
The *CMAC* generation function, `CMAC`, is declared as, 
```
CMAC(K, M, Tlen)
``` 
where `K` is the key, `M` is the message, and `Tlen` is the truncation length of the generated *MAC*, which must be less or equal to `b`, the block size of the underlying algorithm.
#### `CMAC`
---
Pseudo-code for the `CMAC` function is shown below,
```
% `SUBK` derives two keys, `K1` and `K2`, from `K`.
%     Both derived keys are of size `b`.
K1, K2 = SUBK(K)

% Determine the number of blocks to process.
IF Mlen == 0 THEN
	N = 1
ELSE
	N = CEIL(Mlen / b)
ENDIF

% Mask the last block with either `K1` or `K2`.
IF (Mlen % b) == 0 THEN
	M[Mlen - 1] = K1 ^ M[Mlen - 1]
ELSE
	% `PAD` pads a bit-string with `0b1` and consecutive (zero, or more) `0b0`.
	M[Mlen - 1] = K2 ^ PAD(M[Mlen - 1]) 
ENDIF

% Generate the MAC.
C[0] = 0
FOR i in (1, N) BEGIN
	C[i] = CIPH(K, C[i-1] ^ M[i])
ENDLOOP

% Truncate the MAC.
MAC = TRUNCATE(C[N], Tlen)

RETURN MAC
```
where `SUBK` is defined as,
```
# Determine `K0`.
K0 = CIPH(K, 0)

# Determine `K1`.
IF MSB(K0) == 0b0 THEN
	K1 = K0 << 1
ELSE
	# 'Rb' is a constant for a given `b`.
	K1 = (K0 << 1) ^ Rb
ENDIF

# Determine `K2`.
IF MSB(K1) == 0 THEN
	K2 = K1 << 1
ELSE
	K2 = (K1 << 1) ^ Rb
ENDIF

RETURN K1, K2
```
where `Rb` is a constant for a given `b`, defined in [1].

Below is an illustrative diagram of the `CMAC` function.
![[CMAC-Diagram.png]]
## *References*
---
[1] Recommendation for Block Cipher Modes of Operation: CMAC Mode for Authentication, Special Publication 800-38B, NIST