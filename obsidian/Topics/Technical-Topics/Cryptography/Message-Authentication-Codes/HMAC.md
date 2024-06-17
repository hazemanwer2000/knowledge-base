──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Secret Shared Key|Secret Shared Key]]
- [[#Computation|Computation]]
- [[#Truncated MAC|Truncated MAC]]
## Content
---
*HMAC*, as defined in [1], is a method for generating *Message Authentication Codes (MAC)* using *Cryptographic Hashing Functions (CHF)* (i.e., SHA-256).

Any *CHF* can be used with *HMAC*. *HMAC-256* denotes the use of *SHA-256*, and so on.

*Note:* The cryptographic strength of *HMAC* is, therefore, dependent on the underlying hash function.
### Secret Shared Key
---
The secret, shared key is recommended to be at minimum the size of the digest, `L`, in bytes, outputted by the *CHF*.

If the key size exceeds the block size, `B`, in bytes, of the underlying *CHF*, it is hashed using the same *CHF*, and the output digest is used as key instead.
### Computation
---
To compute a *MAC* for any text, using *HMAC*, given the key,
```
H(K XOR opad, H(K XOR ipad, text))
```
where,
```
ipad = '0x36' repeated B times
opad = '0x5C' repeated B times
```

*Note:* If the key size is less than `B`, `0x00` is appended repeatedly until it is `B` bytes long.
### Truncated MAC
---
It is recommend not to truncate the output *MAC* to be less than neither `L/2` bytes, or 80 bits.
## *References*
---
[1] HMAC: Keyed-Hashing for Message Authentication, RFC 2104.