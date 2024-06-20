──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Key Manager (KeyM)* module, which resides in the Service layer, in functionality, API and configuration.

The *KeyM* module can be divided into two sub-modules: crypto-key sub-module, and certificate sub-module.

*Note:* The crypto-key sub-module is not discussed within this document.
### Specification
---
...
### Function(s)
---
...
### Configuration
---
```
KeyMGeneral [C, 1]
	KeyMCertificateChainMaxDepth [P]
	KeyMCertificateManagerEnabled [P]
	KeyMCryptoKeyManagerEnabled [P]

KeyMCertificate [C, 0..*]
	KeyMCertAlgorithmType [P]
	KeyMCertFormatType [P]
	KeyMCertificateId [P]
	KeyMCertificateMaxLength [P]
	KeyMCertificateName [P]
	KeyMCertificateStorage [P]
	KeyMCertCsmSignatureGenerateJobRef [R, 0..1]
	KeyMCertCsmSignatureVerifyJobRef [R, 1]
	KeyMCertCsmSignatureVerifyKeyRef [R, 1]
	KeyMCertificateCsmKeyTargetRef [R, 0..1]
	KeyMCertificateNvmBlockRef [R, 0..1]
	KeyMCertUpperHierarchicalCertRef [R, 1]

	KeyMCertificateElement [C, 0..*]
		
```
###### `KeyMCertificate`
---
```
Path: KeyMCertificate/KeyMCertificateStorage
Description: Specifies storage location of certificate.

Possible value(s):
	KEYM_STORAGE_IN_CSM
	KEYM_STORAGE_IN_NVM
	KEYM_STORAGE_IN_RAM
```

```
Path: KeyMCertificate/KeyMCertificateCsmKeyTargetRef
Description: References 'CsmKey' where certificate is stored, if 'KeyMCertificateStorage' is set to 'KEYM_STORAGE_IN_CSM'.
```
## References
---
[1] Specification of Key Manager, AUTOSAR Classic Platform, R20-11