──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Ethernet Driver* module, which resides in the MCAL layer, in functionality, API and configuration.
### Function(s)
---

| Name                    | Type | Description                                                                                                                            |
| ----------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `Eth_Init`              | API  | Initialize module.                                                                                                                     |
| `Eth_GetPhysAddr`       | API  | Get assigned physical (i.e., MAC) address.                                                                                             |
| `Eth_SetPhysAddr`       | API  | Set physical (i.e., MAC) address.                                                                                                      |
| `Eth_SetControllerMode` | API  | Set controller mode, either `ACTIVE` or `DOWN`.                                                                                        |
| `Eth_GetControllerMode` | API  | Get controller mode.                                                                                                                   |
| `Eth_WriteMii`          | API  | Writes a PHY's register.                                                                                                               |
| `Eth_ReadMii`           | API  | Reads a PHY's register.                                                                                                                |
| `Eth_ProvideTxBuffer`   | API  | Allocates a TX buffer, to be used with `Eth_Transmit`.                                                                                 |
| `Eth_Transmit`          | API  | Triggers transmission of a TX buffer, specifying if confirmation is required.                                                          |
| `Eth_TxConfirmation`    | API  | Checks the status of all previous transmissions, and calls `EthIf_TxConfirmation` for each, if previously specified by `Eth_Transmit`. |
| `Eth_Receive`           | API  | Checks pending receptions, calls `EthIf_RxIndication` once, and indicates if more receptions are pending.                              |

*Note:* `Eth_TxConfirmation` is called in the `EthIf_MainFunctionTx`, if TX interrupt is disabled for the corresponding controller.

*Note:* `Eth_Receive` is called, repeatedly, in the `EthIf_MainFunctionRx`, if RX interrupt is disabled for the corresponding controller.
### Configuration
---
```
EthConfigSet [C, 1]

	EthCtrlConfig [C, 1..*]
		EthCtrlEnableMii [P]
		EthCtrlEnableRxInterrupt [P]
		EthCtrlEnableTxInterrupt [P]
		EthCtrlIdx [P]
		EthCtrlMacLayerSpeed [P]
		EthCtrlMacLayerSubType [P]
		EthCtrlMacLayerType [P]
		EthCtrlPhyAddress [P]

EthGeneral [C, 1]
	EthIndex [P]
	EthMainFunctionPeriod [P]
	EthMaxCtrlsSupported [P]

	EthCtrlOffloading [C, 1]
		EthCtrlEnableOffloadChecksumICMP [P]
		EthCtrlEnableOffloadChecksumIPv4 [P]
		EthCtrlEnableOffloadChecksumTCP [P]
		EthCtrlEnableOffloadChecksumUDP [P]
```
###### `EthCtrlConfig`
---
```
Path: EthConfigSet/EthCtrlConfig/EthCtrlEnableMii
Description: Enables the 'Eth_ReadMii' and 'Eth_WriteMii' API(s).
```

```
Path: EthConfigSet/EthCtrlConfig/EthCtrlMacLayerSpeed
Description: Specifies the baud rate.

Possible value(s):
	ETH_MAC_LAYER_SPEED_10M
	ETH_MAC_LAYER_SPEED_100M
	ETH_MAC_LAYER_SPEED_1G
	...
```

```
Path: EthConfigSet/EthCtrlConfig/EthCtrlMacLayerSubType
Description: Specifies the type of interface to the PHY hardware.

Possible value(s):
	STANDARD
	REDUCED
	...
```

```
Path: EthConfigSet/EthCtrlConfig/EthCtrlMacLayerType
Description: Specifies the type of interface to the PHY hardware.

Possible value(s):
	ETH_MAC_LAYER_TYPE_XMII
	ETH_MAC_LAYER_TYPE_XGMII
	...
```
## References
---
[1] Specification of Ethernet Driver, AUTOSAR Classic Platform, R20-11