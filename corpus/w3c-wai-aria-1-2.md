↑
←

Accessible Rich Internet Applications (WAI-ARIA) 1.2

W3C Recommendation 06 June 2023

More details about this document
This version:
https://www.w3.org/TR/2023/REC-wai-aria-1.2-20230606/
Latest published version:
https://www.w3.org/TR/wai-aria-1.2/
Latest editor's draft:
https://w3c.github.io/aria/
History:
https://www.w3.org/standards/history/wai-aria-1.2
Commit history
Implementation report:
https://w3c.github.io/test-results/core-aam-1.2/
Previous Recommendation:
https://www.w3.org/TR/wai-aria-1.1/
Editors:
Joanmarie Diggs (Igalia, S.L.)
James Nurthen (Adobe)
Michael Cooper (W3C)
Carolyn MacLeod (IBM)
Former editors:
Shane McCarron (Spec-Ops) (Editor until 2018)
Richard Schwerdtfeger (Knowbility) (Editor until October 2017)
James Craig (Apple Inc.) (Editor until May 2016)
Feedback:
GitHub w3c/aria (pull requests, new issue, open issues)
Errata:
Errata exists.

See also translations.

Copyright © 2013-2023 World Wide Web Consortium. W3C® liability, trademark and permissive document license rules apply.

Abstract

Accessibility of web content requires semantic information about widgets, structures, and behaviors, in order to allow assistive technologies to convey appropriate information to persons with disabilities. This specification provides an ontology of roles, states, and properties that define accessible user interface elements and can be used to improve the accessibility and interoperability of web content and applications. These semantics are designed to allow an author to properly convey user interface behaviors and structural information to assistive technologies in document-level markup. This version adds features new since WAI-ARIA 1.1 [wai-aria-1.1] to improve interoperability with assistive technologies to form a more consistent accessibility model for [HTML] and [SVG2]. This specification complements both [HTML] and [SVG2].

This document is part of the WAI-ARIA suite described in the WAI-ARIA Overview.

Status of This Document

This section describes the status of this document at the time of its publication. A list of current W3C publications and the latest revision of this technical report can be found in the W3C technical reports index at https://www.w3.org/TR/.

WAI-ARIA 1.2 is a W3C Recommendation. The Advisory Committee (AC) as well as the W3C Director have endorsed this specification to become a W3C Recommendation. For details about implementation experience, see the WAI-ARIA 1.2 Implementation Report. A history of changes to WAI-ARIA 1.2 is available in the appendix.

This document was published by the Accessible Rich Internet Applications Working Group as a Recommendation using the Recommendation track.

W3C recommends the wide deployment of this specification as a standard for the Web.

A W3C Recommendation is a specification that, after extensive consensus-building, is endorsed by W3C and its Members, and has commitments from Working Group members to royalty-free licensing for implementations.

This document was produced by a group operating under the W3C Patent Policy. W3C maintains a public list of any patent disclosures made in connection with the deliverables of the group; that page also includes instructions for disclosing a patent. An individual who has actual knowledge of a patent which the individual believes contains Essential Claim(s) must disclose the information in accordance with section 6 of the W3C Patent Policy.

This document is governed by the 2 November 2021 W3C Process Document.

table of contents
Abstract
Status of This Document
1.
Introduction
1.1
Rich Internet Application Accessibility
1.2
Target Audience
1.3
User Agent Support
1.4
Co-Evolution of WAI-ARIA and Host Languages
1.5
Authoring Practices
1.5.1
Authoring Tools
1.5.2
Testing Practices and Tools
1.6
Assistive Technologies
2.
Important Terms
3.
Conformance
3.1
Non-interference with the Host Language
3.2
All WAI-ARIA in DOM
3.3
Assistive Technology Notifications Communicated to Web Applications
3.4
Conformance Checkers
3.5
Deprecated Requirements
4.
Using WAI-ARIA
4.1
WAI-ARIA Roles
4.2
WAI-ARIA States and Properties
4.3
Managing Focus and Supporting Keyboard Navigation
4.3.1
Information for Authors
4.3.2
Information for User Agents
5.
The Roles Model
5.1
Relationships Between Concepts
5.1.1
Superclass Role
5.1.2
Subclass Roles
5.1.3
Related Concepts
5.1.4
Base Concept
5.2
Characteristics of Roles
5.2.1
Abstract Roles
5.2.2
Required States and Properties
5.2.3
Supported States and Properties
5.2.4
Inherited States and Properties
5.2.5
Prohibited States and Properties
5.2.6
Required Owned Elements
5.2.7
Required Context Role
5.2.8
Accessible Name Calculation
5.2.8.1
Name Computation
5.2.8.2
Description Computation
5.2.8.3
Accessible Name and Description Computation
5.2.8.4
Roles Supporting Name from Author
5.2.8.5
Roles Supporting Name from Content
5.2.8.6
Roles which cannot be named (Name prohibited)
5.2.9
Presentational Children
5.2.10
Implicit Value for Role
5.3
Categorization of Roles
5.3.1
Abstract Roles
5.3.2
Widget Roles
5.3.3
Document Structure Roles
5.3.4
Landmark Roles
5.3.5
Live Region Roles
5.3.6
Window Roles
5.4
Definition of Roles
6.
Supported States and Properties
6.1
Clarification of States versus Properties
6.2
Characteristics of States and Properties
6.2.1
Related Concepts
6.2.2
Used in Roles
6.2.3
Inherits into Roles
6.2.4
Value
6.3
ARIA Attributes
6.3.1
Multi-value Attribute Values
6.3.2
IDL reflection of ARIA attributes
6.3.3
Operating System Accessibility API mapping of multi-value ARIA attributes
6.3.4
ARIA nullable DOMString Attributes
6.3.4.1
Example Attribute Usage
6.4
Translatable States and Properties
6.5
Global States and Properties
6.6
Taxonomy of WAI-ARIA States and Properties
6.6.1
Widget Attributes
6.6.2
Live Region Attributes
6.6.3
Drag-and-Drop Attributes
6.6.4
Relationship Attributes
6.7
Definitions of States and Properties (all aria-* attributes)
7.
Accessibility Tree
7.1
Excluding Elements from the Accessibility Tree
7.2
Including Elements in the Accessibility Tree
8.
Implementation in Host Languages
8.1
Role Attribute
8.2
State and Property Attributes
8.3
Focus Navigation
8.4
Implicit WAI-ARIA Semantics
8.5
Conflicts with Host Language Semantics
8.6
State and Property Attribute Processing
8.6.1
ID Reference Error Processing
8.7
CSS Selectors
9.
Handling Author Errors
9.1
Roles
9.2
States and Properties
10.
IDL Interface
10.1
Interface Mixin ARIAMixin
10.2
ARIA Attribute Correspondence
10.2.1
Disambiguation Pattern
10.2.2
IDL Attribute Name Notes or Exceptions
10.3
ARIAMixin Mixed in to Element
10.4
Example IDL Attribute Usage
11.
Privacy and Security Considerations
A.
Mapping WAI-ARIA Value types to languages
B.
Substantive changes since the WAI-ARIA 1.1 Recommendation
C.
Acknowledgments
C.1
Participants active in the ARIA WG at the time of publication
C.2
Other ARIA contributors, commenters, and previously active participants
C.3
Enabling funders
D.
References
D.1
Normative references
D.2
Informative references
Dedication

This version of the ARIA specification is dedicated to the memory of Carolyn MacLeod whose contributions are found throughout this document. She graced our work with equanimity and sagacity, and her untimely passing will long be missed by our community.

1. Introduction

This section is non-normative.

The goals of this specification include:

expanding the accessibility information that may be supplied by the author;
requiring that supporting host languages provide full keyboard support that may be implemented in a device-independent way, for example, by telephones, handheld devices, e-book readers, and televisions;
improving the accessibility of dynamic content generated by scripts; and
providing for interoperability with assistive technologies.

WAI-ARIA is a technical specification that provides a framework to improve the accessibility and interoperability of web content and applications. This document is primarily for developers creating custom widgets and other web application components. Please see the WAI-ARIA Overview for links to related documents for other audiences, such as WAI-ARIA Authoring Practices [WAI-ARIA-PRACTICES-1.2] that introduces developers to the accessibility problems that WAI-ARIA is intended to solve, the fundamental concepts, and the technical approach of WAI-ARIA.

This document currently handles two aspects of roles: user interface functionality and structural relationships. For more information and use cases, see WAI-ARIA Authoring Practices [WAI-ARIA-PRACTICES-1.2] for the use of roles in making interactive content accessible.

Roles defined by this specification are designed to support the roles used by platform accessibility APIs. Declaration of these roles on elements within dynamic web content is intended to support interoperability between the web content and assistive technologies that utilize accessibility APIs.

The schema to support this standard has been designed to be extensible so that custom roles can be created by extending base roles. This allows user agents to support at least the base role, and user agents that support the custom role can provide enhanced access. Note that much of this could be formalized in [XMLSCHEMA11-2]. However, being able to define similarities between roles, such as baseConcepts and more descriptive definitions, would not be available in XSD.

WAI-ARIA 1.2 is a member of the WAI-ARIA 1.2 suite that defines how to expose semantics of WAI-ARIA and other web content languages to accessibility APIs.

1.1 Rich Internet Application Accessibility

The domain of web accessibility defines how to make web content usable by persons with disabilities. Persons with certain types of disabilities use assistive technologies (AT) to interact with content. Assistive technologies can transform the presentation of content into a format more suitable to the user, and can allow the user to interact in different ways. For example, the user may need to, or choose to, interact with a slider widget via arrow keys, instead of dragging and dropping with a mouse. In order to accomplish this effectively, the software needs to understand the semantics of the content. Semantics is the science of meaning; in this case, used to assign roles, states, and properties that apply to user interface and content elements as a human would understand. For instance, if a paragraph is semantically identified as such, assistive technologies can interact with it as a unit separable from the rest of the content, knowing the exact boundaries of that paragraph. An adjustable range slider or collapsible list (a.k.a. a tree widget) are more complex examples, in which various parts of the widget have semantics that need to be properly identified for assistive technologies to support effective interaction.

New technologies often overlook semantics required for accessibility, and new authoring practices often misuse the intended semantics of those technologies. Elements that have one defined meaning in the language are used with a different meaning intended to be understood by the user.

For example, web application developers create collapsible tree widgets in HTML using CSS and JavaScript even though HTML has no semantic tree element. To a non-disabled user, it may look and act like a collapsible tree widget, but without appropriate semantics, the tree widget may not be perceivable to, or operable by, a person with a disability because assistive technologies may not recognize the role. Similarly, web application developers create interactive button widgets in SVG using JavaScript even though SVG has no semantic button element. To a non-disabled user, it may look and act like a button widget, but without appropriate semantics, the button widget may not be perceivable to, or operable by, a person with a disability because assistive technologies may not recognize the role.

The incorporation of WAI-ARIA is a way for an author to provide proper semantics for custom widgets to make these widgets accessible, usable, and interoperable with assistive technologies. This specification identifies the types of widgets and structures that are commonly recognized by accessibility products, by providing an ontology of corresponding roles that can be attached to content. This allows elements with a given role to be understood as a particular widget or structural type regardless of any semantics inherited from the implementing host language. Roles are a common property of platform accessibility APIs which assistive technologies use to provide the user with effective presentation and interaction.

The Roles Model includes interaction widgets and elements denoting document structure. The Roles Model describes inheritance and details the attributes each role supports. Information about mapping of roles to accessibility APIs is provided by the Core Accessibility API Mappings [CORE-AAM-1.2].

Roles are element types and will not change with time or user actions. Role information is used by assistive technologies, through interaction with the user agent, to provide normal processing of the specified element type.

States and properties are used to declare important attributes of an element that affect and describe interaction. They enable the user agent and operating system to properly handle the element even when the attributes are dynamically changed by client-side scripts. For example, alternative input and output technology, such as screen readers and speech dictation software, need to be able to recognize and effectively manipulate and communicate various interaction states (e.g., disabled, checked) to the user.

While it is possible for assistive technologies to access these properties directly through the Document Object Model [DOM], the preferred mechanism is for the user agent to map the states and properties to the accessibility API of the operating system. See the Core Accessibility API Mappings [CORE-AAM-1.2] and the Accessible Name and Description Computation [ACCNAME-1.2] for details.

Figure 1.0 illustrates the relationship between user agents (e.g., browsers), accessibility APIs, and assistive technologies. It describes the "contract" provided by the user agent to assistive technologies, which includes typical accessibility information found in the accessibility API for many of our accessible platforms for GUIs (role, state, selection, event notification, relationship information, and descriptions). The DOM, usually HTML, acts as the data model and view in a typical model-view-controller relationship, and JavaScript acts as the controller by manipulating the style and content of the displayed data. The user agent conveys relevant information to the operating system's accessibility API, which can be used by any assistive technologies, such as screen readers.

Figure 1: The contract model with accessibility APIs

For more information see WAI-ARIA Authoring Practices for the use of roles in making interactive content accessible.

Users of alternate input devices need keyboard accessible content. The new semantics, when combined with the recommended keyboard interactions provided in WAI-ARIA Authoring Practices, will allow alternate input solutions to facilitate command and control via an alternate input solution.

WAI-ARIA introduces navigational landmarks through its Roles Model and the XHTML role landmarks, which can help persons with dexterity and vision impairments by providing for improved keyboard navigation. WAI-ARIA may also be used to assist persons with cognitive learning disabilities. The additional semantics allow authors to restructure and substitute alternative content as needed.

Assistive technologies need the ability to support alternative inputs by getting and setting the current value of widget states and properties. Assistive technologies also need to determine what objects are selected and manage widgets that allow multiple selections, such as list boxes and grids.

Speech-based command and control systems can benefit from WAI-ARIA semantics like the role attribute to assist in conveying audio information to the user. For example, upon encountering an element with a role of menu with child elements of role menuitem each containing text content representing a different flavor, a speech system might state to the user, "Select one of three choices: chocolate, strawberry, or vanilla."

WAI-ARIA is intended to be used as a supplement for native language semantics, not a replacement. When the host language provides a feature that provides equivalent accessibility to the WAI-ARIA feature, use the host language feature. WAI-ARIA should only be used in cases where the host language lacks the needed role, state, and property indicators. Use a host language feature that is as similar as possible to the WAI-ARIA feature, then refine the meaning by adding WAI-ARIA. For instance, a multi-selectable grid could be implemented as a table, and then WAI-ARIA used to clarify that it is an interactive grid, not just a static data table. This allows for the best possible fallback for user agents that do not support WAI-ARIA and preserves the integrity of the host language semantics.

1.2 Target Audience

This specification defines the basic model for WAI-ARIA, including roles, states, properties, and values. It impacts several audiences:

User agents that process content containing WAI-ARIA features;
Assistive technologies that present content in special ways to user with disabilities;
Authors who create content;
Authoring tools that help authors create conforming content; and
Conformance checkers that verify appropriate use of WAI-ARIA.

Each conformance requirement indicates the audience to which it applies.

Although this specification is applicable to the above audiences, it is not specifically targeted to, nor is it intended to be the sole source of information for, any of these audiences. The following documents provide important supporting information:

[WAI-ARIA-PRACTICES-1.2] addresses authoring recommendations for HTML, and is also of interest to developers of authoring tools and conformance checkers.
[CORE-AAM-1.2] addresses developers of user agents and assistive technologies.
[ACCNAME-1.2] also addresses developers of user agents and assistive technologies.
1.3 User Agent Support

WAI-ARIA relies on user agent support for its features in two ways:

Mainstream user agents use WAI-ARIA to alter how host language features are exposed to accessibility APIs in order to improve accessibility. The mechanism for this is defined in the Core Accessibility API Mappings.
Assistive technologies use the enhanced information available in an accessibility API, or uses the WAI-ARIA markup directly via the DOM, to convey semantic and interaction information to the user.

Aside from using WAI-ARIA markup to improve what is exposed to accessibility APIs, user agents behave as they would natively. Assistive technologies react to the extra information in the accessibility API as they already do for the same information on non-web content. User agents that are not assistive technologies, however, need do nothing beyond providing appropriate updates to the accessibility API.

The WAI-ARIA specification neither requires nor forbids user agents from enhancing native presentation and interaction behaviors on the basis of WAI-ARIA markup. Mainstream user agents might expose WAI-ARIA navigational landmarks (for example, as a dialog box or through a keyboard command) with the intention to facilitate navigation for all users. User agents are encouraged to maximize their usefulness to users, including users without disabilities.

WAI-ARIA is intended to provide missing semantics so that the intent of the author may be conveyed to assistive technologies. Generally, authors using WAI-ARIA will provide the appropriate presentation and interaction features. Over time, host languages may add WAI-ARIA equivalents, such as new form controls, that are implemented as standard accessible user interface controls by the user agent. This allows authors to use them instead of custom WAI-ARIA enabled user interface components. In this case the user agent would support the native host language feature. Developers of host languages that implement WAI-ARIA are advised to continue supporting WAI-ARIA semantics when they do not adversely conflict with implicit host language semantics, as WAI-ARIA semantics more clearly reflect the intent of the author if the host language features are inadequate to meet the author's needs.

1.4 Co-Evolution of WAI-ARIA and Host Languages

WAI-ARIA is intended to augment semantics in supporting languages like [HTML] and [SVG2], or to be used as an accessibility enhancement technology in other markup-based languages that do not explicitly include support for ARIA. It clarifies semantics to assistive technologies when authors create new types of objects, via style and script, that are not yet directly supported by the language of the page, because the invention of new types of objects is faster than standardized support for them appears in web languages.

It is not appropriate to create objects with style and script when the host language provides a semantic element for that type of object. While WAI-ARIA can improve the accessibility of these objects, accessibility is best provided by allowing the user agent to handle the object natively. For example, it's better to use an h1 element in HTML than to use the heading role on a div element.

It is expected that, over time, host languages will evolve to provide semantics for objects that currently can only be declared with WAI-ARIA. This is natural and desirable, as one goal of WAI-ARIA is to help stimulate the emergence of more semantic and accessible markup. When native semantics for a given feature become available, it is appropriate for authors to use the native feature and stop using WAI-ARIA for that feature. Legacy content may continue to use WAI-ARIA, however, so the need for user agents to support WAI-ARIA remains.

While specific features of WAI-ARIA may lose importance over time, the general possibility of WAI-ARIA to add semantics to web pages is expected to be a persistent need. Host languages may not implement all the semantics WAI-ARIA provides, and various host languages may implement different subsets of the features. New types of objects are continually being developed, and one goal of WAI-ARIA is to provide a way to make such objects accessible, because web authoring practices often advance faster than host language standards. In this way, WAI-ARIA and host languages both evolve together but at different rates.

Some host languages exist to create semantics for features other than the user interface. For example, SVG expresses the semantics behind production of graphical objects, not of user interface components that those objects may represent. Host languages might, by design, not provide native semantics that map to WAI-ARIA features. In these cases, WAI-ARIA could be adopted as a long-term approach to add semantic information to user interface components.

1.5 Authoring Practices
1.5.1 Authoring Tools

Many of the requirements in the definitions of WAI-ARIA roles, states, and properties can be checked automatically during the development process, similar to other quality control processes used for validating code. To assist authors who are creating custom widgets, authoring tools may compare widget roles, states, and properties to those supported in WAI-ARIA as well as those supported in related and cross-referenced roles, states, and properties. Authoring tools may notify authors of errors in widget design patterns, and may also prompt developers for information that cannot be determined from context alone. For example, a scripting library can determine the labels for the tree items in a tree view, but would need to prompt the author to label the entire tree. To help authors visualize a logical accessibility structure, an authoring environment might provide an outline view of a web resource based on the WAI-ARIA markup.

In both HTML and SVG, tabindex is an important way browsers support keyboard focus navigation for implementations of WAI-ARIA; authoring and debugging tools may check to make sure tabindex values are properly set. For example, error conditions may include cases where more than one treeitem in a tree has a tabindex value greater than or equal to 0, where tabindex is not set on any treeitem, or where aria-activedescendant is not defined when the element with the role tree has a tabindex value of greater than or equal to 0.

1.5.2 Testing Practices and Tools

The accessibility of interactive content cannot be confirmed by static checks alone. Developers of interactive content should test for device-independent access to widgets and applications, and should verify accessibility API access to all content and changes during user interaction.

1.6 Assistive Technologies

Programmatic access to accessibility semantics is essential for assistive technologies. Most assistive technologies interact with user agents, like other applications, through a recognized accessibility API. Perceivable objects in the user interface are exposed to assistive technologies as accessible objects, defined by the accessibility API interfaces. To do this properly, accessibility information – role, states, properties as well as contextual information – needs to be accurately conveyed to the assistive technologies through the accessibility API. When a state change occurs, the user agent provides the appropriate event notification to the accessibility API. Contextual information, in many host languages like HTML, can be determined from the DOM itself as it provides a contextual tree hierarchy.

While some assistive technologies interact with these accessibility APIs, others may access the content directly from the DOM. These technologies can restructure, simplify, style, or reflow the content to help a different set of users. Common use cases for these types of adaptations may be the aging population, persons with cognitive impairments, or persons in environments that interfere with use of their tools. For example, the availability of regional navigational landmarks may allow for a mobile device adaptation that shows only portions of the content at any one time based on its semantics. This could reduce the amount of information the user needs to process at any one time. In other situations it may be appropriate to replace a custom user interface control with something that is easier to navigate with a keyboard, or touch screen device.

2. Important Terms

This section is non-normative.

While some terms are defined in place, the following definitions are used throughout this document.

Accessibility API

Operating systems and other platforms provide a set of interfaces that expose information about objects and events to assistive technologies. Assistive technologies use these interfaces to get information about and interact with those widgets. Examples of accessibility APIs are Microsoft Active Accessibility [MSAA], Microsoft User Interface Automation [UI-AUTOMATION], MSAA with UIA Express [UIA-EXPRESS], the Mac OS X Accessibility Protocol [AXAPI], the Linux/Unix Accessibility Toolkit [ATK] and Assistive Technology Service Provider Interface [AT-SPI], and IAccessible2 [IAccessible2].

Accessibility Subtree

An accessible object in the accessibility tree and its descendants in that tree. It does not include objects which have relationships other than parent-child in that tree. For example, it does not include objects linked via aria-flowto unless those objects are also descendants in the accessibility tree.

Accessibility Tree

Tree of accessible objects that represents the structure of the user interface (UI). Each node in the accessibility tree represents an element in the UI as exposed through the accessibility API; for example, a push button, a check box, or container.

Accessible Description

An accessible description provides additional information, related to an interface element, that complements the accessible name. The accessible description might or might not be visually perceivable.

Accessible Name

The accessible name is the name of a user interface element. Each platform accessibility API provides the accessible name property. The value of the accessible name may be derived from a visible (e.g., the visible text on a button) or invisible (e.g., the text alternative that describes an icon) property of the user interface element. See related accessible description.

A simple use for the accessible name property may be illustrated by an "OK" button. The text "OK" is the accessible name. When the button receives focus, assistive technologies may concatenate the platform's role description with the accessible name. For example, a screen reader may speak "push-button OK" or "OK button". The order of concatenation and specifics of the role description (e.g., "button", "push-button", "clickable button") are determined by platform accessibility APIs or assistive technologies.

Accessible object

A node in the accessibility tree of a platform accessibility API. Accessible objects expose various states, properties, and events for use by assistive technologies. In the context of markup languages (e.g., HTML and SVG) in general, and of WAI-ARIA in particular, markup elements and their attributes are represented as accessible objects.

Activation behavior

The action taken when an event, typically initiated by users through an input device, causes an element to fulfill a defined role. The role may be defined for that element by the host language, or by author-defined variables, or both. The role for any given element may be a generic action, or may be unique to that element. For example, the activation behavior of an HTML or SVG <a> element shall be to cause the user agent to traverse the link specified in the href attribute, with the further optional parameter of specifying the browsing context for the traversal (such as the current window or tab, a named window, or a new window); the activation behavior of an HTML <input> element with the type attribute value submit shall be to send the values of the form elements to an author-defined IRI by the author-defined HTTP method.

Assistive Technologies

Hardware and/or software that:

relies on services provided by a user agent to retrieve and render Web content
works with a user agent or web content itself through the use of APIs, and
provides services beyond those offered by the user agent to facilitate user interaction with web content by people with disabilities

This definition may differ from that used in other documents.

Examples of assistive technologies that are important in the context of this document include the following:

screen magnifiers, which are used to enlarge and improve the visual readability of rendered text and images;
screen readers, which are most-often used to convey information through synthesized speech or a refreshable Braille display;
text-to-speech software, which is used to convert text into synthetic speech;
speech recognition software, which is used to allow spoken control and dictation;
alternate input technologies (including head pointers, on-screen keyboards, single switches, and sip/puff devices), which are used to simulate the keyboard;
alternate pointing devices, which are used to simulate mouse pointing and clicking.
Attribute

In this specification, attribute is used as it is in markup languages. Attributes are structural features added to elements to provide information about the states and properties of the object represented by the element.

Class

A set of instance objects that share similar characteristics.

Deprecated

A deprecated role, state, or property is one which has been outdated by newer constructs or changed circumstances, and which may be removed in future versions of the WAI-ARIA specification. User agents are encouraged to continue to support items identified as deprecated for backward compatibility. For more information, see Deprecated Requirements in the Conformance section.

Desktop focus event

Event from/to the host operating system via the accessibility API, notifying of a change of input focus.

DOMString
Sequence of 16-bit unsigned integers, typically interpreted as UTF-16 code units. This corresponds to the JavaScript primitive String type.
Element

In this specification, element is used as it is in markup languages. Elements are the structural elements in markup language that contains the data profile for objects.

Event

A programmatic message used to communicate discrete changes in the state of an object to other objects in a computational system. User input to a web page is commonly mediated through abstract events that describe the interaction and can provide notice of changes to the state of a document object. In some programming languages, events are more commonly known as notifications.

Expose

Translated to platform-specific accessibility APIs as defined in the Core Accessibility API Mappings.

Graphical Document

A document containing graphic representations with user-navigable parts. Charts, maps, diagrams, blueprints, and dashboards are examples of graphical documents. A graphical document is composed using any combination of symbols, images, text, and graphic primitives (shapes such as circles, points, lines, paths, rectangles, etc).

Hidden

Indicates that the element is not visible, perceivable, or interactive to any user. An element is considered hidden if it or any one of its ancestor elements is not rendered or is explicitly hidden.

Informative

Content provided for information purposes and not required for conformance. Content required for conformance is referred to as normative.

Keyboard Accessible

Accessible to the user using a keyboard or assistive technologies that mimic keyboard input, such as a sip and puff tube. References in this document relate to WCAG 2.1 Guideline 2.1: Make all functionality available from a keyboard [WCAG21].

Landmark

A type of region on a page to which the user may want quick access. Content in such a region is different from that of other regions on the page and relevant to a specific user purpose, such as navigating, searching, perusing the primary content, etc.

Live Region

