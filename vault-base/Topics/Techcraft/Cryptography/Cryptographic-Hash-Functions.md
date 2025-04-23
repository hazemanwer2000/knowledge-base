## *Sub-topics!*
---
* [[SHA-1]]
## *Content*
---
A *Cryptographic Hash Function (CHF)* is a one-way function, that has some special properties:
* *Pre-Image Resistance*
	* Given an output, `O`, of a CHF, it should be impossible, without brute force, to find an input, `I`, where `O = CHF(I)`.
* *Second Pre-Image Resistance*
	* Given an output, `O`, and an input, `I`, where `O = CHF(I)`, it should be impossible, without brute force, to find another input, `I'`, where `O = CHF(I')`.
* *Collision Resistance*
	* It should be impossible, without brute force, to find any two inputs, `I` and `I'`, where `CHF(I) = CHF(I')`.