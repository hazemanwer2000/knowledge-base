──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#ASN.1|ASN.1]]
- [[#DER|DER]]
	- [[#DER#The Tag|The Tag]]
		- [[#The Tag#Overriding Tag Values|Overriding Tag Values]]
	- [[#DER#The Length|The Length]]
	- [[#DER#The Value|The Value]]
- [[#X.509 Format|X.509 Format]]
	- [[#X.509 Format#`TBSCertificate`|`TBSCertificate`]]
		- [[#`TBSCertificate`#`version`|`version`]]
		- [[#`TBSCertificate`#`AlgorithmIdentifier`|`AlgorithmIdentifier`]]
		- [[#`TBSCertificate`#`Name`|`Name`]]
		- [[#`TBSCertificate`#`Validity`|`Validity`]]
		- [[#`TBSCertificate`#`SubjectPublicKeyInfo`|`SubjectPublicKeyInfo`]]
## Content
---
A *X.509 certificate* is a standardized *public-key certificate* [1]. A public-key certificate binds an identity to a public key using a digital signature. It contains, at minimal, a public key, and is signed by a *Certificate Authority (CA)*, directly or indirectly. This allows the possessor of the corresponding private key to become part of the *chain of trust*, that begins with the *CA* and ends with the respective entity.

*X.509* certificates are specified in *ASN.1*, an *abstract syntax* for defining data structures on a high-level. Usually, an *X.509* certificate is communicated in *DER* format, which stands for *Distinguished Encoding Rules*, a set of encoding rules for *ASN.1* structures.
### ASN.1
---
*ASN.1* stands for *Abstract Syntax Notation One*, an abstract syntax for defining data structures on a high-level. [2]

*ASN.1* defines different primitive types, some of which are listed below.

| Name                | Description                                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `BOOLEAN`           | Boolean, `TRUE` or `FALSE`.                                                                                      |
| `INTEGER`           | An integer.                                                                                                      |
| `BIT STRING`        | A stream of bits.                                                                                                |
| `OCTET STRING`      | A stream of bytes.                                                                                               |
| `OBJECT IDENTIFIER` | An object identifier, *OID*, a unique sequence of numbers used to identify objects, usually based on a standard. |
The notation `::=` is used to represent *type assignment*. For example,
```
type-name ::= BOOLEAN
```
*ASN.1* also defines different complex types, some of which are listed below.

| Name          | Description                            |
| ------------- | -------------------------------------- |
| `SEQUENCE`    | Analogous to a `struct` in C language. |
| `SEQUENCE OF` | Analogous to an array in C language.   |
| `SET`         | An unordered `SEQUENCE`.               |
| `ENUMERATED`  | Analogous to an `enum` in C language.  |
| `CHOICE`      | Analogous to a `union` in C language.  |
```
type-name ::= SEQUENCE {
	type-name TYPE-NAME,
	... }

type-name ::= SEQUENCE OF type-name

type-name ::= SET {
	type-name TYPE-NAME,
	... }

type-name ::= ENUMERATED {
	label-0(0),
	label-1(1), 
	... } DEFAULT label-x

type-name ::= CHOICE {
	type-name TYPE-NAME,
	... }
```
The label `OPTIONAL` may be the suffix of any type assignment, denoting that this field is optional.
```
type-name ::= SEQUENCE {
	type-name TYPE-NAME OPTIONAL,
	... }
```
### DER
---
A set of encoding rules are required to compile *ASN.1* structures from abstract syntax to *transfer syntax*, a format in which they can be communicated unambiguously.

*DER* is a commonly used set of encoding rules for *ASN.1* structures, among them are *X.509* certificates. [3]

*DER* represents each type as a triplet: tag *(T)*, length *(L)* and value *(V)*. Each type is given a unique tag.

#### The Tag
---
The first octet of the tag is encoded as shown below,

![[DER-Tag-First-Octet.png|450]]
where the class is encoded as shown below.

![[DER-Tag-Class.png|450]]

If the tag number is larger than or equal to `0x1F`, then,
* In the first octet, the tag number is fixed to `0b11111`, and does not denote the actual tag number.
* In subsequent octets (one, or more), the tag number is represented in bits $0$ to $6$.
* In subsequent octets, except the last, bit $7$ is set to `1`. In the last octet, bit $7$ is set to `0`.

*Note:* A `CHOICE` is given the tag value of the chosen type. It has no tag value of its own.
##### Overriding Tag Values
---
*DER*, in compliance with *ASN.1*, allows the overriding of tag values, by preceding types with square brackets, and the override value in between. For example,
```
type-name ::= [0] SEQUENCE {
	type-name TYPE-NAME,
	... }
```
By default, in *DER* format, a sequence has a tag value of `0x30`. However, this tag value is overridden with the value `0x0`.

The keywords `IMPLICIT` and `EXPLICIT` following the square brackets specify one of two different methods of tag overriding.

If `IMPLICIT`, the tag is overridden directly (i.e., the old tag value is replaced with the new tag value). If `EXPLICIT`, the new tag value encapsulates the old tag value, in a new *TLV* triplet. For example,
```
Let {T} [L] (V) denote a TLV triplet, then

CASE 'IMPLICIT':
	{T_new} [L] (V)

CASE 'EXPLICIT':
	{T_new} [L'] ( {T_old} [L] (V) )
```
#### The Length
---
If the length is less than or equal to `0x7F`, it is represented as a single octet. Otherwise,
* In the first octet, bits $0$ to $6$ denote the number of octets to follow (one, or more). Bit $7$ is fixed to `1`.
* In subsequent octets, the length is represented.
#### The Value
---
Each primitive type is defined a specific representation. Refer to [3] for all representations.
### X.509 Format
---
The following is the *ASN.1* definition of a *X.509* certificate.
```
Certificate ::= SEQUENCE {
	tbsCertificate TBSCertificate,
	signatureAlgorithm AlgorithmIdentifier,
	signatureValue BIT STRING }
```
#### `TBSCertificate`
---
The `TBSCertificate` type denotes the structure to be signed.
```
TBSCertificate ::= SEQUENCE {
	version [0] EXPLICIT Version DEFAULT v1,
	serialNumber INTEGER,
	signatureAlgorithm AlgorithmIdentifier,
	issuer Name,
	validity Validity,
	subject Name,
	subjectPublicKeyInfo SubjectPublicKeyInfo,
	...
}
```
##### `Version`
---
The `Version` type denotes the *X.509* certificate standard version used.
```
Version ::= ENUMERATED { v1(0), v2(1), v3(3) }
```
##### `AlgorithmIdentifier`
---
The `AlgorithmIdentifier` type denotes the signature generation/verification algorithm used.
```
AlgorithmIdentifier ::= SEQUENCE {
	algorithm OBJECT IDENTIFIER,
	parameters ANY DEFINED BY algorithm OPTIONAL }
```
##### `Name`
---
The `Name` type is used to identify an entity; the issuer (i.e., the signing entity), or the subject.
```
Name ::= SEQUENCE OF RelativeDistinguishedName

RelativeDistinguishedName ::= SET OF AttributeTypeAndValue

AttributeTypeAndValue ::= SEQUENCE {
	type AttributeType,
	value AttributeValue }

AttributeType ::= OBJECT IDENTIFIER

AttributeValue ::= ANY DEFINED BY AttributeType
```
##### `Validity`
---
The `Validity` type is used to set the time frame within which the certificate is valid.
```
Validity ::= SEQUENCE {
	notBefore Time,
	notAfter Time }

Time ::= CHOICE {
	utcTime UTCTime
	generalTime GeneralizedTime }
```
##### `SubjectPublicKeyInfo`
---
The `SubjectPublicKeyInfo` type denotes the algorithm used to generate the public key, and the value of the public key.
```
SubjectPublicKeyInfo ::= SEQUENCE {
	algorithm AlgorithmIdentifier,
	subjectPublicKey BIT STRING }
```
## *References*
---
[1] Internet X.509 PKI Certificate and CRL Profile, RFC 2459, IETF
[2] ASN.1 Complete, John Larmouth
[3] ITU-T, X.690, ASN.1 Encoding Rules: BER, CER and DER 