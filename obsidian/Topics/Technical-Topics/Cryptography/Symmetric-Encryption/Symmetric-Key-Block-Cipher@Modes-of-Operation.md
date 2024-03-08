──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*

## Content
---
For any symmetric-key, block-cipher algorithm (e.g., AES), [1] defines a number of confidential *modes* of operation, that define how plain-text is to be encrypted into cipher-text (and vice versa), using the semantics of the underlying algorithm (i.e., `[DE-]CIPHER(KEY, BLOCK)`).

### Initialization Vector *(IV)*
---
For some of the modes described below, an *Initialization Vector (IV)* is required. This is usually a randomly-generated value (e.g., using *TRNG* hardware) that is used only once (i.e., a nonce) per confidential message.

An *IV* is not confidential, and can be communicated, along with the encrypted text. However, it must be integrity- (and hence, as well, authenticity-) protected.
### Electronic Code Book *(ECB)*
---
In *Electronic Code Book (ECB)* mode, each block is encrypted independently,
$$C_j = CIPH_K(P_j)$$
and, hence, decrypted independently,
$$P_j = CIPH_{K}^{-1}(C_j)$$
where $j$ spans from $1$ to $n$, the number of blocks.
### Cipher Block Chaining *(CBC)*
---
In *Cipher Block Chaining (CBC)* mode, each block is XOR'ed with the previous cipher-text block, before being encrypted, while the first block is XOR'ed with the *IV*.
$$
C_j = \begin{cases} 
	CIPH_K(P_j \oplus IV) & \text{if } j = 1 \\
	CIPH_K(P_j \oplus C_{j-1}) & \text{if } 2 \ge j \le n
\end{cases}
$$
While decrypting,
$$
P_j = \begin{cases} 
	CIPH_{K}^{-1}(C_j) \oplus IV & \text{if } j = 1 \\
	CIPH_{K}^{-1}(C_j) \oplus C_{j-1} & \text{if } 2 \ge j \le n
\end{cases}
$$
### Counter Mode *(CTR)*
---

## *References*
---
[1] Recommendation for Block Cipher Modes of Operation: Methods and Techniques, Special Publication 800-38A, NIST