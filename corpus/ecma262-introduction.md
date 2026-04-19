Introduction

This Ecma Standard defines the ECMAScript 2027 Language. It is the eighteenth edition of the ECMAScript Language Specification. ECMAScript is based on several originating technologies, the most well-known being JavaScript (Netscape) and JScript (Microsoft). The language was invented by Brendan Eich at Netscape and first appeared in that company's Navigator 2.0 browser. Though best known as the language embedded in web browsers, it has also been widely adopted for use outside the browser, including server and embedded applications, and has grown to be one of the world's most widely used general-purpose programming languages.

The development of the ECMAScript Language Specification started in November 1996. The first edition of this Ecma Standard was adopted by the Ecma General Assembly of June 1997.

That Ecma Standard was submitted to ISO/IEC JTC 1 for adoption under the fast-track procedure, and approved as international standard ISO/IEC 16262, in April 1998. The Ecma General Assembly of June 1998 approved the second edition of ECMA-262 to keep it fully aligned with ISO/IEC 16262. Changes between the first and the second edition are editorial in nature.

The third edition of the Standard introduced powerful regular expressions, better string handling, new control statements, try/catch exception handling, tighter definition of errors, formatting for numeric output and minor changes in anticipation of future language growth. The third edition of the ECMAScript standard was adopted by the Ecma General Assembly of December 1999 and published as ISO/IEC 16262:2002 in June 2002.

After publication of the third edition, ECMAScript achieved massive adoption in conjunction with the World Wide Web where it has become the programming language that is supported by essentially all web browsers. Significant work was done to develop a fourth edition of ECMAScript. However, that work was not completed and not published as the fourth edition of ECMAScript but some of it was incorporated into the development of the sixth edition.

The fifth edition of ECMAScript (published as ECMA-262 5th edition) codified de facto interpretations of the language specification that have become common among browser implementations and added support for new features that had emerged since the publication of the third edition. Such features include accessor properties, reflective creation and inspection of objects, program control of property attributes, additional array manipulation functions, support for the JSON object encoding format, and a strict mode that provides enhanced error checking and program security. The fifth edition was adopted by the Ecma General Assembly of December 2009.

The fifth edition was submitted to ISO/IEC JTC 1 for adoption under the fast-track procedure, and approved as international standard ISO/IEC 16262:2011. Edition 5.1 of the ECMAScript Standard incorporated minor corrections and is the same text as ISO/IEC 16262:2011. The 5.1 Edition was adopted by the Ecma General Assembly of June 2011.

Focused development of the sixth edition started in 2009, as the fifth edition was being prepared for publication. However, this was preceded by significant experimentation and language enhancement design efforts dating to the publication of the third edition in 1999. In a very real sense, the completion of the sixth edition is the culmination of a fifteen year effort. The goals for this edition included providing better support for large applications, library creation, and for use of ECMAScript as a compilation target for other languages. Some of its major enhancements included modules, class declarations, lexical block scoping, iterators and generators, promises for asynchronous programming, destructuring patterns, and proper tail calls. The ECMAScript library of built-ins was expanded to support additional data abstractions including maps, sets, and arrays of binary numeric values as well as additional support for Unicode supplementary characters in strings and regular expressions. The built-ins were also made extensible via subclassing. The sixth edition provides the foundation for regular, incremental language and library enhancements. The sixth edition was adopted by the General Assembly of June 2015.

ECMAScript 2016 was the first ECMAScript edition released under Ecma TC39's new yearly release cadence and open development process. A plain-text source document was built from the ECMAScript 2015 source document to serve as the base for further development entirely on GitHub. Over the year of this standard's development, hundreds of pull requests and issues were filed representing thousands of bug fixes, editorial fixes and other improvements. Additionally, numerous software tools were developed to aid in this effort including Ecmarkup, Ecmarkdown, and Grammarkdown. ES2016 also included support for a new exponentiation operator and adds a new method to Array.prototype called includes.

ECMAScript 2017 introduced Async Functions, Shared Memory, and Atomics along with smaller language and library enhancements, bug fixes, and editorial updates. Async functions improve the asynchronous programming experience by providing syntax for promise-returning functions. Shared Memory and Atomics introduce a new memory model that allows multi-agent programs to communicate using atomic operations that ensure a well-defined execution order even on parallel CPUs. It also included new static methods on Object: Object.values, Object.entries, and Object.getOwnPropertyDescriptors.

ECMAScript 2018 introduced support for asynchronous iteration via the async iterator protocol and async generators. It also included four new regular expression features: the dotAll flag, named capture groups, Unicode property escapes, and look-behind assertions. Lastly it included object rest and spread properties.

ECMAScript 2019 introduced a few new built-in functions: flat and flatMap on Array.prototype for flattening arrays, Object.fromEntries for directly turning the return value of Object.entries into a new Object, and trimStart and trimEnd on String.prototype as better-named alternatives to the widely implemented but non-standard String.prototype.trimLeft and trimRight built-ins. In addition, it included a few minor updates to syntax and semantics. Updated syntax included optional catch binding parameters and allowing U+2028 (LINE SEPARATOR) and U+2029 (PARAGRAPH SEPARATOR) in string literals to align with JSON. Other updates included requiring that Array.prototype.sort be a stable sort, requiring that JSON.stringify return well-formed UTF-8 regardless of input, and clarifying Function.prototype.toString by requiring that it either return the corresponding original source text or a standard placeholder.

ECMAScript 2020, the 11th edition, introduced the matchAll method for Strings, to produce an iterator for all match objects generated by a global regular expression; import(), a syntax to asynchronously import Modules with a dynamic specifier; BigInt, a new number primitive for working with arbitrary precision integers; Promise.allSettled, a new Promise combinator that does not short-circuit; globalThis, a universal way to access the global this value; dedicated export * as ns from 'module' syntax for use within modules; increased standardization of for-in enumeration order; import.meta, a host-populated object available in Modules that may contain contextual information about the Module; as well as adding two new syntax features to improve working with “nullish” values (undefined or null): nullish coalescing, a value selection operator; and optional chaining, a property access and function invocation operator that short-circuits if the value to access/invoke is nullish.

ECMAScript 2021, the 12th edition, introduced the replaceAll method for Strings; Promise.any, a Promise combinator that short-circuits when an input value is fulfilled; AggregateError, a new Error type to represent multiple errors at once; logical assignment operators (??=, &&=, ||=); WeakRef, for referring to a target object without preserving it from garbage collection, and FinalizationRegistry, to manage registration and unregistration of cleanup operations performed when target objects are garbage collected; separators for numeric literals (1_000); and Array.prototype.sort was made more precise, reducing the amount of cases that result in an implementation-defined sort order.

ECMAScript 2022, the 13th edition, introduced top-level await, allowing the keyword to be used at the top level of modules; new class elements: public and private instance fields, public and private static fields, private instance methods and accessors, and private static methods and accessors; static blocks inside classes, to perform per-class evaluation initialization; the #x in obj syntax, to test for presence of private fields on objects; regular expression match indices via the /d flag, which provides start and end indices for matched substrings; the cause property on Error objects, which can be used to record a causation chain in errors; the at method for Strings, Arrays, and TypedArrays, which allows relative indexing; and Object.hasOwn, a convenient alternative to Object.prototype.hasOwnProperty.

ECMAScript 2023, the 14th edition, introduced the toSorted, toReversed, with, findLast, and findLastIndex methods on Array.prototype and TypedArray.prototype, as well as the toSpliced method on Array.prototype; added support for #! comments at the beginning of files to better facilitate executable ECMAScript files; and allowed the use of most Symbols as keys in weak collections.

ECMAScript 2024, the 15th edition, added facilities for resizing and transferring ArrayBuffers and SharedArrayBuffers; added a new RegExp /v flag for creating RegExps with more advanced features for working with sets of strings; and introduced the Promise.withResolvers convenience method for constructing Promises, the Object.groupBy and Map.groupBy methods for aggregating data, the Atomics.waitAsync method for asynchronously waiting for a change to shared memory, and the String.prototype.isWellFormed and String.prototype.toWellFormed methods for checking and ensuring that strings contain only well-formed Unicode.

ECMAScript 2025, the 16th edition, added a new Iterator global with associated static and prototype methods for working with iterators; added methods to Set.prototype for performing common operations on Sets; added support for importing JSON modules as well as syntax for declaring attributes of imported modules; added the RegExp.escape method for escaping a string to be safely used in a regular expression; added syntax for enabling and disabling modifier flags inline within regular expressions; added the Promise.try method for calling functions which may or may not return a Promise and ensuring the result is always a Promise; and added a new Float16Array TypedArray kind as well as the related DataView.prototype.getFloat16, DataView.prototype.setFloat16, and Math.f16round methods.

ECMAScript 2026, the 17th edition, added Math.sumPrecise for summing an iterable of Numbers of varying magnitude while minimizing precision loss; Iterator.concat for sequencing iterators; Array.fromAsync for constructing Arrays from async iterables and other async sources; Error.isError for identifying error objects; methods to Map.prototype and WeakMap.prototype for providing a default value to use during retrieval when a key is not already present; methods to Uint8Array for converting to and from Strings of hexadecimal- and base64-encoded binary data; a parameter to JSON.parse revivers to access the matched segment of JSON source; and JSON.rawJSON for fine control over JSON.stringify output for primitive values.

Dozens of individuals representing many organizations have made very significant contributions within Ecma TC39 to the development of this edition and to the prior editions. In addition, a vibrant community has emerged supporting TC39's ECMAScript efforts. This community has reviewed numerous drafts, filed thousands of bug reports, performed implementation experiments, contributed test suites, and educated the world-wide developer community about ECMAScript. Unfortunately, it is impossible to identify and acknowledge every person and organization who has contributed to this effort.

Allen Wirfs-Brock
ECMA-262, Project Editor, 6th Edition

Brian Terlson
ECMA-262, Project Editor, 7th through 10th Editions

Jordan Harband
ECMA-262, Project Editor, 10th through 12th Editions

Kevin Gibbons
ECMA-262, Project Editor, 12th through 17th Editions

Shu-yu Guo
ECMA-262, Project Editor, 12th through 18th Editions

Michael Ficarra
ECMA-262, Project Editor, 12th through 18th Editions

Richard Gibson
ECMA-262, Project Editor, 18th Edition

Ron Buckton
ECMA-262, Project Editor, 18th Edition

Nicolò Ribaudo
ECMA-262, Project Editor, 18th Edition

Linus Groh
ECMA-262, Project Editor, 18th Edition

1 Scope

This Standard defines the ECMAScript 2027 general-purpose programming language.

2 Conformance

A conforming implementation of ECMAScript must provide and support all the types, values, objects, properties, functions, and program syntax and semantics described in this specification.

A conforming implementation of ECMAScript must interpret source text input in conformance with the latest version of the Unicode Standard and ISO/IEC 10646.

A conforming implementation of ECMAScript that provides an application programming interface (API) that supports programs that need to adapt to the linguistic and cultural conventions used by different human languages and countries must implement the interface defined by the most recent edition of ECMA-402 that is compatible with this specification.

A conforming implementation of ECMAScript may provide additional types, values, objects, properties, and functions beyond those described in this specification. In particular, a conforming implementation of ECMAScript may provide properties not described in this specification, and values for those properties, for objects that are described in this specification.

A conforming implementation of ECMAScript may support program and regular expression syntax not described in this specification. In particular, a conforming implementation of ECMAScript may support program syntax that makes use of any “future reserved words” noted in subclause 12.7.2 of this specification.

A conforming implementation of ECMAScript must not implement any extension that is listed as a Forbidden Extension in subclause 17.1.

A conforming implementation of ECMAScript must not redefine any facilities that are not implementation-defined, implementation-approximated, or host-defined.

A conforming implementation of ECMAScript may choose to implement or not implement Normative Optional subclauses, unless otherwise indicated. Web browsers are generally required to implement all normative optional subclauses. (See Annex B.) If any Normative Optional behaviour is implemented, all of the behaviour in the containing Normative Optional clause must be implemented. A Normative Optional clause is denoted in this specification with the words "Normative Optional" in a coloured box, as shown below.

NORMATIVE OPTIONAL
2.1 Example Normative Optional Clause Heading

Example clause contents.

A conforming implementation of ECMAScript must implement Legacy subclauses, unless they are also marked as Normative Optional. All of the language features and behaviours specified within Legacy subclauses have one or more undesirable characteristics. However, their continued usage in existing applications prevents their removal from this specification. These features are not considered part of the core ECMAScript language. Programmers should not use or assume the existence of these features and behaviours when writing new ECMAScript code.

LEGACY
2.2 Example Legacy Clause Heading

Example clause contents.

NORMATIVE OPTIONAL, LEGACY
2.3 Example Legacy Normative Optional Clause Heading

Example clause contents.

3 Normative References

The following referenced documents are indispensable for the application of this document. For dated references, only the edition cited applies. For undated references, the latest edition of the referenced document (including any amendments) applies.

IEEE 754-2019, IEEE Standard for Floating-Point Arithmetic.

The Unicode Standard.
https://unicode.org/versions/latest

ISO/IEC 10646, Information Technology — Universal Multiple-Octet Coded Character Set (UCS) plus Amendment 1:2005, Amendment 2:2006, Amendment 3:2008, Amendment 4:2008, and additional amendments and corrigenda, or successor.

ECMA-402, ECMAScript Internationalization API Specification, specifically the annual edition corresponding to this edition of this specification.
https://www.ecma-international.org/publications-and-standards/standards/ecma-402/

ECMA-404, The JSON Data Interchange Format.
https://www.ecma-international.org/publications-and-standards/standards/ecma-404/

4 Overview

This section contains a non-normative overview of the ECMAScript language.

ECMAScript is an object-oriented programming language for performing computations and manipulating computational objects within a host environment. ECMAScript as defined here is not intended to be computationally self-sufficient; indeed, there are no provisions in this specification for input of external data or output of computed results. Instead, it is expected that the computational environment of an ECMAScript program will provide not only the objects and other facilities described in this specification but also certain environment-specific objects, whose description and behaviour are beyond the scope of this specification except to indicate that they may provide certain properties that can be accessed and certain functions that can be called from an ECMAScript program.

ECMAScript was originally designed to be used as a scripting language, but has become widely used as a general-purpose programming language. A scripting language is a programming language that is used to manipulate, customize, and automate the facilities of an existing system. In such systems, useful functionality is already available through a user interface, and the scripting language is a mechanism for exposing that functionality to program control. In this way, the existing system is said to provide a host environment of objects and facilities, which completes the capabilities of the scripting language. A scripting language is intended for use by both professional and non-professional programmers.

ECMAScript was originally designed to be a Web scripting language, providing a mechanism to enliven Web pages in browsers and to perform server computation as part of a Web-based client-server architecture. ECMAScript is now used to provide core scripting capabilities for a variety of host environments. Therefore the core language is specified in this document apart from any particular host environment.

ECMAScript usage has moved beyond simple scripting and it is now used for the full spectrum of programming tasks in many different environments and scales. As the usage of ECMAScript has expanded, so have the features and facilities it provides. ECMAScript is now a fully featured general-purpose programming language.

4.1 Web Scripting

A web browser provides an ECMAScript host environment for client-side computation including, for instance, objects that represent windows, menus, pop-ups, dialog boxes, text areas, anchors, frames, history, cookies, and input/output. Further, the host environment provides a means to attach scripting code to events such as change of focus, page and image loading, unloading, error and abort, selection, form submission, and mouse actions. Scripting code appears within the HTML and the displayed page is a combination of user interface elements and fixed and computed text and images. The scripting code is reactive to user interaction, and there is no need for a main program.

A web server provides a different host environment for server-side computation including objects representing requests, clients, and files; and mechanisms to lock and share data. By using browser-side and server-side scripting together, it is possible to distribute computation between the client and server while providing a customized user interface for a Web-based application.

Each Web browser and server that supports ECMAScript supplies its own host environment, completing the ECMAScript execution environment.

4.2 Hosts and Implementations

To aid integrating ECMAScript into host environments, this specification defers the definition of certain facilities (e.g., abstract operations), either in whole or in part, to a source outside of this specification. Editorially, this specification distinguishes the following kinds of deferrals.

An implementation is an external source that further defines facilities enumerated in Annex D or those that are marked as implementation-defined or implementation-approximated. In informal use, an implementation refers to a concrete artefact, such as a particular web browser.

An implementation-defined facility is one that defers its definition to an external source without further qualification. This specification does not make any recommendations for particular behaviours, and conforming implementations are free to choose any behaviour within the constraints put forth by this specification.

An implementation-approximated facility is one that defers its definition to an external source while recommending an ideal behaviour. While conforming implementations are free to choose any behaviour within the constraints put forth by this specification, they are encouraged to strive to approximate the ideal. Some mathematical operations, such as Math.exp, are implementation-approximated.

A host is an external source that further defines facilities listed in Annex D but does not further define other implementation-defined or implementation-approximated facilities. In informal use, a host refers to the set of all implementations, such as the set of all web browsers, that interface with this specification in the same way via Annex D. A host is often an external specification, such as WHATWG HTML (https://html.spec.whatwg.org/). In other words, facilities that are host-defined are often further defined in external specifications.

A host hook is an abstract operation that is defined in whole or in part by an external source. All host hooks must be listed in Annex D. A host hook must conform to at least the following requirements:

It must return either a normal completion or a throw completion.

A host-defined facility is one that defers its definition to an external source without further qualification and is listed in Annex D. Implementations that are not hosts may also provide definitions for host-defined facilities.

A host environment is a particular choice of definition for all host-defined facilities. A host environment typically includes objects or functions which allow obtaining input and providing output as host-defined properties of the global object.

This specification follows the editorial convention of always using the most specific term. For example, if a facility is host-defined, it should not be referred to as implementation-defined.

Both hosts and implementations may interface with this specification via the language types, specification types, abstract operations, grammar productions, intrinsic objects, and intrinsic symbols defined herein.

4.3 ECMAScript Overview

The following is an informal overview of ECMAScript—not all parts of the language are described. This overview is not part of the standard proper.

ECMAScript is object-based: basic language and host facilities are provided by objects, and an ECMAScript program is a cluster of communicating objects. In ECMAScript, an object is a collection of zero or more properties each with attributes that determine how each property can be used—for example, when the Writable attribute for a property is set to false, any attempt by executed ECMAScript code to assign a different value to the property fails. Properties are containers that hold other objects, primitive values, or functions. A primitive value is a member of one of the following built-in types: Undefined, Null, Boolean, Number, BigInt, String, and Symbol; an object is a member of the built-in type Object; and a function is a callable object. A function that is associated with an object via a property is called a method.

ECMAScript defines a collection of built-in objects that round out the definition of ECMAScript entities. These built-in objects include the global object; objects that are fundamental to the runtime semantics of the language including Object, Function, Boolean, Symbol, and various Error objects; objects that represent and manipulate numeric values including Math, Number, and Date; the text processing objects String and RegExp; objects that are indexed collections of values including Array and nine different kinds of Typed Arrays whose elements all have a specific numeric data representation; keyed collections including Map and Set objects; objects supporting structured data including the JSON object, ArrayBuffer, SharedArrayBuffer, and DataView; objects supporting control abstractions including generator functions and Promise objects; and reflection objects including Proxy and Reflect.

ECMAScript also defines a set of built-in operators. ECMAScript operators include various unary operations, multiplicative operators, additive operators, bitwise shift operators, relational operators, equality operators, binary bitwise operators, binary logical operators, assignment operators, and the comma operator.

Large ECMAScript programs are supported by modules which allow a program to be divided into multiple sequences of statements and declarations. Each module explicitly identifies declarations it uses that need to be provided by other modules and which of its declarations are available for use by other modules.

ECMAScript syntax intentionally resembles Java syntax. ECMAScript syntax is relaxed to enable it to serve as an easy-to-use scripting language. For example, a variable is not required to have its type declared nor are types associated with properties, and defined functions are not required to have their declarations appear textually before calls to them.

4.3.1 Objects

Even though ECMAScript includes syntax for class definitions, ECMAScript objects are not fundamentally class-based such as those in C++, Smalltalk, or Java. Instead objects may be created in various ways including via a literal notation or via constructors which create objects and then execute code that initializes all or part of them by assigning initial values to their properties. Each constructor is a function that has a property named "prototype" that is used to implement prototype-based inheritance and shared properties. Objects are created by using constructors in new expressions; for example, new Date(2009, 11) creates a new Date object. Invoking a constructor without using new has consequences that depend on the constructor. For example, Date() produces a string representation of the current date and time rather than an object.

Every object created by a constructor has an implicit reference (called the object's prototype) to the value of its constructor's "prototype" property. Furthermore, a prototype may have a non-null implicit reference to its prototype, and so on; this is called the prototype chain. When a reference is made to a property in an object, that reference is to the property of that name in the first object in the prototype chain that contains a property of that name. In other words, first the object mentioned directly is examined for such a property; if that object contains the named property, that is the property to which the reference refers; if that object does not contain the named property, the prototype for that object is examined next; and so on.

Figure 1: Object/Prototype Relationships

In a class-based object-oriented language, in general, state is carried by instances, methods are carried by classes, and inheritance is only of structure and behaviour. In ECMAScript, the state and methods are carried by objects, while structure, behaviour, and state are all inherited.

All objects that do not directly contain a particular property that their prototype contains share that property and its value. Figure 1 illustrates this:

CF is a constructor (and also an object). Five objects have been created by using new expressions: cf1, cf2, cf3, cf4, and cf5. Each of these objects contains properties named "q1" and "q2". The dashed lines represent the implicit prototype relationship; so, for example, cf3's prototype is CFp. The constructor, CF, has two properties itself, named "P1" and "P2", which are not visible to CFp, cf1, cf2, cf3, cf4, or cf5. The property named "CFP1" in CFp is shared by cf1, cf2, cf3, cf4, and cf5 (but not by CF), as are any properties found in CFp's implicit prototype chain that are not named "q1", "q2", or "CFP1". Notice that there is no implicit prototype link between CF and CFp.

Unlike most class-based object languages, properties can be added to objects dynamically by assigning values to them. That is, constructors are not required to name or assign values to all or any of the constructed object's properties. In the above diagram, one could add a new shared property for cf1, cf2, cf3, cf4, and cf5 by assigning a new value to the property in CFp.

Although ECMAScript objects are not inherently class-based, it is often convenient to define class-like abstractions based upon a common pattern of constructor functions, prototype objects, and methods. The ECMAScript built-in objects themselves follow such a class-like pattern. Beginning with ECMAScript 2015, the ECMAScript language includes syntactic class definitions that permit programmers to concisely define objects that conform to the same class-like abstraction pattern used by the built-in objects.

4.3.2 The Strict Variant of ECMAScript

The ECMAScript Language recognizes the possibility that some users of the language may wish to restrict their usage of some features available in the language. They might do so in the interests of security, to avoid what they consider to be error-prone features, to get enhanced error checking, or for other reasons of their choosing. In support of this possibility, ECMAScript defines a strict variant of the language. The strict variant of the language excludes some specific syntactic and semantic features of the regular ECMAScript language and modifies the detailed semantics of some features. The strict variant also specifies additional error conditions that must be reported by throwing error exceptions in situations that are not specified as errors by the non-strict form of the language.

The strict variant of ECMAScript is commonly referred to as the strict mode of the language. Strict mode selection and use of the strict mode syntax and semantics of ECMAScript is explicitly made at the level of individual ECMAScript source text units as described in 11.2.2. Because strict mode is selected at the level of a syntactic source text unit, strict mode only imposes restrictions that have local effect within such a source text unit. Strict mode does not restrict or modify any aspect of the ECMAScript semantics that must operate consistently across multiple source text units. A complete ECMAScript program may be composed of both strict mode and non-strict mode ECMAScript source text units. In this case, strict mode only applies when actually executing code that is defined within a strict mode source text unit.

In order to conform to this specification, an ECMAScript implementation must implement both the full unrestricted ECMAScript language and the strict variant of the ECMAScript language as defined by this specification. In addition, an implementation must support the combination of unrestricted and strict mode source text units into a single composite program.

4.4 Terms and Definitions

For the purposes of this document, the following terms and definitions apply.

4.4.1 implementation-approximated

an implementation-approximated facility is defined in whole or in part by an external source but has a recommended, ideal behaviour in this specification

4.4.2 implementation-defined

an implementation-defined facility is defined in whole or in part by an external source to this specification

4.4.3 host-defined

same as implementation-defined

NOTE

Editorially, see clause 4.2.

4.4.4 type

set of data values as defined in clause 6

4.4.5 primitive value

member of one of the types Undefined, Null, Boolean, Number, BigInt, Symbol, or String as defined in clause 6

NOTE

A primitive value is a datum that is represented directly at the lowest level of the language implementation.

4.4.6 object

member of the type Object

NOTE

An object is a collection of properties and has a single prototype object. The prototype may be null.

4.4.7 constructor

function object that creates and initializes objects

NOTE

The value of a constructor's "prototype" property is a prototype object that is used to implement inheritance and shared properties.

4.4.8 prototype

object that provides shared properties for other objects

NOTE

When a constructor creates an object, that object implicitly references the constructor's "prototype" property for the purpose of resolving property references. The constructor's "prototype" property can be referenced by the program expression constructor.prototype, and properties added to an object's prototype are shared, through inheritance, by all objects sharing the prototype. Alternatively, a new object may be created with an explicitly specified prototype by using the Object.create built-in function.

4.4.9 ordinary object

object that has the default behaviour for the essential internal methods that must be supported by all objects

4.4.10 exotic object

object that does not have the default behaviour for one or more of the essential internal methods

NOTE

Any object that is not an ordinary object is an exotic object.

4.4.11 standard object

object whose semantics are defined by this specification

4.4.12 built-in object

object specified and supplied by an ECMAScript implementation

NOTE

Standard built-in objects are defined in this specification. An ECMAScript implementation may specify and supply additional kinds of built-in objects.

4.4.13 undefined value

primitive value used when a variable has not been assigned a value

4.4.14 Undefined type

type whose sole value is the undefined value

4.4.15 null value

primitive value that represents the intentional absence of any object value

4.4.16 Null type

type whose sole value is the null value

4.4.17 Boolean value

member of the Boolean type

NOTE

There are only two Boolean values, true and false.

4.4.18 Boolean type

type consisting of the primitive values true and false

4.4.19 Boolean object

member of the Object type that is an instance of the standard built-in Boolean constructor

NOTE

A Boolean object is created by using the Boolean constructor in a new expression, supplying a Boolean value as an argument. The resulting object has an internal slot whose value is the Boolean value. A Boolean object can be coerced to a Boolean value.

4.4.20 String value

primitive value that is a finite ordered sequence of zero or more 16-bit unsigned integer values

NOTE

A String value is a member of the String type. Each integer value in the sequence usually represents a single 16-bit unit of UTF-16 text. However, ECMAScript does not place any restrictions or requirements on the values except that they must be 16-bit unsigned integers.

4.4.21 String type

set of all possible String values

4.4.22 String object

member of the Object type that is an instance of the standard built-in String constructor

NOTE

A String object is created by using the String constructor in a new expression, supplying a String value as an argument. The resulting object has an internal slot whose value is the String value. A String object can be coerced to a String value by calling the String constructor as a function (22.1.1.1).

4.4.23 Number value

primitive value corresponding to a double-precision 64-bit binary format IEEE 754-2019 value

NOTE

A Number value is a member of the Number type and is a direct representation of a number.

4.4.24 Number type

set of all possible Number values including NaN (“not a number”), +∞𝔽 (positive infinity), and -∞𝔽 (negative infinity)

4.4.25 Number object

member of the Object type that is an instance of the standard built-in Number constructor

NOTE

A Number object is created by using the Number constructor in a new expression, supplying a Number value as an argument. The resulting object has an internal slot whose value is the Number value. A Number object can be coerced to a Number value by calling the Number constructor as a function (21.1.1.1).

4.4.26 Infinity

Number value that is the positive infinite Number value

4.4.27 NaN

Number value that is an IEEE 754-2019 NaN (“not a number”) value

4.4.28 BigInt value

primitive value corresponding to an arbitrary-precision integer value

4.4.29 BigInt type

set of all possible BigInt values

4.4.30 BigInt object

member of the Object type that is an instance of the standard built-in BigInt constructor

4.4.31 Symbol value

primitive value that represents a unique, non-String Object property key

4.4.32 Symbol type

set of all possible Symbol values

4.4.33 Symbol object

member of the Object type that is an instance of the standard built-in Symbol constructor

4.4.34 function

member of the Object type that may be invoked as a subroutine

NOTE

In addition to its properties, a function contains executable code and state that determine how it behaves when invoked. A function's code may or may not be written in ECMAScript.

4.4.35 built-in function

built-in object that is a function

NOTE

Examples of built-in functions include parseInt and Math.exp. A host or implementation may provide additional built-in functions that are not described in this specification.

4.4.36 built-in constructor

built-in function that is a constructor

NOTE

Examples of built-in constructors include Object and Function. A host or implementation may provide additional built-in constructors that are not described in this specification.

4.4.37 property

part of an object that associates a key (either a String value or a Symbol value) and a value

NOTE
