──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Ethernet Interface* module, in functionality, API and configuration.
### Specification
---
The module allows the configuration of virtual controller(s).
* Each virtual controller is associated with a unique VLAN ID (i.e., 1:1 relationship).
* Each virtual controller references a specific physical controller from the ethernet driver.
* Upper-layer module(s) deal with virtual controller(s).
* `EthIf_GetVlanId` may be used to query the VLAN ID associated with a specific virtual controller.

Upon the reception, or successful transmission, of a frame, the appropriate RX indication, or TX confirmation, function is called, based on the frame's *EtherType* (see `EthIfFrameOwnerConfig`).
### Function(s)
---

| Name                      | Type      | Description                                                                                                                                                  |
| ------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `EthIf_Init`              | API       | Initialize module.                                                                                                                                           |
| `EthIf_GetPhysAddr`       | API       | Get assigned physical (i.e., MAC) address.                                                                                                                   |
| `EthIf_SetPhysAddr`       | API       | Set physical (i.e., MAC) address.                                                                                                                            |
| `EthIf_SetControllerMode` | API       | Set virtual controller's mode. If all virtual controller(s) associated with a physical controller are set to `DOWN` mode, `Eth_SetControllerMode` is called. |
| `EthIf_GetControllerMode` | API       | Get virtual controller's mode.                                                                                                                               |
| `EthIf_GetVlanId`         | API       | Get VLAN ID, associated with a virtual controller.                                                                                                           |
| `EthIf_ProvideTxBuffer`   | API       | Pseudo-wrapper call, to `Eth_ProvideTxBuffer`.                                                                                                               |
| `EthIf_Transmit`          | API       | Pseudo-wrapper call, to `EthIf_Transmit`.                                                                                                                    |
| `EthIf_MainFunctionRx`    | Scheduled | If RX interrupt is disabled, calls `Eth_Receive` repeatedly.                                                                                                 |
| `EthIf_MainFunctionTx`    | Scheduled | If TX interrupt is disabled, calls `Eth_TxConfirmation`.                                                                                                     |
| `EthIf_RxIndication`      | Callback  | Called by the Ethernet Driver, to indicate the reception of a frame.                                                                                         |
| `EthIf_TxConfirmation`    | Callback  | Called by the Ethernet Driver, to confirm the transmission of a frame.                                                                                       |
### Configuration
---
```
EthIfConfigSet [C, 1]

	EthIfController [C, 1..*]
		EthIfCtrlIdx [P]
		EthIfCtrlMtu [P]
		EthIfVlanId [P, 0..1]
		EthIfPhysControllerRef [R, 1]

	EthIfPhysController [C, 1..*]
		EthIfPhysControllerIdx [P]
		EthIfEthCtrlRef [R, 1]

	EthIfFrameOwnerConfig [C, 0..*]
		EthIfFrameType [P]
		EthIfRxIndicationConfigRef [R, 0..1]
		EthIfTxConfirmationConfigRef [R, 0..1]

	EthIfRxIndicationConfig [C, 0..*]
		EthIfRxIndicationFunction [P]

	EthIfTxConfirmationConfig [C, 0..*]
		EthIfTxConfirmationFunction [P]

EthIfGeneral [C, 1]
	EthIfMainFunctionPeriod [P]
```
###### `EthIfFrameOwnerConfig`
---
```
Path: EthIfConfigSet/EthIfFrameOwnerConfig/EthIfFrameType
Description: Specifies the frame's 'EtherType' (e.g., IPv4, ARP).
```
## References
---
[1] Specification of Ethernet Interface module, AUTOSAR Classic Platform, R20-11