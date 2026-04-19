# RFC 3986: Uniform Resource Identifier (URI): Generic Syntax
[[RFC Home](https://www.rfc-editor.org/ "RFC Editor")] [[TEXT](https://www.rfc-editor.org/rfc/rfc3986.txt)|[PDF](https://www.rfc-editor.org/rfc/pdfrfc/rfc3986.txt.pdf)|[HTML](https://www.rfc-editor.org/rfc/rfc3986.html)] [[Tracker](https://datatracker.ietf.org/doc/rfc3986 "IETF Datatracker information for this document")] [[IPR](https://datatracker.ietf.org/ipr/search/?rfc=3986&submit=rfc "IPR disclosures related to this document")] [[Errata](https://www.rfc-editor.org/errata/rfc3986)] [[Info page](https://www.rfc-editor.org/info/rfc3986 "Info page")] 

 INTERNET STANDARD

Updated by: [7320](https://www.rfc-editor.org/rfc/rfc7320), [8820](https://www.rfc-editor.org/rfc/rfc8820)Errata Exist Network Working Group                                     T. Berners-Lee
Request for Comments: 3986                                       W3C/MIT
STD: 66                                                      R. Fielding
Updates: [1738](https://www.rfc-editor.org/rfc/rfc1738)                                               Day Software
Obsoletes: [2732](https://www.rfc-editor.org/rfc/rfc2732), [2396](https://www.rfc-editor.org/rfc/rfc2396), [1808](https://www.rfc-editor.org/rfc/rfc1808)                                  L. Masinter
Category: Standards Track                                  Adobe Systems
                                                            January 2005

           Uniform Resource Identifier (URI): Generic Syntax

Status of This Memo

   This document specifies an Internet standards track protocol for the
   Internet community, and requests discussion and suggestions for
   improvements.  Please refer to the current edition of the "Internet
   Official Protocol Standards" (STD 1) for the standardization state
   and status of this protocol.  Distribution of this memo is unlimited.

Copyright Notice

   Copyright (C) The Internet Society (2005).

Abstract

   A Uniform Resource Identifier (URI) is a compact sequence of
   characters that identifies an abstract or physical resource.  This
   specification defines the generic URI syntax and a process for
   resolving URI references that might be in relative form, along with
   guidelines and security considerations for the use of URIs on the
   Internet.  The URI syntax defines a grammar that is a superset of all
   valid URIs, allowing an implementation to parse the common components
   of a URI reference without knowing the scheme-specific requirements
   of every possible identifier.  This specification does not define a
   generative grammar for URIs; that task is performed by the individual
   specifications of each URI scheme.

Berners-Lee, et al. Standards Track [Page 1]

* * *

[RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) URI Generic Syntax January 2005

Table of Contents

   [1](https://www.rfc-editor.org/rfc/rfc3986#section-1).  Introduction . . . . . . . . . . . . . . . . . . . . . . . . .  [4](https://www.rfc-editor.org/rfc/rfc3986#page-4)
       [1.1](https://www.rfc-editor.org/rfc/rfc3986#section-1.1).  Overview of URIs . . . . . . . . . . . . . . . . . . . .  [4](https://www.rfc-editor.org/rfc/rfc3986#page-4)
             [1.1.1](https://www.rfc-editor.org/rfc/rfc3986#section-1.1.1).  Generic Syntax . . . . . . . . . . . . . . . . .  [6](https://www.rfc-editor.org/rfc/rfc3986#page-6)
             [1.1.2](https://www.rfc-editor.org/rfc/rfc3986#section-1.1.2).  Examples . . . . . . . . . . . . . . . . . . . .  [7](https://www.rfc-editor.org/rfc/rfc3986#page-7)
             [1.1.3](https://www.rfc-editor.org/rfc/rfc3986#section-1.1.3).  URI, URL, and URN  . . . . . . . . . . . . . . .  [7](https://www.rfc-editor.org/rfc/rfc3986#page-7)
       [1.2](https://www.rfc-editor.org/rfc/rfc3986#section-1.2).  Design Considerations  . . . . . . . . . . . . . . . . .  [8](https://www.rfc-editor.org/rfc/rfc3986#page-8)
             [1.2.1](https://www.rfc-editor.org/rfc/rfc3986#section-1.2.1).  Transcription  . . . . . . . . . . . . . . . . .  [8](https://www.rfc-editor.org/rfc/rfc3986#page-8)
             [1.2.2](https://www.rfc-editor.org/rfc/rfc3986#section-1.2.2).  Separating Identification from Interaction . . .  [9](https://www.rfc-editor.org/rfc/rfc3986#page-9)
             [1.2.3](https://www.rfc-editor.org/rfc/rfc3986#section-1.2.3).  Hierarchical Identifiers . . . . . . . . . . . . [10](https://www.rfc-editor.org/rfc/rfc3986#page-10)
       [1.3](https://www.rfc-editor.org/rfc/rfc3986#section-1.3).  Syntax Notation  . . . . . . . . . . . . . . . . . . . . [11](https://www.rfc-editor.org/rfc/rfc3986#page-11)
   [2](https://www.rfc-editor.org/rfc/rfc3986#section-2).  Characters . . . . . . . . . . . . . . . . . . . . . . . . . . [11](https://www.rfc-editor.org/rfc/rfc3986#page-11)
       [2.1](https://www.rfc-editor.org/rfc/rfc3986#section-2.1).  Percent-Encoding . . . . . . . . . . . . . . . . . . . . [12](https://www.rfc-editor.org/rfc/rfc3986#page-12)
       [2.2](https://www.rfc-editor.org/rfc/rfc3986#section-2.2).  Reserved Characters  . . . . . . . . . . . . . . . . . . [12](https://www.rfc-editor.org/rfc/rfc3986#page-12)
       [2.3](https://www.rfc-editor.org/rfc/rfc3986#section-2.3).  Unreserved Characters  . . . . . . . . . . . . . . . . . [13](https://www.rfc-editor.org/rfc/rfc3986#page-13)
       [2.4](https://www.rfc-editor.org/rfc/rfc3986#section-2.4).  When to Encode or Decode . . . . . . . . . . . . . . . . [14](https://www.rfc-editor.org/rfc/rfc3986#page-14)
       [2.5](https://www.rfc-editor.org/rfc/rfc3986#section-2.5).  Identifying Data . . . . . . . . . . . . . . . . . . . . [14](https://www.rfc-editor.org/rfc/rfc3986#page-14)
   [3](https://www.rfc-editor.org/rfc/rfc3986#section-3).  Syntax Components  . . . . . . . . . . . . . . . . . . . . . . [16](https://www.rfc-editor.org/rfc/rfc3986#page-16)
       [3.1](https://www.rfc-editor.org/rfc/rfc3986#section-3.1).  Scheme . . . . . . . . . . . . . . . . . . . . . . . . . [17](https://www.rfc-editor.org/rfc/rfc3986#page-17)
       [3.2](https://www.rfc-editor.org/rfc/rfc3986#section-3.2).  Authority  . . . . . . . . . . . . . . . . . . . . . . . [17](https://www.rfc-editor.org/rfc/rfc3986#page-17)
             [3.2.1](https://www.rfc-editor.org/rfc/rfc3986#section-3.2.1).  User Information . . . . . . . . . . . . . . . . [18](https://www.rfc-editor.org/rfc/rfc3986#page-18)
             [3.2.2](https://www.rfc-editor.org/rfc/rfc3986#section-3.2.2).  Host . . . . . . . . . . . . . . . . . . . . . . [18](https://www.rfc-editor.org/rfc/rfc3986#page-18)
             [3.2.3](https://www.rfc-editor.org/rfc/rfc3986#section-3.2.3).  Port . . . . . . . . . . . . . . . . . . . . . . [22](https://www.rfc-editor.org/rfc/rfc3986#page-22)
       [3.3](https://www.rfc-editor.org/rfc/rfc3986#section-3.3).  Path . . . . . . . . . . . . . . . . . . . . . . . . . . [22](https://www.rfc-editor.org/rfc/rfc3986#page-22)
       [3.4](https://www.rfc-editor.org/rfc/rfc3986#section-3.4).  Query  . . . . . . . . . . . . . . . . . . . . . . . . . [23](https://www.rfc-editor.org/rfc/rfc3986#page-23)
       [3.5](https://www.rfc-editor.org/rfc/rfc3986#section-3.5).  Fragment . . . . . . . . . . . . . . . . . . . . . . . . [24](https://www.rfc-editor.org/rfc/rfc3986#page-24)
   [4](https://www.rfc-editor.org/rfc/rfc3986#section-4).  Usage  . . . . . . . . . . . . . . . . . . . . . . . . . . . . [25](https://www.rfc-editor.org/rfc/rfc3986#page-25)
       [4.1](https://www.rfc-editor.org/rfc/rfc3986#section-4.1).  URI Reference  . . . . . . . . . . . . . . . . . . . . . [25](https://www.rfc-editor.org/rfc/rfc3986#page-25)
       [4.2](https://www.rfc-editor.org/rfc/rfc3986#section-4.2).  Relative Reference . . . . . . . . . . . . . . . . . . . [26](https://www.rfc-editor.org/rfc/rfc3986#page-26)
       [4.3](https://www.rfc-editor.org/rfc/rfc3986#section-4.3).  Absolute URI . . . . . . . . . . . . . . . . . . . . . . [27](https://www.rfc-editor.org/rfc/rfc3986#page-27)
       [4.4](https://www.rfc-editor.org/rfc/rfc3986#section-4.4).  Same-Document Reference  . . . . . . . . . . . . . . . . [27](https://www.rfc-editor.org/rfc/rfc3986#page-27)
       [4.5](https://www.rfc-editor.org/rfc/rfc3986#section-4.5).  Suffix Reference . . . . . . . . . . . . . . . . . . . . [27](https://www.rfc-editor.org/rfc/rfc3986#page-27)
   [5](https://www.rfc-editor.org/rfc/rfc3986#section-5).  Reference Resolution . . . . . . . . . . . . . . . . . . . . . [28](https://www.rfc-editor.org/rfc/rfc3986#page-28)
       [5.1](https://www.rfc-editor.org/rfc/rfc3986#section-5.1).  Establishing a Base URI  . . . . . . . . . . . . . . . . [28](https://www.rfc-editor.org/rfc/rfc3986#page-28)
             [5.1.1](https://www.rfc-editor.org/rfc/rfc3986#section-5.1.1).  Base URI Embedded in Content . . . . . . . . . . [29](https://www.rfc-editor.org/rfc/rfc3986#page-29)
             [5.1.2](https://www.rfc-editor.org/rfc/rfc3986#section-5.1.2).  Base URI from the Encapsulating Entity . . . . . [29](https://www.rfc-editor.org/rfc/rfc3986#page-29)
             [5.1.3](https://www.rfc-editor.org/rfc/rfc3986#section-5.1.3).  Base URI from the Retrieval URI  . . . . . . . . [30](https://www.rfc-editor.org/rfc/rfc3986#page-30)
             [5.1.4](https://www.rfc-editor.org/rfc/rfc3986#section-5.1.4).  Default Base URI . . . . . . . . . . . . . . . . [30](https://www.rfc-editor.org/rfc/rfc3986#page-30)
       [5.2](https://www.rfc-editor.org/rfc/rfc3986#section-5.2).  Relative Resolution  . . . . . . . . . . . . . . . . . . [30](https://www.rfc-editor.org/rfc/rfc3986#page-30)
             [5.2.1](https://www.rfc-editor.org/rfc/rfc3986#section-5.2.1).  Pre-parse the Base URI . . . . . . . . . . . . . [31](https://www.rfc-editor.org/rfc/rfc3986#page-31)
             [5.2.2](https://www.rfc-editor.org/rfc/rfc3986#section-5.2.2).  Transform References . . . . . . . . . . . . . . [31](https://www.rfc-editor.org/rfc/rfc3986#page-31)
             [5.2.3](https://www.rfc-editor.org/rfc/rfc3986#section-5.2.3).  Merge Paths  . . . . . . . . . . . . . . . . . . [32](https://www.rfc-editor.org/rfc/rfc3986#page-32)
             [5.2.4](https://www.rfc-editor.org/rfc/rfc3986#section-5.2.4).  Remove Dot Segments  . . . . . . . . . . . . . . [33](https://www.rfc-editor.org/rfc/rfc3986#page-33)
       [5.3](https://www.rfc-editor.org/rfc/rfc3986#section-5.3).  Component Recomposition  . . . . . . . . . . . . . . . . [35](https://www.rfc-editor.org/rfc/rfc3986#page-35)
       [5.4](https://www.rfc-editor.org/rfc/rfc3986#section-5.4).  Reference Resolution Examples  . . . . . . . . . . . . . [35](https://www.rfc-editor.org/rfc/rfc3986#page-35)
             [5.4.1](https://www.rfc-editor.org/rfc/rfc3986#section-5.4.1).  Normal Examples  . . . . . . . . . . . . . . . . [36](https://www.rfc-editor.org/rfc/rfc3986#page-36)
             [5.4.2](https://www.rfc-editor.org/rfc/rfc3986#section-5.4.2).  Abnormal Examples  . . . . . . . . . . . . . . . [36](https://www.rfc-editor.org/rfc/rfc3986#page-36)

Berners-Lee, et al. Standards Track [Page 2]

* * *

[RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) URI Generic Syntax January 2005

   [6](https://www.rfc-editor.org/rfc/rfc3986#section-6).  Normalization and Comparison . . . . . . . . . . . . . . . . . [38](https://www.rfc-editor.org/rfc/rfc3986#page-38)
       [6.1](https://www.rfc-editor.org/rfc/rfc3986#section-6.1).  Equivalence  . . . . . . . . . . . . . . . . . . . . . . [38](https://www.rfc-editor.org/rfc/rfc3986#page-38)
       [6.2](https://www.rfc-editor.org/rfc/rfc3986#section-6.2).  Comparison Ladder  . . . . . . . . . . . . . . . . . . . [39](https://www.rfc-editor.org/rfc/rfc3986#page-39)
             [6.2.1](https://www.rfc-editor.org/rfc/rfc3986#section-6.2.1).  Simple String Comparison . . . . . . . . . . . . [39](https://www.rfc-editor.org/rfc/rfc3986#page-39)
             [6.2.2](https://www.rfc-editor.org/rfc/rfc3986#section-6.2.2).  Syntax-Based Normalization . . . . . . . . . . . [40](https://www.rfc-editor.org/rfc/rfc3986#page-40)
             [6.2.3](https://www.rfc-editor.org/rfc/rfc3986#section-6.2.3).  Scheme-Based Normalization . . . . . . . . . . . [41](https://www.rfc-editor.org/rfc/rfc3986#page-41)
             [6.2.4](https://www.rfc-editor.org/rfc/rfc3986#section-6.2.4).  Protocol-Based Normalization . . . . . . . . . . [42](https://www.rfc-editor.org/rfc/rfc3986#page-42)
   [7](https://www.rfc-editor.org/rfc/rfc3986#section-7).  Security Considerations  . . . . . . . . . . . . . . . . . . . [43](https://www.rfc-editor.org/rfc/rfc3986#page-43)
       [7.1](https://www.rfc-editor.org/rfc/rfc3986#section-7.1).  Reliability and Consistency  . . . . . . . . . . . . . . [43](https://www.rfc-editor.org/rfc/rfc3986#page-43)
       [7.2](https://www.rfc-editor.org/rfc/rfc3986#section-7.2).  Malicious Construction . . . . . . . . . . . . . . . . . [43](https://www.rfc-editor.org/rfc/rfc3986#page-43)
       [7.3](https://www.rfc-editor.org/rfc/rfc3986#section-7.3).  Back-End Transcoding . . . . . . . . . . . . . . . . . . [44](https://www.rfc-editor.org/rfc/rfc3986#page-44)
       [7.4](https://www.rfc-editor.org/rfc/rfc3986#section-7.4).  Rare IP Address Formats  . . . . . . . . . . . . . . . . [45](https://www.rfc-editor.org/rfc/rfc3986#page-45)
       [7.5](https://www.rfc-editor.org/rfc/rfc3986#section-7.5).  Sensitive Information  . . . . . . . . . . . . . . . . . [45](https://www.rfc-editor.org/rfc/rfc3986#page-45)
       [7.6](https://www.rfc-editor.org/rfc/rfc3986#section-7.6).  Semantic Attacks . . . . . . . . . . . . . . . . . . . . [45](https://www.rfc-editor.org/rfc/rfc3986#page-45)
   [8](https://www.rfc-editor.org/rfc/rfc3986#section-8).  IANA Considerations  . . . . . . . . . . . . . . . . . . . . . [46](https://www.rfc-editor.org/rfc/rfc3986#page-46)
   [9](https://www.rfc-editor.org/rfc/rfc3986#section-9).  Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . [46](https://www.rfc-editor.org/rfc/rfc3986#page-46)
   [10](https://www.rfc-editor.org/rfc/rfc3986#section-10). References . . . . . . . . . . . . . . . . . . . . . . . . . . [46](https://www.rfc-editor.org/rfc/rfc3986#page-46)
       [10.1](https://www.rfc-editor.org/rfc/rfc3986#section-10.1). Normative References . . . . . . . . . . . . . . . . . . [46](https://www.rfc-editor.org/rfc/rfc3986#page-46)
       [10.2](https://www.rfc-editor.org/rfc/rfc3986#section-10.2). Informative References . . . . . . . . . . . . . . . . . [47](https://www.rfc-editor.org/rfc/rfc3986#page-47)
   [A](https://www.rfc-editor.org/rfc/rfc3986#appendix-A).  Collected ABNF for URI . . . . . . . . . . . . . . . . . . . . [49](https://www.rfc-editor.org/rfc/rfc3986#page-49)
   [B](https://www.rfc-editor.org/rfc/rfc3986#appendix-B).  Parsing a URI Reference with a Regular Expression  . . . . . . [50](https://www.rfc-editor.org/rfc/rfc3986#page-50)
   [C](https://www.rfc-editor.org/rfc/rfc3986#appendix-C).  Delimiting a URI in Context  . . . . . . . . . . . . . . . . . [51](https://www.rfc-editor.org/rfc/rfc3986#page-51)
   [D](https://www.rfc-editor.org/rfc/rfc3986#appendix-D).  Changes from [RFC 2396](https://www.rfc-editor.org/rfc/rfc2396)  . . . . . . . . . . . . . . . . . . . . [53](https://www.rfc-editor.org/rfc/rfc3986#page-53)
       [D.1](https://www.rfc-editor.org/rfc/rfc3986#appendix-D.1).  Additions  . . . . . . . . . . . . . . . . . . . . . . . [53](https://www.rfc-editor.org/rfc/rfc3986#page-53)
       [D.2](https://www.rfc-editor.org/rfc/rfc3986#appendix-D.2).  Modifications  . . . . . . . . . . . . . . . . . . . . . [53](https://www.rfc-editor.org/rfc/rfc3986#page-53)
   Index  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . [56](https://www.rfc-editor.org/rfc/rfc3986#page-56)
   Authors' Addresses . . . . . . . . . . . . . . . . . . . . . . . . [60](https://www.rfc-editor.org/rfc/rfc3986#page-60)
   Full Copyright Statement . . . . . . . . . . . . . . . . . . . . . [61](https://www.rfc-editor.org/rfc/rfc3986#page-61)

Berners-Lee, et al. Standards Track [Page 3]

* * *

[RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) URI Generic Syntax January 2005

[1](https://www.rfc-editor.org/rfc/rfc3986#section-1). Introduction

   A Uniform Resource Identifier (URI) provides a simple and extensible
   means for identifying a resource.  This specification of URI syntax
   and semantics is derived from concepts introduced by the World Wide
   Web global information initiative, whose use of these identifiers
   dates from 1990 and is described in "Universal Resource Identifiers
   in WWW" [[RFC1630](https://www.rfc-editor.org/rfc/rfc1630 "\"Universal Resource Identifiers in WWW: A Unifying Syntax for the Expression of Names and Addresses of Objects on the Network as used in the World-Wide Web\"")].  The syntax is designed to meet the
   recommendations laid out in "Functional Recommendations for Internet
   Resource Locators" [[RFC1736](https://www.rfc-editor.org/rfc/rfc1736 "\"Functional Recommendations for Internet Resource Locators\"")] and "Functional Requirements for Uniform
   Resource Names" [[RFC1737](https://www.rfc-editor.org/rfc/rfc1737 "\"Functional Requirements for Uniform Resource Names\"")].

   This document obsoletes [[RFC2396](https://www.rfc-editor.org/rfc/rfc2396 "\"Uniform Resource Identifiers (URI): Generic Syntax\"")], which merged "Uniform Resource
   Locators" [[RFC1738](https://www.rfc-editor.org/rfc/rfc1738 "\"Uniform Resource Locators (URL)\"")] and "Relative Uniform Resource Locators"
   [[RFC1808](https://www.rfc-editor.org/rfc/rfc1808 "\"Relative Uniform Resource Locators\"")] in order to define a single, generic syntax for all URIs.
   It obsoletes [[RFC2732](https://www.rfc-editor.org/rfc/rfc2732 "\"Format for Literal IPv6 Addresses in URL's\"")], which introduced syntax for an IPv6 address.
   It excludes portions of [RFC 1738](https://www.rfc-editor.org/rfc/rfc1738) that defined the specific syntax of
   individual URI schemes; those portions will be updated as separate
   documents.  The process for registration of new URI schemes is
   defined separately by [[BCP35](https://www.rfc-editor.org/rfc/rfc3986#ref-BCP35 "\"Registration Procedures for URL Scheme Names\"")].  Advice for designers of new URI
   schemes can be found in [[RFC2718](https://www.rfc-editor.org/rfc/rfc2718 "\"Guidelines for new URL Schemes\"")].  All significant changes from [RFC](https://www.rfc-editor.org/rfc/rfc2396)
   [2396](https://www.rfc-editor.org/rfc/rfc2396) are noted in [Appendix D](https://www.rfc-editor.org/rfc/rfc3986#appendix-D).

   This specification uses the terms "character" and "coded character
   set" in accordance with the definitions provided in [[BCP19](https://www.rfc-editor.org/rfc/rfc3986#ref-BCP19 "\"IANA Charset Registration Procedures\"")], and
   "character encoding" in place of what [[BCP19](https://www.rfc-editor.org/rfc/rfc3986#ref-BCP19 "\"IANA Charset Registration Procedures\"")] refers to as a
   "charset".

[1.1](https://www.rfc-editor.org/rfc/rfc3986#section-1.1). Overview of URIs

   URIs are characterized as follows:

   Uniform

      Uniformity provides several benefits.  It allows different types
      of resource identifiers to be used in the same context, even when
      the mechanisms used to access those resources may differ.  It
      allows uniform semantic interpretation of common syntactic
      conventions across different types of resource identifiers.  It
      allows introduction of new types of resource identifiers without
      interfering with the way that existing identifiers are used.  It
      allows the identifiers to be reused in many different contexts,
      thus permitting new applications or protocols to leverage a pre-
      existing, large, and widely used set of resource identifiers.

Berners-Lee, et al. Standards Track [Page 4]

* * *

[RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) URI Generic Syntax January 2005

   Resource

      This specification does not limit the scope of what might be a
      resource; rather, the term "resource" is used in a general sense
      for whatever might be identified by a URI.  Familiar examples
      include an electronic document, an image, a source of information
      with a consistent purpose (e.g., "today's weather report for Los
      Angeles"), a service (e.g., an HTTP-to-SMS gateway), and a
      collection of other resources.  A resource is not necessarily
      accessible via the Internet; e.g., human beings, corporations, and
      bound books in a library can also be resources.  Likewise,
      abstract concepts can be resources, such as the operators and
      operands of a mathematical equation, the types of a relationship
      (e.g., "parent" or "employee"), or numeric values (e.g., zero,
      one, and infinity).

   Identifier

      An identifier embodies the information required to distinguish
      what is being identified from all other things within its scope of
      identification.  Our use of the terms "identify" and "identifying"
      refer to this purpose of distinguishing one resource from all
      other resources, regardless of how that purpose is accomplished
      (e.g., by name, address, or context).  These terms should not be
      mistaken as an assumption that an identifier defines or embodies
      the identity of what is referenced, though that may be the case
      for some identifiers.  Nor should it be assumed that a system
      using URIs will access the resource identified: in many cases,
      URIs are used to denote resources without any intention that they
      be accessed.  Likewise, the "one" resource identified might not be
      singular in nature (e.g., a resource might be a named set or a
      mapping that varies over time).

   A URI is an identifier consisting of a sequence of characters
   matching the syntax rule named <URI> in [Section 3](https://www.rfc-editor.org/rfc/rfc3986#section-3).  It enables
   uniform identification of resources via a separately defined
   extensible set of naming schemes ([Section 3.1](https://www.rfc-editor.org/rfc/rfc3986#section-3.1)).  How that
   identification is accomplished, assigned, or enabled is delegated to
   each scheme specification.

   This specification does not place any limits on the nature of a
   resource, the reasons why an application might seek to refer to a
   resource, or the kinds of systems that might use URIs for the sake of
   identifying resources.  This specification does not require that a
   URI persists in identifying the same resource over time, though that
   is a common goal of all URI schemes.  Nevertheless, nothing in this

Berners-Lee, et al. Standards Track [Page 5]

* * *

[RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) URI Generic Syntax January 2005

   specification prevents an application from limiting itself to
   particular types of resources, or to a subset of URIs that maintains
   characteristics desired by that application.

   URIs have a global scope and are interpreted consistently regardless
   of context, though the result of that interpretation may be in
   relation to the end-user's context.  For example, "[http://localhost/](http://localhost/)"
   has the same interpretation for every user of that reference, even
   though the network interface corresponding to "localhost" may be
   different for each end-user: interpretation is independent of access.
   However, an action made on the basis of that reference will take
   place in relation to the end-user's context, which implies that an
   action intended to refer to a globally unique thing must use a URI
   that distinguishes that resource from all other things.  URIs that
   identify in relation to the end-user's local context should only be
   used when the context itself is a defining aspect of the resource,
   such as when an on-line help manual refers to a file on the end-
   user's file system (e.g., "file:///etc/hosts").

[1.1.1](https://www.rfc-editor.org/rfc/rfc3986#section-1.1.1). Generic Syntax

   Each URI begins with a scheme name, as defined in [Section 3.1](https://www.rfc-editor.org/rfc/rfc3986#section-3.1), that
   refers to a specification for assigning identifiers within that
   scheme.  As such, the URI syntax is a federated and extensible naming
   system wherein each scheme's specification may further restrict the
   syntax and semantics of identifiers using that scheme.

   This specification defines those elements of the URI syntax that are
   required of all URI schemes or are common to many URI schemes.  It
   thus defines the syntax and semantics needed to implement a scheme-
   independent parsing mechanism for URI references, by which the
   scheme-dependent handling of a URI can be postponed until the
   scheme-dependent semantics are needed.  Likewise, protocols and data
   formats that make use of URI references can refer to this
   specification as a definition for the range of syntax allowed for all
   URIs, including those schemes that have yet to be defined.  This
   decouples the evolution of identification schemes from the evolution
   of protocols, data formats, and implementations that make use of
   URIs.

   A parser of the generic URI syntax can parse any URI reference into
   its major components.  Once the scheme is determined, further
   scheme-specific parsing can be performed on the components.  In other
   words, the URI generic syntax is a superset of the syntax of all URI
   schemes.

Berners-Lee, et al. Standards Track [Page 6]

* * *

[RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) URI Generic Syntax January 2005

[1.1.2](https://www.rfc-editor.org/rfc/rfc3986#section-1.1.2). Examples

   The following example URIs illustrate several URI schemes and
   variations in their common syntax components:

      [ftp://ftp.is.co.za/rfc/rfc1808.txt](ftp://ftp.is.co.za/rfc/rfc1808.txt)

      [http://www.ietf.org/rfc/rfc2396.txt](http://www.ietf.org/rfc/rfc2396.txt)

      ldap://[2001:db8::7]/c=GB?objectClass?one

      mailto:John.Doe@example.com

      news:comp.infosystems.www.servers.unix

      tel:+1-816-555-1212

      telnet://192.0.2.16:80/

      urn:oasis:names:specification:docbook:dtd:xml:4.1.2

[1.1.3](https://www.rfc-editor.org/rfc/rfc3986#section-1.1.3). URI, URL, and URN

   A URI can be further classified as a locator, a name, or both.  The
   term "Uniform Resource Locator" (URL) refers to the subset of URIs
   that, in addition to identifying a resource, provide a means of
   locating the resource by describing its primary access mechanism
   (e.g., its network "location").  The term "Uniform Resource Name"
   (URN) has been used historically to refer to both URIs under the
   "urn" scheme [[RFC2141](https://www.rfc-editor.org/rfc/rfc2141 "\"URN Syntax\"")], which are required to remain globally unique
   and persistent even when the resource ceases to exist or becomes
   unavailable, and to any other URI with the properties of a name.

   An individual scheme does not have to be classified as being just one
   of "name" or "locator".  Instances of URIs from any given scheme may
   have the characteristics of names or locators or both, often
   depending on the persistence and care in the assignment of
   identifiers by the naming authority, rather than on any quality of
   the scheme.  Future specifications and related documentation should
   use the general term "URI" rather than the more restrictive terms
   "URL" and "URN" [[RFC3305](https://www.rfc-editor.org/rfc/rfc3305 "\"Report from the Joint W3C/IETF URI Planning Interest Group: Uniform Resource Identifiers (URIs), URLs, and Uniform Resource Names (URNs): Clarifications and Recommendations\"")].

Berners-Lee, et al. Standards Track [Page 7]

* * *

[RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) URI Generic Syntax January 2005

[1.2](https://www.rfc-editor.org/rfc/rfc3986#section-1.2). Design Considerations

[1.2.1](https://www.rfc-editor.org/rfc/rfc3986#section-1.2.1). Transcription

   The URI syntax has been designed with global transcription as one of
   its main considerations.  A URI is a sequence of characters from a
   very limited set: the letters of the basic Latin alphabet, digits,
   and a few special characters.  A URI may be represented in a variety
   of ways; e.g., ink on paper, pixels on a screen, or a sequence of
   character encoding octets.  The interpretation of a URI depends only
   on the characters used and not on how those characters are
   represented in a network protocol.

   The goal of transcription can be described by a simple scenario.
   Imagine two colleagues, Sam and Kim, sitting in a pub at an
   international conference and exchanging research ideas.  Sam asks Kim
   for a location to get more information, so Kim writes the URI for the
   research site on a napkin.  Upon returning home, Sam takes out the
   napkin and types the URI into a computer, which then retrieves the
   information to which Kim referred.

   There are several design considerations revealed by the scenario:

   o  A URI is a sequence of characters that is not always represented
      as a sequence of octets.

   o  A URI might be transcribed from a non-network source and thus
      should consist of characters that are most likely able to be
      entered into a computer, within the constraints imposed by
      keyboards (and related input devices) across languages and
      locales.

   o  A URI often has to be remembered by people, and it is easier for
      people to remember a URI when it consists of meaningful or
      familiar components.

   These design considerations are not always in alignment.  For
   example, it is often the case that the most meaningful name for a URI
   component would require characters that cannot be typed into some
   systems.  The ability to transcribe a resource identifier from one
   medium to another has been considered more important than having a
   URI consist of the most meaningful of components.

   In local or regional contexts and with improving technology, users
   might benefit from being able to use a wider range of characters;
   such use is not defined by this specification.  Percent-encoded
   octets ([Section 2.1](https://www.rfc-editor.org/rfc/rfc3986#section-2.1)) may be used within a URI to represent characters
   outside the range of the US-ASCII coded character set if this

Berners-Lee, et al. Standards Track [Page 8]

* * *

[RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) URI Generic Syntax January 2005

   representation is allowed by the scheme or by the protocol element in
   which the URI is referenced.  Such a definition should specify the
   character encoding used to map those characters to octets prior to
   being percent-encoded for the URI.

[1.2.2](https://www.rfc-editor.org/rfc/rfc3986#section-1.2.2). Separating Identification from Interaction

   A common misunderstanding of URIs is that they are only used to refer
   to accessible resources.  The URI itself only provides
   identification; access to the resource is neither guaranteed nor
   implied by the presence of a URI.  Instead, any operation associated
   with a URI reference is defined by the protocol element, data format
   attribute, or natural language text in which it appears.

   Given a URI, a system may attempt to perform a variety of operations
   on the resource, as might be characterized by words such as "access",
   "update", "replace", or "find attributes".  Such operations are
   defined by the protocols that make use of URIs, not by this
   specification.  However, we do use a few general terms for describing
   common operations on URIs.  URI "resolution" is the process of
   determining an access mechanism and the appropriate parameters
   necessary to dereference a URI; this resolution may require several
   iterations.  To use that access mechanism to perform an action on the
   URI's resource is to "dereference" the URI.

   When URIs are used within information retrieval systems to identify
   sources of information, the most common form of URI dereference is
   "retrieval": making use of a URI in order to retrieve a
   representation of its associated resource.  A "representation" is a
   sequence of octets, along with representation metadata describing
   those octets, that constitutes a record of the state of the resource
   at the time when the representation is generated.  Retrieval is
   achieved by a process that might include using the URI as a cache key
   to check for a locally cached representation, resolution of the URI
   to determine an appropriate access mechanism (if any), and
   dereference of the URI for the sake of applying a retrieval
   operation.  Depending on the protocols used to perform the retrieval,
   additional information might be supplied about the resource (resource
   metadata) and its relation to other resources.

   URI references in information retrieval systems are designed to be
   late-binding: the result of an access is generally determined when it
   is accessed and may vary over time or due to other aspects of the
   interaction.  These references are created in order to be used in the
   future: what is being identified is not some specific result that was
   obtained in the past, but rather some characteristic that is expected
   to be true for future results.  In such cases, the resource referred
   to by the URI is actually a sameness of characteristics as observed

Berners-Lee, et al. Standards Track [Page 9]

* * *

[RFC 3986](https://www.rfc-editor.org/rfc/rfc3986) URI Generic Syntax January 2005

   over time, perhaps elucidated by additional comments or assertions
   made by the resource provider.

   Although many URI schemes are named after protocols, this does not
   imply that use of these URIs will result in access to the resource
   via the named protocol.  URIs are often used simply for the sake of
   identification.  Even when a URI is used to retrieve a representation
   of a resource, that access might be through gateways, proxies,
   caches, and name resolution services that are independent of the
   protocol associated with the scheme name.  The resolution of some
   URIs may require the use of more than one protocol (e.g., both DNS
   and HTTP are typically used to access an "http" URI's origin server
   when a representation isn't found in a local cache).

[1.2.3](https://www.rfc-editor.org/rfc/rfc3986#section-1.2.3). Hierarchical Identifiers

   The URI syntax is organized hierarchically, with components listed in
   order of decreasing significance from left to right.  For some URI
   schemes, the visible hierarchy is limited to the scheme itself:
   everything after the scheme component delimiter (":") is considered
   opaque to URI processing.  Other URI schemes make the hierarchy
   explicit and visible to generic parsing algorithms.

   The generic syntax uses the slash ("/"), question mark ("?"), and
   number sign ("#") characters to delimit components that are
   significant to the generic parser's hierarchical interpretation of an
   identifier.  In addition to aiding the readability of such
   identifiers through the consistent use of familiar syntax, this
   uniform representation of hierarchy across naming schemes allows
   scheme-independent references to be made relative to that hierarchy.

   It is often the case that a group or "tree" of documents has been
   constructed to serve a common purpose, wherein the vast majority of
   URI references in these documents point to resources within the tree
   rather than outside it.  Similarly, documents located at a particular
   site are much more likely to refer to other resources at that site
   than to resources at remote sites.  Relative referencing of URIs
   allows document trees to be partially independent of their location
   and access scheme.  For instance, it is possible for a single set of
   hypertext documents to be simultaneously accessible and traversable
   via each of the "file", "http", and "ftp" schemes if the documents
   refer to each other with relative references.  Furthermore, such
   document trees can be moved, as a whole, without changing any of the
   relative references.

   A relative reference ([Section 4.2](https://www.rfc-editor.org/rfc/rfc3986#section-4.2)) refers to a resource by describing
   the difference within a hierarchical name space between the reference
   context and the target URI.  The reference resolution algorithm,

