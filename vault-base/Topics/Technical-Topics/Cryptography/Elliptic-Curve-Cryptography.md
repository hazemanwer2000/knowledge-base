──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Domain Parameters|Domain Parameters]]
- [[#Public Key Derivation|Public Key Derivation]]
- [[#ECDSA|ECDSA]]
- [[#ECDH|ECDH]]
## Content
---
### Mathematical Background
---
#### Modular Arithmetic
---
In modular arithmetic, results are reduced to modulo $n$, where $n$ is the modulus, $n \ge 1$.

In addition, the following,
$$ (a + b) \mod n$$
is equivalent to,
$$ ((a \mod n) + (b \mod n)) \mod n$$

In multiplication, the following,
$$ ab \mod n$$
is equivalent to,
$$ (a \mod n)(b \mod n) \mod n$$

Instead of equivalence, congruence is used. The following,
$$
a \equiv b \pmod{n}
$$
means that $a$ is congruent to $b$, modulo $n$. This means that,
$$a \mod n = b \mod n$$

A modular inverse, $a^{-1}$, must satisfy,
$$ a a^{-!} \equiv 1 \pmod{n}$$





*Elliptic Curve Cryptography (ECC)* uses elliptic curves over finite fields (i.e., galois fields) to define useful cryptographic operations, such as digital signature generation and verification (i.e., *ECDSA*) and secure key exchange (i.e., *ECDH*).

A field is a set on which addition and multiplication, among other operations, are defined and satisfy the *field axioms*, including *associativity*, *commutativity*, and *additive* and *multiplicative identities*. For example, the set of all real numbers, $\mathbb{R}$, is an infinite field. A finite field, $GF(q)$, is a field, with a finite set of $q$ elements.

An elliptic curve defined over $GF(q)$, has all mathematical operations, coefficients and values defined within $GF(q)$.
### Domain Parameters
---
Before using any cryptographic operations based on *ECC*, parties involved must agree on the *domain parameters*, $D$. This includes the type and coefficients, $a$ and $b$, of the elliptic curve used, and the type and size, $q$, of the finite field used.

Additionally, the domain parameters include the *base* point $G=(G_x, G_y)$, and its order, $n$. For $i=0$ to $i = n - 1$, the scalar multiplication (i.e., adding a point repeatedly to itself) of $i$ by $G$, $i(G)$, should yield all points on the curve.

For defined and recommended domain parameters, $D$, refer to [2].
### Public Key Derivation
---
Let $(d, Q)$ be the private-public key pair, and $d \in [1, n-1]$, then $Q = d(G)$.

*Note:* Given $Q$, it is computationally infeasible to determine $d$. 
### ECDSA
---
*Elliptic Curve Digital Signature Algorithm (ECDSA)*, as specified in [1], defines two procedures, one for signature generation, and another for signature verification.

To generate a signature, given $D$, $d$, and $H$, the chosen *CHF* (e.g., SHA-1, SHA-256),
* Compute $H(M)$, where $M$ is the message to be signed.
* If the digest size is larger than $len(n)$, set $e$ as the left-most bits $ceil(log_2(n))$ of $H(M)$, otherwise, simply set $e$ as $H(M)$.
* Generate a random integer, $k$, $k \in [1, n-1]$.
* Compute $R = k(G)$.
* Compute $r = R_{x} \bmod n$.
* Compute $s = k^{-1} \cdot (e + r \cdot d) \bmod n$
* Output $(r, s)$, as the signature.

To verify a signature, $(r, s)$, given $D$, $Q$, and $H$,
* Compute $H(M)$.
* If the digest size is larger than $ceil(log_2(n))$, set $e$ as the left-most bits $ceil(log_2(n))$ of $H(M)$, otherwise, simply set $e$ as $H(M)$.
* Compute $u = e \cdot s^{-1} \bmod n$, and $v = r \cdot s^{-1} \bmod n$.
* Compute $R = u(G) + v(Q)$.
* Compute $r' = R_x \bmod n$.
* If $r'$ is equal to $r$, then verification succeeds. Otherwise, it fails.
### ECDH
---
*Elliptic Curve Diffie-Hellman (ECDH)* is the *ECC*-equivalent of *Diffie-Hellman*, an algorithm to facilitate secure key exchange, while communicating over an unsecure channel.

Each party generates a private-public key pair, $(d, Q)$. Then, each party communicates its public key to the other. A shared secret is then derived by both parties synonymously, as, 
$$S = d_A(Q_B) = d_B(Q_A) = (d_A \cdot d_B)(G) = (d_B \cdot d_A)(G)$$

*Note:* Usually, $S$ acts as the *seed* for a *Key Derivation Function (KDF)*, which uses a pseudo-random function, such as *HMAC* based on SHA-256, to derive key material (i.e., stretch the seed into lengthy key material).
## *References*
---
[1] Digital Signature Standard (DSS), FIPS 186-5, NIST
[2] Recommendation for Discrete Logarithm-based Cryptography: Elliptic Curve Domain Parameters, Special Publication 800-186, NIST