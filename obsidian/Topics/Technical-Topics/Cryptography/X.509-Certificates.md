──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
## Content
---
A *X.509 certificate* is a standardized *public-key certificate* [1]. A public-key certificate binds an identity to a public key using a digital signature. It contains, at minimal, a public key, and is signed by a *Certificate Authority (CA)*, directly or indirectly. This allows the possessor of the corresponding private key to become part of the *chain of trust*, that begins with the *CA* and ends with the respective entity.

*X.509* certificates are specified in *ASN.1*, an *abstract syntax* for defining data structures on a high-level. Usually, an *X.509* certificate is communicated in *DER* format, which stands for *Distinguished Encoding Rules*, a set of encoding rules for *ASN.1* structures.
### ASN.1
---
*ASN.1* stands for *Abstract Syntax Notation One*, an abstract syntax for defining data structures on a high-level.

*ASN.1* defines different primitive types, some of which are listed below.

| Name                | Description                                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `BOOLEAN`           | Boolean, `TRUE` or `FALSE`.                                                                                      |
| `INTEGER`           | An integer.                                                                                                      |
| `BIT STRING`        | A stream of bits.                                                                                                |
| `OCTET STRING`      | A stream of bytes.                                                                                               |
| `OBJECT IDENTIFIER` | An object identifier, *OID*, a unique sequence of numbers used to identify objects, usually based on a standard. |
*ASN.1* also defines different complex types, some of which are listed below.

| Name          | Description                            |
| ------------- | -------------------------------------- |
| `SEQUENCE`    | Analogous to a `struct` in C language. |
| `SEQUENCE OF` | Analogous to an array in C language.   |
| `SET`         | An unordered `SEQUENCE`.               |
| `ENUMERATION` | Analogous to an `enum` in C language.  |
| `CHOICE`      | Analogous to a `union` in C language.  |
## *References*
---
[1] Internet X.509 PKI Certificate and CRL Profile, RFC 2459, IETF
[2] ASN.1 Complete, John Larmouth