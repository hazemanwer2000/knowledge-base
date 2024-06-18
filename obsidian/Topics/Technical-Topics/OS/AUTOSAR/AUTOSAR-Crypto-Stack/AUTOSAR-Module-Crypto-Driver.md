──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Crypto Driver* module, which resides in the MCAL layer, in functionality, API and configuration.
### Specification
---
### Function(s)
---
#### API(s)
---
###### `Crypto_Init`
---
```
Name: 'Crypto_Init'
Description: Initializes module.
Sync/Async: Sync
Re-entrant: No
```
#### Scheduled Function(s)
---
###### `Crypto_MainFunction`
---
```
Name: 'Crypto_MainFunction'
Description: If there are async. jobs, and job queuing is supported, this function is called cyclically to process queued jobs. 
```
### Configuration
---
```
CryptoGeneral [C, 1]
	CryptoInstanceId [P]
	CryptoMainFunctionPeriod [P]

CryptoDriverObjects [C, 1]

	CryptoDriverObject [C, 0..*]
		CryptoDriverObjectId [P]
		CryptoQueueSize [P]
		CryptoPrimitiveRef [R, 1..*]

CryptoKeys [C, 1]

	CryptoKey [C, 1..*]
		CryptoKeyId [P]
		CryptoKeyTypeRef [R, 1]

CryptoKeyTypes [C, 1]

	CryptoKeyType [C, 1..*]
		CryptoKeyElementRef [R, 1..*]

CryptoKeyElements [C, 1]

	CryptoKeyElement [C, 1..*]
		CryptoKeyElementAllowPartialAccess [P]
		CryptoKeyElementFormat [P]
		CryptoKeyElementInitValue [P]
		CryptoKeyElementPersist [P]
		CryptoKeyElementReadAccess [P]
		CryptoKeyElementWriteAccess [P]
		CryptoKeyElementSize [P]

CryptoPrimitives [C, 1]

	CryptoPrimitive [C, 1..*]
		CryptoPrimitiveService [P]
		CryptoPrimitiveAlgorithmFamily [P, 1..*]
		CryptoPrimitiveAlgorithnMode [P, 1..*]
		CryptoPrimitiveAlgorithnSecondaryFamily [P, 1..*]
		CryptoPrimitiveAlgorithmFamilyCustomRef [R, 0..*]
		CryptoPrimitiveAlgorithmModeCustomRef [R, 0..*]
		CryptoPrimitiveAlgorithmSecondaryFamilyCustomRef [R, 0..*]

	CryptoPrimitiveAlgorithmFamilyCustom [C, 0..*]
		CryptoPrimitiveAlgorithmFamilyCustomId [P]

	CryptoPrimitiveAlgorithmModeCustom [C, 0..*]
		CryptoPrimitiveAlgorithmModeCustomId [P]
```
###### `CryptoKeyElement`
---
```
Path: CryptoKeyElements/CryptoKeyElement/CryptoKeyElementAllowPartialAccess
Description: Enables reading/writing to a key element, with data smaller than its size.
```

```
Path: CryptoKeyElements/CryptoKeyElement/CryptoKeyElementFormat
Description: Specifies format representation of key material, when extracted/read from the driver.

Possible value(s):
	CRYPTO_KE_FORMAT_BIN_OCTET
	...
```

```
Path: CryptoKeyElements/CryptoKeyElement/CryptoKeyElementInitValue
Description: Specifies initial value, used to fill key element upon start-up, if key element is non-persistent, or persistent but has never been written before.
```

```
Path: CryptoKeyElements/CryptoKeyElement/CryptoKeyElementReadAccess
Description: Defines read-access to a key-element.

Possible value(s):
	CRYPTO_RA_ALLOWED - Readable as plain-text.
	CRYPTO_RA_ENCRYPTED - Readable encrypted.
	CRYPTO_RA_INTERNAL_COPY - Can be copied to another key element, internally.
	CRYPTO_RA_DENIED - Not readable.
```

```
Path: CryptoKeyElements/CryptoKeyElement/CryptoKeyElementWriteAccess
Description: Defines write-access to a key-element.

Possible value(s):
	CRYPTO_WA_ALLOWED - Writeable as plain-text.
	CRYPTO_RA_ENCRYPTED - Writeable encrypted.
	CRYPTO_RA_INTERNAL_COPY - Can be copied into from another key element, internally.
	CRYPTO_RA_DENIED - Not writeable.
```
## References
---
[1] ...