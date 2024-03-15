──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
## Content
---
*Elliptic Curve Cryptography (ECC)* uses elliptic curves over finite fields (i.e., galois fields) to define useful cryptographic operations, such as digital signature generation and verification (i.e., *ECDSA*) and key exchange (i.e., *ECDH*).

A field is a set on which addition and multiplication, among other operations, are defined and satisfy the *field axioms*, including *associativity*, *commutativity*, and *additive* and *multiplicative* identities. For example, the set of all real numbers, $\mathbb{R}$, is an infinite field. A finite field, $GF(q)$, is a field, with a finite set of $q$ elements.

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
The *Elliptic Curve Digital Signature Algorithm (ECDSA)* defines two procedures, one for signature generation, and another for signature verification.

To generate a signature, given $D$ and $d$,
* 
## *References*
---
[1] Digital Signature Standard (DSS), FIPS 186-5, NIST
[2] Recommendation for Discrete Logarithm-based Cryptography: Elliptic Curve Domain Parameters, Special Publication 800-186, NIST