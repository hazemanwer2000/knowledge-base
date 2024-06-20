──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
- [[#Specification|Specification]]
- [[#Function(s)|Function(s)]]
	- [[#Function(s)#API(s)|API(s)]]
	- [[#Function(s)#Scheduled Function(s)|Scheduled Function(s)]]
- [[#Configuration|Configuration]]
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Crypto Driver* module, which resides in the MCAL layer, in functionality, API and configuration.
### Specification
---
The module allows the configuration of *Crypto Driver Objects*,
* each representing a hardware, or software resource (e.g., AES accelerator).
* Each object references different primitives, that it is capable of performing (e.g., AES-CMAC, SHA-1, etc).
* Hence, each object may have its own queue of pending jobs, and,
* the driver should be capable of executing *N* jobs in parallel, where *N* is the number of objects available.

For job processing, the *Crypto Driver* supports,
* Synchronous and asynchronous processing, and,
* `START-UPDATE-FINISH` operation mode(s), of which multiple may be requested at once.

The following is the state machine of a job.

![[AUTOSAR-Crypto-Driver-Job-State-Machine.png|600]]

*Note:* The same job cannot be triggered while still being processed. However, while not currently being processed, and having `START` or `UPDATE` previously triggered, a job can be restarted, with all current (in-/out-)put data discarded, if triggered with `START` operation mode.

*Note:* A Crypto Driver Object is considered busy still, if a job has been triggered with the `START` operation mode, and not yet the `FINISH` operation mode. 
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
###### `Crypto_ProcessJob`
---
```
Name: 'Crypto_ProcessJob'
Description: Triggers the processing of a job.
Sync/Async: Depends on CSM Job config.
Re-entrant: Re-entrant, but not for the same Crypto Driver Object.
Parameters (in):
	[1] Crypto Driver Object ID.
Parameters (in-out):
	[1] Pointer to CSM Job.
```
###### `Crypto_CancelJob`
---
```
Name: 'Crypto_CancelJob'
Description: Cancels the processing of a job.
Sync/Async: Sync.
Re-entrant: Re-entrant, but not for the same Crypto Driver Object.
Parameters (in):
	[1] Crypto Driver Object ID.
Parameters (in-out):
	[1] Pointer to CSM Job.
```
##### Key Management
---

| API                          | Description                                                                                                          |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| Crypto_KeyElementSet         | Writes key element, and sets associated key state as `INVALID`.                                                      |
| Crypto_KeyElementGet         | Reads key element.                                                                                                   |
| Crypto_KeySetValid           | Sets key state as `VALID`.                                                                                           |
| Crypto_KeySetInvalid         | Sets key state as `INVALID`.                                                                                         |
| Crypto_KeyGetStatus          | Queries key state, `VALID` or `INVALID`.                                                                             |
| Crypto_KeyDerive             | Derives key (i.e., using PRNG), using a given password, and salt (i.e., random value).                               |
| Crypto_KeyGenerate           | Generates key (e.g., asymmetric ECC key-pair).                                                                       |
| Crypto_KeyExchangeCalcPubVal | For ECDH, generates key (e.g., asymmetric ECC key-pair), and returns public key.                                     |
| Crypto_KeyExchangeCalcSecret | For ECDH, uses passed argument (i.e., peer's public key), and referenced private key, to derive shared secret value. |
| Crypto_RandomSeed            | For PRNG, generates a new seed value, based on passed argument.                                                      |
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
		CryptoKeyElementId [P]

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

```
Path: CryptoKeyElements/CryptoKeyElement/CryptoKeyElementId
Description: Identifies the usage of the key element (e.g., key material, IV, etc).
```

*Note:* Refer to [2], for the list of appropriate ID value(s) for each key-element, per usage (e.g., encryption, signature generation, etc).
## References
---
[1] Specification of Crypto Driver, AUTOSAR Classic Platform, R20-11
[2] Specification of Crypto Service Manager, AUTOSAR Classic Platform, R20-11