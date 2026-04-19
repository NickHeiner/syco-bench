# RFC 7231: Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content
[[RFC Home](https://www.rfc-editor.org/ "RFC Editor")] [[TEXT](https://www.rfc-editor.org/rfc/rfc7231.txt)|[PDF](https://www.rfc-editor.org/rfc/pdfrfc/rfc7231.txt.pdf)|[HTML](https://www.rfc-editor.org/rfc/rfc7231.html)] [[Tracker](https://datatracker.ietf.org/doc/rfc7231 "IETF Datatracker information for this document")] [[IPR](https://datatracker.ietf.org/ipr/search/?rfc=7231&submit=rfc "IPR disclosures related to this document")] [[Errata](https://www.rfc-editor.org/errata/rfc7231)] [[Info page](https://www.rfc-editor.org/info/rfc7231 "Info page")] 

Obsoleted by: [9110](https://www.rfc-editor.org/rfc/rfc9110) PROPOSED STANDARD

Errata Exist Internet Engineering Task Force (IETF)                  R. Fielding, Ed.
Request for Comments: 7231                                         Adobe
Obsoletes: [2616](https://www.rfc-editor.org/rfc/rfc2616)                                          J. Reschke, Ed.
Updates: [2817](https://www.rfc-editor.org/rfc/rfc2817)                                                 greenbytes
Category: Standards Track                                      June 2014
ISSN: 2070-1721

     Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content

Abstract

   The Hypertext Transfer Protocol (HTTP) is a stateless application-
   level protocol for distributed, collaborative, hypertext information
   systems.  This document defines the semantics of HTTP/1.1 messages,
   as expressed by request methods, request header fields, response
   status codes, and response header fields, along with the payload of
   messages (metadata and body content) and mechanisms for content
   negotiation.

Status of This Memo

   This is an Internet Standards Track document.

   This document is a product of the Internet Engineering Task Force
   (IETF).  It represents the consensus of the IETF community.  It has
   received public review and has been approved for publication by the
   Internet Engineering Steering Group (IESG).  Further information on
   Internet Standards is available in [Section 2 of RFC 5741](https://www.rfc-editor.org/rfc/rfc5741#section-2).

   Information about the current status of this document, any errata,
   and how to provide feedback on it may be obtained at
   [http://www.rfc-editor.org/info/rfc7231](https://www.rfc-editor.org/info/rfc7231).

Fielding & Reschke Standards Track [Page 1]

* * *

[RFC 7231](https://www.rfc-editor.org/rfc/rfc7231) HTTP/1.1 Semantics and Content June 2014

Copyright Notice

   Copyright (c) 2014 IETF Trust and the persons identified as the
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

   This document may contain material from IETF Documents or IETF
   Contributions published or made publicly available before November
   10, 2008.  The person(s) controlling the copyright in some of this
   material may not have granted the IETF Trust the right to allow
   modifications of such material outside the IETF Standards Process.
   Without obtaining an adequate license from the person(s) controlling
   the copyright in such materials, this document may not be modified
   outside the IETF Standards Process, and derivative works of it may
   not be created outside the IETF Standards Process, except to format
   it for publication as an RFC or to translate it into languages other
   than English.

Fielding & Reschke Standards Track [Page 2]

* * *

[RFC 7231](https://www.rfc-editor.org/rfc/rfc7231) HTTP/1.1 Semantics and Content June 2014

Table of Contents

   [1](https://www.rfc-editor.org/rfc/rfc7231#section-1). Introduction ....................................................[6](https://www.rfc-editor.org/rfc/rfc7231#page-6)
      [1.1](https://www.rfc-editor.org/rfc/rfc7231#section-1.1). Conformance and Error Handling .............................[6](https://www.rfc-editor.org/rfc/rfc7231#page-6)
      [1.2](https://www.rfc-editor.org/rfc/rfc7231#section-1.2). Syntax Notation ............................................[6](https://www.rfc-editor.org/rfc/rfc7231#page-6)
   [2](https://www.rfc-editor.org/rfc/rfc7231#section-2). Resources .......................................................[7](https://www.rfc-editor.org/rfc/rfc7231#page-7)
   [3](https://www.rfc-editor.org/rfc/rfc7231#section-3). Representations .................................................[7](https://www.rfc-editor.org/rfc/rfc7231#page-7)
      [3.1](https://www.rfc-editor.org/rfc/rfc7231#section-3.1). Representation Metadata ....................................[8](https://www.rfc-editor.org/rfc/rfc7231#page-8)
           [3.1.1](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.1). Processing Representation Data ......................[8](https://www.rfc-editor.org/rfc/rfc7231#page-8)
           [3.1.2](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.2). Encoding for Compression or Integrity ..............[11](https://www.rfc-editor.org/rfc/rfc7231#page-11)
           [3.1.3](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.3). Audience Language ..................................[13](https://www.rfc-editor.org/rfc/rfc7231#page-13)
           [3.1.4](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.4). Identification .....................................[14](https://www.rfc-editor.org/rfc/rfc7231#page-14)
      [3.2](https://www.rfc-editor.org/rfc/rfc7231#section-3.2). Representation Data .......................................[17](https://www.rfc-editor.org/rfc/rfc7231#page-17)
      [3.3](https://www.rfc-editor.org/rfc/rfc7231#section-3.3). Payload Semantics .........................................[17](https://www.rfc-editor.org/rfc/rfc7231#page-17)
      [3.4](https://www.rfc-editor.org/rfc/rfc7231#section-3.4). Content Negotiation .......................................[18](https://www.rfc-editor.org/rfc/rfc7231#page-18)
           [3.4.1](https://www.rfc-editor.org/rfc/rfc7231#section-3.4.1). Proactive Negotiation ..............................[19](https://www.rfc-editor.org/rfc/rfc7231#page-19)
           [3.4.2](https://www.rfc-editor.org/rfc/rfc7231#section-3.4.2). Reactive Negotiation ...............................[20](https://www.rfc-editor.org/rfc/rfc7231#page-20)
   [4](https://www.rfc-editor.org/rfc/rfc7231#section-4). Request Methods ................................................[21](https://www.rfc-editor.org/rfc/rfc7231#page-21)
      [4.1](https://www.rfc-editor.org/rfc/rfc7231#section-4.1). Overview ..................................................[21](https://www.rfc-editor.org/rfc/rfc7231#page-21)
      [4.2](https://www.rfc-editor.org/rfc/rfc7231#section-4.2). Common Method Properties ..................................[22](https://www.rfc-editor.org/rfc/rfc7231#page-22)
           [4.2.1](https://www.rfc-editor.org/rfc/rfc7231#section-4.2.1). Safe Methods .......................................[22](https://www.rfc-editor.org/rfc/rfc7231#page-22)
           [4.2.2](https://www.rfc-editor.org/rfc/rfc7231#section-4.2.2). Idempotent Methods .................................[23](https://www.rfc-editor.org/rfc/rfc7231#page-23)
           [4.2.3](https://www.rfc-editor.org/rfc/rfc7231#section-4.2.3). Cacheable Methods ..................................[24](https://www.rfc-editor.org/rfc/rfc7231#page-24)
      [4.3](https://www.rfc-editor.org/rfc/rfc7231#section-4.3). Method Definitions ........................................[24](https://www.rfc-editor.org/rfc/rfc7231#page-24)
           [4.3.1](https://www.rfc-editor.org/rfc/rfc7231#section-4.3.1). GET ................................................[24](https://www.rfc-editor.org/rfc/rfc7231#page-24)
           [4.3.2](https://www.rfc-editor.org/rfc/rfc7231#section-4.3.2). HEAD ...............................................[25](https://www.rfc-editor.org/rfc/rfc7231#page-25)
           [4.3.3](https://www.rfc-editor.org/rfc/rfc7231#section-4.3.3). POST ...............................................[25](https://www.rfc-editor.org/rfc/rfc7231#page-25)
           [4.3.4](https://www.rfc-editor.org/rfc/rfc7231#section-4.3.4). PUT ................................................[26](https://www.rfc-editor.org/rfc/rfc7231#page-26)
           [4.3.5](https://www.rfc-editor.org/rfc/rfc7231#section-4.3.5). DELETE .............................................[29](https://www.rfc-editor.org/rfc/rfc7231#page-29)
           [4.3.6](https://www.rfc-editor.org/rfc/rfc7231#section-4.3.6). CONNECT ............................................[30](https://www.rfc-editor.org/rfc/rfc7231#page-30)
           [4.3.7](https://www.rfc-editor.org/rfc/rfc7231#section-4.3.7). OPTIONS ............................................[31](https://www.rfc-editor.org/rfc/rfc7231#page-31)
           [4.3.8](https://www.rfc-editor.org/rfc/rfc7231#section-4.3.8). TRACE ..............................................[32](https://www.rfc-editor.org/rfc/rfc7231#page-32)
   [5](https://www.rfc-editor.org/rfc/rfc7231#section-5). Request Header Fields ..........................................[33](https://www.rfc-editor.org/rfc/rfc7231#page-33)
      [5.1](https://www.rfc-editor.org/rfc/rfc7231#section-5.1). Controls ..................................................[33](https://www.rfc-editor.org/rfc/rfc7231#page-33)
           [5.1.1](https://www.rfc-editor.org/rfc/rfc7231#section-5.1.1). Expect .............................................[34](https://www.rfc-editor.org/rfc/rfc7231#page-34)
           [5.1.2](https://www.rfc-editor.org/rfc/rfc7231#section-5.1.2). Max-Forwards .......................................[36](https://www.rfc-editor.org/rfc/rfc7231#page-36)
      [5.2](https://www.rfc-editor.org/rfc/rfc7231#section-5.2). Conditionals ..............................................[36](https://www.rfc-editor.org/rfc/rfc7231#page-36)
      [5.3](https://www.rfc-editor.org/rfc/rfc7231#section-5.3). Content Negotiation .......................................[37](https://www.rfc-editor.org/rfc/rfc7231#page-37)
           [5.3.1](https://www.rfc-editor.org/rfc/rfc7231#section-5.3.1). Quality Values .....................................[37](https://www.rfc-editor.org/rfc/rfc7231#page-37)
           [5.3.2](https://www.rfc-editor.org/rfc/rfc7231#section-5.3.2). Accept .............................................[38](https://www.rfc-editor.org/rfc/rfc7231#page-38)
           [5.3.3](https://www.rfc-editor.org/rfc/rfc7231#section-5.3.3). Accept-Charset .....................................[40](https://www.rfc-editor.org/rfc/rfc7231#page-40)
           [5.3.4](https://www.rfc-editor.org/rfc/rfc7231#section-5.3.4). Accept-Encoding ....................................[41](https://www.rfc-editor.org/rfc/rfc7231#page-41)
           [5.3.5](https://www.rfc-editor.org/rfc/rfc7231#section-5.3.5). Accept-Language ....................................[42](https://www.rfc-editor.org/rfc/rfc7231#page-42)
      [5.4](https://www.rfc-editor.org/rfc/rfc7231#section-5.4). Authentication Credentials ................................[44](https://www.rfc-editor.org/rfc/rfc7231#page-44)
      [5.5](https://www.rfc-editor.org/rfc/rfc7231#section-5.5). Request Context ...........................................[44](https://www.rfc-editor.org/rfc/rfc7231#page-44)
           [5.5.1](https://www.rfc-editor.org/rfc/rfc7231#section-5.5.1). From ...............................................[44](https://www.rfc-editor.org/rfc/rfc7231#page-44)
           [5.5.2](https://www.rfc-editor.org/rfc/rfc7231#section-5.5.2). Referer ............................................[45](https://www.rfc-editor.org/rfc/rfc7231#page-45)
           [5.5.3](https://www.rfc-editor.org/rfc/rfc7231#section-5.5.3). User-Agent .........................................[46](https://www.rfc-editor.org/rfc/rfc7231#page-46)

Fielding & Reschke Standards Track [Page 3]

* * *

[RFC 7231](https://www.rfc-editor.org/rfc/rfc7231) HTTP/1.1 Semantics and Content June 2014

   [6](https://www.rfc-editor.org/rfc/rfc7231#section-6). Response Status Codes ..........................................[47](https://www.rfc-editor.org/rfc/rfc7231#page-47)
      [6.1](https://www.rfc-editor.org/rfc/rfc7231#section-6.1). Overview of Status Codes ..................................[48](https://www.rfc-editor.org/rfc/rfc7231#page-48)
      [6.2](https://www.rfc-editor.org/rfc/rfc7231#section-6.2). Informational 1xx .........................................[50](https://www.rfc-editor.org/rfc/rfc7231#page-50)
           [6.2.1](https://www.rfc-editor.org/rfc/rfc7231#section-6.2.1). 100 Continue .......................................[50](https://www.rfc-editor.org/rfc/rfc7231#page-50)
           [6.2.2](https://www.rfc-editor.org/rfc/rfc7231#section-6.2.2). 101 Switching Protocols ............................[50](https://www.rfc-editor.org/rfc/rfc7231#page-50)
      [6.3](https://www.rfc-editor.org/rfc/rfc7231#section-6.3). Successful 2xx ............................................[51](https://www.rfc-editor.org/rfc/rfc7231#page-51)
           [6.3.1](https://www.rfc-editor.org/rfc/rfc7231#section-6.3.1). 200 OK .............................................[51](https://www.rfc-editor.org/rfc/rfc7231#page-51)
           [6.3.2](https://www.rfc-editor.org/rfc/rfc7231#section-6.3.2). 201 Created ........................................[52](https://www.rfc-editor.org/rfc/rfc7231#page-52)
           [6.3.3](https://www.rfc-editor.org/rfc/rfc7231#section-6.3.3). 202 Accepted .......................................[52](https://www.rfc-editor.org/rfc/rfc7231#page-52)
           [6.3.4](https://www.rfc-editor.org/rfc/rfc7231#section-6.3.4). 203 Non-Authoritative Information ..................[52](https://www.rfc-editor.org/rfc/rfc7231#page-52)
           [6.3.5](https://www.rfc-editor.org/rfc/rfc7231#section-6.3.5). 204 No Content .....................................[53](https://www.rfc-editor.org/rfc/rfc7231#page-53)
           [6.3.6](https://www.rfc-editor.org/rfc/rfc7231#section-6.3.6). 205 Reset Content ..................................[53](https://www.rfc-editor.org/rfc/rfc7231#page-53)
      [6.4](https://www.rfc-editor.org/rfc/rfc7231#section-6.4). Redirection 3xx ...........................................[54](https://www.rfc-editor.org/rfc/rfc7231#page-54)
           [6.4.1](https://www.rfc-editor.org/rfc/rfc7231#section-6.4.1). 300 Multiple Choices ...............................[55](https://www.rfc-editor.org/rfc/rfc7231#page-55)
           [6.4.2](https://www.rfc-editor.org/rfc/rfc7231#section-6.4.2). 301 Moved Permanently ..............................[56](https://www.rfc-editor.org/rfc/rfc7231#page-56)
           [6.4.3](https://www.rfc-editor.org/rfc/rfc7231#section-6.4.3). 302 Found ..........................................[56](https://www.rfc-editor.org/rfc/rfc7231#page-56)
           [6.4.4](https://www.rfc-editor.org/rfc/rfc7231#section-6.4.4). 303 See Other ......................................[57](https://www.rfc-editor.org/rfc/rfc7231#page-57)
           [6.4.5](https://www.rfc-editor.org/rfc/rfc7231#section-6.4.5). 305 Use Proxy ......................................[58](https://www.rfc-editor.org/rfc/rfc7231#page-58)
           [6.4.6](https://www.rfc-editor.org/rfc/rfc7231#section-6.4.6). 306 (Unused) .......................................[58](https://www.rfc-editor.org/rfc/rfc7231#page-58)
           [6.4.7](https://www.rfc-editor.org/rfc/rfc7231#section-6.4.7). 307 Temporary Redirect .............................[58](https://www.rfc-editor.org/rfc/rfc7231#page-58)
      [6.5](https://www.rfc-editor.org/rfc/rfc7231#section-6.5). Client Error 4xx ..........................................[58](https://www.rfc-editor.org/rfc/rfc7231#page-58)
           [6.5.1](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.1). 400 Bad Request ....................................[58](https://www.rfc-editor.org/rfc/rfc7231#page-58)
           [6.5.2](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.2). 402 Payment Required ...............................[59](https://www.rfc-editor.org/rfc/rfc7231#page-59)
           [6.5.3](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.3). 403 Forbidden ......................................[59](https://www.rfc-editor.org/rfc/rfc7231#page-59)
           [6.5.4](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.4). 404 Not Found ......................................[59](https://www.rfc-editor.org/rfc/rfc7231#page-59)
           [6.5.5](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.5). 405 Method Not Allowed .............................[59](https://www.rfc-editor.org/rfc/rfc7231#page-59)
           [6.5.6](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.6). 406 Not Acceptable .................................[60](https://www.rfc-editor.org/rfc/rfc7231#page-60)
           [6.5.7](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.7). 408 Request Timeout ................................[60](https://www.rfc-editor.org/rfc/rfc7231#page-60)
           [6.5.8](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.8). 409 Conflict .......................................[60](https://www.rfc-editor.org/rfc/rfc7231#page-60)
           [6.5.9](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.9). 410 Gone ...........................................[60](https://www.rfc-editor.org/rfc/rfc7231#page-60)
           [6.5.10](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.10). 411 Length Required ...............................[61](https://www.rfc-editor.org/rfc/rfc7231#page-61)
           [6.5.11](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.11). 413 Payload Too Large .............................[61](https://www.rfc-editor.org/rfc/rfc7231#page-61)
           [6.5.12](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.12). 414 URI Too Long ..................................[61](https://www.rfc-editor.org/rfc/rfc7231#page-61)
           [6.5.13](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.13). 415 Unsupported Media Type ........................[62](https://www.rfc-editor.org/rfc/rfc7231#page-62)
           [6.5.14](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.14). 417 Expectation Failed ............................[62](https://www.rfc-editor.org/rfc/rfc7231#page-62)
           [6.5.15](https://www.rfc-editor.org/rfc/rfc7231#section-6.5.15). 426 Upgrade Required ..............................[62](https://www.rfc-editor.org/rfc/rfc7231#page-62)
      [6.6](https://www.rfc-editor.org/rfc/rfc7231#section-6.6). Server Error 5xx ..........................................[62](https://www.rfc-editor.org/rfc/rfc7231#page-62)
           [6.6.1](https://www.rfc-editor.org/rfc/rfc7231#section-6.6.1). 500 Internal Server Error ..........................[63](https://www.rfc-editor.org/rfc/rfc7231#page-63)
           [6.6.2](https://www.rfc-editor.org/rfc/rfc7231#section-6.6.2). 501 Not Implemented ................................[63](https://www.rfc-editor.org/rfc/rfc7231#page-63)
           [6.6.3](https://www.rfc-editor.org/rfc/rfc7231#section-6.6.3). 502 Bad Gateway ....................................[63](https://www.rfc-editor.org/rfc/rfc7231#page-63)
           [6.6.4](https://www.rfc-editor.org/rfc/rfc7231#section-6.6.4). 503 Service Unavailable ............................[63](https://www.rfc-editor.org/rfc/rfc7231#page-63)
           [6.6.5](https://www.rfc-editor.org/rfc/rfc7231#section-6.6.5). 504 Gateway Timeout ................................[63](https://www.rfc-editor.org/rfc/rfc7231#page-63)
           [6.6.6](https://www.rfc-editor.org/rfc/rfc7231#section-6.6.6). 505 HTTP Version Not Supported .....................[64](https://www.rfc-editor.org/rfc/rfc7231#page-64)
   [7](https://www.rfc-editor.org/rfc/rfc7231#section-7). Response Header Fields .........................................[64](https://www.rfc-editor.org/rfc/rfc7231#page-64)
      [7.1](https://www.rfc-editor.org/rfc/rfc7231#section-7.1). Control Data ..............................................[64](https://www.rfc-editor.org/rfc/rfc7231#page-64)
ed            7.1.1. Origination Date ...................................[65](https://www.rfc-editor.org/rfc/rfc7231#page-65)
           [7.1.2](https://www.rfc-editor.org/rfc/rfc7231#section-7.1.2). Location ...........................................[68](https://www.rfc-editor.org/rfc/rfc7231#page-68)
           [7.1.3](https://www.rfc-editor.org/rfc/rfc7231#section-7.1.3). Retry-After ........................................[69](https://www.rfc-editor.org/rfc/rfc7231#page-69)

Fielding & Reschke Standards Track [Page 4]

* * *

[RFC 7231](https://www.rfc-editor.org/rfc/rfc7231) HTTP/1.1 Semantics and Content June 2014

           [7.1.4](https://www.rfc-editor.org/rfc/rfc7231#section-7.1.4). Vary ...............................................[70](https://www.rfc-editor.org/rfc/rfc7231#page-70)
      [7.2](https://www.rfc-editor.org/rfc/rfc7231#section-7.2). Validator Header Fields ...................................[71](https://www.rfc-editor.org/rfc/rfc7231#page-71)
      [7.3](https://www.rfc-editor.org/rfc/rfc7231#section-7.3). Authentication Challenges .................................[72](https://www.rfc-editor.org/rfc/rfc7231#page-72)
      [7.4](https://www.rfc-editor.org/rfc/rfc7231#section-7.4). Response Context ..........................................[72](https://www.rfc-editor.org/rfc/rfc7231#page-72)
           [7.4.1](https://www.rfc-editor.org/rfc/rfc7231#section-7.4.1). Allow ..............................................[72](https://www.rfc-editor.org/rfc/rfc7231#page-72)
           [7.4.2](https://www.rfc-editor.org/rfc/rfc7231#section-7.4.2). Server .............................................[73](https://www.rfc-editor.org/rfc/rfc7231#page-73)
   [8](https://www.rfc-editor.org/rfc/rfc7231#section-8). IANA Considerations ............................................[73](https://www.rfc-editor.org/rfc/rfc7231#page-73)
      [8.1](https://www.rfc-editor.org/rfc/rfc7231#section-8.1). Method Registry ...........................................[73](https://www.rfc-editor.org/rfc/rfc7231#page-73)
           [8.1.1](https://www.rfc-editor.org/rfc/rfc7231#section-8.1.1). Procedure ..........................................[74](https://www.rfc-editor.org/rfc/rfc7231#page-74)
           [8.1.2](https://www.rfc-editor.org/rfc/rfc7231#section-8.1.2). Considerations for New Methods .....................[74](https://www.rfc-editor.org/rfc/rfc7231#page-74)
           [8.1.3](https://www.rfc-editor.org/rfc/rfc7231#section-8.1.3). Registrations ......................................[75](https://www.rfc-editor.org/rfc/rfc7231#page-75)
      [8.2](https://www.rfc-editor.org/rfc/rfc7231#section-8.2). Status Code Registry ......................................[75](https://www.rfc-editor.org/rfc/rfc7231#page-75)
           [8.2.1](https://www.rfc-editor.org/rfc/rfc7231#section-8.2.1). Procedure ..........................................[75](https://www.rfc-editor.org/rfc/rfc7231#page-75)
           [8.2.2](https://www.rfc-editor.org/rfc/rfc7231#section-8.2.2). Considerations for New Status Codes ................[76](https://www.rfc-editor.org/rfc/rfc7231#page-76)
           [8.2.3](https://www.rfc-editor.org/rfc/rfc7231#section-8.2.3). Registrations ......................................[76](https://www.rfc-editor.org/rfc/rfc7231#page-76)
      [8.3](https://www.rfc-editor.org/rfc/rfc7231#section-8.3). Header Field Registry .....................................[77](https://www.rfc-editor.org/rfc/rfc7231#page-77)
           [8.3.1](https://www.rfc-editor.org/rfc/rfc7231#section-8.3.1). Considerations for New Header Fields ...............[78](https://www.rfc-editor.org/rfc/rfc7231#page-78)
           [8.3.2](https://www.rfc-editor.org/rfc/rfc7231#section-8.3.2). Registrations ......................................[80](https://www.rfc-editor.org/rfc/rfc7231#page-80)
      [8.4](https://www.rfc-editor.org/rfc/rfc7231#section-8.4). Content Coding Registry ...................................[81](https://www.rfc-editor.org/rfc/rfc7231#page-81)
           [8.4.1](https://www.rfc-editor.org/rfc/rfc7231#section-8.4.1). Procedure ..........................................[81](https://www.rfc-editor.org/rfc/rfc7231#page-81)
           [8.4.2](https://www.rfc-editor.org/rfc/rfc7231#section-8.4.2). Registrations ......................................[81](https://www.rfc-editor.org/rfc/rfc7231#page-81)
   [9](https://www.rfc-editor.org/rfc/rfc7231#section-9). Security Considerations ........................................[81](https://www.rfc-editor.org/rfc/rfc7231#page-81)
      [9.1](https://www.rfc-editor.org/rfc/rfc7231#section-9.1). Attacks Based on File and Path Names ......................[82](https://www.rfc-editor.org/rfc/rfc7231#page-82)
      [9.2](https://www.rfc-editor.org/rfc/rfc7231#section-9.2). Attacks Based on Command, Code, or Query Injection ........[82](https://www.rfc-editor.org/rfc/rfc7231#page-82)
      [9.3](https://www.rfc-editor.org/rfc/rfc7231#section-9.3). Disclosure of Personal Information ........................[83](https://www.rfc-editor.org/rfc/rfc7231#page-83)
      [9.4](https://www.rfc-editor.org/rfc/rfc7231#section-9.4). Disclosure of Sensitive Information in URIs ...............[83](https://www.rfc-editor.org/rfc/rfc7231#page-83)
      [9.5](https://www.rfc-editor.org/rfc/rfc7231#section-9.5). Disclosure of Fragment after Redirects ....................[84](https://www.rfc-editor.org/rfc/rfc7231#page-84)
      [9.6](https://www.rfc-editor.org/rfc/rfc7231#section-9.6). Disclosure of Product Information .........................[84](https://www.rfc-editor.org/rfc/rfc7231#page-84)
      [9.7](https://www.rfc-editor.org/rfc/rfc7231#section-9.7). Browser Fingerprinting ....................................[84](https://www.rfc-editor.org/rfc/rfc7231#page-84)
   [10](https://www.rfc-editor.org/rfc/rfc7231#section-10). Acknowledgments ...............................................[85](https://www.rfc-editor.org/rfc/rfc7231#page-85)
   [11](https://www.rfc-editor.org/rfc/rfc7231#section-11). References ....................................................[85](https://www.rfc-editor.org/rfc/rfc7231#page-85)
      [11.1](https://www.rfc-editor.org/rfc/rfc7231#section-11.1). Normative References .....................................[85](https://www.rfc-editor.org/rfc/rfc7231#page-85)
      [11.2](https://www.rfc-editor.org/rfc/rfc7231#section-11.2). Informative References ...................................[86](https://www.rfc-editor.org/rfc/rfc7231#page-86)
   [Appendix A](https://www.rfc-editor.org/rfc/rfc7231#appendix-A). Differences between HTTP and MIME .....................[89](https://www.rfc-editor.org/rfc/rfc7231#page-89)
      [A.1](https://www.rfc-editor.org/rfc/rfc7231#appendix-A.1). MIME-Version ..............................................[89](https://www.rfc-editor.org/rfc/rfc7231#page-89)
      [A.2](https://www.rfc-editor.org/rfc/rfc7231#appendix-A.2). Conversion to Canonical Form ..............................[89](https://www.rfc-editor.org/rfc/rfc7231#page-89)
      [A.3](https://www.rfc-editor.org/rfc/rfc7231#appendix-A.3). Conversion of Date Formats ................................[90](https://www.rfc-editor.org/rfc/rfc7231#page-90)
      [A.4](https://www.rfc-editor.org/rfc/rfc7231#appendix-A.4). Conversion of Content-Encoding ............................[90](https://www.rfc-editor.org/rfc/rfc7231#page-90)
      [A.5](https://www.rfc-editor.org/rfc/rfc7231#appendix-A.5). Conversion of Content-Transfer-Encoding ...................[90](https://www.rfc-editor.org/rfc/rfc7231#page-90)
      [A.6](https://www.rfc-editor.org/rfc/rfc7231#appendix-A.6). MHTML and Line Length Limitations .........................[90](https://www.rfc-editor.org/rfc/rfc7231#page-90)
   [Appendix B](https://www.rfc-editor.org/rfc/rfc7231#appendix-B). Changes from [RFC 2616](https://www.rfc-editor.org/rfc/rfc2616) .................................[91](https://www.rfc-editor.org/rfc/rfc7231#page-91)
   [Appendix C](https://www.rfc-editor.org/rfc/rfc7231#appendix-C). Imported ABNF .........................................[93](https://www.rfc-editor.org/rfc/rfc7231#page-93)
   [Appendix D](https://www.rfc-editor.org/rfc/rfc7231#appendix-D). Collected ABNF ........................................[94](https://www.rfc-editor.org/rfc/rfc7231#page-94)
   Index .............................................................[97](https://www.rfc-editor.org/rfc/rfc7231#page-97)

Fielding & Reschke Standards Track [Page 5]

* * *

[RFC 7231](https://www.rfc-editor.org/rfc/rfc7231) HTTP/1.1 Semantics and Content June 2014

[1](https://www.rfc-editor.org/rfc/rfc7231#section-1). Introduction

   Each Hypertext Transfer Protocol (HTTP) message is either a request
   or a response.  A server listens on a connection for a request,
   parses each message received, interprets the message semantics in
   relation to the identified request target, and responds to that
   request with one or more response messages.  A client constructs
   request messages to communicate specific intentions, examines
   received responses to see if the intentions were carried out, and
   determines how to interpret the results.  This document defines
   HTTP/1.1 request and response semantics in terms of the architecture
   defined in [[RFC7230](https://www.rfc-editor.org/rfc/rfc7230 "\"Hypertext Transfer Protocol (HTTP/1.1): Message Syntax and Routing\"")].

   HTTP provides a uniform interface for interacting with a resource
   ([Section 2](https://www.rfc-editor.org/rfc/rfc7231#section-2)), regardless of its type, nature, or implementation, via
   the manipulation and transfer of representations ([Section 3](https://www.rfc-editor.org/rfc/rfc7231#section-3)).

   HTTP semantics include the intentions defined by each request method
   ([Section 4](https://www.rfc-editor.org/rfc/rfc7231#section-4)), extensions to those semantics that might be described in
   request header fields ([Section 5](https://www.rfc-editor.org/rfc/rfc7231#section-5)), the meaning of status codes to
   indicate a machine-readable response ([Section 6](https://www.rfc-editor.org/rfc/rfc7231#section-6)), and the meaning of
   other control data and resource metadata that might be given in
   response header fields ([Section 7](https://www.rfc-editor.org/rfc/rfc7231#section-7)).

   This document also defines representation metadata that describe how
   a payload is intended to be interpreted by a recipient, the request
   header fields that might influence content selection, and the various
   selection algorithms that are collectively referred to as "content
   negotiation" ([Section 3.4](https://www.rfc-editor.org/rfc/rfc7231#section-3.4)).

[1.1](https://www.rfc-editor.org/rfc/rfc7231#section-1.1). Conformance and Error Handling

   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
   document are to be interpreted as described in [[RFC2119](https://www.rfc-editor.org/rfc/rfc2119 "\"Key words for use in RFCs to Indicate Requirement Levels\"")].

   Conformance criteria and considerations regarding error handling are
   defined in [Section 2.5 of [RFC7230]](https://www.rfc-editor.org/rfc/rfc7230#section-2.5).

[1.2](https://www.rfc-editor.org/rfc/rfc7231#section-1.2). Syntax Notation

   This specification uses the Augmented Backus-Naur Form (ABNF)
   notation of [[RFC5234](https://www.rfc-editor.org/rfc/rfc5234 "\"Augmented BNF for Syntax Specifications: ABNF\"")] with a list extension, defined in [Section 7 of [RFC7230]](https://www.rfc-editor.org/rfc/rfc7230#section-7), that allows for compact definition of comma-separated
   lists using a '#' operator (similar to how the '*' operator indicates
   repetition).  [Appendix C](https://www.rfc-editor.org/rfc/rfc7231#appendix-C) describes rules imported from other
   documents.  [Appendix D](https://www.rfc-editor.org/rfc/rfc7231#appendix-D) shows the collected grammar with all list
   operators expanded to standard ABNF notation.

Fielding & Reschke Standards Track [Page 6]

* * *

[RFC 7231](https://www.rfc-editor.org/rfc/rfc7231) HTTP/1.1 Semantics and Content June 2014

   This specification uses the terms "character", "character encoding
   scheme", "charset", and "protocol element" as they are defined in
   [[RFC6365](https://www.rfc-editor.org/rfc/rfc6365 "\"Terminology Used in Internationalization in the IETF\"")].

[2](https://www.rfc-editor.org/rfc/rfc7231#section-2). Resources

   The target of an HTTP request is called a "resource".  HTTP does not
   limit the nature of a resource; it merely defines an interface that
   might be used to interact with resources.  Each resource is
   identified by a Uniform Resource Identifier (URI), as described in
   [Section 2.7 of [RFC7230]](https://www.rfc-editor.org/rfc/rfc7230#section-2.7).

   When a client constructs an HTTP/1.1 request message, it sends the
   target URI in one of various forms, as defined in ([Section 5.3 of [RFC7230]](https://www.rfc-editor.org/rfc/rfc7230#section-5.3)).  When a request is received, the server reconstructs an
   effective request URI for the target resource ([Section 5.5 of [RFC7230]](https://www.rfc-editor.org/rfc/rfc7230#section-5.5)).

   One design goal of HTTP is to separate resource identification from
   request semantics, which is made possible by vesting the request
   semantics in the request method ([Section 4](https://www.rfc-editor.org/rfc/rfc7231#section-4)) and a few
   request-modifying header fields ([Section 5](https://www.rfc-editor.org/rfc/rfc7231#section-5)).  If there is a conflict
   between the method semantics and any semantic implied by the URI
   itself, as described in [Section 4.2.1](https://www.rfc-editor.org/rfc/rfc7231#section-4.2.1), the method semantics take
   precedence.

[3](https://www.rfc-editor.org/rfc/rfc7231#section-3). Representations

   Considering that a resource could be anything, and that the uniform
   interface provided by HTTP is similar to a window through which one
   can observe and act upon such a thing only through the communication
   of messages to some independent actor on the other side, an
   abstraction is needed to represent ("take the place of") the current
   or desired state of that thing in our communications.  That
   abstraction is called a representation [[REST](https://www.rfc-editor.org/rfc/rfc7231#ref-REST "\"Architectural Styles and the Design of Network-based Software Architectures\"")].

   For the purposes of HTTP, a "representation" is information that is
   intended to reflect a past, current, or desired state of a given
   resource, in a format that can be readily communicated via the
   protocol, and that consists of a set of representation metadata and a
   potentially unbounded stream of representation data.

   An origin server might be provided with, or be capable of generating,
   multiple representations that are each intended to reflect the
   current state of a target resource.  In such cases, some algorithm is
   used by the origin server to select one of those representations as
   most applicable to a given request, usually based on content
   negotiation.  This "selected representation" is used to provide the

Fielding & Reschke Standards Track [Page 7]

* * *

[RFC 7231](https://www.rfc-editor.org/rfc/rfc7231) HTTP/1.1 Semantics and Content June 2014

   data and metadata for evaluating conditional requests [[RFC7232](https://www.rfc-editor.org/rfc/rfc7232 "\"Hypertext Transfer Protocol (HTTP/1.1): Conditional Requests\"")] and
   constructing the payload for 200 (OK) and 304 (Not Modified)
   responses to GET ([Section 4.3.1](https://www.rfc-editor.org/rfc/rfc7231#section-4.3.1)).

[3.1](https://www.rfc-editor.org/rfc/rfc7231#section-3.1). Representation Metadata

   Representation header fields provide metadata about the
   representation.  When a message includes a payload body, the
   representation header fields describe how to interpret the
   representation data enclosed in the payload body.  In a response to a
   HEAD request, the representation header fields describe the
   representation data that would have been enclosed in the payload body
   if the same request had been a GET.

   The following header fields convey representation metadata:

   +-------------------+-----------------+
   | Header Field Name | Defined in...   |
   +-------------------+-----------------+
   | Content-Type      | [Section 3.1.1.5](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.1.5) |
   | Content-Encoding  | [Section 3.1.2.2](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.2.2) |
   | Content-Language  | [Section 3.1.3.2](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.3.2) |
   | Content-Location  | [Section 3.1.4.2](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.4.2) |
   +-------------------+-----------------+

[3.1.1](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.1). Processing Representation Data

[3.1.1.1](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.1.1). Media Type

   HTTP uses Internet media types [[RFC2046](https://www.rfc-editor.org/rfc/rfc2046 "\"Multipurpose Internet Mail Extensions (MIME) Part Two: Media Types\"")] in the Content-Type
   ([Section 3.1.1.5](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.1.5)) and Accept ([Section 5.3.2](https://www.rfc-editor.org/rfc/rfc7231#section-5.3.2)) header fields in order
   to provide open and extensible data typing and type negotiation.
   Media types define both a data format and various processing models:
   how to process that data in accordance with each context in which it
   is received.

     media-type = type "/" subtype *( OWS ";" OWS parameter )
     type       = token
     subtype    = token

   The type/subtype MAY be followed by parameters in the form of
   name=value pairs.

     parameter      = token "=" ( token / quoted-string )

Fielding & Reschke Standards Track [Page 8]

* * *

[RFC 7231](https://www.rfc-editor.org/rfc/rfc7231) HTTP/1.1 Semantics and Content June 2014

   The type, subtype, and parameter name tokens are case-insensitive.
   Parameter values might or might not be case-sensitive, depending on
   the semantics of the parameter name.  The presence or absence of a
   parameter might be significant to the processing of a media-type,
   depending on its definition within the media type registry.

   A parameter value that matches the token production can be
   transmitted either as a token or within a quoted-string.  The quoted
   and unquoted values are equivalent.  For example, the following
   examples are all equivalent, but the first is preferred for
   consistency:

     text/html;charset=utf-8
     text/html;charset=UTF-8
     Text/HTML;Charset="utf-8"
     text/html; charset="utf-8"

   Internet media types ought to be registered with IANA according to
   the procedures defined in [[BCP13](https://www.rfc-editor.org/rfc/rfc7231#ref-BCP13 "\"Media Type Specifications and Registration Procedures\"")].

      Note: Unlike some similar constructs in other header fields, media
      type parameters do not allow whitespace (even "bad" whitespace)
      around the "=" character.

[3.1.1.2](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.1.2). Charset

   HTTP uses charset names to indicate or negotiate the character
   encoding scheme of a textual representation [[RFC6365](https://www.rfc-editor.org/rfc/rfc6365 "\"Terminology Used in Internationalization in the IETF\"")].  A charset is
   identified by a case-insensitive token.

     charset = token

   Charset names ought to be registered in the IANA "Character Sets"
   registry (<[http://www.iana.org/assignments/character-sets](http://www.iana.org/assignments/character-sets)>) according
   to the procedures defined in [[RFC2978](https://www.rfc-editor.org/rfc/rfc2978 "\"IANA Charset Registration Procedures\"")].

[3.1.1.3](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.1.3). Canonicalization and Text Defaults

   Internet media types are registered with a canonical form in order to
   be interoperable among systems with varying native encoding formats.
   Representations selected or transferred via HTTP ought to be in
   canonical form, for many of the same reasons described by the
   Multipurpose Internet Mail Extensions (MIME) [[RFC2045](https://www.rfc-editor.org/rfc/rfc2045 "\"Multipurpose Internet Mail Extensions (MIME) Part One: Format of Internet Message Bodies\"")].  However, the
   performance characteristics of email deployments (i.e., store and
   forward messages to peers) are significantly different from those
   common to HTTP and the Web (server-based information services).
   Furthermore, MIME's constraints for the sake of compatibility with
   older mail transfer protocols do not apply to HTTP (see [Appendix A](https://www.rfc-editor.org/rfc/rfc7231#appendix-A)).

Fielding & Reschke Standards Track [Page 9]

* * *

[RFC 7231](https://www.rfc-editor.org/rfc/rfc7231) HTTP/1.1 Semantics and Content June 2014

   MIME's canonical form requires that media subtypes of the "text" type
   use CRLF as the text line break.  HTTP allows the transfer of text
   media with plain CR or LF alone representing a line break, when such
   line breaks are consistent for an entire representation.  An HTTP
   sender MAY generate, and a recipient MUST be able to parse, line
   breaks in text media that consist of CRLF, bare CR, or bare LF.  In
   addition, text media in HTTP is not limited to charsets that use
   octets 13 and 10 for CR and LF, respectively.  This flexibility
   regarding line breaks applies only to text within a representation
   that has been assigned a "text" media type; it does not apply to
   "multipart" types or HTTP elements outside the payload body (e.g.,
   header fields).

   If a representation is encoded with a content-coding, the underlying
   data ought to be in a form defined above prior to being encoded.

[3.1.1.4](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.1.4). Multipart Types

   MIME provides for a number of "multipart" types -- encapsulations of
   one or more representations within a single message body.  All
   multipart types share a common syntax, as defined in [Section 5.1.1 of [RFC2046]](https://www.rfc-editor.org/rfc/rfc2046#section-5.1.1), and include a boundary parameter as part of the media type
   value.  The message body is itself a protocol element; a sender MUST
   generate only CRLF to represent line breaks between body parts.

   HTTP message framing does not use the multipart boundary as an
   indicator of message body length, though it might be used by
   implementations that generate or process the payload.  For example,
   the "multipart/form-data" type is often used for carrying form data
   in a request, as described in [[RFC2388](https://www.rfc-editor.org/rfc/rfc2388 "\"Returning Values from Forms: multipart/ form-data\"")], and the "multipart/
   byteranges" type is defined by this specification for use in some 206
   (Partial Content) responses [[RFC7233](https://www.rfc-editor.org/rfc/rfc7233 "\"Hypertext Transfer Protocol (HTTP/1.1): Range Requests\"")].

[3.1.1.5](https://www.rfc-editor.org/rfc/rfc7231#section-3.1.1.5). Content-Type

   The "Content-Type" header field indicates the media type of the
   associated representation: either the representation enclosed in the
   message payload or the selected representation, as determined by the
   message semantics.  The indicated media type defines both the data
   format and how that data is intended to be processed by a recipient,
   within the scope of the received message semantics, after any content
   codings indicated by Content-Encoding are decoded.

     Content-Type = media-type

Fielding & Reschke Standards Track [Page 10]

* * *

[RFC 7231](https://www.rfc-editor.org/rfc/rfc7231) HTTP/1.1 Semantics and Content June 2014
