# WebRTC: Real-Time Communication in Browsers

[](https://www.w3.org/)

# WebRTC: Real-Time Communication in Browsers

[W3C Recommendation](https://www.w3.org/standards/types#REC)13 March 2025

More details about this document This version:[https://www.w3.org/TR/2025/REC-webrtc-20250313/](https://www.w3.org/TR/2025/REC-webrtc-20250313/)Latest published version:[https://www.w3.org/TR/webrtc/](https://www.w3.org/TR/webrtc/)Latest editor's draft:[https://w3c.github.io/webrtc-pc/](https://w3c.github.io/webrtc-pc/)History:[https://www.w3.org/standards/history/webrtc/](https://www.w3.org/standards/history/webrtc/)[Commit history](https://github.com/w3c/webrtc-pc/commits/main)Test suite:[https://github.com/web-platform-tests/wpt/tree/master/webrtc/](https://github.com/web-platform-tests/wpt/tree/master/webrtc/)Implementation report:[https://w3c.github.io/webrtc-interop-reports/webrtc-pc-report.html](https://w3c.github.io/webrtc-interop-reports/webrtc-pc-report.html)Editors:Cullen Jennings (Cisco) Florent Castelli (Google) Henrik Boström (Google) Jan-Ivar Bruaroey (Mozilla)  Former editors: Adam Bergkvist (Ericsson) - Until 01 June 2018 Daniel C. Burnett (Invited Expert) - Until 01 June 2018 Anant Narayanan (Mozilla) - Until 01 November 2012 Bernard Aboba (Microsoft Corporation) - Until 01 March 2017 Taylor Brandstetter (Google) - Until 01 June 2018 Feedback:[GitHub w3c/webrtc-pc](https://github.com/w3c/webrtc-pc/) ([pull requests](https://github.com/w3c/webrtc-pc/pulls/), [new issue](https://github.com/w3c/webrtc-pc/issues/new/choose), [open issues](https://github.com/w3c/webrtc-pc/issues/)) [public-webrtc@w3.org](mailto:public-webrtc@w3.org?subject=%5Bwebrtc%5D%20YOUR%20TOPIC%20HERE) with subject line [webrtc] _… message topic …_ ([archives](https://lists.w3.org/Archives/Public/public-webrtc))Participate[Mailing list](https://lists.w3.org/Archives/Public/public-webrtc/)

See also [**translations**](https://www.w3.org/Translations/?technology=webrtc).

Initial Author of this Specification was Ian Hickson, Google Inc., with the following copyright statement:

 © Copyright 2004-2011 Apple Computer, Inc., Mozilla Foundation, and Opera Software ASA. You are granted a license to use, reproduce and create derivative works of this document. All subsequent changes since 26 July 2011 done by the W3C WebRTC Working Group are under the following [Copyright](https://www.w3.org/policies/#copyright):

[Copyright](https://www.w3.org/policies/#copyright) © 2011-2025 [World Wide Web Consortium](https://www.w3.org/). W3C®[liability](https://www.w3.org/policies/#Legal_Disclaimer), [trademark](https://www.w3.org/policies/#W3C_Trademarks) and [permissive document license](https://www.w3.org/copyright/software-license/) rules apply.

* * *

## Abstract

This document defines a set of ECMAScript APIs in WebIDL to allow media and generic application data to be sent to and received from another browser or device implementing the appropriate set of real-time protocols. This specification is being developed in conjunction with a protocol specification developed by the IETF RTCWEB group and an API specification to get access to local media devices.

## Status of This Document

_This section describes the status of this document at the time of its publication. A list of current W3C publications and the latest revision of this technical report can be found in the [W3C technical reports index](https://www.w3.org/TR/) at https://www.w3.org/TR/._

This document includes [Candidate Amendments](https://www.w3.org/TR/webrtc/#candidate-amendments).

Its [associated test suite](https://github.com/web-platform-tests/wpt/tree/master/webrtc) has been used to build an [implementation report](https://w3c.github.io/webrtc-interop-reports/webrtc-pc-report.html) of the API at the time of its initial publication as a Recommendation. That test suite has been updated to integrate proposed and candidates amendments identified since then, and an [updated implementation report](https://www.w3.org/2024/10/webrtc-amendments-interop.html) focused on the implementation status of these amendments has been used to select features with double implementation as proposed amendments, now fully incorporated in this version of the Recommendation.

This document was published by the [Web Real-Time Communications Working Group](https://www.w3.org/groups/wg/webrtc) as a Recommendation using the [Recommendation track](https://www.w3.org/policies/process/20231103/#recs-and-notes). It includes [candidate amendments](https://www.w3.org/policies/process/20231103/#candidate-amendments), introducing substantive changes and new features since the previous Recommendation.

W3C recommends the wide deployment of this specification as a standard for the Web.

A W3C Recommendation is a specification that, after extensive consensus-building, is endorsed by W3C and its Members, and has commitments from Working Group members to [royalty-free licensing](https://www.w3.org/policies/patent-policy/#sec-Requirements) for implementations. Future updates to this Recommendation may incorporate [new features](https://www.w3.org/policies/process/20231103/#allow-new-features).

Candidate additions are marked in the document.

Candidate corrections are marked in the document.

This document was produced by a group operating under the [W3C Patent Policy](https://www.w3.org/policies/patent-policy/). W3C maintains a [public list of any patent disclosures](https://www.w3.org/groups/wg/webrtc/ipr) made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent which the individual believes contains [Essential Claim(s)](https://www.w3.org/policies/patent-policy/#def-essential) must disclose the information in accordance with [section 6 of the W3C Patent Policy](https://www.w3.org/policies/patent-policy/#sec-Disclosure).

This document is governed by the [03 November 2023 W3C Process Document](https://www.w3.org/policies/process/20231103/).

## Table of Contents

1.   [Abstract](https://www.w3.org/TR/webrtc/#abstract)
2.   [Status of This Document](https://www.w3.org/TR/webrtc/#sotd)
3.   [1. Introduction](https://www.w3.org/TR/webrtc/#intro)
4.   [2. Conformance](https://www.w3.org/TR/webrtc/#conformance)
5.   [3. Terminology](https://www.w3.org/TR/webrtc/#terminology)
6.   [4. Peer-to-peer connections](https://www.w3.org/TR/webrtc/#peer-to-peer-connections)
    1.   [4.1 Introduction](https://www.w3.org/TR/webrtc/#introduction)
    2.   [4.2 Configuration](https://www.w3.org/TR/webrtc/#configuration)
        1.   [4.2.1 `RTCConfiguration` Dictionary](https://www.w3.org/TR/webrtc/#rtcconfiguration-dictionary)
        2.   [4.2.2 `RTCIceServer` Dictionary](https://www.w3.org/TR/webrtc/#rtciceserver-dictionary)
        3.   [4.2.3 `RTCIceTransportPolicy` Enum](https://www.w3.org/TR/webrtc/#rtcicetransportpolicy-enum)
        4.   [4.2.4 `RTCBundlePolicy` Enum](https://www.w3.org/TR/webrtc/#rtcbundlepolicy-enum)
        5.   [4.2.5 `RTCRtcpMuxPolicy` Enum](https://www.w3.org/TR/webrtc/#rtcrtcpmuxpolicy-enum)
        6.   [4.2.6 Offer/Answer Options](https://www.w3.org/TR/webrtc/#offer-answer-options)

    3.   [4.3 State Definitions](https://www.w3.org/TR/webrtc/#state-definitions)
        1.   [4.3.1 `RTCSignalingState` Enum](https://www.w3.org/TR/webrtc/#rtcsignalingstate-enum)
        2.   [4.3.2 `RTCIceGatheringState` Enum](https://www.w3.org/TR/webrtc/#rtcicegatheringstate-enum)
        3.   [4.3.3 `RTCPeerConnectionState` Enum](https://www.w3.org/TR/webrtc/#rtcpeerconnectionstate-enum)
        4.   [4.3.4 `RTCIceConnectionState` Enum](https://www.w3.org/TR/webrtc/#rtciceconnectionstate-enum)

    4.   [4.4 RTCPeerConnection Interface](https://www.w3.org/TR/webrtc/#rtcpeerconnection-interface)
        1.   [4.4.1 Operation](https://www.w3.org/TR/webrtc/#operation)
            1.   [4.4.1.1 Constructor](https://www.w3.org/TR/webrtc/#constructor)
            2.   [4.4.1.2 Chain an asynchronous operation](https://www.w3.org/TR/webrtc/#chain-an-asynchronous-operation)
            3.   [4.4.1.3 Update the connection state](https://www.w3.org/TR/webrtc/#update-the-connection-state)
            4.   [4.4.1.4 Set the session description](https://www.w3.org/TR/webrtc/#set-the-session-description)
            5.   [4.4.1.5 Set the configuration](https://www.w3.org/TR/webrtc/#set-the-configuration)

        2.   [4.4.2 Interface Definition](https://www.w3.org/TR/webrtc/#interface-definition)
        3.   [4.4.3 Legacy Interface Extensions](https://www.w3.org/TR/webrtc/#legacy-interface-extensions)
            1.   [4.4.3.1 Method extensions](https://www.w3.org/TR/webrtc/#method-extensions)
            2.   [4.4.3.2 Legacy configuration extensions](https://www.w3.org/TR/webrtc/#legacy-configuration-extensions)

        4.   [4.4.4 Garbage collection](https://www.w3.org/TR/webrtc/#garbage-collection)

    5.   [4.5 Error Handling](https://www.w3.org/TR/webrtc/#error-handling)
        1.   [4.5.1 General Principles](https://www.w3.org/TR/webrtc/#general-principles)

    6.   [4.6 Session Description Model](https://www.w3.org/TR/webrtc/#session-description-model)
        1.   [4.6.1 `RTCSdpType`](https://www.w3.org/TR/webrtc/#rtcsdptype)
        2.   [4.6.2 `RTCSessionDescription` Class](https://www.w3.org/TR/webrtc/#rtcsessiondescription-class)

    7.   [4.7 Session Negotiation Model](https://www.w3.org/TR/webrtc/#session-negotiation-model)
        1.   [4.7.1 Setting Negotiation-Needed](https://www.w3.org/TR/webrtc/#setting-negotiation-needed)
        2.   [4.7.2 Clearing Negotiation-Needed](https://www.w3.org/TR/webrtc/#clearing-negotiation-needed)
        3.   [4.7.3 Updating the Negotiation-Needed flag](https://www.w3.org/TR/webrtc/#updating-the-negotiation-needed-flag)

    8.   [4.8 Interfaces for Interactive Connectivity Establishment](https://www.w3.org/TR/webrtc/#interfaces-for-interactive-connectivity-establishment)
        1.   [4.8.1 `RTCIceCandidate` Interface](https://www.w3.org/TR/webrtc/#rtcicecandidate-interface)
            1.   [4.8.1.1 `candidate-attribute` Grammar](https://www.w3.org/TR/webrtc/#candidate-attribute-grammar)
            2.   [4.8.1.2 `RTCIceProtocol` Enum](https://www.w3.org/TR/webrtc/#rtciceprotocol-enum)
            3.   [4.8.1.3 `RTCIceTcpCandidateType` Enum](https://www.w3.org/TR/webrtc/#rtcicetcpcandidatetype-enum)
            4.   [4.8.1.4 `RTCIceCandidateType` Enum](https://www.w3.org/TR/webrtc/#rtcicecandidatetype-enum)
            5.   [4.8.1.5 `RTCIceServerTransportProtocol` Enum](https://www.w3.org/TR/webrtc/#rtciceservertransportprotocol-enum)

        2.   [4.8.2 `RTCPeerConnectionIceEvent`](https://www.w3.org/TR/webrtc/#rtcpeerconnectioniceevent)
        3.   [4.8.3 `RTCPeerConnectionIceErrorEvent`](https://www.w3.org/TR/webrtc/#rtcpeerconnectioniceerrorevent)

    9.   [4.9 Certificate Management](https://www.w3.org/TR/webrtc/#sec.cert-mgmt)
        1.   [4.9.1 `RTCCertificateExpiration` Dictionary](https://www.w3.org/TR/webrtc/#rtccertificateexpiration-dictionary)
        2.   [4.9.2 `RTCCertificate` Interface](https://www.w3.org/TR/webrtc/#rtccertificate-interface)

7.   [5. RTP Media API](https://www.w3.org/TR/webrtc/#rtp-media-api)
    1.   [5.1 RTCPeerConnection Interface Extensions](https://www.w3.org/TR/webrtc/#rtcpeerconnection-interface-extensions)
        1.   [5.1.1 Processing Remote MediaStreamTracks](https://www.w3.org/TR/webrtc/#processing-remote-mediastreamtracks)

    2.   [5.2 `RTCRtpSender` Interface](https://www.w3.org/TR/webrtc/#rtcrtpsender-interface)
        1.   [5.2.1 `RTCRtpParameters` Dictionary](https://www.w3.org/TR/webrtc/#rtcrtpparameters)
        2.   [5.2.2 `RTCRtpSendParameters` Dictionary](https://www.w3.org/TR/webrtc/#rtcsendrtpparameters)
        3.   [5.2.3 `RTCRtpReceiveParameters` Dictionary](https://www.w3.org/TR/webrtc/#rtcreceivertpparameters)
        4.   [5.2.4 `RTCRtpCodingParameters` Dictionary](https://www.w3.org/TR/webrtc/#rtcrtpcodingparameters)
        5.   [5.2.5 `RTCRtpEncodingParameters` Dictionary](https://www.w3.org/TR/webrtc/#rtcrtpencodingparameters)
        6.   [5.2.6 `RTCRtcpParameters` Dictionary](https://www.w3.org/TR/webrtc/#rtcrtcpparameters)
        7.   [5.2.7 `RTCRtpHeaderExtensionParameters` Dictionary](https://www.w3.org/TR/webrtc/#rtcrtpheaderextensionparameters)
        8.   [5.2.8 `RTCRtpCodec` Dictionary](https://www.w3.org/TR/webrtc/#rtcrtpcodec)
        9.   [5.2.9 `RTCRtpCodecParameters` Dictionary](https://www.w3.org/TR/webrtc/#rtcrtpcodecparameters)
        10.   [5.2.10 `RTCRtpCapabilities` Dictionary](https://www.w3.org/TR/webrtc/#rtcrtpcapabilities)
        11.   [5.2.11 `RTCRtpHeaderExtensionCapability` Dictionary](https://www.w3.org/TR/webrtc/#rtcrtpheaderextensioncapability)
        12.   [5.2.12 `RTCSetParameterOptions` Dictionary](https://www.w3.org/TR/webrtc/#rtcsetparameteroptions-dictionary)

    3.   [5.3 `RTCRtpReceiver` Interface](https://www.w3.org/TR/webrtc/#rtcrtpreceiver-interface)
    4.   [5.4 `RTCRtpTransceiver` Interface](https://www.w3.org/TR/webrtc/#rtcrtptransceiver-interface)
        1.   [5.4.1 Simulcast functionality](https://www.w3.org/TR/webrtc/#simulcast-functionality)
            1.   [5.4.1.1 Encoding Parameter Examples](https://www.w3.org/TR/webrtc/#rtcrtpencodingspatialsim-example*)

        2.   [5.4.2 "Hold" functionality](https://www.w3.org/TR/webrtc/#hold-functionality)

    5.   [5.5 `RTCDtlsTransport` Interface](https://www.w3.org/TR/webrtc/#rtcdtlstransport-interface)
        1.   [5.5.1 `RTCDtlsTransportState` Enum](https://www.w3.org/TR/webrtc/#rtcdtlstransportstate-enum)
        2.   [5.5.2 `RTCDtlsFingerprint` Dictionary](https://www.w3.org/TR/webrtc/#rtcdtlsfingerprint)

    6.   [5.6 `RTCIceTransport` Interface](https://www.w3.org/TR/webrtc/#rtcicetransport)
        1.   [5.6.1 `RTCIceParameters` Dictionary](https://www.w3.org/TR/webrtc/#rtciceparameters)
        2.   [5.6.2 `RTCIceCandidatePair` Interface](https://www.w3.org/TR/webrtc/#rtcicecandidatepair)
        3.   [5.6.3 `RTCIceGathererState` Enum](https://www.w3.org/TR/webrtc/#rtcicegathererstate)
        4.   [5.6.4 `RTCIceTransportState` Enum](https://www.w3.org/TR/webrtc/#rtcicetransportstate)
        5.   [5.6.5 `RTCIceRole` Enum](https://www.w3.org/TR/webrtc/#rtcicerole)
        6.   [5.6.6 `RTCIceComponent` Enum](https://www.w3.org/TR/webrtc/#rtcicecomponent)

    7.   [5.7 `RTCTrackEvent`](https://www.w3.org/TR/webrtc/#rtctrackevent)

8.   [6. Peer-to-peer Data API](https://www.w3.org/TR/webrtc/#peer-to-peer-data-api)
    1.   [6.1 RTCPeerConnection Interface Extensions](https://www.w3.org/TR/webrtc/#rtcpeerconnection-interface-extensions-0)
        1.   [6.1.1 `RTCSctpTransport` Interface](https://www.w3.org/TR/webrtc/#rtcsctptransport-interface)
            1.   [6.1.1.1 Create an instance](https://www.w3.org/TR/webrtc/#sctp-transport-create)
            2.   [6.1.1.2 Update max message size](https://www.w3.org/TR/webrtc/#sctp-transport-update-mms)
            3.   [6.1.1.3 Connected procedure](https://www.w3.org/TR/webrtc/#sctp-transport-connected)

        2.   [6.1.2 `RTCSctpTransportState` Enum](https://www.w3.org/TR/webrtc/#rtcsctptransportstate)

    2.   [6.2 `RTCDataChannel`](https://www.w3.org/TR/webrtc/#rtcdatachannel)
        1.   [6.2.1 Creating a data channel](https://www.w3.org/TR/webrtc/#creating-a-data-channel)
        2.   [6.2.2 Announcing a data channel as open](https://www.w3.org/TR/webrtc/#announcing-a-data-channel-as-open)
        3.   [6.2.3 Announcing a data channel instance](https://www.w3.org/TR/webrtc/#announcing-a-data-channel-instance)
        4.   [6.2.4 Closing procedure](https://www.w3.org/TR/webrtc/#closing-procedure)
        5.   [6.2.5 Announcing a data channel as closed](https://www.w3.org/TR/webrtc/#announcing-a-data-channel-as-closed)
        6.   [6.2.6 Transfering data channel](https://www.w3.org/TR/webrtc/#transfering-a-data-channel)
        7.   [6.2.7 Error on creating data channels](https://www.w3.org/TR/webrtc/#error-on-creating-data-channels)
        8.   [6.2.8 Receiving messages on a data channel](https://www.w3.org/TR/webrtc/#receiving-messages-on-a-data-channel)

    3.   [6.3 `RTCDataChannelEvent`](https://www.w3.org/TR/webrtc/#rtcdatachannelevent)
    4.   [6.4 Garbage Collection](https://www.w3.org/TR/webrtc/#garbage-collection-0)

9.   [7. Peer-to-peer DTMF](https://www.w3.org/TR/webrtc/#peer-to-peer-dtmf)
    1.   [7.1 RTCRtpSender Interface Extensions](https://www.w3.org/TR/webrtc/#rtcrtpsender-interface-extensions)
    2.   [7.2 `RTCDTMFSender`](https://www.w3.org/TR/webrtc/#rtcdtmfsender)
    3.   [7.3 canInsertDTMF algorithm](https://www.w3.org/TR/webrtc/#caninsertdtmf-algorithm)
    4.   [7.4 `RTCDTMFToneChangeEvent`](https://www.w3.org/TR/webrtc/#rtcdtmftonechangeevent)

10.   [8. Statistics Model](https://www.w3.org/TR/webrtc/#sec.stats-model)
    1.   [8.1 Introduction](https://www.w3.org/TR/webrtc/#introduction-0)
    2.   [8.2 RTCPeerConnection Interface Extensions](https://www.w3.org/TR/webrtc/#rtcpeerconnection-interface-extensions-1)
    3.   [8.3 `RTCStatsReport` Object](https://www.w3.org/TR/webrtc/#rtcstatsreport-object)
    4.   [8.4 `RTCStats` Dictionary](https://www.w3.org/TR/webrtc/#rtcstats-dictionary)
    5.   [8.5 The stats selection algorithm](https://www.w3.org/TR/webrtc/#the-stats-selection-algorithm)
    6.   [8.6 Mandatory To Implement Stats](https://www.w3.org/TR/webrtc/#mandatory-to-implement-stats)
    7.   [8.7 GetStats Example](https://www.w3.org/TR/webrtc/#getstats-example)

11.   [9. Media Stream API Extensions for Network Use](https://www.w3.org/TR/webrtc/#media-stream-api-extensions-for-network-use)
    1.   [9.1 Introduction](https://www.w3.org/TR/webrtc/#introduction-1)
    2.   [9.2 MediaStream](https://www.w3.org/TR/webrtc/#mediastream-network-use)
        1.   [9.2.1 id](https://www.w3.org/TR/webrtc/#id)

    3.   [9.3 MediaStreamTrack](https://www.w3.org/TR/webrtc/#mediastreamtrack-network-use)
        1.   [9.3.1 MediaTrackSupportedConstraints, MediaTrackCapabilities, MediaTrackConstraints and MediaTrackSettings](https://www.w3.org/TR/webrtc/#mediatracksupportedconstraints-mediatrackcapabilities-mediatrackconstraints-and-mediatracksettings)

12.   [10. Examples and Call Flows](https://www.w3.org/TR/webrtc/#examples-and-call-flows)
    1.   [10.1 Simple Peer-to-peer Example](https://www.w3.org/TR/webrtc/#simple-peer-to-peer-example)
    2.   [10.2 Advanced Peer-to-peer Example with Warm-up](https://www.w3.org/TR/webrtc/#advanced-peer-to-peer-example-with-warm-up)
    3.   [10.3 Simulcast Example](https://www.w3.org/TR/webrtc/#simulcast-example)
    4.   [10.4 Peer-to-peer Data Example](https://www.w3.org/TR/webrtc/#peer-to-peer-data-example)
    5.   [10.5 Call Flow Browser to Browser](https://www.w3.org/TR/webrtc/#call-flow-browser-to-browser)
    6.   [10.6 DTMF Example](https://www.w3.org/TR/webrtc/#dtmf-example)
    7.   [10.7 Perfect Negotiation Example](https://www.w3.org/TR/webrtc/#perfect-negotiation-example)

13.   [11. Error Handling](https://www.w3.org/TR/webrtc/#error-handling-0)
    1.   [11.1 `RTCError` Interface](https://www.w3.org/TR/webrtc/#rtcerror-interface)
        1.   [11.1.1 Constructors](https://www.w3.org/TR/webrtc/#constructors)
        2.   [11.1.2 Attributes](https://www.w3.org/TR/webrtc/#attributes)
        3.   [11.1.3 `RTCErrorInit` Dictionary](https://www.w3.org/TR/webrtc/#rtcerrorinit-dictionary)

    2.   [11.2 `RTCErrorDetailType` Enum](https://www.w3.org/TR/webrtc/#rtcerrordetailtype-enum)
    3.   [11.3 `RTCErrorEvent` Interface](https://www.w3.org/TR/webrtc/#rtcerrorevent-interface)
        1.   [11.3.1 Constructors](https://www.w3.org/TR/webrtc/#constructors-0)
        2.   [11.3.2 Attributes](https://www.w3.org/TR/webrtc/#attributes-0)

    4.   [11.4 `RTCErrorEventInit` Dictionary](https://www.w3.org/TR/webrtc/#rtcerroreventinit-dictionary)
        1.   [11.4.1 Dictionary RTCErrorEventInit Members](https://www.w3.org/TR/webrtc/#dictionary-rtcerroreventinit-members)

14.   [12. Event summary](https://www.w3.org/TR/webrtc/#event-summary)
15.   [13. Privacy and Security Considerations](https://www.w3.org/TR/webrtc/#privacy-and-security-considerations)
    1.   [13.1 Impact on same origin policy](https://www.w3.org/TR/webrtc/#impact-on-same-origin-policy)
    2.   [13.2 Revealing IP addresses](https://www.w3.org/TR/webrtc/#revealing-ip-addresses)
    3.   [13.3 Impact on local network](https://www.w3.org/TR/webrtc/#impact-on-local-network)
    4.   [13.4 Confidentiality of Communications](https://www.w3.org/TR/webrtc/#confidentiality-of-communications)
    5.   [13.5 Persistent information exposed by WebRTC](https://www.w3.org/TR/webrtc/#persistent-information-exposed-by-webrtc)
    6.   [13.6 Setting SDP from remote endpoints](https://www.w3.org/TR/webrtc/#setting-sdp-from-remote-endpoints)

16.   [14. Accessibility Considerations](https://www.w3.org/TR/webrtc/#accessibility-considerations)
17.   [A. Candidate Amendments](https://www.w3.org/TR/webrtc/#candidate-amendments)
18.   [B. Acknowledgements](https://www.w3.org/TR/webrtc/#acknowledgements)
19.   [C. References](https://www.w3.org/TR/webrtc/#references)
    1.   [C.1 Normative references](https://www.w3.org/TR/webrtc/#normative-references)
    2.   [C.2 Informative references](https://www.w3.org/TR/webrtc/#informative-references)

## 1.  Introduction

[](https://www.w3.org/TR/webrtc/#intro)

_This section is non-normative._

There are a number of facets to peer-to-peer communications and video-conferencing in HTML covered by this specification:

*   Connecting to remote peers using NAT-traversal technologies such as ICE, STUN, and TURN. 
*   Sending the locally-produced tracks to remote peers and receiving tracks from remote peers. 
*   Sending arbitrary data directly to remote peers. 

This document defines the APIs used for these features. This specification is being developed in conjunction with a protocol specification developed by the [IETF RTCWEB group](https://datatracker.ietf.org/wg/rtcweb/) and an API specification to get access to local media devices [[GETUSERMEDIA](https://www.w3.org/TR/webrtc/#bib-getusermedia "Media Capture and Streams")] developed by the WebRTC Working Group. An overview of the system can be found in [[RFC8825](https://www.w3.org/TR/webrtc/#bib-rfc8825 "Overview: Real-Time Protocols for Browser-Based Applications")] and [[RFC8826](https://www.w3.org/TR/webrtc/#bib-rfc8826 "Security Considerations for WebRTC")].

## 2. Conformance

[](https://www.w3.org/TR/webrtc/#conformance)

As well as sections marked as non-normative, all authoring guidelines, diagrams, examples, and notes in this specification are non-normative. Everything else in this specification is normative.

The key words _MAY_, _MUST_, _MUST NOT_, and _SHOULD_ in this document are to be interpreted as described in [BCP 14](https://datatracker.ietf.org/doc/html/bcp14) [[RFC2119](https://www.w3.org/TR/webrtc/#bib-rfc2119 "Key words for use in RFCs to Indicate Requirement Levels")] [[RFC8174](https://www.w3.org/TR/webrtc/#bib-rfc8174 "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words")] when, and only when, they appear in all capitals, as shown here.

This specification defines conformance criteria that apply to a single product: the user agent that implements the interfaces that it contains.

Conformance requirements phrased as algorithms or specific steps may be implemented in any manner, so long as the end result is equivalent. (In particular, the algorithms defined in this specification are intended to be easy to follow, and not intended to be performant.)

Implementations that use ECMAScript to implement the APIs defined in this specification _MUST_ implement them in a manner consistent with the ECMAScript Bindings defined in the Web IDL specification [[WEBIDL](https://www.w3.org/TR/webrtc/#bib-webidl "Web IDL Standard")], as this specification uses that specification and terminology.

## 3.  Terminology

[](https://www.w3.org/TR/webrtc/#terminology)

The [`EventHandler`](https://www.w3.org/TR/webrtc/) interface, representing a callback used for event handlers, is defined in [[HTML](https://www.w3.org/TR/webrtc/#bib-html "HTML Standard")].

The concepts [queue a task](https://www.w3.org/TR/webrtc/) and [networking task source](https://www.w3.org/TR/webrtc/) are defined in [[HTML](https://www.w3.org/TR/webrtc/#bib-html "HTML Standard")].

The concept [fire an event](https://www.w3.org/TR/webrtc/) is defined in [[DOM](https://www.w3.org/TR/webrtc/#bib-dom "DOM Standard")].

The terms [event](https://www.w3.org/TR/webrtc/), [event handlers](https://www.w3.org/TR/webrtc/) and [event handler event types](https://www.w3.org/TR/webrtc/) are defined in [[HTML](https://www.w3.org/TR/webrtc/#bib-html "HTML Standard")].

[`Performance`](https://www.w3.org/TR/webrtc/).[`timeOrigin`](https://www.w3.org/TR/webrtc/) and [`Performance`](https://www.w3.org/TR/webrtc/).[`now`](https://www.w3.org/TR/webrtc/)`()` are defined in [[hr-time](https://www.w3.org/TR/webrtc/#bib-hr-time "High Resolution Time")].

The terms [serializable objects](https://html.spec.whatwg.org/multipage/structured-data.html#serializable-objects), [serialization steps](https://www.w3.org/TR/webrtc/), and [deserialization steps](https://www.w3.org/TR/webrtc/) are defined in [[HTML](https://www.w3.org/TR/webrtc/#bib-html "HTML Standard")].

The terms [`MediaStream`](https://www.w3.org/TR/webrtc/), [`MediaStreamTrack`](https://www.w3.org/TR/webrtc/), and [`MediaStreamConstraints`](https://www.w3.org/TR/webrtc/) are defined in [[GETUSERMEDIA](https://www.w3.org/TR/webrtc/#bib-getusermedia "Media Capture and Streams")]. Note that [`MediaStream`](https://www.w3.org/TR/webrtc/) is extended in [9.2 MediaStream](https://www.w3.org/TR/webrtc/#mediastream-network-use) in this document while [`MediaStreamTrack`](https://www.w3.org/TR/webrtc/) is extended in [9.3 MediaStreamTrack](https://www.w3.org/TR/webrtc/#mediastreamtrack-network-use) in this document.

The term [`Blob`](https://www.w3.org/TR/webrtc/) is defined in [[FILEAPI](https://www.w3.org/TR/webrtc/#bib-fileapi "File API")].

The term media description is defined in [[RFC4566](https://www.w3.org/TR/webrtc/#bib-rfc4566 "SDP: Session Description Protocol")].

The term media transport is defined in [[RFC7656](https://www.w3.org/TR/webrtc/#bib-rfc7656 "A Taxonomy of Semantics and Mechanisms for Real-Time Transport Protocol (RTP) Sources")].

The term generation is defined in [[RFC8838](https://www.w3.org/TR/webrtc/#bib-rfc8838 "Trickle ICE: Incremental Provisioning of Candidates for the Interactive Connectivity Establishment (ICE) Protocol")] Section 2.

The terms [stats object](https://www.w3.org/TR/webrtc-stats/#dfn-stats-object) and [monitored object](https://www.w3.org/TR/webrtc-stats/#dfn-monitored-object) are defined in [[WEBRTC-STATS](https://www.w3.org/TR/webrtc/#bib-webrtc-stats "Identifiers for WebRTC's Statistics API")].

When referring to exceptions, the terms [throw](https://www.w3.org/TR/webrtc/) and [created](https://www.w3.org/TR/webrtc/) are defined in [[WEBIDL](https://www.w3.org/TR/webrtc/#bib-webidl "Web IDL Standard")].

The callback [`VoidFunction`](https://www.w3.org/TR/webrtc/) is defined in [[WEBIDL](https://www.w3.org/TR/webrtc/#bib-webidl "Web IDL Standard")].

The term "throw" is used as specified in [[INFRA](https://www.w3.org/TR/webrtc/#bib-infra "Infra Standard")]: it terminates the current processing steps.

The terms fulfilled, rejected, resolved, and settled used in the context of Promises are defined in [[ECMASCRIPT-6.0](https://www.w3.org/TR/webrtc/#bib-ecmascript-6.0 "ECMA-262 6th Edition, The ECMAScript 2015 Language Specification")].

The [AlgorithmIdentifier](https://www.w3.org/TR/WebCryptoAPI/#dfn-AlgorithmIdentifier) is defined in [[WebCryptoAPI](https://www.w3.org/TR/webrtc/#bib-webcryptoapi "Web Cryptography API")].

Note

The general principles for Javascript APIs apply, including the principle of [run-to-completion](https://w3ctag.github.io/design-principles/#js-rtc) and no-data-races as defined in [[API-DESIGN-PRINCIPLES](https://www.w3.org/TR/webrtc/#bib-api-design-principles "Web Platform Design Principles")]. That is, while a task is running, external events do not influence what's visible to the Javascript application. For example, the amount of data buffered on a data channel will increase due to "send" calls while Javascript is executing, and the decrease due to packets being sent will be visible after a task checkpoint.

 It is the responsibility of the user agent to make sure the set of values presented to the application is consistent - for instance that getContributingSources() (which is synchronous) returns values for all sources measured at the same time.

## 4.  Peer-to-peer connections

[](https://www.w3.org/TR/webrtc/#peer-to-peer-connections)

### 4.1  Introduction

[](https://www.w3.org/TR/webrtc/#introduction)

_This section is non-normative._

An [`RTCPeerConnection`](https://www.w3.org/TR/webrtc/#dom-rtcpeerconnection) instance allows an application to establish peer-to-peer communications with another [`RTCPeerConnection`](https://www.w3.org/TR/webrtc/#dom-rtcpeerconnection) instance in another browser, or to another endpoint implementing the required protocols. Communications are coordinated by the exchange of control messages (called a signaling protocol) over a signaling channel which is provided by unspecified means, but generally by a script in the page via the server, e.g. using [`WebSocket`](https://www.w3.org/TR/webrtc/) or [`XMLHttpRequest`](https://www.w3.org/TR/webrtc/).

### 4.2  Configuration

[](https://www.w3.org/TR/webrtc/#configuration)

#### 4.2.1 `RTCConfiguration` Dictionary

[](https://www.w3.org/TR/webrtc/#rtcconfiguration-dictionary)

The [`RTCConfiguration`](https://www.w3.org/TR/webrtc/#dom-rtcconfiguration) defines a set of parameters to configure how the peer-to-peer communication established via [`RTCPeerConnection`](https://www.w3.org/TR/webrtc/#dom-rtcpeerconnection) is established or re-established.

[WebIDL](https://www.w3.org/TR/webrtc/#webidl-196911378)
```
dictionary RTCConfiguration {
  sequence<RTCIceServer> iceServers = [];
  RTCIceTransportPolicy iceTransportPolicy = "all";
  RTCBundlePolicy bundlePolicy = "balanced";
  RTCRtcpMuxPolicy rtcpMuxPolicy = "require";
  sequence<RTCCertificate> certificates = [];
  [EnforceRange] octet iceCandidatePoolSize = 0;
};
```

##### Dictionary [`RTCConfiguration`](https://www.w3.org/TR/webrtc/#dom-rtcconfiguration) Members

[](https://www.w3.org/TR/webrtc/#dictionary-rtcconfiguration-members)

`iceServers` of type sequence<[`RTCIceServer`](https://www.w3.org/TR/webrtc/#dom-rtciceserver)>, defaulting to `[]`. 
An array of objects describing servers available to be used by ICE, such as STUN and TURN servers. If the number of ICE servers exceeds an implementation-defined limit, ignore the ICE servers above the threshold. This implementation defined limit _MUST_ be at least 32.

`iceTransportPolicy` of type [`RTCIceTransportPolicy`](https://www.w3.org/TR/webrtc/#dom-rtcicetransportpolicy), defaulting to `"all"`. 
Indicates which candidates the [ICE Agent](https://www.w3.org/TR/webrtc/#dfn-ice-agent) is allowed to use.

`bundlePolicy` of type [`RTCBundlePolicy`](https://www.w3.org/TR/webrtc/#dom-rtcbundlepolicy), defaulting to `"balanced"`. 
Indicates which [media-bundling policy](https://www.w3.org/TR/webrtc/#dom-rtcbundlepolicy) to use when gathering ICE candidates.

`rtcpMuxPolicy` of type [`RTCRtcpMuxPolicy`](https://www.w3.org/TR/webrtc/#dom-rtcrtcpmuxpolicy), defaulting to `"require"`. 
Indicates which [rtcp-mux policy](https://www.w3.org/TR/webrtc/#dom-rtcrtcpmuxpolicy) to use when gathering ICE candidates.

`certificates` of type sequence<[`RTCCertificate`](https://www.w3.org/TR/webrtc/#dom-rtccertificate)>, defaulting to `[]`. 
A set of certificates that the [`RTCPeerConnection`](https://www.w3.org/TR/webrtc/#dom-rtcpeerconnection) uses to authenticate.

Valid values for this parameter are created through calls to the [`generateCertificate`](https://www.w3.org/TR/webrtc/#dom-rtcpeerconnection-generatecertificate)`()` function.

Although any given DTLS connection will use only one certificate, this attribute allows the caller to provide multiple certificates that support different algorithms. The final certificate will be selected based on the DTLS handshake, which establishes which certificates are allowed. The [`RTCPeerConnection`](https://www.w3.org/TR/webrtc/#dom-rtcpeerconnection) implementation selects which of the certificates is used for a given connection; how certificates are selected is outside the scope of this specification.

Note

Existing implementations only utilize the first certificate provided; the others are ignored.

If this value is absent, then a default set of certificates is generated for each [`RTCPeerConnection`](https://www.w3.org/TR/webrtc/#dom-rtcpeerconnection) instance.

This option allows applications to establish key continuity. An [`RTCCertificate`](https://www.w3.org/TR/webrtc/#dom-rtccertificate) can be persisted in [[INDEXEDDB](https://www.w3.org/TR/webrtc/#bib-indexeddb "Indexed Database API")] and reused. Persistence and reuse also avoids the cost of key generation.

The value for this configuration option cannot change after its value is initially selected.

`iceCandidatePoolSize` of type octet, defaulting to `0`
Size of the prefetched ICE pool as defined in [[RFC9429](https://www.w3.org/TR/webrtc/#bib-rfc9429 "JavaScript Session Establishment Protocol (JSEP)")] ([section 3.5.4.](https://www.rfc-editor.org/rfc/rfc9429#section-3.5.4) and [section 4.1.1.](https://www.rfc-editor.org/rfc/rfc9429#section-4.1.1)).

#### 4.2.2 `RTCIceServer` Dictionary

[](https://www.w3.org/TR/webrtc/#rtciceserver-dictionary)

The [`RTCIceServer`](https://www.w3.org/TR/webrtc/#dom-rtciceserver) dictionary is used to describe the STUN and TURN servers that can be used by the [ICE Agent](https://www.w3.org/TR/webrtc/#dfn-ice-agent) to establish a connection with a peer.

[WebIDL](https://www.w3.org/TR/webrtc/#webidl-238081018)
```
dictionary RTCIceServer {
  required (DOMString or sequence<DOMString>) urls;
  DOMString username;
  DOMString credential;
};
```

##### Dictionary [`RTCIceServer`](https://www.w3.org/TR/webrtc/#dom-rtciceserver) Members

[](https://www.w3.org/TR/webrtc/#dictionary-rtciceserver-members)

`urls` of type (DOMString or sequence<DOMString>), required 
STUN or TURN URI(s) as defined in [[RFC7064](https://www.w3.org/TR/webrtc/#bib-rfc7064 "URI Scheme for the Session Traversal Utilities for NAT (STUN) Protocol")] and [[RFC7065](https://www.w3.org/TR/webrtc/#bib-rfc7065 "Traversal Using Relays around NAT (TURN) Uniform Resource Identifiers")] or other URI types.

`username` of type DOMString
If this [`RTCIceServer`](https://www.w3.org/TR/webrtc/#dom-rtciceserver) object represents a TURN server, then this attribute specifies the username to use with that TURN server.

`credential` of type [`DOMString`](https://www.w3.org/TR/webrtc/)
If this [`RTCIceServer`](https://www.w3.org/TR/webrtc/#dom-rtciceserver) object represents a TURN server, then this attribute specifies the credential to use with that TURN server.

[`credential`](https://www.w3.org/TR/webrtc/#dom-rtciceserver-credential) represents a long-term authentication password, as described in [[RFC5389](https://www.w3.org/TR/webrtc/#bib-rfc5389 "Session Traversal Utilities for NAT (STUN)")], Section 10.2.

An example array of [`RTCIceServer`](https://www.w3.org/TR/webrtc/#dom-rtciceserver) objects is:

[Example 1](https://www.w3.org/TR/webrtc/#example-1)

```
[
  {urls: 'stun:stun1.example.net'},
  {urls: ['turns:turn.example.org', 'turn:turn.example.net'],
    username: 'user',
    credential: 'myPassword',
];
```

#### 4.2.3 `RTCIceTransportPolicy` Enum

[](https://www.w3.org/TR/webrtc/#rtcicetransportpolicy-enum)

As described in [[RFC9429](https://www.w3.org/TR/webrtc/#bib-rfc9429 "JavaScript Session Establishment Protocol (JSEP)")] ([section 4.1.1.](https://www.rfc-editor.org/rfc/rfc9429#section-4.1.1)), if the [`iceTransportPolicy`](https://www.w3.org/TR/webrtc/#dom-rtcconfiguration-icetransportpolicy) member of the [`RTCConfiguration`](https://www.w3.org/TR/webrtc/#dom-rtcconfiguration) is specified, it defines the ICE candidate policy [[RFC9429](https://www.w3.org/TR/webrtc/#bib-rfc9429 "JavaScript Session Establishment Protocol (JSEP)")] ([section 3.5.3.](https://www.rfc-editor.org/rfc/rfc9429#section-3.5.3)) the browser uses to surface the permitted candidates to the application; only these candidates will be used for connectivity checks.

[WebIDL](https://www.w3.org/TR/webrtc/#webidl-1784278863)
```
enum RTCIceTransportPolicy {
  "relay",
  "all"
};
```

[`RTCIceTransportPolicy`](https://www.w3.org/TR/webrtc/#dom-rtcicetransportpolicy) Enumeration description| Enum value | Description |
| --- | --- |
| `relay` | The [ICE Agent](https://www.w3.org/TR/webrtc/#dfn-ice-agent) uses only media relay candidates such as candidates passing through a TURN server. Note This can be used to prevent the remote endpoint from learning the user's IP addresses, which may be desired in certain use cases. For example, in a "call"-based application, the application may want to prevent an unknown caller from learning the callee's IP addresses until the callee has consented in some way. |
| `all` | The [ICE Agent](https://www.w3.org/TR/webrtc/#dfn-ice-agent) can use any type of candidate when this value is specified. Note The implementation can still use its own candidate filtering policy in order to limit the IP addresses exposed to the application, as noted in the description of [`RTCIceCandidate`](https://www.w3.org/TR/webrtc/#dom-rtcicecandidate).[`address`](https://www.w3.org/TR/webrtc/#dom-rtcicecandidate-address). |

#### 4.2.4 `RTCBundlePolicy` Enum

[](https://www.w3.org/TR/webrtc/#rtcbundlepolicy-enum)

As described in [[RFC9429](https://www.w3.org/TR/webrtc/#bib-rfc9429 "JavaScript Session Establishment Protocol (JSEP)")] ([section 4.1.1.](https://www.rfc-editor.org/rfc/rfc9429#section-4.1.1)), bundle policy affects which media tracks are negotiated if the remote endpoint is not bundle-aware, and what ICE candidates are gathered. If the remote endpoint is bundle-aware, all media tracks and data channels are bundled onto the same transport.

[WebIDL](https://www.w3.org/TR/webrtc/#target-bundle-policy)
```
enum RTCBundlePolicy {
  "balanced",
  "max-compat",
  "max-bundle"
};
```

[`RTCBundlePolicy`](https://www.w3.org/TR/webrtc/#dom-rtcbundlepolicy) Enumeration description| Enum value | Description |
| --- | --- |
| `balanced` | Gather ICE candidates for each media type in use (audio, video, and data). If the remote endpoint is not bundle-aware, negotiate only one audio and video track on separate transports. |
| `max-compat` | Gather ICE candidates for each track. If the remote endpoint is not bundle-aware, negotiate all media tracks on separate transports. |
| `max-bundle` | Gather ICE candidates for only one track. If the remote endpoint is not bundle-aware, negotiate only one media track. |

#### 4.2.5 `RTCRtcpMuxPolicy` Enum

[](https://www.w3.org/TR/webrtc/#rtcrtcpmuxpolicy-enum)

As described in [[RFC9429](https://www.w3.org/TR/webrtc/#bib-rfc9429 "JavaScript Session Establishment Protocol (JSEP)")] ([section 4.1.1.](https://www.rfc-editor.org/rfc/rfc9429#section-4.1.1)), the [`RTCRtcpMuxPolicy`](https://www.w3.org/TR/webrtc/#dom-rtcrtcpmuxpolicy) affects what ICE candidates are gathered to support non-multiplexed RTCP. The only value defined in this spec is "[`require`](https://www.w3.org/TR/webrtc/#dom-rtcrtcpmuxpolicy-require)".

[WebIDL](https://www.w3.org/TR/webrtc/#target-rtcp-mux-policy)
```
enum RTCRtcpMuxPolicy {
  "require"
};
```

[`RTCRtcpMuxPolicy`](https://www.w3.org/TR/webrtc/#dom-rtcrtcpmuxpolicy) Enumeration description| Enum value | Description |
| --- | --- |
| `require` | Gather ICE candidates only for RTP and multiplex RTCP on the RTP candidates. If the remote endpoint is not capable of rtcp-mux, session negotiation will fail. |

#### 4.2.6  Offer/Answer Options

[](https://www.w3.org/TR/webrtc/#offer-answer-options)

These dictionaries describe the options that can be used to control the offer/answer creation process.

[WebIDL](https://www.w3.org/TR/webrtc/#webidl-981522324)`dictionary RTCOfferAnswerOptions {};`

##### Dictionary `RTCOfferAnswerOptions` Members

[](https://www.w3.org/TR/webrtc/#dictionary-rtcofferansweroptions-members)

[WebIDL](https://www.w3.org/TR/webrtc/#webidl-1912926860)
```
dictionary RTCOfferOptions : RTCOfferAnswerOptions {
  boolean iceRestart = false;
};
```

##### Dictionary `RTCOfferOptions` Members

[](https://www.w3.org/TR/webrtc/#dictionary-rtcofferoptions-members)

`iceRestart` of type boolean, defaulting to `false`
