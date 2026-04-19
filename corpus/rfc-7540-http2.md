# RFC 7540: Hypertext Transfer Protocol Version 2 (HTTP/2)
[[RFC Home](https://www.rfc-editor.org/ "RFC Editor")] [[TEXT](https://www.rfc-editor.org/rfc/rfc7540.txt)|[PDF](https://www.rfc-editor.org/rfc/pdfrfc/rfc7540.txt.pdf)|[HTML](https://www.rfc-editor.org/rfc/rfc7540.html)] [[Tracker](https://datatracker.ietf.org/doc/rfc7540 "IETF Datatracker information for this document")] [[IPR](https://datatracker.ietf.org/ipr/search/?rfc=7540&submit=rfc "IPR disclosures related to this document")] [[Errata](https://www.rfc-editor.org/errata/rfc7540)] [[Info page](https://www.rfc-editor.org/info/rfc7540 "Info page")] 

Obsoleted by: [9113](https://www.rfc-editor.org/rfc/rfc9113) PROPOSED STANDARD

Updated by: [8740](https://www.rfc-editor.org/rfc/rfc8740)Errata Exist Internet Engineering Task Force (IETF)                         M. Belshe
Request for Comments: 7540                                         BitGo
Category: Standards Track                                        R. Peon
ISSN: 2070-1721                                              Google, Inc
                                                         M. Thomson, Ed.
                                                                 Mozilla
                                                                May 2015

             Hypertext Transfer Protocol Version 2 (HTTP/2)

Abstract

   This specification describes an optimized expression of the semantics
   of the Hypertext Transfer Protocol (HTTP), referred to as HTTP
   version 2 (HTTP/2).  HTTP/2 enables a more efficient use of network
   resources and a reduced perception of latency by introducing header
   field compression and allowing multiple concurrent exchanges on the
   same connection.  It also introduces unsolicited push of
   representations from servers to clients.

   This specification is an alternative to, but does not obsolete, the
   HTTP/1.1 message syntax.  HTTP's existing semantics remain unchanged.

Status of This Memo

   This is an Internet Standards Track document.

   This document is a product of the Internet Engineering Task Force
   (IETF).  It represents the consensus of the IETF community.  It has
   received public review and has been approved for publication by the
   Internet Engineering Steering Group (IESG).  Further information on
   Internet Standards is available in [Section 2 of RFC 5741](https://www.rfc-editor.org/rfc/rfc5741#section-2).

   Information about the current status of this document, any errata,
   and how to provide feedback on it may be obtained at
   [http://www.rfc-editor.org/info/rfc7540](https://www.rfc-editor.org/info/rfc7540).

Belshe, et al. Standards Track [Page 1]

* * *

[RFC 7540](https://www.rfc-editor.org/rfc/rfc7540) HTTP/2 May 2015

Copyright Notice

   Copyright (c) 2015 IETF Trust and the persons identified as the
   document authors.  All rights reserved.

   This document is subject to [BCP 78](https://www.rfc-editor.org/bcp/bcp78) and the IETF Trust's Legal
   Provisions Relating to IETF Documents
   ([http://trustee.ietf.org/license-info](http://trustee.ietf.org/license-info)) in effect on the date of
   publication of this document.  Please review these documents
   carefully, as they describe your rights and restrictions with respect
   to this document.  Code Components extracted from this document must
   include Simplified BSD License text as described in Section 4.e of
   the Trust Legal Provisions and are provided without warranty as
   described in the Simplified BSD License.

Table of Contents

   [1](https://www.rfc-editor.org/rfc/rfc7540#section-1). Introduction ....................................................[4](https://www.rfc-editor.org/rfc/rfc7540#page-4)
   [2](https://www.rfc-editor.org/rfc/rfc7540#section-2). HTTP/2 Protocol Overview ........................................[5](https://www.rfc-editor.org/rfc/rfc7540#page-5)
      [2.1](https://www.rfc-editor.org/rfc/rfc7540#section-2.1). Document Organization ......................................[6](https://www.rfc-editor.org/rfc/rfc7540#page-6)
      [2.2](https://www.rfc-editor.org/rfc/rfc7540#section-2.2). Conventions and Terminology ................................[6](https://www.rfc-editor.org/rfc/rfc7540#page-6)
   [3](https://www.rfc-editor.org/rfc/rfc7540#section-3). Starting HTTP/2 .................................................[7](https://www.rfc-editor.org/rfc/rfc7540#page-7)
      [3.1](https://www.rfc-editor.org/rfc/rfc7540#section-3.1). HTTP/2 Version Identification ..............................[8](https://www.rfc-editor.org/rfc/rfc7540#page-8)
      [3.2](https://www.rfc-editor.org/rfc/rfc7540#section-3.2). Starting HTTP/2 for "http" URIs ............................[8](https://www.rfc-editor.org/rfc/rfc7540#page-8)
           [3.2.1](https://www.rfc-editor.org/rfc/rfc7540#section-3.2.1). HTTP2-Settings Header Field .........................[9](https://www.rfc-editor.org/rfc/rfc7540#page-9)
      [3.3](https://www.rfc-editor.org/rfc/rfc7540#section-3.3). Starting HTTP/2 for "https" URIs ..........................[10](https://www.rfc-editor.org/rfc/rfc7540#page-10)
      [3.4](https://www.rfc-editor.org/rfc/rfc7540#section-3.4). Starting HTTP/2 with Prior Knowledge ......................[10](https://www.rfc-editor.org/rfc/rfc7540#page-10)
      [3.5](https://www.rfc-editor.org/rfc/rfc7540#section-3.5). HTTP/2 Connection Preface .................................[11](https://www.rfc-editor.org/rfc/rfc7540#page-11)
   [4](https://www.rfc-editor.org/rfc/rfc7540#section-4). HTTP Frames ....................................................[12](https://www.rfc-editor.org/rfc/rfc7540#page-12)
      [4.1](https://www.rfc-editor.org/rfc/rfc7540#section-4.1). Frame Format ..............................................[12](https://www.rfc-editor.org/rfc/rfc7540#page-12)
      [4.2](https://www.rfc-editor.org/rfc/rfc7540#section-4.2). Frame Size ................................................[13](https://www.rfc-editor.org/rfc/rfc7540#page-13)
      [4.3](https://www.rfc-editor.org/rfc/rfc7540#section-4.3). Header Compression and Decompression ......................[14](https://www.rfc-editor.org/rfc/rfc7540#page-14)
   [5](https://www.rfc-editor.org/rfc/rfc7540#section-5). Streams and Multiplexing .......................................[15](https://www.rfc-editor.org/rfc/rfc7540#page-15)
      [5.1](https://www.rfc-editor.org/rfc/rfc7540#section-5.1). Stream States .............................................[16](https://www.rfc-editor.org/rfc/rfc7540#page-16)
           [5.1.1](https://www.rfc-editor.org/rfc/rfc7540#section-5.1.1). Stream Identifiers .................................[21](https://www.rfc-editor.org/rfc/rfc7540#page-21)
           [5.1.2](https://www.rfc-editor.org/rfc/rfc7540#section-5.1.2). Stream Concurrency .................................[22](https://www.rfc-editor.org/rfc/rfc7540#page-22)
      [5.2](https://www.rfc-editor.org/rfc/rfc7540#section-5.2). Flow Control ..............................................[22](https://www.rfc-editor.org/rfc/rfc7540#page-22)
           [5.2.1](https://www.rfc-editor.org/rfc/rfc7540#section-5.2.1). Flow-Control Principles ............................[23](https://www.rfc-editor.org/rfc/rfc7540#page-23)
           [5.2.2](https://www.rfc-editor.org/rfc/rfc7540#section-5.2.2). Appropriate Use of Flow Control ....................[24](https://www.rfc-editor.org/rfc/rfc7540#page-24)
      [5.3](https://www.rfc-editor.org/rfc/rfc7540#section-5.3). Stream Priority ...........................................[24](https://www.rfc-editor.org/rfc/rfc7540#page-24)
           [5.3.1](https://www.rfc-editor.org/rfc/rfc7540#section-5.3.1). Stream Dependencies ................................[25](https://www.rfc-editor.org/rfc/rfc7540#page-25)
           [5.3.2](https://www.rfc-editor.org/rfc/rfc7540#section-5.3.2). Dependency Weighting ...............................[26](https://www.rfc-editor.org/rfc/rfc7540#page-26)
           [5.3.3](https://www.rfc-editor.org/rfc/rfc7540#section-5.3.3). Reprioritization ...................................[26](https://www.rfc-editor.org/rfc/rfc7540#page-26)
           [5.3.4](https://www.rfc-editor.org/rfc/rfc7540#section-5.3.4). Prioritization State Management ....................[27](https://www.rfc-editor.org/rfc/rfc7540#page-27)
           [5.3.5](https://www.rfc-editor.org/rfc/rfc7540#section-5.3.5). Default Priorities .................................[28](https://www.rfc-editor.org/rfc/rfc7540#page-28)
      [5.4](https://www.rfc-editor.org/rfc/rfc7540#section-5.4). Error Handling ............................................[28](https://www.rfc-editor.org/rfc/rfc7540#page-28)
           [5.4.1](https://www.rfc-editor.org/rfc/rfc7540#section-5.4.1). Connection Error Handling ..........................[29](https://www.rfc-editor.org/rfc/rfc7540#page-29)
           [5.4.2](https://www.rfc-editor.org/rfc/rfc7540#section-5.4.2). Stream Error Handling ..............................[29](https://www.rfc-editor.org/rfc/rfc7540#page-29)

Belshe, et al. Standards Track [Page 2]

* * *

[RFC 7540](https://www.rfc-editor.org/rfc/rfc7540) HTTP/2 May 2015

           [5.4.3](https://www.rfc-editor.org/rfc/rfc7540#section-5.4.3). Connection Termination .............................[30](https://www.rfc-editor.org/rfc/rfc7540#page-30)
      [5.5](https://www.rfc-editor.org/rfc/rfc7540#section-5.5). Extending HTTP/2 ..........................................[30](https://www.rfc-editor.org/rfc/rfc7540#page-30)
   [6](https://www.rfc-editor.org/rfc/rfc7540#section-6). Frame Definitions ..............................................[31](https://www.rfc-editor.org/rfc/rfc7540#page-31)
      [6.1](https://www.rfc-editor.org/rfc/rfc7540#section-6.1). DATA ......................................................[31](https://www.rfc-editor.org/rfc/rfc7540#page-31)
      [6.2](https://www.rfc-editor.org/rfc/rfc7540#section-6.2). HEADERS ...................................................[32](https://www.rfc-editor.org/rfc/rfc7540#page-32)
      [6.3](https://www.rfc-editor.org/rfc/rfc7540#section-6.3). PRIORITY ..................................................[34](https://www.rfc-editor.org/rfc/rfc7540#page-34)
      [6.4](https://www.rfc-editor.org/rfc/rfc7540#section-6.4). RST_STREAM ................................................[36](https://www.rfc-editor.org/rfc/rfc7540#page-36)
      [6.5](https://www.rfc-editor.org/rfc/rfc7540#section-6.5). SETTINGS ..................................................[36](https://www.rfc-editor.org/rfc/rfc7540#page-36)
           [6.5.1](https://www.rfc-editor.org/rfc/rfc7540#section-6.5.1). SETTINGS Format ....................................[38](https://www.rfc-editor.org/rfc/rfc7540#page-38)
           [6.5.2](https://www.rfc-editor.org/rfc/rfc7540#section-6.5.2). Defined SETTINGS Parameters ........................[38](https://www.rfc-editor.org/rfc/rfc7540#page-38)
           [6.5.3](https://www.rfc-editor.org/rfc/rfc7540#section-6.5.3). Settings Synchronization ...........................[39](https://www.rfc-editor.org/rfc/rfc7540#page-39)
      [6.6](https://www.rfc-editor.org/rfc/rfc7540#section-6.6). PUSH_PROMISE ..............................................[40](https://www.rfc-editor.org/rfc/rfc7540#page-40)
      [6.7](https://www.rfc-editor.org/rfc/rfc7540#section-6.7). PING ......................................................[42](https://www.rfc-editor.org/rfc/rfc7540#page-42)
      [6.8](https://www.rfc-editor.org/rfc/rfc7540#section-6.8). GOAWAY ....................................................[43](https://www.rfc-editor.org/rfc/rfc7540#page-43)
      [6.9](https://www.rfc-editor.org/rfc/rfc7540#section-6.9). WINDOW_UPDATE .............................................[46](https://www.rfc-editor.org/rfc/rfc7540#page-46)
           [6.9.1](https://www.rfc-editor.org/rfc/rfc7540#section-6.9.1). The Flow-Control Window ............................[47](https://www.rfc-editor.org/rfc/rfc7540#page-47)
           [6.9.2](https://www.rfc-editor.org/rfc/rfc7540#section-6.9.2). Initial Flow-Control Window Size ...................[48](https://www.rfc-editor.org/rfc/rfc7540#page-48)
           [6.9.3](https://www.rfc-editor.org/rfc/rfc7540#section-6.9.3). Reducing the Stream Window Size ....................[49](https://www.rfc-editor.org/rfc/rfc7540#page-49)
      [6.10](https://www.rfc-editor.org/rfc/rfc7540#section-6.10). CONTINUATION .............................................[49](https://www.rfc-editor.org/rfc/rfc7540#page-49)
   [7](https://www.rfc-editor.org/rfc/rfc7540#section-7). Error Codes ....................................................[50](https://www.rfc-editor.org/rfc/rfc7540#page-50)
   [8](https://www.rfc-editor.org/rfc/rfc7540#section-8). HTTP Message Exchanges .........................................[51](https://www.rfc-editor.org/rfc/rfc7540#page-51)
      [8.1](https://www.rfc-editor.org/rfc/rfc7540#section-8.1). HTTP Request/Response Exchange ............................[52](https://www.rfc-editor.org/rfc/rfc7540#page-52)
           [8.1.1](https://www.rfc-editor.org/rfc/rfc7540#section-8.1.1). Upgrading from HTTP/2 ..............................[53](https://www.rfc-editor.org/rfc/rfc7540#page-53)
           [8.1.2](https://www.rfc-editor.org/rfc/rfc7540#section-8.1.2). HTTP Header Fields .................................[53](https://www.rfc-editor.org/rfc/rfc7540#page-53)
           [8.1.3](https://www.rfc-editor.org/rfc/rfc7540#section-8.1.3). Examples ...........................................[57](https://www.rfc-editor.org/rfc/rfc7540#page-57)
           [8.1.4](https://www.rfc-editor.org/rfc/rfc7540#section-8.1.4). Request Reliability Mechanisms in HTTP/2 ...........[60](https://www.rfc-editor.org/rfc/rfc7540#page-60)
      [8.2](https://www.rfc-editor.org/rfc/rfc7540#section-8.2). Server Push ...............................................[60](https://www.rfc-editor.org/rfc/rfc7540#page-60)
           [8.2.1](https://www.rfc-editor.org/rfc/rfc7540#section-8.2.1). Push Requests ......................................[61](https://www.rfc-editor.org/rfc/rfc7540#page-61)
           [8.2.2](https://www.rfc-editor.org/rfc/rfc7540#section-8.2.2). Push Responses .....................................[63](https://www.rfc-editor.org/rfc/rfc7540#page-63)
      [8.3](https://www.rfc-editor.org/rfc/rfc7540#section-8.3). The CONNECT Method ........................................[64](https://www.rfc-editor.org/rfc/rfc7540#page-64)
   [9](https://www.rfc-editor.org/rfc/rfc7540#section-9). Additional HTTP Requirements/Considerations ....................[65](https://www.rfc-editor.org/rfc/rfc7540#page-65)
      [9.1](https://www.rfc-editor.org/rfc/rfc7540#section-9.1). Connection Management .....................................[65](https://www.rfc-editor.org/rfc/rfc7540#page-65)
           [9.1.1](https://www.rfc-editor.org/rfc/rfc7540#section-9.1.1). Connection Reuse ...................................[66](https://www.rfc-editor.org/rfc/rfc7540#page-66)
           [9.1.2](https://www.rfc-editor.org/rfc/rfc7540#section-9.1.2). The 421 (Misdirected Request) Status Code ..........[66](https://www.rfc-editor.org/rfc/rfc7540#page-66)
      [9.2](https://www.rfc-editor.org/rfc/rfc7540#section-9.2). Use of TLS Features .......................................[67](https://www.rfc-editor.org/rfc/rfc7540#page-67)
           [9.2.1](https://www.rfc-editor.org/rfc/rfc7540#section-9.2.1). TLS 1.2 Features ...................................[67](https://www.rfc-editor.org/rfc/rfc7540#page-67)
           [9.2.2](https://www.rfc-editor.org/rfc/rfc7540#section-9.2.2). TLS 1.2 Cipher Suites ..............................[68](https://www.rfc-editor.org/rfc/rfc7540#page-68)
   [10](https://www.rfc-editor.org/rfc/rfc7540#section-10). Security Considerations .......................................[69](https://www.rfc-editor.org/rfc/rfc7540#page-69)
      [10.1](https://www.rfc-editor.org/rfc/rfc7540#section-10.1). Server Authority .........................................[69](https://www.rfc-editor.org/rfc/rfc7540#page-69)
      [10.2](https://www.rfc-editor.org/rfc/rfc7540#section-10.2). Cross-Protocol Attacks ...................................[69](https://www.rfc-editor.org/rfc/rfc7540#page-69)
      [10.3](https://www.rfc-editor.org/rfc/rfc7540#section-10.3). Intermediary Encapsulation Attacks .......................[70](https://www.rfc-editor.org/rfc/rfc7540#page-70)
      [10.4](https://www.rfc-editor.org/rfc/rfc7540#section-10.4). Cacheability of Pushed Responses .........................[70](https://www.rfc-editor.org/rfc/rfc7540#page-70)
      [10.5](https://www.rfc-editor.org/rfc/rfc7540#section-10.5). Denial-of-Service Considerations .........................[70](https://www.rfc-editor.org/rfc/rfc7540#page-70)
           [10.5.1](https://www.rfc-editor.org/rfc/rfc7540#section-10.5.1). Limits on Header Block Size .......................[71](https://www.rfc-editor.org/rfc/rfc7540#page-71)
           [10.5.2](https://www.rfc-editor.org/rfc/rfc7540#section-10.5.2). CONNECT Issues ....................................[72](https://www.rfc-editor.org/rfc/rfc7540#page-72)
      [10.6](https://www.rfc-editor.org/rfc/rfc7540#section-10.6). Use of Compression .......................................[72](https://www.rfc-editor.org/rfc/rfc7540#page-72)
      [10.7](https://www.rfc-editor.org/rfc/rfc7540#section-10.7). Use of Padding ...........................................[73](https://www.rfc-editor.org/rfc/rfc7540#page-73)
      [10.8](https://www.rfc-editor.org/rfc/rfc7540#section-10.8). Privacy Considerations ...................................[73](https://www.rfc-editor.org/rfc/rfc7540#page-73)

Belshe, et al. Standards Track [Page 3]

* * *

[RFC 7540](https://www.rfc-editor.org/rfc/rfc7540) HTTP/2 May 2015

   [11](https://www.rfc-editor.org/rfc/rfc7540#section-11). IANA Considerations ...........................................[74](https://www.rfc-editor.org/rfc/rfc7540#page-74)
      [11.1](https://www.rfc-editor.org/rfc/rfc7540#section-11.1). Registration of HTTP/2 Identification Strings ............[74](https://www.rfc-editor.org/rfc/rfc7540#page-74)
      [11.2](https://www.rfc-editor.org/rfc/rfc7540#section-11.2). Frame Type Registry ......................................[75](https://www.rfc-editor.org/rfc/rfc7540#page-75)
      [11.3](https://www.rfc-editor.org/rfc/rfc7540#section-11.3). Settings Registry ........................................[75](https://www.rfc-editor.org/rfc/rfc7540#page-75)
      [11.4](https://www.rfc-editor.org/rfc/rfc7540#section-11.4). Error Code Registry ......................................[76](https://www.rfc-editor.org/rfc/rfc7540#page-76)
      [11.5](https://www.rfc-editor.org/rfc/rfc7540#section-11.5). HTTP2-Settings Header Field Registration .................[77](https://www.rfc-editor.org/rfc/rfc7540#page-77)
      [11.6](https://www.rfc-editor.org/rfc/rfc7540#section-11.6). PRI Method Registration ..................................[78](https://www.rfc-editor.org/rfc/rfc7540#page-78)
      [11.7](https://www.rfc-editor.org/rfc/rfc7540#section-11.7). The 421 (Misdirected Request) HTTP Status Code ...........[78](https://www.rfc-editor.org/rfc/rfc7540#page-78)
      [11.8](https://www.rfc-editor.org/rfc/rfc7540#section-11.8). The h2c Upgrade Token ....................................[78](https://www.rfc-editor.org/rfc/rfc7540#page-78)
   [12](https://www.rfc-editor.org/rfc/rfc7540#section-12). References ....................................................[79](https://www.rfc-editor.org/rfc/rfc7540#page-79)
      [12.1](https://www.rfc-editor.org/rfc/rfc7540#section-12.1). Normative References .....................................[79](https://www.rfc-editor.org/rfc/rfc7540#page-79)
      [12.2](https://www.rfc-editor.org/rfc/rfc7540#section-12.2). Informative References ...................................[81](https://www.rfc-editor.org/rfc/rfc7540#page-81)
   [Appendix A](https://www.rfc-editor.org/rfc/rfc7540#appendix-A). TLS 1.2 Cipher Suite Black List .......................[83](https://www.rfc-editor.org/rfc/rfc7540#page-83)
   Acknowledgements ..................................................[95](https://www.rfc-editor.org/rfc/rfc7540#page-95)
   Authors' Addresses ................................................[96](https://www.rfc-editor.org/rfc/rfc7540#page-96)

[1](https://www.rfc-editor.org/rfc/rfc7540#section-1). Introduction

   The Hypertext Transfer Protocol (HTTP) is a wildly successful
   protocol.  However, the way HTTP/1.1 uses the underlying transport
   ([[RFC7230], Section 6](https://www.rfc-editor.org/rfc/rfc7230#section-6)) has several characteristics that have a
   negative overall effect on application performance today.

   In particular, HTTP/1.0 allowed only one request to be outstanding at
   a time on a given TCP connection.  HTTP/1.1 added request pipelining,
   but this only partially addressed request concurrency and still
   suffers from head-of-line blocking.  Therefore, HTTP/1.0 and HTTP/1.1
   clients that need to make many requests use multiple connections to a
   server in order to achieve concurrency and thereby reduce latency.

   Furthermore, HTTP header fields are often repetitive and verbose,
   causing unnecessary network traffic as well as causing the initial
   TCP [[TCP](https://www.rfc-editor.org/rfc/rfc7540#ref-TCP "\"Transmission Control Protocol\"")] congestion window to quickly fill.  This can result in
   excessive latency when multiple requests are made on a new TCP
   connection.

   HTTP/2 addresses these issues by defining an optimized mapping of
   HTTP's semantics to an underlying connection.  Specifically, it
   allows interleaving of request and response messages on the same
   connection and uses an efficient coding for HTTP header fields.  It
   also allows prioritization of requests, letting more important
   requests complete more quickly, further improving performance.

Belshe, et al. Standards Track [Page 4]

* * *

[RFC 7540](https://www.rfc-editor.org/rfc/rfc7540) HTTP/2 May 2015

   The resulting protocol is more friendly to the network because fewer
   TCP connections can be used in comparison to HTTP/1.x.  This means
   less competition with other flows and longer-lived connections, which
   in turn lead to better utilization of available network capacity.

   Finally, HTTP/2 also enables more efficient processing of messages
   through use of binary message framing.

[2](https://www.rfc-editor.org/rfc/rfc7540#section-2). HTTP/2 Protocol Overview

   HTTP/2 provides an optimized transport for HTTP semantics.  HTTP/2
   supports all of the core features of HTTP/1.1 but aims to be more
   efficient in several ways.

   The basic protocol unit in HTTP/2 is a frame ([Section 4.1](https://www.rfc-editor.org/rfc/rfc7540#section-4.1)).  Each
   frame type serves a different purpose.  For example, HEADERS and DATA
   frames form the basis of HTTP requests and responses ([Section 8.1](https://www.rfc-editor.org/rfc/rfc7540#section-8.1));
   other frame types like SETTINGS, WINDOW_UPDATE, and PUSH_PROMISE are
   used in support of other HTTP/2 features.

   Multiplexing of requests is achieved by having each HTTP request/
   response exchange associated with its own stream ([Section 5](https://www.rfc-editor.org/rfc/rfc7540#section-5)).
   Streams are largely independent of each other, so a blocked or
   stalled request or response does not prevent progress on other
   streams.

   Flow control and prioritization ensure that it is possible to
   efficiently use multiplexed streams.  Flow control ([Section 5.2](https://www.rfc-editor.org/rfc/rfc7540#section-5.2))
   helps to ensure that only data that can be used by a receiver is
   transmitted.  Prioritization ([Section 5.3](https://www.rfc-editor.org/rfc/rfc7540#section-5.3)) ensures that limited
   resources can be directed to the most important streams first.

   HTTP/2 adds a new interaction mode whereby a server can push
   responses to a client ([Section 8.2](https://www.rfc-editor.org/rfc/rfc7540#section-8.2)).  Server push allows a server to
   speculatively send data to a client that the server anticipates the
   client will need, trading off some network usage against a potential
   latency gain.  The server does this by synthesizing a request, which
   it sends as a PUSH_PROMISE frame.  The server is then able to send a
   response to the synthetic request on a separate stream.

   Because HTTP header fields used in a connection can contain large
   amounts of redundant data, frames that contain them are compressed
   ([Section 4.3](https://www.rfc-editor.org/rfc/rfc7540#section-4.3)).  This has especially advantageous impact upon request
   sizes in the common case, allowing many requests to be compressed
   into one packet.

Belshe, et al. Standards Track [Page 5]

* * *

[RFC 7540](https://www.rfc-editor.org/rfc/rfc7540) HTTP/2 May 2015

[2.1](https://www.rfc-editor.org/rfc/rfc7540#section-2.1). Document Organization

   The HTTP/2 specification is split into four parts:

   o  Starting HTTP/2 ([Section 3](https://www.rfc-editor.org/rfc/rfc7540#section-3)) covers how an HTTP/2 connection is
      initiated.

   o  The frame ([Section 4](https://www.rfc-editor.org/rfc/rfc7540#section-4)) and stream ([Section 5](https://www.rfc-editor.org/rfc/rfc7540#section-5)) layers describe the
      way HTTP/2 frames are structured and formed into multiplexed
      streams.

   o  Frame ([Section 6](https://www.rfc-editor.org/rfc/rfc7540#section-6)) and error ([Section 7](https://www.rfc-editor.org/rfc/rfc7540#section-7)) definitions include
      details of the frame and error types used in HTTP/2.

   o  HTTP mappings ([Section 8](https://www.rfc-editor.org/rfc/rfc7540#section-8)) and additional requirements ([Section 9](https://www.rfc-editor.org/rfc/rfc7540#section-9))
      describe how HTTP semantics are expressed using frames and
      streams.

   While some of the frame and stream layer concepts are isolated from
   HTTP, this specification does not define a completely generic frame
   layer.  The frame and stream layers are tailored to the needs of the
   HTTP protocol and server push.

[2.2](https://www.rfc-editor.org/rfc/rfc7540#section-2.2). Conventions and Terminology

   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
   document are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) [[RFC2119](https://www.rfc-editor.org/rfc/rfc2119 "\"Key words for use in RFCs to Indicate Requirement Levels\"")].

   All numeric values are in network byte order.  Values are unsigned
   unless otherwise indicated.  Literal values are provided in decimal
   or hexadecimal as appropriate.  Hexadecimal literals are prefixed
   with "0x" to distinguish them from decimal literals.

   The following terms are used:

   client:  The endpoint that initiates an HTTP/2 connection.  Clients
      send HTTP requests and receive HTTP responses.

   connection:  A transport-layer connection between two endpoints.

   connection error:  An error that affects the entire HTTP/2
      connection.

   endpoint:  Either the client or server of the connection.

Belshe, et al. Standards Track [Page 6]

* * *

[RFC 7540](https://www.rfc-editor.org/rfc/rfc7540) HTTP/2 May 2015

   frame:  The smallest unit of communication within an HTTP/2
      connection, consisting of a header and a variable-length sequence
      of octets structured according to the frame type.

   peer:  An endpoint.  When discussing a particular endpoint, "peer"
      refers to the endpoint that is remote to the primary subject of
      discussion.

   receiver:  An endpoint that is receiving frames.

   sender:  An endpoint that is transmitting frames.

   server:  The endpoint that accepts an HTTP/2 connection.  Servers
      receive HTTP requests and send HTTP responses.

   stream:  A bidirectional flow of frames within the HTTP/2 connection.

   stream error:  An error on the individual HTTP/2 stream.

   Finally, the terms "gateway", "intermediary", "proxy", and "tunnel"
   are defined in [Section 2.3 of [RFC7230]](https://www.rfc-editor.org/rfc/rfc7230#section-2.3).  Intermediaries act as both
   client and server at different times.

   The term "payload body" is defined in [Section 3.3 of [RFC7230]](https://www.rfc-editor.org/rfc/rfc7230#section-3.3).

[3](https://www.rfc-editor.org/rfc/rfc7540#section-3). Starting HTTP/2

   An HTTP/2 connection is an application-layer protocol running on top
   of a TCP connection ([[TCP](https://www.rfc-editor.org/rfc/rfc7540#ref-TCP "\"Transmission Control Protocol\"")]).  The client is the TCP connection
   initiator.

   HTTP/2 uses the same "http" and "https" URI schemes used by HTTP/1.1.
   HTTP/2 shares the same default port numbers: 80 for "http" URIs and
   443 for "https" URIs.  As a result, implementations processing
   requests for target resource URIs like "http://example.org/foo" or
   "https://example.com/bar" are required to first discover whether the
   upstream server (the immediate peer to which the client wishes to
   establish a connection) supports HTTP/2.

   The means by which support for HTTP/2 is determined is different for
   "http" and "https" URIs.  Discovery for "http" URIs is described in
   [Section 3.2](https://www.rfc-editor.org/rfc/rfc7540#section-3.2).  Discovery for "https" URIs is described in [Section 3.3](https://www.rfc-editor.org/rfc/rfc7540#section-3.3).

Belshe, et al. Standards Track [Page 7]

* * *

[RFC 7540](https://www.rfc-editor.org/rfc/rfc7540) HTTP/2 May 2015

[3.1](https://www.rfc-editor.org/rfc/rfc7540#section-3.1). HTTP/2 Version Identification

   The protocol defined in this document has two identifiers.

   o  The string "h2" identifies the protocol where HTTP/2 uses
      Transport Layer Security (TLS) [[TLS12](https://www.rfc-editor.org/rfc/rfc7540#ref-TLS12 "\"The Transport Layer Security (TLS) Protocol Version 1.2\"")].  This identifier is used
      in the TLS application-layer protocol negotiation (ALPN) extension
      [[TLS-ALPN](https://www.rfc-editor.org/rfc/rfc7540#ref-TLS-ALPN "\"Transport Layer Security (TLS) Application-Layer Protocol Negotiation Extension\"")] field and in any place where HTTP/2 over TLS is
      identified.

      The "h2" string is serialized into an ALPN protocol identifier as
      the two-octet sequence: 0x68, 0x32.

   o  The string "h2c" identifies the protocol where HTTP/2 is run over
      cleartext TCP.  This identifier is used in the HTTP/1.1 Upgrade
      header field and in any place where HTTP/2 over TCP is identified.

      The "h2c" string is reserved from the ALPN identifier space but
      describes a protocol that does not use TLS.

   Negotiating "h2" or "h2c" implies the use of the transport, security,
   framing, and message semantics described in this document.

[3.2](https://www.rfc-editor.org/rfc/rfc7540#section-3.2). Starting HTTP/2 for "http" URIs

   A client that makes a request for an "http" URI without prior
   knowledge about support for HTTP/2 on the next hop uses the HTTP
   Upgrade mechanism ([Section 6.7 of [RFC7230]](https://www.rfc-editor.org/rfc/rfc7230#section-6.7)).  The client does so by
   making an HTTP/1.1 request that includes an Upgrade header field with
   the "h2c" token.  Such an HTTP/1.1 request MUST include exactly one
   HTTP2-Settings ([Section 3.2.1](https://www.rfc-editor.org/rfc/rfc7540#section-3.2.1)) header field.

   For example:

     GET / HTTP/1.1
     Host: server.example.com
     Connection: Upgrade, HTTP2-Settings
     Upgrade: h2c
     HTTP2-Settings: <base64url encoding of HTTP/2 SETTINGS payload>

   Requests that contain a payload body MUST be sent in their entirety
   before the client can send HTTP/2 frames.  This means that a large
   request can block the use of the connection until it is completely
   sent.

   If concurrency of an initial request with subsequent requests is
   important, an OPTIONS request can be used to perform the upgrade to
   HTTP/2, at the cost of an additional round trip.

Belshe, et al. Standards Track [Page 8]

* * *

[RFC 7540](https://www.rfc-editor.org/rfc/rfc7540) HTTP/2 May 2015

   A server that does not support HTTP/2 can respond to the request as
   though the Upgrade header field were absent:

     HTTP/1.1 200 OK
     Content-Length: 243
     Content-Type: text/html

     ...

   A server MUST ignore an "h2" token in an Upgrade header field.
   Presence of a token with "h2" implies HTTP/2 over TLS, which is
   instead negotiated as described in [Section 3.3](https://www.rfc-editor.org/rfc/rfc7540#section-3.3).

   A server that supports HTTP/2 accepts the upgrade with a 101
   (Switching Protocols) response.  After the empty line that terminates
   the 101 response, the server can begin sending HTTP/2 frames.  These
   frames MUST include a response to the request that initiated the
   upgrade.

   For example:

     HTTP/1.1 101 Switching Protocols
     Connection: Upgrade
     Upgrade: h2c

     [ HTTP/2 connection ...

   The first HTTP/2 frame sent by the server MUST be a server connection
   preface ([Section 3.5](https://www.rfc-editor.org/rfc/rfc7540#section-3.5)) consisting of a SETTINGS frame ([Section 6.5](https://www.rfc-editor.org/rfc/rfc7540#section-6.5)).
   Upon receiving the 101 response, the client MUST send a connection
   preface ([Section 3.5](https://www.rfc-editor.org/rfc/rfc7540#section-3.5)), which includes a SETTINGS frame.

   The HTTP/1.1 request that is sent prior to upgrade is assigned a
   stream identifier of 1 (see [Section 5.1.1](https://www.rfc-editor.org/rfc/rfc7540#section-5.1.1)) with default priority
   values ([Section 5.3.5](https://www.rfc-editor.org/rfc/rfc7540#section-5.3.5)).  Stream 1 is implicitly "half-closed" from
   the client toward the server (see [Section 5.1](https://www.rfc-editor.org/rfc/rfc7540#section-5.1)), since the request is
   completed as an HTTP/1.1 request.  After commencing the HTTP/2
   connection, stream 1 is used for the response.

[3.2.1](https://www.rfc-editor.org/rfc/rfc7540#section-3.2.1). HTTP2-Settings Header Field

   A request that upgrades from HTTP/1.1 to HTTP/2 MUST include exactly
   one "HTTP2-Settings" header field.  The HTTP2-Settings header field
   is a connection-specific header field that includes parameters that
   govern the HTTP/2 connection, provided in anticipation of the server
   accepting the request to upgrade.

     HTTP2-Settings    = token68

Belshe, et al. Standards Track [Page 9]

* * *

[RFC 7540](https://www.rfc-editor.org/rfc/rfc7540) HTTP/2 May 2015

   A server MUST NOT upgrade the connection to HTTP/2 if this header
   field is not present or if more than one is present.  A server MUST
   NOT send this header field.

   The content of the HTTP2-Settings header field is the payload of a
   SETTINGS frame ([Section 6.5](https://www.rfc-editor.org/rfc/rfc7540#section-6.5)), encoded as a base64url string (that is,
   the URL- and filename-safe Base64 encoding described in [Section 5 of [RFC4648]](https://www.rfc-editor.org/rfc/rfc4648#section-5), with any trailing '=' characters omitted).  The ABNF
   [[RFC5234](https://www.rfc-editor.org/rfc/rfc5234 "\"Augmented BNF for Syntax Specifications: ABNF\"")] production for "token68" is defined in [Section 2.1 of [RFC7235]](https://www.rfc-editor.org/rfc/rfc7235#section-2.1).

   Since the upgrade is only intended to apply to the immediate
   connection, a client sending the HTTP2-Settings header field MUST
   also send "HTTP2-Settings" as a connection option in the Connection
   header field to prevent it from being forwarded (see [Section 6.1 of [RFC7230]](https://www.rfc-editor.org/rfc/rfc7230#section-6.1)).

   A server decodes and interprets these values as it would any other
   SETTINGS frame.  Explicit acknowledgement of these settings
   ([Section 6.5.3](https://www.rfc-editor.org/rfc/rfc7540#section-6.5.3)) is not necessary, since a 101 response serves as
   implicit acknowledgement.  Providing these values in the upgrade
   request gives a client an opportunity to provide parameters prior to
   receiving any frames from the server.

[3.3](https://www.rfc-editor.org/rfc/rfc7540#section-3.3). Starting HTTP/2 for "https" URIs

   A client that makes a request to an "https" URI uses TLS [[TLS12](https://www.rfc-editor.org/rfc/rfc7540#ref-TLS12 "\"The Transport Layer Security (TLS) Protocol Version 1.2\"")] with
   the application-layer protocol negotiation (ALPN) extension
   [[TLS-ALPN](https://www.rfc-editor.org/rfc/rfc7540#ref-TLS-ALPN "\"Transport Layer Security (TLS) Application-Layer Protocol Negotiation Extension\"")].

   HTTP/2 over TLS uses the "h2" protocol identifier.  The "h2c"
   protocol identifier MUST NOT be sent by a client or selected by a
   server; the "h2c" protocol identifier describes a protocol that does
