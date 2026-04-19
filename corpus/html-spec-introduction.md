# HTML Standard
[](https://whatwg.org/)
# HTML

Living Standard — Last Updated 15 April 2026

[Table of Contents](https://html.spec.whatwg.org/multipage/) — [2 Common infrastructure →](https://html.spec.whatwg.org/multipage/infrastructure.html)
1.   [1 Introduction](https://html.spec.whatwg.org/multipage/introduction.html#introduction)
    1.   [1.1 Where does this specification fit?](https://html.spec.whatwg.org/multipage/introduction.html#abstract)
    2.   [1.2 Is this HTML5?](https://html.spec.whatwg.org/multipage/introduction.html#is-this-html5?)
    3.   [1.3 Background](https://html.spec.whatwg.org/multipage/introduction.html#background)
    4.   [1.4 Audience](https://html.spec.whatwg.org/multipage/introduction.html#audience)
    5.   [1.5 Scope](https://html.spec.whatwg.org/multipage/introduction.html#scope)
    6.   [1.6 History](https://html.spec.whatwg.org/multipage/introduction.html#history-2)
    7.   [1.7 Design notes](https://html.spec.whatwg.org/multipage/introduction.html#design-notes)
        1.   [1.7.1 Serializability of script execution](https://html.spec.whatwg.org/multipage/introduction.html#serialisability-of-script-execution)
        2.   [1.7.2 Extensibility](https://html.spec.whatwg.org/multipage/introduction.html#extensibility)

    8.   [1.8 HTML vs XML syntax](https://html.spec.whatwg.org/multipage/introduction.html#html-vs-xhtml)
    9.   [1.9 Structure of this specification](https://html.spec.whatwg.org/multipage/introduction.html#structure-of-this-specification)
        1.   [1.9.1 How to read this specification](https://html.spec.whatwg.org/multipage/introduction.html#how-to-read-this-specification)
        2.   [1.9.2 Typographic conventions](https://html.spec.whatwg.org/multipage/introduction.html#typographic-conventions)

    10.   [1.10 A quick introduction to HTML](https://html.spec.whatwg.org/multipage/introduction.html#a-quick-introduction-to-html)
        1.   [1.10.1 Writing secure applications with HTML](https://html.spec.whatwg.org/multipage/introduction.html#writing-secure-applications-with-html)
        2.   [1.10.2 Common pitfalls to avoid when using the scripting APIs](https://html.spec.whatwg.org/multipage/introduction.html#common-pitfalls-to-avoid-when-using-the-scripting-apis)
        3.   [1.10.3 How to catch mistakes when writing HTML: validators and conformance checkers](https://html.spec.whatwg.org/multipage/introduction.html#how-to-catch-mistakes-when-writing-html:-validators-and-conformance-checkers)

    11.   [1.11 Conformance requirements for authors](https://html.spec.whatwg.org/multipage/introduction.html#conformance-requirements-for-authors)
        1.   [1.11.1 Presentational markup](https://html.spec.whatwg.org/multipage/introduction.html#presentational-markup)
        2.   [1.11.2 Syntax errors](https://html.spec.whatwg.org/multipage/introduction.html#syntax-errors)
        3.   [1.11.3 Restrictions on content models and on attribute values](https://html.spec.whatwg.org/multipage/introduction.html#restrictions-on-content-models-and-on-attribute-values)

    12.   [1.12 Suggested reading](https://html.spec.whatwg.org/multipage/introduction.html#suggested-reading)

## 1 Introduction[](https://html.spec.whatwg.org/multipage/introduction.html#introduction)

### 1.1 Where does this specification fit?[](https://html.spec.whatwg.org/multipage/introduction.html#abstract)

This specification defines a big part of the web platform, in lots of detail. Its place in the web platform specification stack relative to other specifications can be best summed up as follows:

### 1.2 Is this HTML5?[](https://html.spec.whatwg.org/multipage/introduction.html#is-this-html5?)

_This section is non-normative._

In short: Yes.

In more length: the term "HTML5" is widely used as a buzzword to refer to modern web technologies, many of which (though by no means all) are developed at the WHATWG. This document is one such; others are available from [the WHATWG Standards overview](https://spec.whatwg.org/).

### 1.3 Background[](https://html.spec.whatwg.org/multipage/introduction.html#background)

_This section is non-normative._

HTML is the World Wide Web's core markup language. Originally, HTML was primarily designed as a language for semantically describing scientific documents. Its general design, however, has enabled it to be adapted, over the subsequent years, to describe a number of other types of documents and even applications.

### 1.4 Audience[](https://html.spec.whatwg.org/multipage/introduction.html#audience)

_This section is non-normative._

This specification is intended for authors of documents and scripts that use the features defined in this specification, implementers of tools that operate on pages that use the features defined in this specification, and individuals wishing to establish the correctness of documents or implementations with respect to the requirements of this specification.

This document is probably not suited to readers who do not already have at least a passing familiarity with web technologies, as in places it sacrifices clarity for precision, and brevity for completeness. More approachable tutorials and authoring guides can provide a gentler introduction to the topic.

In particular, familiarity with the basics of DOM is necessary for a complete understanding of some of the more technical parts of this specification. An understanding of Web IDL, HTTP, XML, Unicode, character encodings, JavaScript, and CSS will also be helpful in places but is not essential.

### 1.5 Scope[](https://html.spec.whatwg.org/multipage/introduction.html#scope)

_This section is non-normative._

This specification is limited to providing a semantic-level markup language and associated semantic-level scripting APIs for authoring accessible pages on the web ranging from static documents to dynamic applications.

The scope of this specification does not include providing mechanisms for media-specific customization of presentation (although default rendering rules for web browsers are included at the end of this specification, and several mechanisms for hooking into CSS are provided as part of the language).

The scope of this specification is not to describe an entire operating system. In particular, hardware configuration software, image manipulation tools, and applications that users would be expected to use with high-end workstations on a daily basis are out of scope. In terms of applications, this specification is targeted specifically at applications that would be expected to be used by users on an occasional basis, or regularly but from disparate locations, with low CPU requirements. Examples of such applications include online purchasing systems, searching systems, games (especially multiplayer online games), public telephone books or address books, communications software (email clients, instant messaging clients, discussion software), document editing software, etc.

### 1.6 History[](https://html.spec.whatwg.org/multipage/introduction.html#history-2)

_This section is non-normative._

For its first five years (1990-1995), HTML went through a number of revisions and experienced a number of extensions, primarily hosted first at CERN, and then at the IETF.

With the creation of the W3C, HTML's development changed venue again. A first abortive attempt at extending HTML in 1995 known as HTML 3.0 then made way to a more pragmatic approach known as HTML 3.2, which was completed in 1997. HTML4 quickly followed later that same year.

The following year, the W3C membership decided to stop evolving HTML and instead begin work on an XML-based equivalent, called XHTML. This effort started with a reformulation of HTML4 in XML, known as XHTML 1.0, which added no new features except the new serialization, and which was completed in 2000. After XHTML 1.0, the W3C's focus turned to making it easier for other working groups to extend XHTML, under the banner of XHTML Modularization. In parallel with this, the W3C also worked on a new language that was not compatible with the earlier HTML and XHTML languages, calling it XHTML2.

Around the time that HTML's evolution was stopped in 1998, parts of the API for HTML developed by browser vendors were specified and published under the name DOM Level 1 (in 1998) and DOM Level 2 Core and DOM Level 2 HTML (starting in 2000 and culminating in 2003). These efforts then petered out, with some DOM Level 3 specifications published in 2004 but the working group being closed before all the Level 3 drafts were completed.

In 2003, the publication of XForms, a technology which was positioned as the next generation of web forms, sparked a renewed interest in evolving HTML itself, rather than finding replacements for it. This interest was borne from the realization that XML's deployment as a web technology was limited to entirely new technologies (like RSS and later Atom), rather than as a replacement for existing deployed technologies (like HTML).

A proof of concept to show that it was possible to extend HTML4's forms to provide many of the features that XForms 1.0 introduced, without requiring browsers to implement rendering engines that were incompatible with existing HTML web pages, was the first result of this renewed interest. At this early stage, while the draft was already publicly available, and input was already being solicited from all sources, the specification was only under Opera Software's copyright.

The idea that HTML's evolution should be reopened was tested at a W3C workshop in 2004, where some of the principles that underlie the HTML5 work (described below), as well as the aforementioned early draft proposal covering just forms-related features, were presented to the W3C jointly by Mozilla and Opera. The proposal was rejected on the grounds that the proposal conflicted with the previously chosen direction for the web's evolution; the W3C staff and membership voted to continue developing XML-based replacements instead.

Shortly thereafter, Apple, Mozilla, and Opera jointly announced their intent to continue working on the effort under the umbrella of a new venue called the WHATWG. A public mailing list was created, and the draft was moved to the WHATWG site. The copyright was subsequently amended to be jointly owned by all three vendors, and to allow reuse of the specification.

The WHATWG was based on several core principles, in particular that technologies need to be backwards compatible, that specifications and implementations need to match even if this means changing the specification rather than the implementations, and that specifications need to be detailed enough that implementations can achieve complete interoperability without reverse-engineering each other.

The latter requirement in particular required that the scope of the HTML5 specification include what had previously been specified in three separate documents: HTML4, XHTML1, and DOM2 HTML. It also meant including significantly more detail than had previously been considered the norm.

In 2006, the W3C indicated an interest to participate in the development of HTML5 after all, and in 2007 formed a working group chartered to work with the WHATWG on the development of the HTML5 specification. Apple, Mozilla, and Opera allowed the W3C to publish the specification under the W3C copyright, while keeping a version with the less restrictive license on the WHATWG site.

For a number of years, both groups then worked together. In 2011, however, the groups came to the conclusion that they had different goals: the W3C wanted to publish a "finished" version of "HTML5", while the WHATWG wanted to continue working on a Living Standard for HTML, continuously maintaining the specification rather than freezing it in a state with known problems, and adding new features as needed to evolve the platform.

In 2019, the WHATWG and W3C [signed an agreement](https://www.w3.org/blog/news/archives/7753) to collaborate on a single version of HTML going forward: this document.

### 1.7 Design notes[](https://html.spec.whatwg.org/multipage/introduction.html#design-notes)

_This section is non-normative._

It must be admitted that many aspects of HTML appear at first glance to be nonsensical and inconsistent.

HTML, its supporting DOM APIs, as well as many of its supporting technologies, have been developed over a period of several decades by a wide array of people with different priorities who, in many cases, did not know of each other's existence.

Features have thus arisen from many sources, and have not always been designed in especially consistent ways. Furthermore, because of the unique characteristics of the web, implementation bugs have often become de-facto, and now de-jure, standards, as content is often unintentionally written in ways that rely on them before they can be fixed.

Despite all this, efforts have been made to adhere to certain design goals. These are described in the next few subsections.

#### 1.7.1 Serializability of script execution[](https://html.spec.whatwg.org/multipage/introduction.html#serialisability-of-script-execution)

_This section is non-normative._

To avoid exposing web authors to the complexities of multithreading, the HTML and DOM APIs are designed such that no script can ever detect the simultaneous execution of other scripts. Even with [workers](https://html.spec.whatwg.org/multipage/workers.html#worker), the intent is that the behavior of implementations can be thought of as completely serializing the execution of all scripts in all globals.

The exception to this general design principle is the JavaScript `SharedArrayBuffer` class. Using `SharedArrayBuffer` objects, it can in fact be observed that scripts in other [agents](https://tc39.es/ecma262/#sec-agents) are executing simultaneously. Furthermore, due to the JavaScript memory model, there are situations which not only are un-representable via serialized _script_ execution, but also un-representable via serialized _statement_ execution among those scripts.

#### 1.7.2 Extensibility[](https://html.spec.whatwg.org/multipage/introduction.html#extensibility)

_This section is non-normative._

HTML has a wide array of extensibility mechanisms that can be used for adding semantics in a safe manner:

*   Authors can use the `class` attribute to extend elements, effectively creating their own elements, while using the most applicable existing "real" HTML element, so that browsers and other tools that don't know of the extension can still support it somewhat well. This is the tack used by microformats, for example.

*   Authors can include data for inline client-side scripts or server-side site-wide scripts to process using the `data-*=""` attributes. These are guaranteed to never be touched by browsers, and allow scripts to include data on HTML elements that scripts can then look for and process.

*   Authors can use the `<meta name="" content="">` mechanism to include page-wide metadata.

*   Authors can use the `rel=""` mechanism to annotate links with specific meanings by registering [extensions to the predefined set of link types](https://html.spec.whatwg.org/multipage/links.html#concept-rel-extensions). This is also used by microformats.

*   Authors can embed raw data using the `<script type="">` mechanism with a custom type, for further handling by inline or server-side scripts.

*   Authors can extend APIs using the JavaScript prototyping mechanism. This is widely used by script libraries, for instance.

*   Authors can use the microdata feature (the `itemscope=""` and `itemprop=""` attributes) to embed nested name-value pairs of data to be shared with other applications and sites.

*   Authors can define, share, and use [custom elements](https://html.spec.whatwg.org/multipage/custom-elements.html#custom-element) to extend the vocabulary of HTML. The requirements of [valid custom element names](https://html.spec.whatwg.org/multipage/custom-elements.html#valid-custom-element-name) ensure forward compatibility (since no elements will be added to HTML, SVG, or MathML with hyphen-containing local names in the future).

### 1.8 HTML vs XML syntax[](https://html.spec.whatwg.org/multipage/introduction.html#html-vs-xhtml)

_This section is non-normative._

This specification defines an abstract language for describing documents and applications, and some APIs for interacting with in-memory representations of resources that use this language.

The in-memory representation is known as "DOM HTML", or "the DOM" for short.

There are various concrete syntaxes that can be used to transmit resources that use this abstract language, two of which are defined in this specification.

The first such concrete syntax is the HTML syntax. This is the format suggested for most authors. It is compatible with most legacy web browsers. If a document is transmitted with the `text/html`[MIME type](https://mimesniff.spec.whatwg.org/#mime-type), then it will be processed as an HTML document by web browsers. This specification defines the latest HTML syntax, known simply as "HTML".

The second concrete syntax is XML. When a document is transmitted with an [XML MIME type](https://mimesniff.spec.whatwg.org/#xml-mime-type), such as `application/xhtml+xml`, then it is treated as an XML document by web browsers, to be parsed by an XML processor. Authors are reminded that the processing for XML and HTML differs; in particular, even minor syntax errors will prevent a document labeled as XML from being rendered fully, whereas they would be ignored in the HTML syntax.

The XML syntax for HTML was formerly referred to as "XHTML", but this specification does not use that term (among other reasons, because no such term is used for the HTML syntaxes of MathML and SVG).

The DOM, the HTML syntax, and the XML syntax cannot all represent the same content. For example, namespaces cannot be represented using the HTML syntax, but they are supported in the DOM and in the XML syntax. Similarly, documents that use the `noscript` feature can be represented using the HTML syntax, but cannot be represented with the DOM or in the XML syntax. Comments that contain the string "`-->`" can only be represented in the DOM, not in the HTML and XML syntaxes.

### 1.9 Structure of this specification[](https://html.spec.whatwg.org/multipage/introduction.html#structure-of-this-specification)

_This section is non-normative._

This specification is divided into the following major sections:

[Introduction](https://html.spec.whatwg.org/multipage/introduction.html#introduction)Non-normative materials providing a context for the HTML standard.[Common infrastructure](https://html.spec.whatwg.org/multipage/infrastructure.html#infrastructure)The conformance classes, algorithms, definitions, and the common underpinnings of the rest of the specification.[Semantics, structure, and APIs of HTML documents](https://html.spec.whatwg.org/multipage/dom.html#dom)Documents are built from elements. These elements form a tree using the DOM. This section defines the features of this DOM, as well as introducing the features common to all elements, and the concepts used in defining elements.[The elements of HTML](https://html.spec.whatwg.org/multipage/semantics.html#semantics)Each element has a predefined meaning, which is explained in this section. Rules for authors on how to use the element, along with user agent requirements for how to handle each element, are also given. This includes large signature features of HTML such as video playback and subtitles, form controls and form submission, and a 2D graphics API known as the HTML canvas.[Microdata](https://html.spec.whatwg.org/multipage/microdata.html#microdata)This specification introduces a mechanism for adding machine-readable annotations to documents, so that tools can extract trees of name-value pairs from the document. This section describes this mechanism and some algorithms that can be used to convert HTML documents into other formats. This section also defines some sample Microdata vocabularies for contact information, calendar events, and licensing works.[User interaction](https://html.spec.whatwg.org/multipage/interaction.html#editing)HTML documents can provide a number of mechanisms for users to interact with and modify content, which are described in this section, such as how focus works, and drag-and-drop.[Loading web pages](https://html.spec.whatwg.org/multipage/browsers.html#browsers)HTML documents do not exist in a vacuum — this section defines many of the features that affect environments that deal with multiple pages, such as web browsers.[Web application APIs](https://html.spec.whatwg.org/multipage/webappapis.html#webappapis)This section introduces basic features for scripting of applications in HTML.[Web workers](https://html.spec.whatwg.org/multipage/workers.html#workers)This section defines an API for background threads in JavaScript.[Worklets](https://html.spec.whatwg.org/multipage/worklets.html#worklets)This section defines infrastructure for APIs that need to run JavaScript separately from the main JavaScript execution environment.[The communication APIs](https://html.spec.whatwg.org/multipage/comms.html#comms)This section describes some mechanisms that applications written in HTML can use to communicate with other applications from different domains running on the same client. It also introduces a server-push event stream mechanism known as Server Sent Events or `EventSource`, and a two-way full-duplex socket protocol for scripts known as Web Sockets.[Web storage](https://html.spec.whatwg.org/multipage/webstorage.html#webstorage)This section defines a client-side storage mechanism based on name-value pairs.[The HTML syntax](https://html.spec.whatwg.org/multipage/syntax.html#syntax)[The XML syntax](https://html.spec.whatwg.org/multipage/xhtml.html#xhtml)All of these features would be for naught if they couldn't be represented in a serialized form and sent to other people, and so these sections define the syntaxes of HTML and XML, along with rules for how to parse content using those syntaxes.[Rendering](https://html.spec.whatwg.org/multipage/rendering.html#rendering)This section defines the default rendering rules for web browsers.
There are also some appendices, listing [obsolete features](https://html.spec.whatwg.org/multipage/obsolete.html#obsolete) and [IANA considerations](https://html.spec.whatwg.org/multipage/iana.html#iana), and several indices.

#### 1.9.1 How to read this specification[](https://html.spec.whatwg.org/multipage/introduction.html#how-to-read-this-specification)

This specification should be read like all other specifications. First, it should be read cover-to-cover, multiple times. Then, it should be read backwards at least once. Then it should be read by picking random sections from the contents list and following all the cross-references.

As described in the conformance requirements section below, this specification describes conformance criteria for a variety of conformance classes. In particular, there are conformance requirements that apply to _producers_, for example authors and the documents they create, and there are conformance requirements that apply to _consumers_, for example web browsers. They can be distinguished by what they are requiring: a requirement on a producer states what is allowed, while a requirement on a consumer states how software is to act.

For example, "the `foo` attribute's value must be a [valid integer](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-integer)" is a requirement on producers, as it lays out the allowed values; in contrast, the requirement "the `foo` attribute's value must be parsed using the [rules for parsing integers](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#rules-for-parsing-integers)" is a requirement on consumers, as it describes how to process the content.

**Requirements on producers have no bearing whatsoever on consumers.**

Continuing the above example, a requirement stating that a particular attribute's value is constrained to being a [valid integer](https://html.spec.whatwg.org/multipage/common-microsyntaxes.html#valid-integer) emphatically does _not_ imply anything about the requirements on consumers. It might be that the consumers are in fact required to treat the attribute as an opaque string, completely unaffected by whether the value conforms to the requirements or not. It might be (as in the previous example) that the consumers are required to parse the value using specific rules that define how invalid (non-numeric in this case) values are to be processed.

#### 1.9.2 Typographic conventions[](https://html.spec.whatwg.org/multipage/introduction.html#typographic-conventions)

This is a definition, requirement, or explanation.

This is a note.

This is an example.

This is an open issue.

This is a warning.

```
[Exposed=Window]
interface Example {
  // this is an IDL definition
};
```
`variable = object.method([optionalArgument])`
This is a note to authors describing the usage of an interface.

`/* this is a CSS fragment */`
The defining instance of a term is marked up like this. Uses of that term are marked up like [this](https://html.spec.whatwg.org/multipage/introduction.html#x-this) or like _[this](https://html.spec.whatwg.org/multipage/introduction.html#x-this)_.

The defining instance of an element, attribute, or API is marked up like `this`. References to that element, attribute, or API are marked up like `this`.

Other code fragments are marked up `like this`.

Variables are marked up like this.

In an algorithm, steps in [synchronous sections](https://html.spec.whatwg.org/multipage/webappapis.html#synchronous-section) are marked with ⌛.

In some cases, requirements are given in the form of lists with conditions and corresponding requirements. In such cases, the requirements that apply to a condition are always the first set of requirements that follow the condition, even in the case of there being multiple sets of conditions for those requirements. Such cases are presented as follows:

This is a condition This is another condition This is the requirement that applies to the conditions above. This is a third condition This is the requirement that applies to the third condition. 
### 1.10 A quick introduction to HTML[](https://html.spec.whatwg.org/multipage/introduction.html#a-quick-introduction-to-html)

_This section is non-normative._

A basic HTML document looks like this:

```
<!DOCTYPE html>
<html lang="en">
 <head>
  <title>Sample page</title>
 </head>
 <body>
  <h1>Sample page</h1>
  <p>This is a <a href="demo.html">simple</a> sample.</p>
  <!-- this is a comment -->
 </body>
</html>
```

HTML documents consist of a tree of elements and text. Each element is denoted in the source by a [start tag](https://html.spec.whatwg.org/multipage/syntax.html#syntax-start-tag), such as "`<body>`", and an [end tag](https://html.spec.whatwg.org/multipage/syntax.html#syntax-end-tag), such as "`</body>`". (Certain start tags and end tags can in certain cases be [omitted](https://html.spec.whatwg.org/multipage/syntax.html#syntax-tag-omission) and are implied by other tags.)

Tags have to be nested such that elements are all completely within each other, without overlapping:

`<p>This is <em>very <strong>wrong</em>!</strong></p>``<p>This <em>is <strong>correct</strong>.</em></p>`
This specification defines a set of elements that can be used in HTML, along with rules about the ways in which the elements can be nested.

Elements can have attributes, which control how the elements work. In the example below, there is a [hyperlink](https://html.spec.whatwg.org/multipage/links.html#hyperlink), formed using the `a` element and its `href` attribute:

`<a href="demo.html">simple</a>`
[Attributes](https://html.spec.whatwg.org/multipage/syntax.html#syntax-attributes) are placed inside the start tag, and consist of a [name](https://html.spec.whatwg.org/multipage/syntax.html#syntax-attribute-name) and a [value](https://html.spec.whatwg.org/multipage/syntax.html#syntax-attribute-value), separated by an "`=`" character. The attribute value can remain [unquoted](https://html.spec.whatwg.org/multipage/syntax.html#unquoted) if it doesn't contain [ASCII whitespace](https://infra.spec.whatwg.org/#ascii-whitespace) or any of `"``'`````=``<` or `>`. Otherwise, it has to be quoted using either single or double quotes. The value, along with the "`=`" character, can be omitted altogether if the value is the empty string.

```
<!-- empty attributes -->
<input name=address disabled>
<input name=address disabled="">

<!-- attributes with a value -->
<input name=address maxlength=200>
<input name=address maxlength='200'>
<input name=address maxlength="200">
```

HTML user agents (e.g., web browsers) then _parse_ this markup, turning it into a DOM (Document Object Model) tree. A DOM tree is an in-memory representation of a document.

DOM trees contain several kinds of nodes, in particular a `DocumentType` node, `Element` nodes, `Text` nodes, `Comment` nodes, and in some cases `ProcessingInstruction` nodes.

The [markup snippet at the top of this section](https://html.spec.whatwg.org/multipage/introduction.html#intro-early-example) would be turned into the following DOM tree:

*   DOCTYPE: `html`
*   `html``lang`="`en`"
    *   `head`
        *   `#text`: ⏎␣␣
        *   `title`
            *   `#text`: Sample page

        *   `#text`: ⏎␣

    *   `#text`: ⏎␣
    *   `body`
        *   `#text`: ⏎␣␣
        *   `h1`
            *   `#text`: Sample page

        *   `#text`: ⏎␣␣
        *   `p`
            *   `#text`: This is a 
            *   `a``href`="`demo.html`"
                *   `#text`: simple

            *   `#text`:  sample.

        *   `#text`: ⏎␣␣
        *   `#comment`:  this is a comment 
        *   `#text`: ⏎␣⏎

The [document element](https://dom.spec.whatwg.org/#document-element) of this tree is the `html` element, which is the element always found in that position in HTML documents. It contains two elements, `head` and `body`, as well as a `Text` node between them.

There are many more `Text` nodes in the DOM tree than one would initially expect, because the source contains a number of spaces (represented here by "␣") and line breaks ("⏎") that all end up as `Text` nodes in the DOM. However, for historical reasons not all of the spaces and line breaks in the original markup appear in the DOM. In particular, all the whitespace before `head` start tag ends up being dropped silently, and all the whitespace after the `body` end tag ends up placed at the end of the `body`.

The `head` element contains a `title` element, which itself contains a `Text` node with the text "Sample page". Similarly, the `body` element contains an `h1` element, a `p` element, and a comment.

* * *

This DOM tree can be manipulated from scripts in the page. Scripts (typically in JavaScript) are small programs that can be embedded using the `script` element or using [event handler content attributes](https://html.spec.whatwg.org/multipage/webappapis.html#event-handler-content-attributes). For example, here is a form with a script that sets the value of the form's `output` element to say "Hello World":

```
<form name="main">
 Result: <output name="result"></output>
 <script>
  document.forms.main.elements.result.value = 'Hello World';
 </script>
</form>
```

Each element in the DOM tree is represented by an object, and these objects have APIs so that they can be manipulated. For instance, a link (e.g. the `a` element in the tree above) can have its "`href`" attribute changed in several ways:

```
var a = document.links[0]; // obtain the first link in the document
a.href = 'sample.html'; // change the destination URL of the link
a.protocol = 'https'; // change just the scheme part of the URL
a.setAttribute('href', 'https://example.com/'); // change the content attribute directly
```

Since DOM trees are used as the way to represent HTML documents when they are processed and presented by implementations (especially interactive implementations like web browsers), this specification is mostly phrased in terms of DOM trees, instead of the markup described above.

* * *

HTML documents represent a media-independent description of interactive content. HTML documents might be rendered to a screen, or through a speech synthesizer, or on a braille display. To influence exactly how such rendering takes place, authors can use a styling language such as CSS.

In the following example, the page has been made yellow-on-blue using CSS.

```
<!DOCTYPE html>
<html lang="en">
 <head>
  <title>Sample styled page</title>
  <style>
   body { background: navy; color: yellow; }
  </style>
 </head>
 <body>
  <h1>Sample styled page</h1>
  <p>This page is just a demo.</p>
 </body>
</html>
```

For more details on how to use HTML, authors are encouraged to consult tutorials and guides. Some of the examples included in this specification might also be of use, but the novice author is cautioned that this specification, by necessity, defines the language with a level of detail that might be difficult to understand at first.

#### 1.10.1 Writing secure applications with HTML[](https://html.spec.whatwg.org/multipage/introduction.html#writing-secure-applications-with-html)

_This section is non-normative._

When HTML is used to create interactive sites, care needs to be taken to avoid introducing vulnerabilities through which attackers can compromise the integrity of the site itself or of the site's users.

A comprehensive study of this matter is beyond the scope of this document, and authors are strongly encouraged to study the matter in more detail. However, this section attempts to provide a quick introduction to some common pitfalls in HTML application development.

The security model of the web is based on the concept of "origins", and correspondingly many of the potential attacks on the web involve cross-origin actions. [[ORIGIN]](https://html.spec.whatwg.org/multipage/references.html#refsORIGIN)

Not validating user input Cross-site scripting (XSS)SQL injection
When accepting untrusted input, e.g. user-generated content such as text comments, values in URL parameters, messages from third-party sites, etc, it is imperative that the data be validated before use, and properly escaped when displayed. Failing to do this can allow a hostile user to perform a variety of attacks, ranging from the potentially benign, such as providing bogus user information like a negative age, to the serious, such as running scripts every time a user looks at a page that includes the information, potentially propagating the attack in the process, to the catastrophic, such as deleting all data in the server.

When writing filters to validate user input, it is imperative that filters always be safelist-based, allowing known-safe constructs and disallowing all other input. Blocklist-based filters that disallow known-bad inputs and allow everything else are not secure, as not everything that is bad is yet known (for example, because it might be invented in the future).

For example, suppose a page looked at its URL's query string to determine what to display, and the site then redirected the user to that page to display a message, as in:

```
<ul>
 <li><a href="message.cgi?say=Hello">Say Hello</a>
 <li><a href="message.cgi?say=Welcome">Say Welcome</a>
 <li><a href="message.cgi?say=Kittens">Say Kittens</a>
</ul>
```

If the message was just displayed to the user without escaping, a hostile attacker could then craft a URL that contained a script element:

https://example.com/message.cgi?say=%3Cscript%3Ealert%28%27Oh%20no%21%27%29%3C/script%3E
If the attacker then convinced a victim user to visit this page, a script of the attacker's choosing would run on the page. Such a script could do any number of hostile actions, limited only by what the site offers: if the site is an e-commerce shop, for instance, such a script could cause the user to unknowingly make arbitrarily many unwanted purchases.

This is called a cross-site scripting attack.

There are many constructs that can be used to try to trick a site into executing code. Here are some that authors are encouraged to consider when writing safelist filters:

*   When allowing harmless-seeming elements like `img`, it is important to safelist any provided attributes as well. If one allowed all attributes then an attacker could, for instance, use the `onload` attribute to run arbitrary script.
*   When allowing URLs to be provided (e.g. for links), the scheme of each URL also needs to be explicitly safelisted, as there are many schemes that can be abused. The most prominent example is "`javascript:`", but user agents can implement (and indeed, have historically implemented) others.
*   Allowing a `base` element to be inserted means any `script` elements in the page with relative links can be hijacked, and similarly that any form submissions can get redirected to a hostile site.

Cross-site request forgery (CSRF)
If a site allows a user to make form submissions with user-specific side-effects, for example posting messages on a forum under the user's name, making purchases, or applying for a passport, it is important to verify that the request was made by the user intentionally, rather than by another site tricking the user into making the request unknowingly.

This problem exists because HTML forms can be submitted to other origins.

Sites can prevent such attacks by populating forms with user-specific hidden tokens, or by checking ``Origin`` headers on all requests.

Clickjacking
A page that provides users with an interface to perform actions that the user might not wish to perform needs to be designed so as to avoid the possibility that users can be tricked into activating the interface.

One way that a user could be so tricked is if a hostile site places the victim site in a small `iframe` and then convinces the user to click, for instance by having the user play a reaction game. Once the user is playing the game, the hostile site can quickly position the iframe under the mouse cursor just as the user is about to click, thus tricking the user into clicking the victim site's interface.
