──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Mathematical Background|Mathematical Background]]
	- [[#Mathematical Background#Modular Arithmetic|Modular Arithmetic]]
	- [[#Mathematical Background#Finite Fields|Finite Fields]]
		- [[#Finite Fields#The Euclidean Algorithm (Optional)|The Euclidean Algorithm (Optional)]]
	- [[#Mathematical Background#Elliptic Curves|Elliptic Curves]]
- [[#Elliptic Curve Cryptography|Elliptic Curve Cryptography]]
	- [[#Elliptic Curve Cryptography#Elliptic Curve Discrete Log Problem (ECDLP)|Elliptic Curve Discrete Log Problem (ECDLP)]]
	- [[#Elliptic Curve Cryptography#Domain Parameters|Domain Parameters]]
	- [[#Elliptic Curve Cryptography#Public Key Derivation|Public Key Derivation]]
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

A modular negative wraps around. This means that,
$$-3 \mod 7 = 4$$

Instead of equivalence, congruence is used. The following,
$$
a \equiv b \pmod{n}
$$
means that $a$ is congruent to $b$, modulo $n$. This means that,
$$a \mod n = b \mod n$$

A modular inverse, $a^{-1}$, must satisfy,
$$ a a^{-1} \equiv 1 \pmod{n}$$
#### Finite Fields
---
A finite (or galois) field is a finite set of elements on which addition, subtraction, multiplication and division are defined. 

An example of a finite field is $\mathbb{F}_{p}$, where,
* $p$ is a prime number,
* $x$ is an element, $x \in [0, p-1]$, $x \in \mathbb{Z}$, and,
* modular arithmetic applies (i.e., $\mod p$).
##### The Euclidean Algorithm (Optional)
---
The *Euclidean Algorithm* states that,
* $gcd(a, b)$, where $a \ge b$, is equivalent to $gcd(b, a \mod b)$, and,
* $gcd(x, 0) = x$.

The *Extended Euclidean Algorithm* extends the *Euclidean Algorithm* by deriving $x$ and $y$, where,
* $ax + by = gcd(a, b)$, and,
* $x, y \in \mathbb{Z}$.

If $gcd(a, n) = 1$ (e.g., $n$ is a prime number), then,
$$ a a^{-1} \equiv 1 \pmod{n}$$
which is equivalent to,
$$aa^{-1} + ny = 1$$
can be solved for $a^{-1}$, the modular inverse of $a$, using the *Extended Euclidean Algorithm*.
#### Elliptic Curves
---
An elliptic curve (over infinite field $\mathbb{R}$) is defined by,
$$y^{2} = x^{3} + ax + b$$
where,
$$4a^{3} + 27b^{2} \ne 0$$
*Note:* The $4a^{3} + 27b^{2} \ne 0$ condition guarantees that the elliptic curve has no cusps or self-intersections.

Elliptic curves define an addition operation, $+$, between points, where,
* **Closure:** For points $P$ and $Q$ on the curve, $P + Q$ is also a point on the curve.
* **Identity/Inverse:** Point $I$, the identity, is the point at infinity. For point $P$ on the curve, its inverse, $-P$, exists, as its reflection on the x-axis, and $P + (-P) = I$.
* **Associativity:** For points $P$, $Q$, and $R$ on the curve, $(P + Q) + R = P + (Q + R)$.

The addition operation is defined as,
* For points $P$ and $Q$ on the curve, where $P \ne Q$,
	* Draw a line through $P$ and $Q$.
	* Find the (third) intersection point, $R$, of the line with the elliptic curve.
	* Reflect $R$ over the x-axis to yield $P + Q$.
* For points $P$ and $Q$ on the curve, where $P = Q$,
	* Draw a tangent line through $P$.
	* Find the intersection point, $R$, of the line with the elliptic curve.
	* Reflect $R$ over the x-axis to yield $P + Q$.

Scalar multiplication of $k$ with a point, $P$, on the curve, is defined as adding $P$ to itself $k$ times.
### Elliptic Curve Cryptography
---
####  Elliptic Curve Discrete Log Problem (ECDLP)
---
*Elliptic Curve Cryptography (ECC)* relies on the *Elliptic Curve Discrete Log Problem (ECDLP)*.

For an elliptic curve over $\mathbb{F}_{p}$, and an arbitrary (base-)point $G$,
* Forward computation of $Q = kG$ is easy, but,
* Reverse computation of $k$ is extremely hard.

For a base-point $G$, there exists an order $n$, where $nG = I$, and for values of $k > n$, $Q$ starts to repeat.
#### Domain Parameters
---
Before using any cryptographic operations based on *ECC*, parties involved must agree on the *domain parameters*, $D$. This includes,
* The coefficients $a$ and $b$ of the elliptic curve.
* The order of finite field, $p$.
* The base-point $G$, and its order $n$.
#### Public Key Derivation
---
Let $(d, Q)$ be the private-public key pair, and $d \in [1, n-1]$, then $Q = d(G)$.
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