──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Specification|Specification]]
- [[#Function(s)|Function(s)]]
	- [[#Function(s)#Scheduled|Scheduled]]
		- [[#`KeyM_MainFunction`|`KeyM_MainFunction`]]
		- [[#`KeyM_MainBackgroundFunction`|`KeyM_MainBackgroundFunction`]]
	- [[#Function(s)#API(s)|API(s)]]
		- [[#`KeyM_Init`|`KeyM_Init`]]
		- [[#`KeyM_SetCertificate`|`KeyM_SetCertificate`]]
		- [[#`KeyM_VerifyCertificate`|`KeyM_VerifyCertificate`]]
		- [[#`KeyM_VerifyCertificateChain`|`KeyM_VerifyCertificateChain`]]
		- [[#`KeyM_VerifyCertificates`|`KeyM_VerifyCertificates`]]
		- [[#`KeyM_CertGetStatus`|`KeyM_CertGetStatus`]]
		- [[#`KeyM_GetCertificate`|`KeyM_GetCertificate`]]
		- [[#`KeyM_CertElementGet`|`KeyM_CertElementGet`]]
		- [[#`KeyM_Deinit`|`KeyM_Deinit`]]
- [[#Configuration|Configuration]]
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Key Manager (KeyM)* module, which resides in the Service layer, in functionality, API and configuration.

The *KeyM* module can be divided into two sub-modules: crypto-key sub-module, and certificate sub-module.

*Note:* The crypto-key sub-module is not discussed within this document.
### Specification
---
The following figure illustrates the references between different configured certificate(s) in the *KeyM*, and associated job(s) and key(s) in the *Csm*.

![[AUTOSAR-KeyM-Csm-Cfg.png|900]]

To install a certificate:
* `KeyM_SetCertificate` is called, to set and trigger parsing of certificate.
	* Before this call, the status of the certificate is `KEYM_CERTIFICATE_NOT_AVAILABLE` (unless it was previously set, or read from non-volatile memory).
	* After this call, the status of the certificate is `KEYM_CERTIFICATE_NOT_PARSED`.
	* If parsing completes successfully, which executes in the background, the status becomes `KEYM_CERTIFICATE_PARSED_NOT_VALIDATED`.
* `KeyM_Verify<...>` is called, to verify certificate asynchronously.
	* If successful, the status of the certificate becomes `KEYM_CERTIFICATE_VALID`.

*Note:* More than one certificate can be verified at once, if they are all set, form a certificate-chain, and verification is requested on the lowest hierarchal certificate.
### Function(s)
---
#### Scheduled
---
###### `KeyM_MainFunction`
---
```
Name: 'KeyM_MainFunction'
Description: Handles cyclic activities.
```
###### `KeyM_MainBackgroundFunction`
---
```
Name: 'KeyM_MainBackgroundFunction'
Description: Handles cyclic activities, that should execute in a background task.
```
#### API(s)
---
###### `KeyM_Init`
---
```
Name: 'KeyM_Init'
Description: Initializes module, including loading of certificates from non-volatile memory (if present).
Sync/Async: Sync.
Re-entrant: Not re-entrant.
Parameters (in):
	[1] Pointer to cfg.
```
###### `KeyM_SetCertificate`
---
```
Name: 'KeyM_SetCertificate'
Description: Sets certificate, triggers parsing of certificate.
Sync/Async: Sync.
Re-entrant: Not re-entrant.
Parameters (in):
	[1] Cert. ID
	[2] Cert. {length, buffer} Pointer 
```
###### `KeyM_VerifyCertificate`
---
```
Name: 'KeyM_VerifyCertificate'
Description: Triggers verification of certificate, with 'KeyM_SetCertificate' called previously.
				Any unverified certificate in its chain is also verified, top-to-bottom.
				If configured, a callback is called upon conclusion.
Sync/Async: Async.
Re-entrant: Not re-entrant.
Parameters (in):
	[1] Cert. ID
```
###### `KeyM_VerifyCertificateChain`
---
```
Name: 'KeyM_VerifyCertificateChain'
Description: Similar to 'KeyM_VerifyCertificate', but allows for the verification of unconfigured, intermediate certificates, as part of the chain.
Sync/Async: Async.
Re-entrant: Not re-entrant.
Parameters (in):
	[1] Cert. ID
	[2] Pointer to additional certificate(s)
	[3] No. of additional certificate(s)
```

###### `KeyM_VerifyCertificates`
---
```
Name: 'KeyM_VerifyCertificates'
Description: Verifies one certificate against another, irrelevant of the configured hierarchy.
				If the upper cert. is not verified already, an error is returned.
				If configured, a callback is called upon conclusion.
Sync/Async: Async.
Re-entrant: Not re-entrant.
Parameters (in):
	[1] Cert. ID
	[1] Upper Cert. ID
```
###### `KeyM_CertGetStatus`
---
```
Name: 'KeyM_CertGetStatus'
Description: Returns the status of a specific cert.
Sync/Async: Sync.
Re-entrant: Not re-entrant.
Parameters (in):
	[1] Cert. ID
```
###### `KeyM_GetCertificate`
---
```
Name: 'KeyM_GetCertificate'
Description: Gets a certificate.
Sync/Async: Sync.
Re-entrant: Not re-entrant.
Parameters (in):
	[1] Cert. ID
Parameters (in-out):
	[1] Cert. {length, buffer} Pointer 
```
###### `KeyM_CertElementGet`
---
```
Name: 'KeyM_CertElementGet'
Description: Gets a certificate element.
Sync/Async: Sync.
Re-entrant: Not re-entrant.
Parameters (in):
	[1] Cert. ID
	[2] Cert. element ID
Parameters (in-out):
	[1] Pointer to cert. element length
Parameters (out):
	[1] Pointer to cert. element buffer
```
###### `KeyM_Deinit`
---
```
Name: 'KeyM_Deinit'
Description: De-initializes module, including the active destruction of all data in RAM.
Sync/Async: Sync.
Re-entrant: Not re-entrant.
```
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
		KeyMCertificateElementOfStructure [P]
		KeyMCertificateElementObjectId [P, 0..1]
		KeyMCertificateElementMaxLength [P]
		KeyMCertificateElementId [P]
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
###### `KeyMCertificateElement`
---
```
Path: KeyMCertificate/KeyMCertificateElement/KeyMCertificateElementOfStructure
Description: Specifies certificate element to search within.

Possible value(s):
	CertificateIssuerName
	CertificateSubjectName
	CertificateSerialNumber
	CertificateSignatureAlgorithm
	...
```
## References
---
[1] Specification of Key Manager, AUTOSAR Classic Platform, R20-11