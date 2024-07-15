──────── *for more from the author, visit* [github.com/hazemanwer2000](https://github.com/hazemanwer2000). ────────
## *Table of Contents*
...
## Content
---
*AUTOSAR* specifies a *Basic Software (BSW) Service Discovery (Sd)* module, in functionality, API and configuration [1].

It is responsible for the realization of the SOME/IP-SD protocol [2].
### Specification
---
#### SOME/IP-SD
---
##### Header Format
---
SOME/IP-SD messages are sent as SOME/IP messages. Hence, a SOME/IP header precedes the SOME/IP-SD header, and consists of, most notably,
* Service ID, fixed to `0xFFFF`.
* Method/Event/Field ID, fixed to `0x8100`.
* Request ID, consists of,
	* Client ID, fixed to `0x0`.
		* *Note:* Only a single SD client may reside within an ECU.
	* Session ID, increments per SD message sent, per client.
		* *Note:* Even though SD message(s) are `NOTIFICATION`(s), the Session ID must be used.
* Interface Version, fixed to `0x1`.
* Message Type, fixed to `NOTIFICATION`.

The SD header format, as shown below, consists of,
* Flags (Size: 1 byte)
	* Reboot flag (Position: 7), which is initially set, and is reset after the Session ID wraps for the first time.
		* *Note:* A reboot of an SD client is detected if either,
			* Reboot flag transitions from `0` to `1`.
			* Reboot flag remains `1`, and the Session ID, let it be ($X$), ($X_{n+1} > X_n$) is not true.
* Variable number of entries.
* Variable number of option(s).

![[SOME-IP-SD-Header-Format.png|725]]

*Note:* SOME/IP-SD messages must be sent over UDP.
##### Entry Types
---
###### Type-1
---
The format of an SD Type-1 Entry, as shown below, consists most notably of,
* Type (Size: 1 byte), which may be,
	* `FindService`
	* `(Stop)OfferService`
* First/Second Option(s) Run Index (Size: 2x1 byte)
* First/Second Option(s) Run Length (Size: 2x1 nibble)
* Time-To-Live (Size: 3 bytes), which denotes the length of time this entry is valid for.

![[SOME-IP-SD-Entry-Type-1.png|650]]

*Note:* An Option Run is a sequential number of option(s) in the Option(s) Array, referenced via an index and length.

*Note:* A TTL with value 0 denotes a `Stop<...>` Entry.

*Note:* The presence of all binary 1's in any relevant field (e.g., Minor Version), denotes the acceptance of any value, or selection of all value(s), for that field.
###### Type-2
---
The format of an SD Type-2 Entry, as shown below, differs from a Type-1 entry in,
* Type (Size: 1 byte), which may be,
	* `(Stop)SubscribeEventgroup`
	* `SubscribeEventgroup(N)Ack`
* Counter (Size: 1 nibble), which is used to differentiate between identical subscription(s), with differing End-point option(s). When unused, it shall be 0.
* Event-Group ID (Size: 2 bytes)
	* *Note:* An event-group is a grouping of different event(s) and field(s), to be received as `NOTIFICATION`(s).

![[SOME-IP-SD-Entry-Type-2.png|650]]

*Note:* For `SubscribeEventgroup(N)Ack` entries, a TTL with value 0 denotes a `SubscribeEventgroupNack` Entry.
##### Option Types
---
###### IPv4 Endpoint
---
The following is the format of an IPv4 Endpoint Option.
* An `OfferService` Entry must reference an IPv4 Endpoint Option, to denote the end-point of the service-instance.
* A `SubscribeEventgroup` must reference an IPv4 Endpoint Option, to denote the end-point of the client.

*Note:* Upon subscription, non-`NOTIFICATION` SOME/IP message(s) shall be sent as Unicast traffic, between the end-point(s) of the service-instance and the client.

![[SOME-IP-SD-Option-Endpoint-IPv4.png|725]]

Additionally, the following variation(s) of the IPv4 Endpoint Option exist, that differ only in the Type field,
* IPv4 Multi-cast Endpoint Option, which may be included in the `SubscribeEventgroupAck` Entry, to denote a Multi-cast Endpoint to which `NOTIFICATION`(s) may be sent (see below).
### Server(s)
---
A server-service may be in one of the following state(s) (i.e., `SD_SERVER_SERVICE_<...>`),
* `DOWN`, default after `Sd_Init` is called, and `SdServerServiceAutoAvailable` is set to false.
* `AVAILABLE`, if `SdServerServiceAutoAvailable` is set to true.

*Note:* `Sd_ServerServiceSetState` may be used to alter the state of a server-service.

After a server-service is `AVAILABLE`, it enters the Initial-Wait phase.
* It shall remain in this phase for a random time-delay, between `SdServerTimerInitialOfferDelayMax` and `SdServerTimerInitialOfferDelayMin`, before sending its first `OfferService` Entry and transitioning to the Repetition phase.
* While in this phase, received `FindService` Entries shall be discarded.

Upon entering the Repetition phase,
* `for i in range(SdServerTimerInitialOfferRepetitionsMax):`
	* `delay((i+1) * SdServerTimerInitialOfferRepetitionBaseDelay)`
	* Send `OfferService` Entry (as Multi-cast traffic).
* Finally, a transition to the Main phase occurs.
* While in this phase, received `FindService` Entries shall be responded to (as Uni-cast traffic).

Upon entering the Main phase,
* `if SdServerTimerOfferCyclicDelay > 0:`
	* `while(True):`
		* `delay(SdServerTimerOfferCyclicDelay)`
		* Send `OfferService` Entry (as Multi-cast traffic).

While in either the Repetition or Main phase(s),
* `SubscribeEventgroup` Entries are responded to.
	* For UDP, as an example,
		* End-point of the server-service is the local IP-address and port of `SdServerServiceUdpRef`.
		* Socket connection(s) in `SdServerServiceUdpRef` are used for Unicast traffic with subscriber(s).
	* For Multi-cast,
		* End-point of the Multi-cast traffic is the remote IP-address and port of `SdMulticastEventSoConRef`.
		* `switch (SdEventHandlerMulticastThreshold):`
			* `case 0:`
				* `NOTIFICATION(s)` are always sent as Unicast traffic.
			* `case 1:`
				* `NOTIFICATION(s)` are always sent as Multi-cast traffic.
			* `case N:`
				* `if subscribersCount < N`:
					* `NOTIFICATION(s)` are sent as Unicast traffic.
				* `else:`
					* `NOTIFICATION(s)` are sent as Multi-cast traffic.
	* `<...>ActivationRef` are different routing-group(s), to be enabled/disabled in different context(s).
	* `<...>TriggeringRef` are different routing-group(s), used to trigger the sending of initial field value(s).
	* If any event-handler has at least one subscriber, it transitions from the `RELEASED` to the `REQUESTED` state.
### Client(s)
---
A client-service may be in one of the following state(s) (i.e., `SD_CLIENT_SERVICE_<...>`),
* `RELEASED`, default after `Sd_Init` is called, and `SdClientServiceAutoRequire` is set to false.
* `REQUESTED`, if `SdClientServiceAutoRequire` is set to true.

*Note:* `Sd_ClientServiceSetState` may be used to alter the state of a client-service.

An event-group may be in one of the following state(s) (i.e., `SD_CONSUMED_EVENT_GROUP_<...>`),
* `RELEASED`, default after `Sd_Init` is called, and `SdConsumedEventGroupAutoRequired` is set to false.
* `REQUESTED`, if `SdConsumedEventGroupAutoRequired` is set to true, as soon as the associated client-service is `REQUESTED`.

*Note:* `Sd_ConsumedEventGroupSetState` may be used to alter the state of an event-group.
### Configuration
---
```
SdConfig [C, 1]

	SdInstance [C, 0..*]

		SdClientService [C, 0..*]
			SdClientServiceHandleId [P]
			SdClientServiceAutoRequire [P]
			SdClientServiceId [P]
			SdClientServiceInstanceId [P]
			SdClientServiceMajorVersion [P]
			SdClientServiceMinorVersion [P]
			SdClientServiceUdpRef [R, 0..1]
			SdClientServiceTcpRef [R, 0..1]
			SdClientServiceTimerRef [R, 1]
			SdServiceGroupRef [R, 0..*]

			SdConsumedEventGroup [C, 0..*]
				SdConsumedEventGroupHandleId [P]
				SdConsumedEventGroupAutoRequire [P]
				SdConsumedEventGroupId [P]
				SdConsumedEventGroupUdpActivationRef [R, 0..1]
				SdConsumedEventGroupTcpActivationRef [R, 0..1]
				SdConsumedEventGroupMulticastGroupRef [R, 0..1]
				SdConsumedEventGroupMulticastActivationRef [R, 0..1]
				SdConsumedEventGroupTimerRef [R, 1]

			SdConsumedMethods [C, 0..1]
				SdClientServiceActivationRef [R, 1]

		SdClientTimer [C, 0..*]
			SdClientTimerInitialFindDelayMax [P]
			SdClientTimerInitialFindDelayMin [P]
			SdClientTimerInitialFindRepetitionsBaseDelay [P]
			SdClientTimerInitialFindRepetitionsMax [P]
			SdClientTimerRequestResponseMaxDelay [P]
			SdClientTimerRequestResponseMinDelay [P]
			SdClientTimerTTL [P]
			SdSubscribeEventgroupRetryDelay [P]
			SdSubscribeEventgroupRetryMax [P]

		SdServerService [C, 0..*]
			SdServerServiceHandleId [P]
			SdServerServiceAutoAvailable [P]
			SdServerServiceId [P]
			SdServerServiceInstanceId [P]
			SdServerServiceMajorVersion [P]
			SdServerServiceMinorVersion [P]
			SdServerServiceTcpRef [R, 0..1]
			SdServerServiceUdpRef [R, 0..1]
			SdServerServiceTimerRef [R, 1]
			SdServerGroupRef [R, 0..*]

			SdEventHandler [C, 0..*]
				SdEventHandlerHandleId [P]
				SdEventHandlerMulticastThreshold [P]
				SdEventHandlerTimerRef [R, 1]

				SdEventHandlerMulticast [C, 0..1]
					SdEventActivationRef [R, 1]
					SdMulticastEventSoConRef [R, 1]

				SdEventHandlerTcp [C, 0..1]
					SdEventActivationRef [R, 1]
					SdEventTriggeringRef [R, 1]

				SdEventHandlerUdp [C, 0..1]
					SdEventActivationRef [R, 1]
					SdEventTriggeringRef [R, 1]

			SdProvidedMethods [C, 0..1]
				SdServerServiceActivationRef [R, 1]

		SdServerTimer [C, 0..*]
			SdServerTimerInitialOfferDelayMax [P]
			SdServerTimerInitialOfferDelayMin [P]
			SdServerTimerInitialOfferRepetitionBaseDelay [P]
			SdServerTimerInitialOfferRepetitionsMax [P]
			SdServerTimerOfferCyclicDelay [P]
			SdServerTimerRequestResponseMaxDelay [P]
			SdServerTimerRequestResponseMinDelay [P]
			SdServerTimerTTL [P]

		SdInstanceTxPdu [C, 1]
			SdTxPduRef [R, 1]

		SdInstanceUnicastRxPdu [C, 1]
			SdRxPduRef [R, 1]

		SdInstanceMulticastRxPdu [C, 1]
			SdRxPduRef [R, 1]

	SdServiceGroup [C, 0..*]
		SdServiceGroupHandleId [P]

SdGeneral [C, 1]
	SdMainFunctionCycleTime [P]
	SdSubscribeEventgroupRetryEnable [P]
```
## References
---
[1] Specification of Socket Adaptor module, AUTOSAR Classic Platform, R20-11
[2] SOME/IP-SD Protocol Specification, AUTOSAR Classic Platform, R22-11