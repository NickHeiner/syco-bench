# RFC 822: STANDARD FOR THE FORMAT OF ARPA INTERNET TEXT MESSAGES
[[RFC Home](https://www.rfc-editor.org/ "RFC Editor")] [[TEXT](https://www.rfc-editor.org/rfc/rfc822.txt)|[PDF](https://www.rfc-editor.org/rfc/pdfrfc/rfc822.txt.pdf)|[HTML](https://www.rfc-editor.org/rfc/rfc822.html)] [[Tracker](https://datatracker.ietf.org/doc/rfc822 "IETF Datatracker information for this document")] [[IPR](https://datatracker.ietf.org/ipr/search/?rfc=822&submit=rfc "IPR disclosures related to this document")] [[Errata](https://www.rfc-editor.org/errata/rfc0822)] [[Info page](https://www.rfc-editor.org/info/rfc822 "Info page")] 

Obsoleted by: [2822](https://www.rfc-editor.org/rfc/rfc2822) INTERNET STANDARD

Updated by: [1123](https://www.rfc-editor.org/rfc/rfc1123), [2156](https://www.rfc-editor.org/rfc/rfc2156), [1327](https://www.rfc-editor.org/rfc/rfc1327), [1138](https://www.rfc-editor.org/rfc/rfc1138), [1148](https://www.rfc-editor.org/rfc/rfc1148)Errata Exist     RFC #  822
     
     Obsoletes:  RFC #733  (NIC #41952)
     
     
     
     
     
     
     
     
     
     
     
     
                        STANDARD FOR THE FORMAT OF
     
                        ARPA INTERNET TEXT MESSAGES
     
     
     
     
     
     
                              August 13, 1982
     
     
     
     
     
     
                                Revised by
     
                             David H. Crocker
     
     
                      Dept. of Electrical Engineering
                 University of Delaware, Newark, DE  19711
                      Network:  DCrocker @ UDel-Relay
     
     
     
     
     
     
     
     
     
     
     
     

* * *

Standard for ARPA Internet Text Messages
     
     
                             TABLE OF CONTENTS
     
     
     PREFACE ....................................................   [ii](https://www.rfc-editor.org/rfc/rfc822#page-ii)
     
     [1](https://www.rfc-editor.org/rfc/rfc822#section-1).  INTRODUCTION ...........................................    [1](https://www.rfc-editor.org/rfc/rfc822#page-1)
     
         [1.1](https://www.rfc-editor.org/rfc/rfc822#section-1.1).  Scope ............................................    [1](https://www.rfc-editor.org/rfc/rfc822#page-1)
         [1.2](https://www.rfc-editor.org/rfc/rfc822#section-1.2).  Communication Framework ..........................    [2](https://www.rfc-editor.org/rfc/rfc822#page-2)
     
     [2](https://www.rfc-editor.org/rfc/rfc822#section-2).  NOTATIONAL CONVENTIONS .................................    [3](https://www.rfc-editor.org/rfc/rfc822#page-3)
     
     [3](https://www.rfc-editor.org/rfc/rfc822#section-3).  LEXICAL ANALYSIS OF MESSAGES ...........................    [5](https://www.rfc-editor.org/rfc/rfc822#page-5)
     
         [3.1](https://www.rfc-editor.org/rfc/rfc822#section-3.1).  General Description ..............................    [5](https://www.rfc-editor.org/rfc/rfc822#page-5)
         [3.2](https://www.rfc-editor.org/rfc/rfc822#section-3.2).  Header Field Definitions .........................    [9](https://www.rfc-editor.org/rfc/rfc822#page-9)
         [3.3](https://www.rfc-editor.org/rfc/rfc822#section-3.3).  Lexical Tokens ...................................   [10](https://www.rfc-editor.org/rfc/rfc822#page-10)
         [3.4](https://www.rfc-editor.org/rfc/rfc822#section-3.4).  Clarifications ...................................   [11](https://www.rfc-editor.org/rfc/rfc822#page-11)
     
     [4](https://www.rfc-editor.org/rfc/rfc822#section-4).  MESSAGE SPECIFICATION ..................................   [17](https://www.rfc-editor.org/rfc/rfc822#page-17)
     
         [4.1](https://www.rfc-editor.org/rfc/rfc822#section-4.1).  Syntax ...........................................   [17](https://www.rfc-editor.org/rfc/rfc822#page-17)
         [4.2](https://www.rfc-editor.org/rfc/rfc822#section-4.2).  Forwarding .......................................   [19](https://www.rfc-editor.org/rfc/rfc822#page-19)
         [4.3](https://www.rfc-editor.org/rfc/rfc822#section-4.3).  Trace Fields .....................................   [20](https://www.rfc-editor.org/rfc/rfc822#page-20)
         [4.4](https://www.rfc-editor.org/rfc/rfc822#section-4.4).  Originator Fields ................................   [21](https://www.rfc-editor.org/rfc/rfc822#page-21)
         [4.5](https://www.rfc-editor.org/rfc/rfc822#section-4.5).  Receiver Fields ..................................   [23](https://www.rfc-editor.org/rfc/rfc822#page-23)
         [4.6](https://www.rfc-editor.org/rfc/rfc822#section-4.6).  Reference Fields .................................   [23](https://www.rfc-editor.org/rfc/rfc822#page-23)
         [4.7](https://www.rfc-editor.org/rfc/rfc822#section-4.7).  Other Fields .....................................   [24](https://www.rfc-editor.org/rfc/rfc822#page-24)
     
     [5](https://www.rfc-editor.org/rfc/rfc822#section-5).  DATE AND TIME SPECIFICATION ............................   [26](https://www.rfc-editor.org/rfc/rfc822#page-26)
     
         [5.1](https://www.rfc-editor.org/rfc/rfc822#section-5.1).  Syntax ...........................................   [26](https://www.rfc-editor.org/rfc/rfc822#page-26)
         [5.2](https://www.rfc-editor.org/rfc/rfc822#section-5.2).  Semantics ........................................   [26](https://www.rfc-editor.org/rfc/rfc822#page-26)
     
     [6](https://www.rfc-editor.org/rfc/rfc822#section-6).  ADDRESS SPECIFICATION ..................................   [27](https://www.rfc-editor.org/rfc/rfc822#page-27)
     
         [6.1](https://www.rfc-editor.org/rfc/rfc822#section-6.1).  Syntax ...........................................   [27](https://www.rfc-editor.org/rfc/rfc822#page-27)
         [6.2](https://www.rfc-editor.org/rfc/rfc822#section-6.2).  Semantics ........................................   [27](https://www.rfc-editor.org/rfc/rfc822#page-27)
         [6.3](https://www.rfc-editor.org/rfc/rfc822#section-6.3).  Reserved Address .................................   [33](https://www.rfc-editor.org/rfc/rfc822#page-33)
     
     [7](https://www.rfc-editor.org/rfc/rfc822#section-7).  BIBLIOGRAPHY ...........................................   [34](https://www.rfc-editor.org/rfc/rfc822#page-34)
     
     
                             APPENDIX
     
     [A](https://www.rfc-editor.org/rfc/rfc822#appendix-A).  EXAMPLES ...............................................   [36](https://www.rfc-editor.org/rfc/rfc822#page-36)
     [B](https://www.rfc-editor.org/rfc/rfc822#appendix-B).  SIMPLE FIELD PARSING ...................................   [40](https://www.rfc-editor.org/rfc/rfc822#page-40)
     [C](https://www.rfc-editor.org/rfc/rfc822#appendix-C).  DIFFERENCES FROM RFC #733 ..............................   [41](https://www.rfc-editor.org/rfc/rfc822#page-41)
     [D](https://www.rfc-editor.org/rfc/rfc822#appendix-D).  ALPHABETICAL LISTING OF SYNTAX RULES ...................   [44](https://www.rfc-editor.org/rfc/rfc822#page-44)
     
     
     August 13, 1982               - i -                      RFC #822

* * *

Standard for ARPA Internet Text Messages
     
     
                                  PREFACE
     
     
          By 1977, the Arpanet employed several informal standards for
     the  text  messages (mail) sent among its host computers.  It was
     felt necessary to codify these practices and  provide  for  those
     features  that  seemed  imminent.   The result of that effort was
     Request for Comments (RFC) #733, "Standard for the Format of ARPA
     Network Text Message", by Crocker, Vittal, Pogran, and Henderson.
     The specification attempted to avoid major  changes  in  existing
     software, while permitting several new features.
     
          This document revises the specifications  in  RFC  #733,  in
     order  to  serve  the  needs  of the larger and more complex ARPA
     Internet.  Some of RFC #733's features failed  to  gain  adequate
     acceptance.   In  order to simplify the standard and the software
     that follows it, these features have been removed.   A  different
     addressing  scheme  is  used, to handle the case of inter-network
     mail; and the concept of re-transmission has been introduced.
     
          This specification is intended for use in the ARPA Internet.
     However, an attempt has been made to free it of any dependence on
     that environment, so that it can be applied to other network text
     message systems.
     
          The specification of RFC #733 took place over the course  of
     one  year, using the ARPANET mail environment, itself, to provide
     an on-going forum for discussing the capabilities to be included.
     More  than  twenty individuals, from across the country, partici-
     pated in  the  original  discussion.   The  development  of  this
     revised specification has, similarly, utilized network mail-based
     group discussion.  Both specification efforts  greatly  benefited
     from the comments and ideas of the participants.
     
          The syntax of the standard,  in  RFC  #733,  was  originally
     specified  in  the  Backus-Naur Form (BNF) meta-language.  Ken L.
     Harrenstien, of SRI International, was responsible for  re-coding
     the  BNF  into  an  augmented  BNF  that makes the representation
     smaller and easier to understand.
     
     
     
     
     
     
     
     
     
     
     
     
     August 13, 1982              - ii -                      RFC #822

* * *

Standard for ARPA Internet Text Messages
     
     
     [1](https://www.rfc-editor.org/rfc/rfc822#section-1). INTRODUCTION
     
     [1.1](https://www.rfc-editor.org/rfc/rfc822#section-1.1). SCOPE
     
          This standard specifies a syntax for text messages that  are
     sent  among  computer  users, within the framework of "electronic
     mail".  The standard supersedes  the  one  specified  in  ARPANET
     Request  for Comments #733, "Standard for the Format of ARPA Net-
     work Text Messages".
     
          In this context, messages are viewed as having  an  envelope
     and  contents.   The  envelope  contains  whatever information is
     needed to accomplish transmission  and  delivery.   The  contents
     compose  the object to be delivered to the recipient.  This stan-
     dard applies only to the format and some of the semantics of mes-
     sage  contents.   It contains no specification of the information
     in the envelope.
     
          However, some message systems may use information  from  the
     contents  to create the envelope.  It is intended that this stan-
     dard facilitate the acquisition of such information by programs.
     
          Some message systems may  store  messages  in  formats  that
     differ  from the one specified in this standard.  This specifica-
     tion is intended strictly as a definition of what message content
     format is to be passed BETWEEN hosts.
     
     Note:  This standard is NOT intended to dictate the internal for-
            mats  used  by sites, the specific message system features
            that they are expected to support, or any of  the  charac-
            teristics  of  user interface programs that create or read
            messages.
     
          A distinction should be made between what the  specification
     REQUIRES  and  what  it ALLOWS.  Messages can be made complex and
     rich with formally-structured components of information or can be
     kept small and simple, with a minimum of such information.  Also,
     the standard simplifies the interpretation  of  differing  visual
     formats  in  messages;  only  the  visual  aspect of a message is
     affected and not the interpretation  of  information  within  it.
     Implementors may choose to retain such visual distinctions.
     
          The formal definition is divided into four levels.  The bot-
     tom level describes the meta-notation used in this document.  The
     second level describes basic lexical analyzers that  feed  tokens
     to  higher-level  parsers.   Next is an overall specification for
     messages; it permits distinguishing individual fields.   Finally,
     there is definition of the contents of several structured fields.
     
     
     
     August 13, 1982               - 1 -                      RFC #822

* * *

Standard for ARPA Internet Text Messages
     
     
     [1.2](https://www.rfc-editor.org/rfc/rfc822#section-1.2). COMMUNICATION FRAMEWORK
     
          Messages consist of lines of text.   No  special  provisions
     are  made for encoding drawings, facsimile, speech, or structured
     text.  No significant consideration has been given  to  questions
     of  data  compression  or to transmission and storage efficiency,
     and the standard tends to be free with the number  of  bits  con-
     sumed.   For  example,  field  names  are specified as free text,
     rather than special terse codes.
     
          A general "memo" framework is used.  That is, a message con-
     sists of some information in a rigid format, followed by the main
     part of the message, with a format that is not specified in  this
     document.   The  syntax of several fields of the rigidly-formated
     ("headers") section is defined in  this  specification;  some  of
     these fields must be included in all messages.
     
          The syntax  that  distinguishes  between  header  fields  is
     specified  separately  from  the  internal  syntax for particular
     fields.  This separation is intended to allow simple  parsers  to
     operate on the general structure of messages, without concern for
     the detailed structure of individual header fields.   Appendix  B
     is provided to facilitate construction of these parsers.
     
          In addition to the fields specified in this document, it  is
     expected  that  other fields will gain common use.  As necessary,
     the specifications for these "extension-fields" will be published
     through  the same mechanism used to publish this document.  Users
     may also  wish  to  extend  the  set  of  fields  that  they  use
     privately.  Such "user-defined fields" are permitted.
     
          The framework severely constrains document tone and  appear-
     ance and is primarily useful for most intra-organization communi-
     cations and  well-structured   inter-organization  communication.
     It  also  can  be used for some types of inter-process communica-
     tion, such as simple file transfer and remote job entry.  A  more
     robust  framework might allow for multi-font, multi-color, multi-
     dimension encoding of information.  A  less  robust  one,  as  is
     present  in  most  single-machine  message  systems,  would  more
     severely constrain the ability to add fields and the decision  to
     include specific fields.  In contrast with paper-based communica-
     tion, it is interesting to note that the RECEIVER  of  a  message
     can   exercise  an  extraordinary  amount  of  control  over  the
     message's appearance.  The amount of actual control available  to
     message  receivers  is  contingent upon the capabilities of their
     individual message systems.
     
     
     
     
     
     August 13, 1982               - 2 -                      RFC #822

* * *

Standard for ARPA Internet Text Messages
     
     
     [2](https://www.rfc-editor.org/rfc/rfc822#section-2). NOTATIONAL CONVENTIONS
     
          This specification uses an augmented Backus-Naur Form  (BNF)
     notation.  The differences from standard BNF involve naming rules
     and indicating repetition and "local" alternatives.
     
     [2.1](https://www.rfc-editor.org/rfc/rfc822#section-2.1). RULE NAMING
     
          Angle brackets ("<", ">") are not  used,  in  general.   The
     name  of  a rule is simply the name itself, rather than "<name>".
     Quotation-marks enclose literal text (which may be  upper  and/or
     lower  case).   Certain  basic  rules  are  in uppercase, such as
     SPACE, TAB, CRLF, DIGIT, ALPHA, etc.  Angle brackets are used  in
     rule  definitions,  and  in  the rest of this  document, whenever
     their presence will facilitate discerning the use of rule names.
     
     [2.2](https://www.rfc-editor.org/rfc/rfc822#section-2.2). RULE1 / RULE2: ALTERNATIVES
     
          Elements separated by slash ("/") are alternatives.   There-
     fore "foo / bar" will accept foo or bar.
     
     [2.3](https://www.rfc-editor.org/rfc/rfc822#section-2.3). (RULE1 RULE2): LOCAL ALTERNATIVES
     
          Elements enclosed in parentheses are  treated  as  a  single
     element.   Thus,  "(elem  (foo  /  bar)  elem)"  allows the token
     sequences "elem foo elem" and "elem bar elem".
     
     [2.4](https://www.rfc-editor.org/rfc/rfc822#section-2.4). *RULE: REPETITION
     
          The character "*" preceding an element indicates repetition.
     The full form is:
     
                              <l>*<m>element
     
     indicating at least <l> and at most <m> occurrences  of  element.
     Default values are 0 and infinity so that "*(element)" allows any
     number, including zero; "1*element" requires at  least  one;  and
     "1*2element" allows one or two.
     
     [2.5](https://www.rfc-editor.org/rfc/rfc822#section-2.5). [RULE]: OPTIONAL
     
          Square brackets enclose optional elements; "[foo  bar]"   is
     equivalent to "*1(foo bar)".
     
     [2.6](https://www.rfc-editor.org/rfc/rfc822#section-2.6). NRULE: SPECIFIC REPETITION
     
          "<n>(element)" is equivalent to "<n>*<n>(element)"; that is,
     exactly  <n>  occurrences  of (element). Thus 2DIGIT is a 2-digit
     number, and 3ALPHA is a string of three alphabetic characters.
     
     
     August 13, 1982               - 3 -                      RFC #822

* * *

Standard for ARPA Internet Text Messages
     
     
     [2.7](https://www.rfc-editor.org/rfc/rfc822#section-2.7). #RULE: LISTS
     
          A construct "#" is defined, similar to "*", as follows:
     
                              <l>#<m>element
     
     indicating at least <l> and at most <m> elements, each  separated
     by  one  or more commas (","). This makes the usual form of lists
     very easy; a rule such as '(element *("," element))' can be shown
     as  "1#element".   Wherever this construct is used, null elements
     are allowed, but do not  contribute  to  the  count  of  elements
     present.   That  is,  "(element),,(element)"  is  permitted,  but
     counts as only two elements.  Therefore, where at least one  ele-
     ment  is required, at least one non-null element must be present.
     Default values are 0 and infinity so that "#(element)" allows any
     number,  including  zero;  "1#element" requires at least one; and
     "1#2element" allows one or two.
     
     [2.8](https://www.rfc-editor.org/rfc/rfc822#section-2.8). ; COMMENTS
     
          A semi-colon, set off some distance to  the  right  of  rule
     text,  starts  a comment that continues to the end of line.  This
     is a simple way of including useful notes in  parallel  with  the
     specifications.
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
