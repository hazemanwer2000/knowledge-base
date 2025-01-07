──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Pre-processing|Pre-processing]]
	- [[#Pre-processing#Padding|Padding]]
	- [[#Pre-processing#Parsing|Parsing]]
	- [[#Pre-processing#Initial Hash|Initial Hash]]
- [[#Computation|Computation]]
## Content
---
*SHA-1* is a *Cryptographic Hash Function (CHF)*, defined in [1], along with other functions.

For every function defined in [1], a number of fixed parameters are defined, for *SHA-1* in particular,

| Parameter        | Unit | Value |
| ---------------- | ---- | ----- |
| Block Size ($m$) | Bits | $512$ |
| Word Size ($w$)  | Bits | $32$  |
| Hash Size        | Bits | $160$ |
| Digest Size      | Bits | $160$ |

*Note:* The output of a *CHF*, for a given input message, is called the message *digest*.

*Note:* For a given function and input, a *hash* is the output before truncation, and a *digest* is the truncated *hash*, using the left-most bits. If the hash size equals the digest size, no truncation is necessary.

Every function in [1] is defined as a series of steps, which will be outlined in detail for *SHA-1* in this document.
### Pre-processing
---
At the *pre-processing* stage, the message is *padded*, *parsed*, and an initial hash is set.
#### Padding
---
At the *padding* stage, `0b1` is appended, followed by a variable $k$ number of `0b0`, again followed by a $2w$ (i.e., $64$ for *SHA-1*) bit value, that represents the length of the input message, $l$, in bits.

The variable $k$ is selected to be the minimum non-negative value that satisfies,
$$(l + 1 + k + 2w) \bmod m = 0$$
#### Parsing
---
At the *parsing* stage, the padded message is interpreted as a series of blocks, where $M^{(i)}$ stands for the $i^{th}$ block, sized $m$ (i.e., $M^{(1)}$, $M^{(2)}$, ..., $M^{(N)}$).

Each block consists of $16$ words, each sized $w$, where $M^{(i)}_j$ stands for the $j^{th}$ word in the $i^{th}$ block (i.e., , $M^{(i)}_0$, $M^{(i)}_1$, ..., $M^{(i)}_{15}$).
#### Initial Hash
---
For every function in [1], an initial hash is defined, $H^{(0)}$. For *SHA-1*,
```
67452301efcdab8998badcfe10325476c3d2e1f0
```
*Note:* For *SHA-1*, $H^{(0)}_{0}$ = `67452301`, and so on.
### Computation
---
Let $f_t(x, y, z)$ be defined as,
$$
f_t(x, y, z) = \begin{cases} 
g_1(x, y, z) & \text{if } 0 \le t \le 19 \\
g_2(x, y, z) & \text{if } 20 \le t \le 39, 60 \le t \le 79 \\
g_3(x, y, z) & \text{if } 40 \le t \le 59 \\
\end{cases}
$$
where,
```
g1(x, y, z) = (x & y) ^ (~x & z)
g2(x, y, z) = x ^ y ^ z
g3(x, y, z) = (x & y) ^ (x & z) ^ (y & z)
```
and all inputs and outputs are $w$-bit sized.

Let $K_t$ be defined as,
```
K_t = 5a827999     if    (0  <= t <= 19)
	= 6ed9eba1     if    (20 <= t <= 39)
	= 8f1bbcdc     if    (40 <= t <= 59)
	= ca62c1d6     if    (60 <= t <= 79)
```

Let $W_t$ be defined as,
$$
W_t = \begin{cases} 
M_t^{(i)} & \text{if } 0 \le t \le 15 \\
\text{ROTL}_{n=1}(W_{t-3} \oplus W_{t-8} \oplus W_{t-14} \oplus W_{t-16}) & \text{if } 16 \le t \le 79
\end{cases}
$$
where *ROTL* is a rotate-left operation, with $n$ denoting the number of bits to rotate by.

Given the preceding definition of $f_t(x, y, z)$, $K_t$, and $W_t$, the *SHA-1* algorithm proceeds as follows:

* From $i=1$ to $i = N$,
	* Initialize $a$, $b$, $c$, $d$, and $e$, as:

		$$a = H^{(i-1)}_{0}$$
		$$b = H^{(i-1)}_{1}$$
		$$c = H^{(i-1)}_{2}$$
		$$d = H^{(i-1)}_{3}$$
		$$e = H^{(i-1)}_{4}$$
	
	* From $t=0$ to $t = 79$,

		$$T = \text{ROTL}_{n=5}(a) + f_t(b, c, d) + e + K_t + W_t$$
		$$e = d$$
		$$d = c$$
		$$c = \text{ROTL}_{n=30}(b)$$
		$$b = a$$
		$$a = T$$

	* Compute $H^{(i)}$,

		$$H^{(i)}_{0} = a + H^{(i-1)}_{0}$$
		$$H^{(i)}_{1} = b + H^{(i-1)}_{1}$$
		$$H^{(i)}_{2} = c + H^{(i-1)}_{2}$$
		$$H^{(i)}_{3} = d + H^{(i-1)}_{3}$$
		$$H^{(i)}_{4} = e + H^{(i-1)}_{4}$$

The final hash value is,
$$H_0^{N} || H_1^{N} || H_2^{N} || H_3^{N} || H_4^{N}$$
## *References*
---
[1] Secure Hash Standard (SHS), FIPS PUB 180-4, NIST.