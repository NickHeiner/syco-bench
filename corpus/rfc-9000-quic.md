# RFC 9000: QUIC: A UDP-Based Multiplexed and Secure Transport

RFC 9000 QUIC Transport Protocol May 2021
Iyengar & Thomson Standards Track[Page]

Stream:Internet Engineering Task Force (IETF)RFC:[9000](https://www.rfc-editor.org/rfc/rfc9000)Category:Standards Track Published:May 2021 ISSN:2070-1721 Authors:

J. Iyengar, Ed.

Fastly

M. Thomson, Ed.

Mozilla

# RFC 9000

# QUIC: A UDP-Based Multiplexed and Secure Transport

## [Abstract](https://www.rfc-editor.org/rfc/rfc9000#abstract)

This document defines the core of the QUIC transport protocol. QUIC provides applications with flow-controlled streams for structured communication, low-latency connection establishment, and network path migration. QUIC includes security measures that ensure confidentiality, integrity, and availability in a range of deployment circumstances. Accompanying documents describe the integration of TLS for key negotiation, loss detection, and an exemplary congestion control algorithm.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-abstract-1)

## [Status of This Memo](https://www.rfc-editor.org/rfc/rfc9000#name-status-of-this-memo)

This is an Internet Standards Track document.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-boilerplate.1-1)

This document is a product of the Internet Engineering Task Force (IETF). It represents the consensus of the IETF community. It has received public review and has been approved for publication by the Internet Engineering Steering Group (IESG). Further information on Internet Standards is available in Section 2 of RFC 7841.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-boilerplate.1-2)

Information about the current status of this document, any errata, and how to provide feedback on it may be obtained at [https://www.rfc-editor.org/info/rfc9000](https://www.rfc-editor.org/info/rfc9000).[¶](https://www.rfc-editor.org/rfc/rfc9000#section-boilerplate.1-3)

## [Copyright Notice](https://www.rfc-editor.org/rfc/rfc9000#name-copyright-notice)

Copyright (c) 2021 IETF Trust and the persons identified as the document authors. All rights reserved.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-boilerplate.2-1)

This document is subject to BCP 78 and the IETF Trust's Legal Provisions Relating to IETF Documents ([https://trustee.ietf.org/license-info](https://trustee.ietf.org/license-info)) in effect on the date of publication of this document. Please review these documents carefully, as they describe your rights and restrictions with respect to this document. Code Components extracted from this document must include Simplified BSD License text as described in Section 4.e of the Trust Legal Provisions and are provided without warranty as described in the Simplified BSD License.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-boilerplate.2-2)

[▲](https://www.rfc-editor.org/rfc/rfc9000#)
## [Table of Contents](https://www.rfc-editor.org/rfc/rfc9000#name-table-of-contents)

*   [1](https://www.rfc-editor.org/rfc/rfc9000#section-1).[Overview](https://www.rfc-editor.org/rfc/rfc9000#name-overview)

    *   [1.1](https://www.rfc-editor.org/rfc/rfc9000#section-1.1).[Document Structure](https://www.rfc-editor.org/rfc/rfc9000#name-document-structure)

    *   [1.2](https://www.rfc-editor.org/rfc/rfc9000#section-1.2).[Terms and Definitions](https://www.rfc-editor.org/rfc/rfc9000#name-terms-and-definitions)

    *   [1.3](https://www.rfc-editor.org/rfc/rfc9000#section-1.3).[Notational Conventions](https://www.rfc-editor.org/rfc/rfc9000#name-notational-conventions)

*   [2](https://www.rfc-editor.org/rfc/rfc9000#section-2).[Streams](https://www.rfc-editor.org/rfc/rfc9000#name-streams)

    *   [2.1](https://www.rfc-editor.org/rfc/rfc9000#section-2.1).[Stream Types and Identifiers](https://www.rfc-editor.org/rfc/rfc9000#name-stream-types-and-identifier)

    *   [2.2](https://www.rfc-editor.org/rfc/rfc9000#section-2.2).[Sending and Receiving Data](https://www.rfc-editor.org/rfc/rfc9000#name-sending-and-receiving-data)

    *   [2.3](https://www.rfc-editor.org/rfc/rfc9000#section-2.3).[Stream Prioritization](https://www.rfc-editor.org/rfc/rfc9000#name-stream-prioritization)

    *   [2.4](https://www.rfc-editor.org/rfc/rfc9000#section-2.4).[Operations on Streams](https://www.rfc-editor.org/rfc/rfc9000#name-operations-on-streams)

*   [3](https://www.rfc-editor.org/rfc/rfc9000#section-3).[Stream States](https://www.rfc-editor.org/rfc/rfc9000#name-stream-states)

    *   [3.1](https://www.rfc-editor.org/rfc/rfc9000#section-3.1).[Sending Stream States](https://www.rfc-editor.org/rfc/rfc9000#name-sending-stream-states)

    *   [3.2](https://www.rfc-editor.org/rfc/rfc9000#section-3.2).[Receiving Stream States](https://www.rfc-editor.org/rfc/rfc9000#name-receiving-stream-states)

    *   [3.3](https://www.rfc-editor.org/rfc/rfc9000#section-3.3).[Permitted Frame Types](https://www.rfc-editor.org/rfc/rfc9000#name-permitted-frame-types)

    *   [3.4](https://www.rfc-editor.org/rfc/rfc9000#section-3.4).[Bidirectional Stream States](https://www.rfc-editor.org/rfc/rfc9000#name-bidirectional-stream-states)

    *   [3.5](https://www.rfc-editor.org/rfc/rfc9000#section-3.5).[Solicited State Transitions](https://www.rfc-editor.org/rfc/rfc9000#name-solicited-state-transitions)

*   [4](https://www.rfc-editor.org/rfc/rfc9000#section-4).[Flow Control](https://www.rfc-editor.org/rfc/rfc9000#name-flow-control)

    *   [4.1](https://www.rfc-editor.org/rfc/rfc9000#section-4.1).[Data Flow Control](https://www.rfc-editor.org/rfc/rfc9000#name-data-flow-control)

    *   [4.2](https://www.rfc-editor.org/rfc/rfc9000#section-4.2).[Increasing Flow Control Limits](https://www.rfc-editor.org/rfc/rfc9000#name-increasing-flow-control-lim)

    *   [4.3](https://www.rfc-editor.org/rfc/rfc9000#section-4.3).[Flow Control Performance](https://www.rfc-editor.org/rfc/rfc9000#name-flow-control-performance)

    *   [4.4](https://www.rfc-editor.org/rfc/rfc9000#section-4.4).[Handling Stream Cancellation](https://www.rfc-editor.org/rfc/rfc9000#name-handling-stream-cancellatio)

    *   [4.5](https://www.rfc-editor.org/rfc/rfc9000#section-4.5).[Stream Final Size](https://www.rfc-editor.org/rfc/rfc9000#name-stream-final-size)

    *   [4.6](https://www.rfc-editor.org/rfc/rfc9000#section-4.6).[Controlling Concurrency](https://www.rfc-editor.org/rfc/rfc9000#name-controlling-concurrency)

*   [5](https://www.rfc-editor.org/rfc/rfc9000#section-5).[Connections](https://www.rfc-editor.org/rfc/rfc9000#name-connections)

    *   [5.1](https://www.rfc-editor.org/rfc/rfc9000#section-5.1).[Connection ID](https://www.rfc-editor.org/rfc/rfc9000#name-connection-id)

        *   [5.1.1](https://www.rfc-editor.org/rfc/rfc9000#section-5.1.1).[Issuing Connection IDs](https://www.rfc-editor.org/rfc/rfc9000#name-issuing-connection-ids)

        *   [5.1.2](https://www.rfc-editor.org/rfc/rfc9000#section-5.1.2).[Consuming and Retiring Connection IDs](https://www.rfc-editor.org/rfc/rfc9000#name-consuming-and-retiring-conn)

    *   [5.2](https://www.rfc-editor.org/rfc/rfc9000#section-5.2).[Matching Packets to Connections](https://www.rfc-editor.org/rfc/rfc9000#name-matching-packets-to-connect)

        *   [5.2.1](https://www.rfc-editor.org/rfc/rfc9000#section-5.2.1).[Client Packet Handling](https://www.rfc-editor.org/rfc/rfc9000#name-client-packet-handling)

        *   [5.2.2](https://www.rfc-editor.org/rfc/rfc9000#section-5.2.2).[Server Packet Handling](https://www.rfc-editor.org/rfc/rfc9000#name-server-packet-handling)

        *   [5.2.3](https://www.rfc-editor.org/rfc/rfc9000#section-5.2.3).[Considerations for Simple Load Balancers](https://www.rfc-editor.org/rfc/rfc9000#name-considerations-for-simple-l)

    *   [5.3](https://www.rfc-editor.org/rfc/rfc9000#section-5.3).[Operations on Connections](https://www.rfc-editor.org/rfc/rfc9000#name-operations-on-connections)

*   [6](https://www.rfc-editor.org/rfc/rfc9000#section-6).[Version Negotiation](https://www.rfc-editor.org/rfc/rfc9000#name-version-negotiation)

    *   [6.1](https://www.rfc-editor.org/rfc/rfc9000#section-6.1).[Sending Version Negotiation Packets](https://www.rfc-editor.org/rfc/rfc9000#name-sending-version-negotiation)

    *   [6.2](https://www.rfc-editor.org/rfc/rfc9000#section-6.2).[Handling Version Negotiation Packets](https://www.rfc-editor.org/rfc/rfc9000#name-handling-version-negotiatio)

    *   [6.3](https://www.rfc-editor.org/rfc/rfc9000#section-6.3).[Using Reserved Versions](https://www.rfc-editor.org/rfc/rfc9000#name-using-reserved-versions)

*   [7](https://www.rfc-editor.org/rfc/rfc9000#section-7).[Cryptographic and Transport Handshake](https://www.rfc-editor.org/rfc/rfc9000#name-cryptographic-and-transport)

    *   [7.1](https://www.rfc-editor.org/rfc/rfc9000#section-7.1).[Example Handshake Flows](https://www.rfc-editor.org/rfc/rfc9000#name-example-handshake-flows)

    *   [7.2](https://www.rfc-editor.org/rfc/rfc9000#section-7.2).[Negotiating Connection IDs](https://www.rfc-editor.org/rfc/rfc9000#name-negotiating-connection-ids)

    *   [7.3](https://www.rfc-editor.org/rfc/rfc9000#section-7.3).[Authenticating Connection IDs](https://www.rfc-editor.org/rfc/rfc9000#name-authenticating-connection-i)

    *   [7.4](https://www.rfc-editor.org/rfc/rfc9000#section-7.4).[Transport Parameters](https://www.rfc-editor.org/rfc/rfc9000#name-transport-parameters)

        *   [7.4.1](https://www.rfc-editor.org/rfc/rfc9000#section-7.4.1).[Values of Transport Parameters for 0-RTT](https://www.rfc-editor.org/rfc/rfc9000#name-values-of-transport-paramet)

        *   [7.4.2](https://www.rfc-editor.org/rfc/rfc9000#section-7.4.2).[New Transport Parameters](https://www.rfc-editor.org/rfc/rfc9000#name-new-transport-parameters)

    *   [7.5](https://www.rfc-editor.org/rfc/rfc9000#section-7.5).[Cryptographic Message Buffering](https://www.rfc-editor.org/rfc/rfc9000#name-cryptographic-message-buffe)

*   [8](https://www.rfc-editor.org/rfc/rfc9000#section-8).[Address Validation](https://www.rfc-editor.org/rfc/rfc9000#name-address-validation)

    *   [8.1](https://www.rfc-editor.org/rfc/rfc9000#section-8.1).[Address Validation during Connection Establishment](https://www.rfc-editor.org/rfc/rfc9000#name-address-validation-during-c)

        *   [8.1.1](https://www.rfc-editor.org/rfc/rfc9000#section-8.1.1).[Token Construction](https://www.rfc-editor.org/rfc/rfc9000#name-token-construction)

        *   [8.1.2](https://www.rfc-editor.org/rfc/rfc9000#section-8.1.2).[Address Validation Using Retry Packets](https://www.rfc-editor.org/rfc/rfc9000#name-address-validation-using-re)

        *   [8.1.3](https://www.rfc-editor.org/rfc/rfc9000#section-8.1.3).[Address Validation for Future Connections](https://www.rfc-editor.org/rfc/rfc9000#name-address-validation-for-futu)

        *   [8.1.4](https://www.rfc-editor.org/rfc/rfc9000#section-8.1.4).[Address Validation Token Integrity](https://www.rfc-editor.org/rfc/rfc9000#name-address-validation-token-in)

    *   [8.2](https://www.rfc-editor.org/rfc/rfc9000#section-8.2).[Path Validation](https://www.rfc-editor.org/rfc/rfc9000#name-path-validation)

        *   [8.2.1](https://www.rfc-editor.org/rfc/rfc9000#section-8.2.1).[Initiating Path Validation](https://www.rfc-editor.org/rfc/rfc9000#name-initiating-path-validation)

        *   [8.2.2](https://www.rfc-editor.org/rfc/rfc9000#section-8.2.2).[Path Validation Responses](https://www.rfc-editor.org/rfc/rfc9000#name-path-validation-responses)

        *   [8.2.3](https://www.rfc-editor.org/rfc/rfc9000#section-8.2.3).[Successful Path Validation](https://www.rfc-editor.org/rfc/rfc9000#name-successful-path-validation)

        *   [8.2.4](https://www.rfc-editor.org/rfc/rfc9000#section-8.2.4).[Failed Path Validation](https://www.rfc-editor.org/rfc/rfc9000#name-failed-path-validation)

*   [9](https://www.rfc-editor.org/rfc/rfc9000#section-9).[Connection Migration](https://www.rfc-editor.org/rfc/rfc9000#name-connection-migration)

    *   [9.1](https://www.rfc-editor.org/rfc/rfc9000#section-9.1).[Probing a New Path](https://www.rfc-editor.org/rfc/rfc9000#name-probing-a-new-path)

    *   [9.2](https://www.rfc-editor.org/rfc/rfc9000#section-9.2).[Initiating Connection Migration](https://www.rfc-editor.org/rfc/rfc9000#name-initiating-connection-migra)

    *   [9.3](https://www.rfc-editor.org/rfc/rfc9000#section-9.3).[Responding to Connection Migration](https://www.rfc-editor.org/rfc/rfc9000#name-responding-to-connection-mi)

        *   [9.3.1](https://www.rfc-editor.org/rfc/rfc9000#section-9.3.1).[Peer Address Spoofing](https://www.rfc-editor.org/rfc/rfc9000#name-peer-address-spoofing)

        *   [9.3.2](https://www.rfc-editor.org/rfc/rfc9000#section-9.3.2).[On-Path Address Spoofing](https://www.rfc-editor.org/rfc/rfc9000#name-on-path-address-spoofing)

        *   [9.3.3](https://www.rfc-editor.org/rfc/rfc9000#section-9.3.3).[Off-Path Packet Forwarding](https://www.rfc-editor.org/rfc/rfc9000#name-off-path-packet-forwarding)

    *   [9.4](https://www.rfc-editor.org/rfc/rfc9000#section-9.4).[Loss Detection and Congestion Control](https://www.rfc-editor.org/rfc/rfc9000#name-loss-detection-and-congesti)

    *   [9.5](https://www.rfc-editor.org/rfc/rfc9000#section-9.5).[Privacy Implications of Connection Migration](https://www.rfc-editor.org/rfc/rfc9000#name-privacy-implications-of-con)

    *   [9.6](https://www.rfc-editor.org/rfc/rfc9000#section-9.6).[Server's Preferred Address](https://www.rfc-editor.org/rfc/rfc9000#name-servers-preferred-address)

        *   [9.6.1](https://www.rfc-editor.org/rfc/rfc9000#section-9.6.1).[Communicating a Preferred Address](https://www.rfc-editor.org/rfc/rfc9000#name-communicating-a-preferred-a)

        *   [9.6.2](https://www.rfc-editor.org/rfc/rfc9000#section-9.6.2).[Migration to a Preferred Address](https://www.rfc-editor.org/rfc/rfc9000#name-migration-to-a-preferred-ad)

        *   [9.6.3](https://www.rfc-editor.org/rfc/rfc9000#section-9.6.3).[Interaction of Client Migration and Preferred Address](https://www.rfc-editor.org/rfc/rfc9000#name-interaction-of-client-migra)

    *   [9.7](https://www.rfc-editor.org/rfc/rfc9000#section-9.7).[Use of IPv6 Flow Label and Migration](https://www.rfc-editor.org/rfc/rfc9000#name-use-of-ipv6-flow-label-and-)

*   [10](https://www.rfc-editor.org/rfc/rfc9000#section-10).[Connection Termination](https://www.rfc-editor.org/rfc/rfc9000#name-connection-termination)

    *   [10.1](https://www.rfc-editor.org/rfc/rfc9000#section-10.1).[Idle Timeout](https://www.rfc-editor.org/rfc/rfc9000#name-idle-timeout)

        *   [10.1.1](https://www.rfc-editor.org/rfc/rfc9000#section-10.1.1).[Liveness Testing](https://www.rfc-editor.org/rfc/rfc9000#name-liveness-testing)

        *   [10.1.2](https://www.rfc-editor.org/rfc/rfc9000#section-10.1.2).[Deferring Idle Timeout](https://www.rfc-editor.org/rfc/rfc9000#name-deferring-idle-timeout)

    *   [10.2](https://www.rfc-editor.org/rfc/rfc9000#section-10.2).[Immediate Close](https://www.rfc-editor.org/rfc/rfc9000#name-immediate-close)

        *   [10.2.1](https://www.rfc-editor.org/rfc/rfc9000#section-10.2.1).[Closing Connection State](https://www.rfc-editor.org/rfc/rfc9000#name-closing-connection-state)

        *   [10.2.2](https://www.rfc-editor.org/rfc/rfc9000#section-10.2.2).[Draining Connection State](https://www.rfc-editor.org/rfc/rfc9000#name-draining-connection-state)

        *   [10.2.3](https://www.rfc-editor.org/rfc/rfc9000#section-10.2.3).[Immediate Close during the Handshake](https://www.rfc-editor.org/rfc/rfc9000#name-immediate-close-during-the-)

    *   [10.3](https://www.rfc-editor.org/rfc/rfc9000#section-10.3).[Stateless Reset](https://www.rfc-editor.org/rfc/rfc9000#name-stateless-reset)

        *   [10.3.1](https://www.rfc-editor.org/rfc/rfc9000#section-10.3.1).[Detecting a Stateless Reset](https://www.rfc-editor.org/rfc/rfc9000#name-detecting-a-stateless-reset)

        *   [10.3.2](https://www.rfc-editor.org/rfc/rfc9000#section-10.3.2).[Calculating a Stateless Reset Token](https://www.rfc-editor.org/rfc/rfc9000#name-calculating-a-stateless-res)

        *   [10.3.3](https://www.rfc-editor.org/rfc/rfc9000#section-10.3.3).[Looping](https://www.rfc-editor.org/rfc/rfc9000#name-looping)

*   [11](https://www.rfc-editor.org/rfc/rfc9000#section-11).[Error Handling](https://www.rfc-editor.org/rfc/rfc9000#name-error-handling)

    *   [11.1](https://www.rfc-editor.org/rfc/rfc9000#section-11.1).[Connection Errors](https://www.rfc-editor.org/rfc/rfc9000#name-connection-errors)

    *   [11.2](https://www.rfc-editor.org/rfc/rfc9000#section-11.2).[Stream Errors](https://www.rfc-editor.org/rfc/rfc9000#name-stream-errors)

*   [12](https://www.rfc-editor.org/rfc/rfc9000#section-12).[Packets and Frames](https://www.rfc-editor.org/rfc/rfc9000#name-packets-and-frames)

    *   [12.1](https://www.rfc-editor.org/rfc/rfc9000#section-12.1).[Protected Packets](https://www.rfc-editor.org/rfc/rfc9000#name-protected-packets)

    *   [12.2](https://www.rfc-editor.org/rfc/rfc9000#section-12.2).[Coalescing Packets](https://www.rfc-editor.org/rfc/rfc9000#name-coalescing-packets)

    *   [12.3](https://www.rfc-editor.org/rfc/rfc9000#section-12.3).[Packet Numbers](https://www.rfc-editor.org/rfc/rfc9000#name-packet-numbers)

    *   [12.4](https://www.rfc-editor.org/rfc/rfc9000#section-12.4).[Frames and Frame Types](https://www.rfc-editor.org/rfc/rfc9000#name-frames-and-frame-types)

    *   [12.5](https://www.rfc-editor.org/rfc/rfc9000#section-12.5).[Frames and Number Spaces](https://www.rfc-editor.org/rfc/rfc9000#name-frames-and-number-spaces)

*   [13](https://www.rfc-editor.org/rfc/rfc9000#section-13).[Packetization and Reliability](https://www.rfc-editor.org/rfc/rfc9000#name-packetization-and-reliabili)

    *   [13.1](https://www.rfc-editor.org/rfc/rfc9000#section-13.1).[Packet Processing](https://www.rfc-editor.org/rfc/rfc9000#name-packet-processing)

    *   [13.2](https://www.rfc-editor.org/rfc/rfc9000#section-13.2).[Generating Acknowledgments](https://www.rfc-editor.org/rfc/rfc9000#name-generating-acknowledgments)

        *   [13.2.1](https://www.rfc-editor.org/rfc/rfc9000#section-13.2.1).[Sending ACK Frames](https://www.rfc-editor.org/rfc/rfc9000#name-sending-ack-frames)

        *   [13.2.2](https://www.rfc-editor.org/rfc/rfc9000#section-13.2.2).[Acknowledgment Frequency](https://www.rfc-editor.org/rfc/rfc9000#name-acknowledgment-frequency)

        *   [13.2.3](https://www.rfc-editor.org/rfc/rfc9000#section-13.2.3).[Managing ACK Ranges](https://www.rfc-editor.org/rfc/rfc9000#name-managing-ack-ranges)

        *   [13.2.4](https://www.rfc-editor.org/rfc/rfc9000#section-13.2.4).[Limiting Ranges by Tracking ACK Frames](https://www.rfc-editor.org/rfc/rfc9000#name-limiting-ranges-by-tracking)

        *   [13.2.5](https://www.rfc-editor.org/rfc/rfc9000#section-13.2.5).[Measuring and Reporting Host Delay](https://www.rfc-editor.org/rfc/rfc9000#name-measuring-and-reporting-hos)

        *   [13.2.6](https://www.rfc-editor.org/rfc/rfc9000#section-13.2.6).[ACK Frames and Packet Protection](https://www.rfc-editor.org/rfc/rfc9000#name-ack-frames-and-packet-prote)

        *   [13.2.7](https://www.rfc-editor.org/rfc/rfc9000#section-13.2.7).[PADDING Frames Consume Congestion Window](https://www.rfc-editor.org/rfc/rfc9000#name-padding-frames-consume-cong)

    *   [13.3](https://www.rfc-editor.org/rfc/rfc9000#section-13.3).[Retransmission of Information](https://www.rfc-editor.org/rfc/rfc9000#name-retransmission-of-informati)

    *   [13.4](https://www.rfc-editor.org/rfc/rfc9000#section-13.4).[Explicit Congestion Notification](https://www.rfc-editor.org/rfc/rfc9000#name-explicit-congestion-notific)

        *   [13.4.1](https://www.rfc-editor.org/rfc/rfc9000#section-13.4.1).[Reporting ECN Counts](https://www.rfc-editor.org/rfc/rfc9000#name-reporting-ecn-counts)

        *   [13.4.2](https://www.rfc-editor.org/rfc/rfc9000#section-13.4.2).[ECN Validation](https://www.rfc-editor.org/rfc/rfc9000#name-ecn-validation)

*   [14](https://www.rfc-editor.org/rfc/rfc9000#section-14).[Datagram Size](https://www.rfc-editor.org/rfc/rfc9000#name-datagram-size)

    *   [14.1](https://www.rfc-editor.org/rfc/rfc9000#section-14.1).[Initial Datagram Size](https://www.rfc-editor.org/rfc/rfc9000#name-initial-datagram-size)

    *   [14.2](https://www.rfc-editor.org/rfc/rfc9000#section-14.2).[Path Maximum Transmission Unit](https://www.rfc-editor.org/rfc/rfc9000#name-path-maximum-transmission-u)

        *   [14.2.1](https://www.rfc-editor.org/rfc/rfc9000#section-14.2.1).[Handling of ICMP Messages by PMTUD](https://www.rfc-editor.org/rfc/rfc9000#name-handling-of-icmp-messages-b)

    *   [14.3](https://www.rfc-editor.org/rfc/rfc9000#section-14.3).[Datagram Packetization Layer PMTU Discovery](https://www.rfc-editor.org/rfc/rfc9000#name-datagram-packetization-laye)

        *   [14.3.1](https://www.rfc-editor.org/rfc/rfc9000#section-14.3.1).[DPLPMTUD and Initial Connectivity](https://www.rfc-editor.org/rfc/rfc9000#name-dplpmtud-and-initial-connec)

        *   [14.3.2](https://www.rfc-editor.org/rfc/rfc9000#section-14.3.2).[Validating the Network Path with DPLPMTUD](https://www.rfc-editor.org/rfc/rfc9000#name-validating-the-network-path)

        *   [14.3.3](https://www.rfc-editor.org/rfc/rfc9000#section-14.3.3).[Handling of ICMP Messages by DPLPMTUD](https://www.rfc-editor.org/rfc/rfc9000#name-handling-of-icmp-messages-by)

    *   [14.4](https://www.rfc-editor.org/rfc/rfc9000#section-14.4).[Sending QUIC PMTU Probes](https://www.rfc-editor.org/rfc/rfc9000#name-sending-quic-pmtu-probes)

        *   [14.4.1](https://www.rfc-editor.org/rfc/rfc9000#section-14.4.1).[PMTU Probes Containing Source Connection ID](https://www.rfc-editor.org/rfc/rfc9000#name-pmtu-probes-containing-sour)

*   [15](https://www.rfc-editor.org/rfc/rfc9000#section-15).[Versions](https://www.rfc-editor.org/rfc/rfc9000#name-versions)

*   [16](https://www.rfc-editor.org/rfc/rfc9000#section-16).[Variable-Length Integer Encoding](https://www.rfc-editor.org/rfc/rfc9000#name-variable-length-integer-enc)

*   [17](https://www.rfc-editor.org/rfc/rfc9000#section-17).[Packet Formats](https://www.rfc-editor.org/rfc/rfc9000#name-packet-formats)

    *   [17.1](https://www.rfc-editor.org/rfc/rfc9000#section-17.1).[Packet Number Encoding and Decoding](https://www.rfc-editor.org/rfc/rfc9000#name-packet-number-encoding-and-)

    *   [17.2](https://www.rfc-editor.org/rfc/rfc9000#section-17.2).[Long Header Packets](https://www.rfc-editor.org/rfc/rfc9000#name-long-header-packets)

        *   [17.2.1](https://www.rfc-editor.org/rfc/rfc9000#section-17.2.1).[Version Negotiation Packet](https://www.rfc-editor.org/rfc/rfc9000#name-version-negotiation-packet)

        *   [17.2.2](https://www.rfc-editor.org/rfc/rfc9000#section-17.2.2).[Initial Packet](https://www.rfc-editor.org/rfc/rfc9000#name-initial-packet)

        *   [17.2.3](https://www.rfc-editor.org/rfc/rfc9000#section-17.2.3).[0-RTT](https://www.rfc-editor.org/rfc/rfc9000#name-0-rtt)

        *   [17.2.4](https://www.rfc-editor.org/rfc/rfc9000#section-17.2.4).[Handshake Packet](https://www.rfc-editor.org/rfc/rfc9000#name-handshake-packet)

        *   [17.2.5](https://www.rfc-editor.org/rfc/rfc9000#section-17.2.5).[Retry Packet](https://www.rfc-editor.org/rfc/rfc9000#name-retry-packet)

    *   [17.3](https://www.rfc-editor.org/rfc/rfc9000#section-17.3).[Short Header Packets](https://www.rfc-editor.org/rfc/rfc9000#name-short-header-packets)

        *   [17.3.1](https://www.rfc-editor.org/rfc/rfc9000#section-17.3.1).[1-RTT Packet](https://www.rfc-editor.org/rfc/rfc9000#name-1-rtt-packet)

    *   [17.4](https://www.rfc-editor.org/rfc/rfc9000#section-17.4).[Latency Spin Bit](https://www.rfc-editor.org/rfc/rfc9000#name-latency-spin-bit)

*   [18](https://www.rfc-editor.org/rfc/rfc9000#section-18).[Transport Parameter Encoding](https://www.rfc-editor.org/rfc/rfc9000#name-transport-parameter-encodin)

    *   [18.1](https://www.rfc-editor.org/rfc/rfc9000#section-18.1).[Reserved Transport Parameters](https://www.rfc-editor.org/rfc/rfc9000#name-reserved-transport-paramete)

    *   [18.2](https://www.rfc-editor.org/rfc/rfc9000#section-18.2).[Transport Parameter Definitions](https://www.rfc-editor.org/rfc/rfc9000#name-transport-parameter-definit)

*   [19](https://www.rfc-editor.org/rfc/rfc9000#section-19).[Frame Types and Formats](https://www.rfc-editor.org/rfc/rfc9000#name-frame-types-and-formats)

    *   [19.1](https://www.rfc-editor.org/rfc/rfc9000#section-19.1).[PADDING Frames](https://www.rfc-editor.org/rfc/rfc9000#name-padding-frames)

    *   [19.2](https://www.rfc-editor.org/rfc/rfc9000#section-19.2).[PING Frames](https://www.rfc-editor.org/rfc/rfc9000#name-ping-frames)

    *   [19.3](https://www.rfc-editor.org/rfc/rfc9000#section-19.3).[ACK Frames](https://www.rfc-editor.org/rfc/rfc9000#name-ack-frames)

        *   [19.3.1](https://www.rfc-editor.org/rfc/rfc9000#section-19.3.1).[ACK Ranges](https://www.rfc-editor.org/rfc/rfc9000#name-ack-ranges)

        *   [19.3.2](https://www.rfc-editor.org/rfc/rfc9000#section-19.3.2).[ECN Counts](https://www.rfc-editor.org/rfc/rfc9000#name-ecn-counts)

    *   [19.4](https://www.rfc-editor.org/rfc/rfc9000#section-19.4).[RESET_STREAM Frames](https://www.rfc-editor.org/rfc/rfc9000#name-reset_stream-frames)

    *   [19.5](https://www.rfc-editor.org/rfc/rfc9000#section-19.5).[STOP_SENDING Frames](https://www.rfc-editor.org/rfc/rfc9000#name-stop_sending-frames)

    *   [19.6](https://www.rfc-editor.org/rfc/rfc9000#section-19.6).[CRYPTO Frames](https://www.rfc-editor.org/rfc/rfc9000#name-crypto-frames)

    *   [19.7](https://www.rfc-editor.org/rfc/rfc9000#section-19.7).[NEW_TOKEN Frames](https://www.rfc-editor.org/rfc/rfc9000#name-new_token-frames)

    *   [19.8](https://www.rfc-editor.org/rfc/rfc9000#section-19.8).[STREAM Frames](https://www.rfc-editor.org/rfc/rfc9000#name-stream-frames)

    *   [19.9](https://www.rfc-editor.org/rfc/rfc9000#section-19.9).[MAX_DATA Frames](https://www.rfc-editor.org/rfc/rfc9000#name-max_data-frames)

    *   [19.10](https://www.rfc-editor.org/rfc/rfc9000#section-19.10).[MAX_STREAM_DATA Frames](https://www.rfc-editor.org/rfc/rfc9000#name-max_stream_data-frames)

    *   [19.11](https://www.rfc-editor.org/rfc/rfc9000#section-19.11).[MAX_STREAMS Frames](https://www.rfc-editor.org/rfc/rfc9000#name-max_streams-frames)

    *   [19.12](https://www.rfc-editor.org/rfc/rfc9000#section-19.12).[DATA_BLOCKED Frames](https://www.rfc-editor.org/rfc/rfc9000#name-data_blocked-frames)

    *   [19.13](https://www.rfc-editor.org/rfc/rfc9000#section-19.13).[STREAM_DATA_BLOCKED Frames](https://www.rfc-editor.org/rfc/rfc9000#name-stream_data_blocked-frames)

    *   [19.14](https://www.rfc-editor.org/rfc/rfc9000#section-19.14).[STREAMS_BLOCKED Frames](https://www.rfc-editor.org/rfc/rfc9000#name-streams_blocked-frames)

    *   [19.15](https://www.rfc-editor.org/rfc/rfc9000#section-19.15).[NEW_CONNECTION_ID Frames](https://www.rfc-editor.org/rfc/rfc9000#name-new_connection_id-frames)

    *   [19.16](https://www.rfc-editor.org/rfc/rfc9000#section-19.16).[RETIRE_CONNECTION_ID Frames](https://www.rfc-editor.org/rfc/rfc9000#name-retire_connection_id-frames)

    *   [19.17](https://www.rfc-editor.org/rfc/rfc9000#section-19.17).[PATH_CHALLENGE Frames](https://www.rfc-editor.org/rfc/rfc9000#name-path_challenge-frames)

    *   [19.18](https://www.rfc-editor.org/rfc/rfc9000#section-19.18).[PATH_RESPONSE Frames](https://www.rfc-editor.org/rfc/rfc9000#name-path_response-frames)

    *   [19.19](https://www.rfc-editor.org/rfc/rfc9000#section-19.19).[CONNECTION_CLOSE Frames](https://www.rfc-editor.org/rfc/rfc9000#name-connection_close-frames)

    *   [19.20](https://www.rfc-editor.org/rfc/rfc9000#section-19.20).[HANDSHAKE_DONE Frames](https://www.rfc-editor.org/rfc/rfc9000#name-handshake_done-frames)

    *   [19.21](https://www.rfc-editor.org/rfc/rfc9000#section-19.21).[Extension Frames](https://www.rfc-editor.org/rfc/rfc9000#name-extension-frames)

*   [20](https://www.rfc-editor.org/rfc/rfc9000#section-20).[Error Codes](https://www.rfc-editor.org/rfc/rfc9000#name-error-codes)

    *   [20.1](https://www.rfc-editor.org/rfc/rfc9000#section-20.1).[Transport Error Codes](https://www.rfc-editor.org/rfc/rfc9000#name-transport-error-codes)

    *   [20.2](https://www.rfc-editor.org/rfc/rfc9000#section-20.2).[Application Protocol Error Codes](https://www.rfc-editor.org/rfc/rfc9000#name-application-protocol-error-)

*   [21](https://www.rfc-editor.org/rfc/rfc9000#section-21).[Security Considerations](https://www.rfc-editor.org/rfc/rfc9000#name-security-considerations)

    *   [21.1](https://www.rfc-editor.org/rfc/rfc9000#section-21.1).[Overview of Security Properties](https://www.rfc-editor.org/rfc/rfc9000#name-overview-of-security-proper)

        *   [21.1.1](https://www.rfc-editor.org/rfc/rfc9000#section-21.1.1).[Handshake](https://www.rfc-editor.org/rfc/rfc9000#name-handshake)

        *   [21.1.2](https://www.rfc-editor.org/rfc/rfc9000#section-21.1.2).[Protected Packets](https://www.rfc-editor.org/rfc/rfc9000#name-protected-packets-2)

        *   [21.1.3](https://www.rfc-editor.org/rfc/rfc9000#section-21.1.3).[Connection Migration](https://www.rfc-editor.org/rfc/rfc9000#name-connection-migration-2)

    *   [21.2](https://www.rfc-editor.org/rfc/rfc9000#section-21.2).[Handshake Denial of Service](https://www.rfc-editor.org/rfc/rfc9000#name-handshake-denial-of-service)

    *   [21.3](https://www.rfc-editor.org/rfc/rfc9000#section-21.3).[Amplification Attack](https://www.rfc-editor.org/rfc/rfc9000#name-amplification-attack)

    *   [21.4](https://www.rfc-editor.org/rfc/rfc9000#section-21.4).[Optimistic ACK Attack](https://www.rfc-editor.org/rfc/rfc9000#name-optimistic-ack-attack)

    *   [21.5](https://www.rfc-editor.org/rfc/rfc9000#section-21.5).[Request Forgery Attacks](https://www.rfc-editor.org/rfc/rfc9000#name-request-forgery-attacks)

        *   [21.5.1](https://www.rfc-editor.org/rfc/rfc9000#section-21.5.1).[Control Options for Endpoints](https://www.rfc-editor.org/rfc/rfc9000#name-control-options-for-endpoin)

        *   [21.5.2](https://www.rfc-editor.org/rfc/rfc9000#section-21.5.2).[Request Forgery with Client Initial Packets](https://www.rfc-editor.org/rfc/rfc9000#name-request-forgery-with-client)

        *   [21.5.3](https://www.rfc-editor.org/rfc/rfc9000#section-21.5.3).[Request Forgery with Preferred Addresses](https://www.rfc-editor.org/rfc/rfc9000#name-request-forgery-with-prefer)

        *   [21.5.4](https://www.rfc-editor.org/rfc/rfc9000#section-21.5.4).[Request Forgery with Spoofed Migration](https://www.rfc-editor.org/rfc/rfc9000#name-request-forgery-with-spoofe)

        *   [21.5.5](https://www.rfc-editor.org/rfc/rfc9000#section-21.5.5).[Request Forgery with Version Negotiation](https://www.rfc-editor.org/rfc/rfc9000#name-request-forgery-with-versio)

        *   [21.5.6](https://www.rfc-editor.org/rfc/rfc9000#section-21.5.6).[Generic Request Forgery Countermeasures](https://www.rfc-editor.org/rfc/rfc9000#name-generic-request-forgery-cou)

    *   [21.6](https://www.rfc-editor.org/rfc/rfc9000#section-21.6).[Slowloris Attacks](https://www.rfc-editor.org/rfc/rfc9000#name-slowloris-attacks)

    *   [21.7](https://www.rfc-editor.org/rfc/rfc9000#section-21.7).[Stream Fragmentation and Reassembly Attacks](https://www.rfc-editor.org/rfc/rfc9000#name-stream-fragmentation-and-re)

    *   [21.8](https://www.rfc-editor.org/rfc/rfc9000#section-21.8).[Stream Commitment Attack](https://www.rfc-editor.org/rfc/rfc9000#name-stream-commitment-attack)

    *   [21.9](https://www.rfc-editor.org/rfc/rfc9000#section-21.9).[Peer Denial of Service](https://www.rfc-editor.org/rfc/rfc9000#name-peer-denial-of-service)

    *   [21.10](https://www.rfc-editor.org/rfc/rfc9000#section-21.10).[Explicit Congestion Notification Attacks](https://www.rfc-editor.org/rfc/rfc9000#name-explicit-congestion-notifica)

    *   [21.11](https://www.rfc-editor.org/rfc/rfc9000#section-21.11).[Stateless Reset Oracle](https://www.rfc-editor.org/rfc/rfc9000#name-stateless-reset-oracle)

    *   [21.12](https://www.rfc-editor.org/rfc/rfc9000#section-21.12).[Version Downgrade](https://www.rfc-editor.org/rfc/rfc9000#name-version-downgrade)

    *   [21.13](https://www.rfc-editor.org/rfc/rfc9000#section-21.13).[Targeted Attacks by Routing](https://www.rfc-editor.org/rfc/rfc9000#name-targeted-attacks-by-routing)

    *   [21.14](https://www.rfc-editor.org/rfc/rfc9000#section-21.14).[Traffic Analysis](https://www.rfc-editor.org/rfc/rfc9000#name-traffic-analysis)

*   [22](https://www.rfc-editor.org/rfc/rfc9000#section-22).[IANA Considerations](https://www.rfc-editor.org/rfc/rfc9000#name-iana-considerations)

    *   [22.1](https://www.rfc-editor.org/rfc/rfc9000#section-22.1).[Registration Policies for QUIC Registries](https://www.rfc-editor.org/rfc/rfc9000#name-registration-policies-for-q)

        *   [22.1.1](https://www.rfc-editor.org/rfc/rfc9000#section-22.1.1).[Provisional Registrations](https://www.rfc-editor.org/rfc/rfc9000#name-provisional-registrations)

        *   [22.1.2](https://www.rfc-editor.org/rfc/rfc9000#section-22.1.2).[Selecting Codepoints](https://www.rfc-editor.org/rfc/rfc9000#name-selecting-codepoints)

        *   [22.1.3](https://www.rfc-editor.org/rfc/rfc9000#section-22.1.3).[Reclaiming Provisional Codepoints](https://www.rfc-editor.org/rfc/rfc9000#name-reclaiming-provisional-code)

        *   [22.1.4](https://www.rfc-editor.org/rfc/rfc9000#section-22.1.4).[Permanent Registrations](https://www.rfc-editor.org/rfc/rfc9000#name-permanent-registrations)

    *   [22.2](https://www.rfc-editor.org/rfc/rfc9000#section-22.2).[QUIC Versions Registry](https://www.rfc-editor.org/rfc/rfc9000#name-quic-versions-registry)

    *   [22.3](https://www.rfc-editor.org/rfc/rfc9000#section-22.3).[QUIC Transport Parameters Registry](https://www.rfc-editor.org/rfc/rfc9000#name-quic-transport-parameters-r)

    *   [22.4](https://www.rfc-editor.org/rfc/rfc9000#section-22.4).[QUIC Frame Types Registry](https://www.rfc-editor.org/rfc/rfc9000#name-quic-frame-types-registry)

    *   [22.5](https://www.rfc-editor.org/rfc/rfc9000#section-22.5).[QUIC Transport Error Codes Registry](https://www.rfc-editor.org/rfc/rfc9000#name-quic-transport-error-codes-)

*   [23](https://www.rfc-editor.org/rfc/rfc9000#section-23).[References](https://www.rfc-editor.org/rfc/rfc9000#name-references)

    *   [23.1](https://www.rfc-editor.org/rfc/rfc9000#section-23.1).[Normative References](https://www.rfc-editor.org/rfc/rfc9000#name-normative-references)

    *   [23.2](https://www.rfc-editor.org/rfc/rfc9000#section-23.2).[Informative References](https://www.rfc-editor.org/rfc/rfc9000#name-informative-references)

*   [Appendix A](https://www.rfc-editor.org/rfc/rfc9000#section-appendix.a).[Pseudocode](https://www.rfc-editor.org/rfc/rfc9000#name-pseudocode)

    *   [A.1](https://www.rfc-editor.org/rfc/rfc9000#section-a.1).[Sample Variable-Length Integer Decoding](https://www.rfc-editor.org/rfc/rfc9000#name-sample-variable-length-inte)

    *   [A.2](https://www.rfc-editor.org/rfc/rfc9000#section-a.2).[Sample Packet Number Encoding Algorithm](https://www.rfc-editor.org/rfc/rfc9000#name-sample-packet-number-encodi)

    *   [A.3](https://www.rfc-editor.org/rfc/rfc9000#section-a.3).[Sample Packet Number Decoding Algorithm](https://www.rfc-editor.org/rfc/rfc9000#name-sample-packet-number-decodi)

    *   [A.4](https://www.rfc-editor.org/rfc/rfc9000#section-a.4).[Sample ECN Validation Algorithm](https://www.rfc-editor.org/rfc/rfc9000#name-sample-ecn-validation-algor)

*   [](https://www.rfc-editor.org/rfc/rfc9000#section-appendix.b)[Contributors](https://www.rfc-editor.org/rfc/rfc9000#name-contributors)

*   [](https://www.rfc-editor.org/rfc/rfc9000#section-appendix.c)[Authors' Addresses](https://www.rfc-editor.org/rfc/rfc9000#name-authors-addresses)

## [1.](https://www.rfc-editor.org/rfc/rfc9000#section-1)[Overview](https://www.rfc-editor.org/rfc/rfc9000#name-overview)

QUIC is a secure general-purpose transport protocol. This document defines version 1 of QUIC, which conforms to the version-independent properties of QUIC defined in [[QUIC-INVARIANTS](https://www.rfc-editor.org/rfc/rfc9000#QUIC-INVARIANTS)].[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1-1)

QUIC is a connection-oriented protocol that creates a stateful interaction between a client and server.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1-2)

The QUIC handshake combines negotiation of cryptographic and transport parameters. QUIC integrates the TLS handshake [[TLS13](https://www.rfc-editor.org/rfc/rfc9000#TLS13)], although using a customized framing for protecting packets. The integration of TLS and QUIC is described in more detail in [[QUIC-TLS](https://www.rfc-editor.org/rfc/rfc9000#QUIC-TLS)]. The handshake is structured to permit the exchange of application data as soon as possible. This includes an option for clients to send data immediately (0-RTT), which requires some form of prior communication or configuration to enable.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1-3)

Endpoints communicate in QUIC by exchanging QUIC packets. Most packets contain frames, which carry control information and application data between endpoints. QUIC authenticates the entirety of each packet and encrypts as much of each packet as is practical. QUIC packets are carried in UDP datagrams [[UDP](https://www.rfc-editor.org/rfc/rfc9000#UDP)] to better facilitate deployment in existing systems and networks.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1-4)

Application protocols exchange information over a QUIC connection via streams, which are ordered sequences of bytes. Two types of streams can be created: bidirectional streams, which allow both endpoints to send data; and unidirectional streams, which allow a single endpoint to send data. A credit-based scheme is used to limit stream creation and to bound the amount of data that can be sent.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1-5)

QUIC provides the necessary feedback to implement reliable delivery and congestion control. An algorithm for detecting and recovering from loss of data is described in [Section 6](https://www.rfc-editor.org/rfc/rfc9002#section-6) of [[QUIC-RECOVERY](https://www.rfc-editor.org/rfc/rfc9000#QUIC-RECOVERY)]. QUIC depends on congestion control to avoid network congestion. An exemplary congestion control algorithm is described in [Section 7](https://www.rfc-editor.org/rfc/rfc9002#section-7) of [[QUIC-RECOVERY](https://www.rfc-editor.org/rfc/rfc9000#QUIC-RECOVERY)].[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1-6)

QUIC connections are not strictly bound to a single network path. Connection migration uses connection identifiers to allow connections to transfer to a new network path. Only clients are able to migrate in this version of QUIC. This design also allows connections to continue after changes in network topology or address mappings, such as might be caused by NAT rebinding.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1-7)

Once established, multiple options are provided for connection termination. Applications can manage a graceful shutdown, endpoints can negotiate a timeout period, errors can cause immediate connection teardown, and a stateless mechanism provides for termination of connections after one endpoint has lost state.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1-8)

### [1.1.](https://www.rfc-editor.org/rfc/rfc9000#section-1.1)[Document Structure](https://www.rfc-editor.org/rfc/rfc9000#name-document-structure)

This document describes the core QUIC protocol and is structured as follows:[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-1)

*   Streams are the basic service abstraction that QUIC provides.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.1.1)

    *   [Section 2](https://www.rfc-editor.org/rfc/rfc9000#streams) describes core concepts related to streams,[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.1.2.1)
    *   [Section 3](https://www.rfc-editor.org/rfc/rfc9000#stream-states) provides a reference model for stream states, and[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.1.2.2)
    *   [Section 4](https://www.rfc-editor.org/rfc/rfc9000#flow-control) outlines the operation of flow control.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.1.2.3)

*   Connections are the context in which QUIC endpoints communicate.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.2.1)

    *   [Section 5](https://www.rfc-editor.org/rfc/rfc9000#connections) describes core concepts related to connections,[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.2.2.1)
    *   [Section 6](https://www.rfc-editor.org/rfc/rfc9000#version-negotiation) describes version negotiation,[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.2.2.2)
    *   [Section 7](https://www.rfc-editor.org/rfc/rfc9000#handshake) details the process for establishing connections,[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.2.2.3)
    *   [Section 8](https://www.rfc-editor.org/rfc/rfc9000#address-validation) describes address validation and critical denial-of-service mitigations,[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.2.2.4)
    *   [Section 9](https://www.rfc-editor.org/rfc/rfc9000#migration) describes how endpoints migrate a connection to a new network path,[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.2.2.5)
    *   [Section 10](https://www.rfc-editor.org/rfc/rfc9000#termination) lists the options for terminating an open connection, and[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.2.2.6)
    *   [Section 11](https://www.rfc-editor.org/rfc/rfc9000#error-handling) provides guidance for stream and connection error handling.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.2.2.7)

*   Packets and frames are the basic unit used by QUIC to communicate.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.3.1)

    *   [Section 12](https://www.rfc-editor.org/rfc/rfc9000#packets-frames) describes concepts related to packets and frames,[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.3.2.1)
    *   [Section 13](https://www.rfc-editor.org/rfc/rfc9000#packetization) defines models for the transmission, retransmission, and acknowledgment of data, and[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.3.2.2)
    *   [Section 14](https://www.rfc-editor.org/rfc/rfc9000#datagram-size) specifies rules for managing the size of datagrams carrying QUIC packets.[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.3.2.3)

*   Finally, encoding details of QUIC protocol elements are described in:[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.4.1)

    *   [Section 15](https://www.rfc-editor.org/rfc/rfc9000#versions) (versions),[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.4.2.1)
    *   [Section 16](https://www.rfc-editor.org/rfc/rfc9000#integer-encoding) (integer encoding),[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.4.2.2)
    *   [Section 17](https://www.rfc-editor.org/rfc/rfc9000#packet-formats) (packet headers),[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.4.2.3)
    *   [Section 18](https://www.rfc-editor.org/rfc/rfc9000#transport-parameter-encoding) (transport parameters),[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.4.2.4)
    *   [Section 19](https://www.rfc-editor.org/rfc/rfc9000#frame-formats) (frames), and[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.4.2.5)
    *   [Section 20](https://www.rfc-editor.org/rfc/rfc9000#error-codes) (errors).[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-2.4.2.6)

Accompanying documents describe QUIC's loss detection and congestion control [[QUIC-RECOVERY](https://www.rfc-editor.org/rfc/rfc9000#QUIC-RECOVERY)], and the use of TLS and other cryptographic mechanisms [[QUIC-TLS](https://www.rfc-editor.org/rfc/rfc9000#QUIC-TLS)].[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-3)

This document defines QUIC version 1, which conforms to the protocol invariants in [[QUIC-INVARIANTS](https://www.rfc-editor.org/rfc/rfc9000#QUIC-INVARIANTS)].[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-4)

To refer to QUIC version 1, cite this document. References to the limited set of version-independent properties of QUIC can cite [[QUIC-INVARIANTS](https://www.rfc-editor.org/rfc/rfc9000#QUIC-INVARIANTS)].[¶](https://www.rfc-editor.org/rfc/rfc9000#section-1.1-5)

### [1.2.](https://www.rfc-editor.org/rfc/rfc9000#section-1.2)[Terms and Definitions](https://www.rfc-editor.org/rfc/rfc9000#name-terms-and-definitions)
