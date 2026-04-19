↑
←

CSS Snapshot 2026

W3C Group Note, 26 March 2026

More details about this document
This version:
https://www.w3.org/TR/2026/NOTE-css-2026-20260326/
Latest published version:
https://www.w3.org/TR/css-2026/
Editor's Draft:
https://drafts.csswg.org/css-2026/
Previous Versions:
https://www.w3.org/TR/2026/NOTE-css-2026-20260226/
History:
https://www.w3.org/standards/history/css-2026/
Feedback:
CSSWG Issues Repository
Editors:
Tab Atkins Jr. (Google)
Elika J. Etemad / fantasai (Apple)
Florian Rivoal (Invited Expert)
Chris Lilley (W3C)
Sebastian Zartner (Invited Expert)
Suggest an Edit for this Spec:
GitHub Editor

Copyright © 2026 World Wide Web Consortium. W3C® liability, trademark and permissive document license rules apply.

Abstract

This document collects together into one definition all the specs that together form the current state of Cascading Style Sheets (CSS) as of 2026. The primary audience is CSS implementers, not CSS authors, as this definition includes modules by specification stability, not Web browser adoption rate.

CSS is a language for describing the rendering of structured documents (such as HTML and XML) on screen, on paper, etc.
Status of this document

This section describes the status of this document at the time of its publication. A list of current W3C publications and the latest revision of this technical report can be found in the W3C standards and drafts index.

This document was published by the CSS Working Group as a Group Note using the Note track. Group Notes are not endorsed by W3C nor its Members.

Please send feedback by filing issues in GitHub (preferred), including the spec code “css-2026” in the title, like this: “[css-2026] …summary of comment…”. All issues and comments are archived. Alternately, feedback can be sent to the (archived) public mailing list www-style@w3.org.

This document is governed by the 18 August 2025 W3C Process Document.

The 15 September 2020 W3C Patent Policy does not carry any licensing requirements or commitments on this document.

This document represents the state of CSS as of 2026.

table of contents
1
Introduction
1.1
What is CSS?
1.2
Background: The W3C Process and CSS
2
Classification of CSS Specifications
2.1
Cascading Style Sheets (CSS) — The Official Definition
2.2
Reliable Candidate Recommendations
2.3
Fairly Stable Modules with limited implementation experience
2.4
Modules with Rough Interoperability
2.5
CSS Levels
2.6
CSS Profiles
3
Requirements for Responsible Implementation of CSS
3.1
Partial Implementations
3.2
Implementations of Unstable and Proprietary Features
3.2.1
Experimentation and Unstable Features
3.2.2
Proprietary and Non-standardized Features
3.2.3
Market Pressure and De Facto Standards
3.3
Implementations of CR-level Features
4
Safe to Release pre-CR Exceptions
5
The text/css media type
6
Security Considerations
7
Privacy Considerations
8
Indices
8.1
Terms Index
8.2
Selector Index
8.3
At-Rule Index
8.4
Property Index
8.5
Values Index
9
Acknowledgements
Conformance
Document conventions
Conformance classes
Partial implementations
Implementations of Unstable and Proprietary Features
Non-experimental implementations
References
Normative References
Informative References
1. Introduction

When the first CSS specification was published, all of CSS was contained in one document that defined CSS Level 1. CSS Level 2 was defined also by a single, multi-chapter document. However for CSS beyond Level 2, the CSS Working Group chose to adopt a modular approach, where each module defines a part of CSS, rather than to define a single monolithic specification. This breaks the specification into more manageable chunks and allows more immediate, incremental improvement to CSS.

Since different CSS modules are at different levels of stability, the CSS Working Group has chosen to publish this profile to define the current scope and state of Cascading Style Sheets as of 2026.

1.1. What is CSS?
Cascading Style Sheets (CSS)
CSS is a language for writing style sheets, and is designed to describe the rendering of structured documents (such as HTML and XML) on a variety of media. CSS is used to describe the presentation of a source document, and usually does not change the underlying semantics expressed by its document language.
Style sheet
A set of rules that specify the presentation of a document. Style sheets are written by an Author, and interpreted by a user agent, to present the document to the User.
Source document
The document to which one or more style sheets apply. A source document’s structure and semantics are encoded using a document language (e.g., HTML, XHTML, or SVG).
Author
An author is a person who writes documents and associated style sheets. An authoring tool is a user agent that generates style sheets.
User
A user is a person who interacts with a user agent to view, hear, or otherwise use the document.
User agent (UA)
A user agent is any program that interprets a document and its associated style sheets on behalf of a user. A user agent may display a document, read it aloud, cause it to be printed, convert it to another format, etc. For the purposes of the CSS specifications, a user agent is one that supports and interprets Cascading Style Sheets as defined in these specifications.
1.2. Background: The W3C Process and CSS

This section is non-normative.

In the W3C Process, a Recommendation-track document passes through three levels of stability, summarized below:

Working Draft (WD)

This is the design phase of a W3C spec. The WG iterates the spec in response to internal and external feedback.

The first official Working Draft is designated the “First Public Working Draft” (FPWD). In the CSSWG, publishing FPWD indicates that the Working Group as a whole has agreed to work on the module, roughly as scoped out and proposed in the editor’s draft.

The transition to the next stage is sometimes called “Last Call Working Draft” (LCWD) phase. The CSSWG transitions Working Drafts once we have resolved all known issues, and can make no further progress without feedback from building tests and implementations.

This “Last Call for Comments” sets a deadline for reporting any outstanding issues, and requires the WG to specially track and address incoming feedback. The comment-tracking document is the Disposition of Comments (DoC). It is submitted along with an updated draft for the Director’s approval, to demonstrate wide review and acceptance.

Candidate Recommendation (CR)
This is the testing phase of a W3C spec. Notably, this phase is about using tests and implementations to test the specification: it is not about testing the implementations. This process often reveals more problems with the spec, and so a Candidate Recommendation will morph over time in response to implementation and testing feedback, though usually less so than during the design phase (WD).

Demonstration of two correct, independent implementations of each feature is required to exit CR, so in this phase the WG builds a test suite and generates implementation reports.

The transition to the next stage is “Proposed Recommendation” (PR). During this phase the W3C Advisory Committee must approve the transition to REC.

Recommendation (REC)
This is the completed state of a W3C spec and represents a maintenance phase. At this point the WG only maintains an errata document and occasionally publishes an updated edition that incorporates the errata back into the spec.

An Editor’s Draft is effectively a live copy of the editors’ own working copy. It may or may not reflect Working Group consensus, and can at times be in a self-inconsistent state. (Because the publishing process at W3C is time-consuming and onerous, the Editor’s Draft is usually the best (most up-to-date) reference for a spec. Efforts are currently underway to reduce the friction of publishing, so that official drafts will be regularly up-to-date and Editor’s Drafts can return to their original function as scratch space.)

2. Classification of CSS Specifications

A list of all CSS modules, stable and in-progress, and their statuses can be found at the CSS Current Work page.

2.1. Cascading Style Sheets (CSS) — The Official Definition

This profile includes only specifications that we consider stable and for which we have enough implementation experience that we are sure of that stability.

NOTE: This is not intended to be a CSS Desktop Browser Profile: inclusion in this profile is based on feature stability only and not on expected use or Web browser adoption. This profile defines CSS in its most complete form.

As of 2026, Cascading Style Sheets (CSS) is defined by the following specifications.

CSS Level 2, latest revision (including errata) [CSS2]
This defines the core of CSS, parts of which are overridden by later specifications. We recommend in particular reading Chapter 2, which introduces some of the basic concepts of CSS and its design principles.
CSS Syntax Module Level 3 [CSS-SYNTAX-3]
Replaces CSS2§4.1, CSS2§4.2, CSS2§4.4, and CSS2§G, redefining how CSS is parsed.
CSS Style Attributes [CSS-STYLE-ATTR]
Defines how CSS declarations can be embedded in markup attributes.
Media Queries Level 3 [CSS3-MEDIAQUERIES]
Replaces CSS2§7.3 and expands on the syntax for media-specific styles.
CSS Conditional Rules Module Level 3 [CSS-CONDITIONAL-3]
Extends and supersedes CSS2§7.2, updating the definition of @media rules to allow nesting and introducing the @supports rule for feature-support queries.
Selectors Level 3 [SELECTORS-3]
Replaces CSS2§5 and CSS2§6.4.3, defining an extended range of selectors.
CSS Namespaces Module Level 3 [CSS3-NAMESPACE]
Introduces an @namespace rule to allow namespace-prefixed selectors.
CSS Cascading and Inheritance Level 4 [CSS-CASCADE-4]
Extends and supersedes CSS2§1.4.3 and CSS2§6, as well as [CSS-CASCADE-3]. Describes how to collate style rules and assign values to all properties on all elements. By way of cascading and inheritance, values are propagated for all properties on all elements.
CSS Values and Units Module Level 3 [CSS-VALUES-3]
Extends and supersedes CSS2§1.4.2.1, CSS2§4.3, and CSS2§A.2.1–3, defining CSS’s property definition syntax and expanding its set of units.
CSS Custom Properties for Cascading Variables Module Level 1 [CSS-VARIABLES-1]
Introduces cascading variables as a new primitive value type that is accepted by all CSS properties, and custom properties for defining them.
CSS Box Model Module Level 3 [CSS-BOX-3]
Replaces CSS2§8.1, §8.2, §8.3 (but not §8.3.1), and §8.4.
CSS Color Module Level 4 [CSS-COLOR-4]
Extends and supersedes CSS2§4.3.6, CSS2§14.1, and CSS2§18.2, also extends and supersedes [CSS-COLOR-3], introducing an extended range of color spaces beyond sRGB, extended color values, and CSS Object Model extensions for color. Also defines the opacity property.
CSS Backgrounds and Borders Module Level 3 [CSS-BACKGROUNDS-3]
Extends and supersedes CSS2§8.5 and CSS2§14.2, providing more control of backgrounds and borders, including layered background images, image borders, and drop shadows.
CSS Images Module Level 3 [CSS-IMAGES-3]
Redefines and incorporates the external 2D image value type, introduces native 2D gradients, and adds additional controls for replaced element sizing and rendering.
CSS Fonts Module Level 3 [CSS-FONTS-3]
Extends and supersedes CSS2§15 and provides more control over font choice and feature selection.
CSS Writing Modes Level 3 [CSS-WRITING-MODES-3]
Defines CSS support for various international writing modes, such as left-to-right (e.g. Latin or Indic), right-to-left (e.g. Hebrew or Arabic), bidirectional (e.g. mixed Latin and Arabic) and vertical (e.g. Asian scripts). Replaces and extends CSS2§8.6 and §9.10.
CSS Multi-column Layout Module Level 1 [CSS-MULTICOL-1]
Introduces multi-column flows to CSS layout.
CSS Flexible Box Layout Module Level 1 [CSS-FLEXBOX-1]
Introduces a flexible linear layout model for CSS.
CSS Basic User Interface Module Level 3 [CSS-UI-3]
Extends and supersedes CSS2§18.1 and CSS2§18.4, defining cursor, outline, and several new CSS features that also enhance the user interface.
CSS Containment Module Level 1 [CSS-CONTAIN-1]
Introduces the contain property, which enforces the independent CSS processing of an element’s subtree in order to enable heavy optimizations by user agents when used well.
CSS Transforms Module Level 1 [CSS-TRANSFORMS-1]
Introduces coordinate-based graphical transformations to CSS.
Compositing and Blending Level 1 [COMPOSITING]
Defines the compositing and blending of overlaid content and introduces features to control their modes.
CSS Easing Functions Level 1 [CSS-EASING-1].
Describes a way for authors to define a transformation that controls the rate of change of some value. Applied to animations, such transformations can be used to produce animations that mimic physical phenomena such as momentum or to cause the animation to move in discrete steps producing robot-like movement.
CSS Counter Styles Level 3 [CSS-COUNTER-STYLES-3]
Introduces the @counter-style rule, which allows authors to define their own custom counter styles for use with CSS list-marker and generated-content counters [CSS-LISTS-3]. It also predefines a set of common counter styles, including the ones present in CSS2 and CSS2.1.

NOTE: Although we don’t anticipate significant changes to the specifications that form this snapshot, their inclusion does not mean they are frozen. The Working Group will continue to address problems as they are found in these specs. Implementers should monitor www-style and/or the CSS Working Group Blog for any resulting changes, corrections, or clarifications.

2.2. Reliable Candidate Recommendations

The following specifications are considered to be in a reliable state, meaning they have largely stable implementations and specifications, but are not yet at the Recommendation level due to minor issues or the need for additional implementation reports.

Media Queries Level 4 [MEDIAQUERIES-4]
Extends and supersedes [CSS3-MEDIAQUERIES], expanding the syntax, deprecating most media types, and introducing new media features.
CSS Scroll Snap Module Level 1 [CSS-SCROLL-SNAP-1]
Contains features to control panning and scrolling behavior with “snap positions”.
CSS Scrollbars Styling Module Level 1 [CSS-SCROLLBARS-1]
Defines properties to influence the visual styling of scrollbars, introducing controls for their color and width.
CSS Grid Layout Module Level 1 [CSS-GRID-1]
Introduces a two-dimensional grid-based layout system, optimized for user interface design. In the grid layout model, the children of a grid container can be positioned into arbitrary slots in a predefined flexible or fixed-size layout grid.
CSS Grid Layout Module Level 2 [CSS-GRID-2]
Extends and supersedes [CSS-GRID-1], introducing “subgrids” for managing nested markup in a shared grid framework.
CSS Cascading and Inheritance Module Level 5 [CSS-CASCADE-5]
Extends and supersedes [CSS-CASCADE-4], introducing cascade layers which provide a structured way to organize and balance concerns within a single origin.
CSS Color Adjustment Module Level 1 [CSS-COLOR-ADJUST-1]
This module introduces a model and controls over automatic color adjustment by the user agent to handle user preferences and device output optimizations.
CSS Conditional Rules Module Level 4 [CSS-CONDITIONAL-4]
Extends [CSS-CONDITIONAL-3] to allow testing for supported selectors.
2.3. Fairly Stable Modules with limited implementation experience

The following modules have completed design work, and are fairly stable, but have not received much testing and implementation experience yet. We hope to incorporate them into the official definition of CSS in a future snapshot.

CSS Display Module Level 3 [CSS-DISPLAY-3]
Replaces CSS2§9.1.2, §9.2.1 (but not §9.2.1.1), §9.2.2 (but not §9.2.2.1), §9.2.3, and §9.2.4 (and lays the foundations for replacing §9.7), defining how the CSS formatting box tree is generated from the document element tree and defining the display property that controls it.
CSS Writing Modes Level 4 [CSS-WRITING-MODES-4]
Extends and supersedes [CSS-WRITING-MODES-3], adding more options for vertical writing.
CSS Fragmentation Module Level 3 [CSS-BREAK-3]
Describes the fragmentation model that partitions a flow into pages, columns, or regions and defines properties that control it. Extends and supersedes CSS2§13.3.
CSS Box Alignment Module Level 3 [CSS-ALIGN-3]
Introduces properties to control the alignment of boxes within their containers in the various CSS box layout models: block layout, table layout, flex layout, and grid layout.
CSS Shapes Module Level 1 [CSS-SHAPES-1]
Extends floats (CSS2§9.5) to effect non-rectangular wrapping shapes.
CSS Text Module Level 3 [CSS-TEXT-3]
Extends and supersedes CSS2§16 excepting §16.3, defining properties for text manipulation and specifying their processing model. It covers line breaking, justification and alignment, white space handling, and text transformation.
CSS Text Decoration Module Level 3 [CSS-TEXT-DECOR-3]
Extends and supersedes CSS2§16.3, providing more control over text decoration lines and adding the ability to specify text emphasis marks and text shadows.
CSS Masking Module Level 1 [CSS-MASKING-1]
Replaces CSS2§11.1.2 and introduces more powerful ways of clipping and masking content.
CSS Speech Module Level 1 [CSS-SPEECH-1]
Replaces CSS2§A, overhauling the (non-normative) speech rendering chapter.
CSS View Transitions Module Level 1 [CSS-VIEW-TRANSITIONS-1]
Defines the View Transition API, along with associated properties and pseudo-elements, which allows developers to create animated visual transitions representing changes in the document state.
2.4. Modules with Rough Interoperability

Although the following modules have been widely deployed with rough interoperability, their details are not fully worked out or sufficiently well-specified and they need more testing and bugfixing. We hope to incorporate them into the official definition of CSS in a future snapshot.

CSS Transitions [CSS-TRANSITIONS-1] and CSS Animations Level 1 [CSS-ANIMATIONS-1].
Introduces mechanisms for transitioning the computed values of CSS properties over time.
CSS Will Change Module Level 1 [CSS-WILL-CHANGE-1]
Introduces a performance hint property called will-change.
Filter Effects Module Level 1 [FILTER-EFFECTS-1]
Introduces filter effects as a way of processing an element’s rendering before it is displayed in the document.
CSS Font Loading Module Level 3 [CSS-FONT-LOADING-3]
Introduces events and interfaces used for dynamically loading font resources.
CSS Box Sizing Module Level 3 [CSS-SIZING-3]
Overlays and extends CSS§10., expanding the value set of the sizing properties, introducing more precise sizing terminology, and defining with more precision and detail various automatic sizing concepts only vaguely defined in CSS2.
CSS Transforms Module Level 2 [CSS-TRANSFORMS-2]
Builds upon [CSS-TRANSFORMS-1] to add new transform functions and properties for three-dimensional transforms, and convenience functions for simple transforms.
CSS Lists and Counters Module Level 3 [CSS-LISTS-3]
Contains CSS features related to list counters: styling them, positioning them, and manipulating their value.
CSS Logical Properties and Values Level 1 [CSS-LOGICAL-1]
Introduces logical properties and values that provide the author with the ability to control layout through logical, rather than physical, direction and dimension mappings. Also defines logical properties and values for the features defined in [CSS2]. These properties are writing-mode relative equivalents of their corresponding physical properties.
CSS Positioned Layout Module Level 3 [CSS-POSITION-3]
Contains defines coordinate-based positioning and offsetting schemes of CSS: relative positioning, sticky positioning, absolute positioning, and fixed positioning.
Resize Observer [RESIZE-OBSERVER-1]
This specification describes an API for observing changes to element’s principal box’s size.
Web Animations [WEB-ANIMATIONS-1]
Defines a model for synchronization and timing of changes to the presentation of a Web page. Also defines an application programming interface for interacting with this model.
CSS Fonts Module Level 4 [CSS-FONTS-4]
Extends and supersedes CSS Fonts 3 and provides more control over font choice and feature selection, including support for OpenType variations.
Motion Path Module Level 1 [MOTION-1]
This module allows authors to position any graphical object and animate it along an author specified path.
CSS Scroll Anchoring Module Level 1 [CSS-SCROLL-ANCHORING-1]
This module aims to minimize content shifts by locking the scroll position of a scroll container to a particular anchor element.
CSS Object Model (CSSOM) [CSSOM-1]
This module defines APIs for parsing, serializing, and manipulating CSS, Media Queries, and Selectors.
CSS Color Module Level 5 [CSS-COLOR-5]
Extends CSS Color 4 to add color spaces and color modification functions.
Selectors Level 4 [SELECTORS-4]
Extends Selectors Level 3 by introducing new pseudo-classes, pseudo-elements, and combinators, enhancing the ability to select elements based on more complex criteria and states.
CSS Containment Module Level 2 [CSS-CONTAIN-2]
Extends CSS Containment 1 to add style containment.
CSSOM View Module [CSSOM-VIEW-1]
This module defines APIs for querying and manipulating the visual viewport and layout viewport, as well as methods for scrolling elements into view.
Geometry Interfaces Module Level 1 [GEOMETRY-1]
This module defines basic basic geometric interfaces to represent points, rectangles, quadrilaterals, and transformation matrices.
CSS Nesting Module Level 1 [CSS-NESTING-1]
This module introduces the ability to nest one style rule inside another, with the selector of the child rule relative to the selector of the parent rule. This increases the modularity and maintainability of CSS stylesheets.
2.5. CSS Levels

Cascading Style Sheets does not have versions in the traditional sense; instead it has levels. Each level of CSS builds on the previous, refining definitions and adding features. The feature set of each higher level is a superset of any lower level, and the behavior allowed for a given feature in a higher level is a subset of that allowed in the lower levels. A user agent conforming to a higher level of CSS is thus also conformant to all lower levels.

CSS Level 1
The CSS Working Group considers the CSS1 specification to be obsolete. CSS Level 1 is defined as all the features defined in the CSS1 specification (properties, values, at-rules, etc), but using the syntax and definitions in the CSS2.1 specification. CSS Style Attributes defines its inclusion in element-specific style attributes.
CSS Level 2
Although the CSS2 specification is technically a W3C Recommendation, it passed into the Recommendation stage before the W3C had defined the Candidate Recommendation stage. Over time implementation experience and further review has brought to light many problems in the CSS2 specification, so instead of expanding an already unwieldy errata list, the CSS Working Group chose to define CSS Level 2 Revision 1 (CSS2.1). In case of any conflict between the two specs CSS2.1 contains the definitive definition.

Once CSS2.1 became Candidate Recommendation—effectively though not officially the same level of stability as CSS2—obsoleted the CSS2 Recommendation. Features in CSS2 that were dropped from CSS2.1 should be considered to be at the Candidate Recommendation stage, but note that many of these have been or will be pulled into a CSS Level 3 working draft, in which case that specification will, once it reaches CR, obsolete the definitions in CSS2.

The CSS2.1 specification defines CSS Level 2 and the CSS Style Attributes specification defines its inclusion in element-specific style attributes.

CSS Level 3
CSS Level 3 builds on CSS Level 2 module by module, using the CSS2.1 specification as its core. Each module adds functionality and/or replaces part of the CSS2.1 specification. The CSS Working Group intends that the new CSS modules will not contradict the CSS2.1 specification: only that they will add functionality and refine definitions. As each module is completed, it will be plugged in to the existing system of CSS2.1 plus previously-completed modules.

From this level on modules are levelled independently: for example Selectors Level 4 may well be completed before CSS Line Module Level 3. Modules with no CSS Level 2 equivalent start at Level 1; modules that update features that existed in CSS Level 2 start at Level 3.

CSS Level 4 and beyond
There is no CSS Level 4. Independent modules can reach level 4 or beyond, but CSS the language no longer has levels. ("CSS Level 3" as a term is used only to differentiate it from the previous monolithic versions.)
2.6. CSS Profiles

Not all implementations will implement all functionality defined in CSS.

In the past, the Working Group published a few Profiles, which were meant to define the minimal subset of CSS that various classes of user agents were expected to support.

This effort has been discontinued, as the Working Group was not finding it effective or useful, and the profiles previously defined are now unmaintained.

NOTE: Partial implementations of CSS, even if that subset is an official profile, must follow the forward-compatible parsing rules for partial implementations.

3. Requirements for Responsible Implementation of CSS

The following sections define several conformance requirements for implementing CSS responsibly, in a way that promotes interoperability in the present and future.

3.1. Partial Implementations

So that authors can exploit the forward-compatible parsing rules to assign fallback values, CSS renderers must treat as invalid (and ignore as appropriate) any at-rules, properties, property values, keywords, and other syntactic constructs for which they have no usable level of support. In particular, user agents must not selectively ignore unsupported property values and honor supported values in a single multi-value property declaration: if any value is considered invalid (as unsupported values must be), CSS requires that the entire declaration be ignored.

3.2. Implementations of Unstable and Proprietary Features

To avoid clashes with future stable CSS features, the CSSWG recommends the following best practices for the implementation of unstable features and proprietary extensions to CSS:

3.2.1. Experimentation and Unstable Features

Implementations of unstable features that are described in W3C specifications but are not interoperable should not be released broadly for general use; but may be released for limited, experimental use in controlled environments.

Why?
For example, a UA could release an unstable features for experimentation through beta or other testing-stage builds; behind a hidden configuration flag; behind a switch enabled only for specific testing partners; or through some other means of limiting dependent use.

A CSS feature is considered unstable until its specification has reached the Candidate Recommendation (CR) stage in the W3C process. In exceptional cases, the CSSWG may additionally, by an officially-recorded resolution, add pre-CR features to the set that are considered safe to release for broad use. See § 4 Safe to Release pre-CR Exceptions.

NOTE: Vendors should consult the WG explicitly and not make assumptions on this point, as a pre-CR spec that hasn’t changed in awhile is usually more out-of-date than stable.

3.2.2. Proprietary and Non-standardized Features

To avoid clashes with future CSS features, the CSS2.1 specification reserves a prefixed syntax [CSS2] for proprietary and experimental extensions to CSS. A CSS feature is a proprietary extension if it is meant for use in a closed environment accessible only to a single vendor’s user agent(s). A UA should support such proprietary extensions only through a vendor-prefixed syntax and not expose them to open (multi-UA) environments such as the World Wide Web.

Why?
For example, Firefox’s XUL-based UI, Apple’s iTunes UI, and Microsoft’s Universal Windows Platform app use extensions to CSS implemented by their respective UAs. So long as these UAs do not allow Web content to access these features, they do not provide an opportunity for such content to become dependent on their proprietary extensions.

Even if a feature is intended to eventually be used in the Web, if it hasn’t yet been standardized it should still not be exposed to the Web.

3.2.3. Market Pressure and De Facto Standards

If a feature is unstable (i.e. the spec has not yet stabilized), but

at least three UAs implement the feature (or a UA has broken the other rules and shipped for broad use an unstable or otherwise non-standard feature in a production release),

and the implementations have rough interoperability,

and the CSS Working Group has recorded consensus that this feature should exist and be released,

implementers may ship that feature unprefixed in broad-release builds. Rough interoperability is satisfied by a subjective judgment that even though there may be differences, the implementations are sufficiently similar to be used in production websites for a substantial number of use cases.

Note that the CSSWG must still be consulted to ensure coordination across vendors and to ensure coherency review by the CSS experts from each vendor. Note also that rough interoperability still usually means painful lack of interop in edge (or not-so-edge) cases, particularly because details have not been ironed out through the standards review process.

Why?
3.2.3.1. Vendor-prefixing Unstable Features

When exposing such a standards-track unstable feature to the Web in a production release, implementations should support both vendor-prefixed and unprefixed syntaxes for the feature. Once the feature has stabilized and the implementation is updated to match interoperable behavior, support for the vendor-prefixed syntax should be removed.

Why?

Anyone promoting unstable features to authors should document them using their standard unprefixed syntax, and avoid encouraging the use of the vendor-prefixed syntax for any purpose other than working around implementation differences.
