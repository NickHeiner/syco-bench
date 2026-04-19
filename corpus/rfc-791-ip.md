# RFC 791: Internet Protocol
[[RFC Home](https://www.rfc-editor.org/ "RFC Editor")] [[TEXT](https://www.rfc-editor.org/rfc/rfc791.txt)|[PDF](https://www.rfc-editor.org/rfc/pdfrfc/rfc791.txt.pdf)|[HTML](https://www.rfc-editor.org/rfc/rfc791.html)] [[Tracker](https://datatracker.ietf.org/doc/rfc791 "IETF Datatracker information for this document")] [[IPR](https://datatracker.ietf.org/ipr/search/?rfc=791&submit=rfc "IPR disclosures related to this document")] [[Errata](https://www.rfc-editor.org/errata/rfc0791)] [[Info page](https://www.rfc-editor.org/info/rfc791 "Info page")] 

 INTERNET STANDARD

Updated by: [1349](https://www.rfc-editor.org/rfc/rfc1349), [2474](https://www.rfc-editor.org/rfc/rfc2474), [6864](https://www.rfc-editor.org/rfc/rfc6864)Errata Exist RFC:  791

                           INTERNET PROTOCOL

                         DARPA INTERNET PROGRAM

                         PROTOCOL SPECIFICATION

                             September 1981

                              prepared for

               Defense Advanced Research Projects Agency
                Information Processing Techniques Office
                         1400 Wilson Boulevard
                       Arlington, Virginia  22209

                                   by

                     Information Sciences Institute
                   University of Southern California
                           4676 Admiralty Way
                   Marina del Rey, California  90291

* * *

* * *

September 1981
                                                       Internet Protocol

                           TABLE OF CONTENTS

    PREFACE ........................................................ [iii](https://www.rfc-editor.org/rfc/rfc791#page-iii)

[1](https://www.rfc-editor.org/rfc/rfc791#section-1).  INTRODUCTION ..................................................... [1](https://www.rfc-editor.org/rfc/rfc791#page-1)

  [1.1](https://www.rfc-editor.org/rfc/rfc791#section-1.1)  Motivation .................................................... [1](https://www.rfc-editor.org/rfc/rfc791#page-1)
  [1.2](https://www.rfc-editor.org/rfc/rfc791#section-1.2)  Scope ......................................................... [1](https://www.rfc-editor.org/rfc/rfc791#page-1)
  [1.3](https://www.rfc-editor.org/rfc/rfc791#section-1.3)  Interfaces .................................................... [1](https://www.rfc-editor.org/rfc/rfc791#page-1)
  [1.4](https://www.rfc-editor.org/rfc/rfc791#section-1.4)  Operation ..................................................... [2](https://www.rfc-editor.org/rfc/rfc791#page-2)

[2](https://www.rfc-editor.org/rfc/rfc791#section-2).  OVERVIEW ......................................................... [5](https://www.rfc-editor.org/rfc/rfc791#page-5)

  [2.1](https://www.rfc-editor.org/rfc/rfc791#section-2.1)  Relation to Other Protocols ................................... [9](https://www.rfc-editor.org/rfc/rfc791#page-9)
  [2.2](https://www.rfc-editor.org/rfc/rfc791#section-2.2)  Model of Operation ............................................ [5](https://www.rfc-editor.org/rfc/rfc791#page-5)
  [2.3](https://www.rfc-editor.org/rfc/rfc791#section-2.3)  Function Description .......................................... [7](https://www.rfc-editor.org/rfc/rfc791#page-7)
  [2.4](https://www.rfc-editor.org/rfc/rfc791#section-2.4)  Gateways ...................................................... [9](https://www.rfc-editor.org/rfc/rfc791#page-9)

[3](https://www.rfc-editor.org/rfc/rfc791#section-3).  SPECIFICATION ................................................... [11](https://www.rfc-editor.org/rfc/rfc791#page-11)

  [3.1](https://www.rfc-editor.org/rfc/rfc791#section-3.1)  Internet Header Format ....................................... [11](https://www.rfc-editor.org/rfc/rfc791#page-11)
  [3.2](https://www.rfc-editor.org/rfc/rfc791#section-3.2)  Discussion ................................................... [23](https://www.rfc-editor.org/rfc/rfc791#page-23)
  [3.3](https://www.rfc-editor.org/rfc/rfc791#section-3.3)  Interfaces ................................................... [31](https://www.rfc-editor.org/rfc/rfc791#page-31)

APPENDIX A:  Examples & Scenarios ................................... [34](https://www.rfc-editor.org/rfc/rfc791#page-34)
APPENDIX B:  Data Transmission Order ................................ [39](https://www.rfc-editor.org/rfc/rfc791#page-39)

GLOSSARY ............................................................ [41](https://www.rfc-editor.org/rfc/rfc791#page-41)

REFERENCES .......................................................... [45](https://www.rfc-editor.org/rfc/rfc791#page-45)

 [Page i]

* * *

 September 1981
Internet Protocol

[Page ii]

* * *

September 1981
                                                       Internet Protocol

                                PREFACE

This document specifies the DoD Standard Internet Protocol.  This
document is based on six earlier editions of the ARPA Internet Protocol
Specification, and the present text draws heavily from them.  There have
been many contributors to this work both in terms of concepts and in
terms of text.  This edition revises aspects of addressing, error
handling, option codes, and the security, precedence, compartments, and
handling restriction features of the internet protocol.

                                                           Jon Postel

                                                           Editor

 [Page iii]

* * *

 September 1981

RFC:  791
Replaces:  [RFC 760](https://www.rfc-editor.org/rfc/rfc760)
IENs 128, 123, 111,
80, 54, 44, 41, 28, 26

                           INTERNET PROTOCOL

                         DARPA INTERNET PROGRAM
                         PROTOCOL SPECIFICATION

                            1.  INTRODUCTION

[1.1](https://www.rfc-editor.org/rfc/rfc791#section-1.1). Motivation

  The Internet Protocol is designed for use in interconnected systems of
  packet-switched computer communication networks.  Such a system has
  been called a "catenet" [[1](https://www.rfc-editor.org/rfc/rfc791#ref-1 "\"The Catenet Model for Internetworking,\"")].  The internet protocol provides for
  transmitting blocks of data called datagrams from sources to
  destinations, where sources and destinations are hosts identified by
  fixed length addresses.  The internet protocol also provides for
  fragmentation and reassembly of long datagrams, if necessary, for
  transmission through "small packet" networks.

[1.2](https://www.rfc-editor.org/rfc/rfc791#section-1.2). Scope

  The internet protocol is specifically limited in scope to provide the
  functions necessary to deliver a package of bits (an internet
  datagram) from a source to a destination over an interconnected system
  of networks.  There are no mechanisms to augment end-to-end data
  reliability, flow control, sequencing, or other services commonly
  found in host-to-host protocols.  The internet protocol can capitalize
  on the services of its supporting networks to provide various types
  and qualities of service.

[1.3](https://www.rfc-editor.org/rfc/rfc791#section-1.3). Interfaces

  This protocol is called on by host-to-host protocols in an internet
  environment.  This protocol calls on local network protocols to carry
  the internet datagram to the next gateway or destination host.

  For example, a TCP module would call on the internet module to take a
  TCP segment (including the TCP header and user data) as the data
  portion of an internet datagram.  The TCP module would provide the
  addresses and other parameters in the internet header to the internet
  module as arguments of the call.  The internet module would then
  create an internet datagram and call on the local network interface to
  transmit the internet datagram.

  In the ARPANET case, for example, the internet module would call on a

 [Page 1]

* * *

 September 1981
Internet Protocol
Introduction

  local net module which would add the 1822 leader [[2](https://www.rfc-editor.org/rfc/rfc791#ref-2 "\"Specification for the Interconnection of a Host and an IMP,\"")] to the internet
  datagram creating an ARPANET message to transmit to the IMP.  The
  ARPANET address would be derived from the internet address by the
  local network interface and would be the address of some host in the
  ARPANET, that host might be a gateway to other networks.

[1.4](https://www.rfc-editor.org/rfc/rfc791#section-1.4). Operation

  The internet protocol implements two basic functions:  addressing and
  fragmentation.

  The internet modules use the addresses carried in the internet header
  to transmit internet datagrams toward their destinations.  The
  selection of a path for transmission is called routing.

  The internet modules use fields in the internet header to fragment and
  reassemble internet datagrams when necessary for transmission through
  "small packet" networks.

  The model of operation is that an internet module resides in each host
  engaged in internet communication and in each gateway that
  interconnects networks.  These modules share common rules for
  interpreting address fields and for fragmenting and assembling
  internet datagrams.  In addition, these modules (especially in
  gateways) have procedures for making routing decisions and other
  functions.

  The internet protocol treats each internet datagram as an independent
  entity unrelated to any other internet datagram.  There are no
  connections or logical circuits (virtual or otherwise).

  The internet protocol uses four key mechanisms in providing its
  service:  Type of Service, Time to Live, Options, and Header Checksum.

  The Type of Service is used to indicate the quality of the service
  desired.  The type of service is an abstract or generalized set of
  parameters which characterize the service choices provided in the
  networks that make up the internet.  This type of service indication
  is to be used by gateways to select the actual transmission parameters
  for a particular network, the network to be used for the next hop, or
  the next gateway when routing an internet datagram.

  The Time to Live is an indication of an upper bound on the lifetime of
  an internet datagram.  It is set by the sender of the datagram and
  reduced at the points along the route where it is processed.  If the
  time to live reaches zero before the internet datagram reaches its
  destination, the internet datagram is destroyed.  The time to live can
  be thought of as a self destruct time limit.

[Page 2]

* * *

September 1981
                                                       Internet Protocol
                                                            Introduction

  The Options provide for control functions needed or useful in some
  situations but unnecessary for the most common communications.  The
  options include provisions for timestamps, security, and special
  routing.

  The Header Checksum provides a verification that the information used
  in processing internet datagram has been transmitted correctly.  The
  data may contain errors.  If the header checksum fails, the internet
  datagram is discarded at once by the entity which detects the error.

  The internet protocol does not provide a reliable communication
  facility.  There are no acknowledgments either end-to-end or
  hop-by-hop.  There is no error control for data, only a header
  checksum.  There are no retransmissions.  There is no flow control.

  Errors detected may be reported via the Internet Control Message
  Protocol (ICMP) [[3](https://www.rfc-editor.org/rfc/rfc791#ref-3 "\"Internet Control Message Protocol - DARPA Internet Program Protocol Specification,\"")] which is implemented in the internet protocol
  module.

 [Page 3]

* * *

 September 1981
Internet Protocol

[Page 4]

* * *

September 1981
                                                       Internet Protocol

                              2.  OVERVIEW

[2.1](https://www.rfc-editor.org/rfc/rfc791#section-2.1). Relation to Other Protocols

  The following diagram illustrates the place of the internet protocol
  in the protocol hierarchy:

                 +------+ +-----+ +-----+     +-----+
                 |Telnet| | FTP | | TFTP| ... | ... |
                 +------+ +-----+ +-----+     +-----+
                       |   |         |           |
                      +-----+     +-----+     +-----+
                      | TCP |     | UDP | ... | ... |
                      +-----+     +-----+     +-----+
                         |           |           |
                      +--------------------------+----+
                      |    Internet Protocol & ICMP   |
                      +--------------------------+----+
                                     |
                        +---------------------------+
                        |   Local Network Protocol  |
                        +---------------------------+

                         Protocol Relationships

                               Figure 1.

  Internet protocol interfaces on one side to the higher level
  host-to-host protocols and on the other side to the local network
  protocol.  In this context a "local network" may be a small network in
  a building or a large network such as the ARPANET.

[2.2](https://www.rfc-editor.org/rfc/rfc791#section-2.2). Model of Operation

  The  model of operation for transmitting a datagram from one
  application program to another is illustrated by the following
  scenario:

    We suppose that this transmission will involve one intermediate
    gateway.

    The sending application program prepares its data and calls on its
    local internet module to send that data as a datagram and passes the
    destination address and other parameters as arguments of the call.

    The internet module prepares a datagram header and attaches the data
    to it.  The internet module determines a local network address for
    this internet address, in this case it is the address of a gateway.

 [Page 5]

* * *

 September 1981
Internet Protocol
Overview

    It sends this datagram and the local network address to the local
    network interface.

    The local network interface creates a local network header, and
    attaches the datagram to it, then sends the result via the local
    network.

    The datagram arrives at a gateway host wrapped in the local network
    header, the local network interface strips off this header, and
    turns the datagram over to the internet module.  The internet module
    determines from the internet address that the datagram is to be
    forwarded to another host in a second network.  The internet module
    determines a local net address for the destination host.  It calls
    on the local network interface for that network to send the
    datagram.

    This local network interface creates a local network header and
    attaches the datagram sending the result to the destination host.

    At this destination host the datagram is stripped of the local net
    header by the local network interface and handed to the internet
    module.

    The internet module determines that the datagram is for an
    application program in this host.  It passes the data to the
    application program in response to a system call, passing the source
    address and other parameters as results of the call.

   Application                                           Application
   Program                                                   Program
         \                                                   /
       Internet Module      Internet Module      Internet Module
             \                 /       \                /
             LNI-1          LNI-1      LNI-2         LNI-2
                \           /             \          /
               Local Network 1           Local Network 2

                            Transmission Path

                                Figure 2

[Page 6]

* * *

September 1981
                                                       Internet Protocol
                                                                Overview

[2.3](https://www.rfc-editor.org/rfc/rfc791#section-2.3). Function Description

  The function or purpose of Internet Protocol is to move datagrams
  through an interconnected set of networks.  This is done by passing
  the datagrams from one internet module to another until the
  destination is reached.  The internet modules reside in hosts and
  gateways in the internet system.  The datagrams are routed from one
  internet module to another through individual networks based on the
  interpretation of an internet address.  Thus, one important mechanism
  of the internet protocol is the internet address.

  In the routing of messages from one internet module to another,
  datagrams may need to traverse a network whose maximum packet size is
  smaller than the size of the datagram.  To overcome this difficulty, a
  fragmentation mechanism is provided in the internet protocol.

  Addressing

    A distinction is made between names, addresses, and routes [[4](https://www.rfc-editor.org/rfc/rfc791#ref-4 "\"Inter-Network Naming, Addressing, and Routing,\"")].   A
    name indicates what we seek.  An address indicates where it is.  A
    route indicates how to get there.  The internet protocol deals
    primarily with addresses.  It is the task of higher level (i.e.,
    host-to-host or application) protocols to make the mapping from
    names to addresses.   The internet module maps internet addresses to
    local net addresses.  It is the task of lower level (i.e., local net
    or gateways) procedures to make the mapping from local net addresses
    to routes.

    Addresses are fixed length of four octets (32 bits).  An address
    begins with a network number, followed by local address (called the
    "rest" field).  There are three formats or classes of internet
    addresses:  in class a, the high order bit is zero, the next 7 bits
    are the network, and the last 24 bits are the local address; in
    class b, the high order two bits are one-zero, the next 14 bits are
    the network and the last 16 bits are the local address; in class c,
    the high order three bits are one-one-zero, the next 21 bits are the
    network and the last 8 bits are the local address.

    Care must be taken in mapping internet addresses to local net
    addresses; a single physical host must be able to act as if it were
    several distinct hosts to the extent of using several distinct
    internet addresses.  Some hosts will also have several physical
    interfaces (multi-homing).

    That is, provision must be made for a host to have several physical
