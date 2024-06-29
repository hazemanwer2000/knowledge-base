──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Ethernet Interface* module, in functionality, API and configuration.
### Specification
---

### Function(s)
---

| Name                      | Type      | Description                                                                                                                                                  |
| ------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `EthIf_Init`              | API       | Initialize module.                                                                                                                                           |
| `Eth_GetPhysAddr`         | API       | Get assigned physical (i.e., MAC) address.                                                                                                                   |
| `Eth_SetPhysAddr`         | API       | Set physical (i.e., MAC) address.                                                                                                                            |
| `EthIf_SetControllerMode` | API       | Set virtual controller's mode. If all virtual controller(s) associated with a physical controller are set to `DOWN` mode, `Eth_SetControllerMode` is called. |
| `EthIf_GetControllerMode` | API       | Get virtual controller's mode.                                                                                                                               |
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
###### `EthCtrlConfig`
---
```
Path: EthIfGeneral/EthIfRxIndicationInterations
Description: Specifies number of 'Eth_Receive' call(s) per 'EthIf_MainFunctionRx' call, if RX interrupt is disabled.
```
###### `EthIfFrameOwnerConfig`
---
```
Path: EthIfConfigSet/EthIfFrameOwnerConfig/EthIfFrameType
Description: Specifies the frame's 'EtherType' (e.g., IPv4, ARP).
```
## References
---
[1] ...