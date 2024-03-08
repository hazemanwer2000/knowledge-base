──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*

- [[#The Algorithm|The Algorithm]]
	- [[#The Algorithm#`Cipher`|`Cipher`]]
		- [[#`Cipher`#`SubBytes`|`SubBytes`]]
		- [[#`Cipher`#`ShiftRows`|`ShiftRows`]]
		- [[#`Cipher`#`MixColumns`|`MixColumns`]]
		- [[#`Cipher`#`AddRoundKey`|`AddRoundKey`]]
	- [[#The Algorithm#`InvCipher`|`InvCipher`]]
- [[#Padding|Padding]]
## Content
---
*AES (Advanced Encryption Standard)* [1] is a document that outlines a *symmetric-key, block-cipher* algorithm, usually referred to with the same name (i.e., the AES encryption algorithm).

The standard defines three variants, outlined below, that differ in some of the parameters of the algorithm. 

| Variant   | *Nk* (Key Size, in bits) | *Nb* (Block Size, in bits) | *Nr* (No. of Rounds) |
| --------- | ------------------------ | -------------------------- | -------------------- |
| *AES-128* | $128$                    | $128$                      | $10$                 |
| *AES-192* | $192$                    | $128$                      | $12$                 |
| *AES-256* | $256$                    | $128$                      | $14$                 |
*Note:* As shown above, all variants transform data in blocks of $128$ bits.
### The Algorithm
---
The document outlines the `Cipher` and `InvCipher` functions, that encrypt and decrypt any data block, respectively.

Both functions are called with the following arguments,
```
[Inv]Cipher(Block, Nr, KeyExpansion(Key))
```

The `KeyExpansion` function derives $Nr + 1$ *round keys*. Each round key is of $Nb$ size. 

*Note:* Refer to [1] for the definition of the `KeyExpansion` function.

*Note:* For transformations defined in the algorithm, each byte is interpreted as belonging to the finite field $GF(2^8)$. Refer to [1] for the definition of addition, multiplication, identities, multiplicate inverses in $GF(2^8)$.
#### `Cipher`
---
In `Cipher`, initially, a block is represented as a $4$ by $4$ matrix of bytes, called the *state*,
$$
state[r, c] = block[r + 4c]
$$
where,
$$
0 \le r \lt 4, 0 \le c \lt 4
$$
Then, the following sequence of function calls is executed,
```
state = AddRoundKey(state, RoundKeys[0])
FOR ir FROM 1 TO (Nr - 1) DO
	state = SubBytes(state)
	state = ShiftRows(state)
	state = MixColumns(state)
	state = AddRoundKey(state, RoundKeys[ir])
state = SubBytes(state)
state = ShiftRows(state)
AddRoundKey(state, RoundKeys[Nr])
```
##### `SubBytes`
---
In `SubBytes`, each byte is transformed independently, using a substitution table called the *AES S-box*.

![[AES-SBox.png|600]]
##### `ShiftRows`
---
In `ShiftRows`, each row is left-rotated by $r$, the row number.

![[AES-ShiftRows.png|400]]
##### `MixColumns`
---
In `MixColumns`, each column is multiplied by a single fixed matrix, shown below.

![[AES-MixColumns.png|325]]
##### `AddRoundKey`
---
In `AddRoundKey`, the round key is represented as a $4$ by $4$ matrix of bytes, similar to the *state*'s representation, and then, added to the state.
#### `InvCipher`
---
In a similar manner, `InvCipher` calls `InvSubBytes`, `InvShiftRows`, `InvMixColumns` and `AddRoundKey` within its implementation.

Refer to [1] for the definition of `InvCipher` and the functions it calls.
### Padding
---
When the plain-text is not block-aligned for any block-cipher algorithm, padding is required. [1] itself does not define a padding scheme.

Popular padding schemes used include *PKCS#7* padding, which involves appending the number of required padding bytes, represented as a byte, repeatedly. For example, if four bytes of padding are required, `04 04 04 04` is appended to the plain-text.
## *References*
---
[1] Advanced Encryption Standard (AES), FIPS 197, NIST.