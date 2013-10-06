Title: ElementTree accessor
Slug: elementtree-accessor
Date: 2009-05-08 12:09
Tags: python, snippet
Category: texts
Lang: en
Description: Simple element tree accessor with examples of code.

As you know, ElementTree's interface is boring and most time you don't need all these *findalls* and *attribs*. 80% of code requires simple operation like: "access to child B and get it's attribute C". So, why to type `root.find('B').attrib['C']`, when you can use simple construction like `root.B.C`? To accomplish this task, I [wrote a simple wrapper][et-accessor] for ElementTree.

    :::python
    #########################################################
    # Title: Simple ElementTree accessor
    # Author: Alexander Artemenko <svetlyak.40wt@gmail.com>
    # Site: http://aartemenko.com
    # License: New BSD License
    #########################################################

    class Accessor(object):
        """Easy to use ElementTree accessor."""

        def __init__(self, xml):
            self.xml = xml

        def __repr__(self):
            return '<Element %s>' % self.xml.tag

        def __len__(self):
            return self.xml.__len__()

        def __iter__(self):
            return iter(self.xml)

        def __getattribute__(self, name):
            """
            >>> from xml.etree import ElementTree as ET
            >>> xml = ET.fromstring('<a b="blah"><c id="1"/><c id="2"><d>Hello</d></c></a>')
            >>> a = Accessor(xml)
            >>> a.b
            'blah'
            >>> a.c
            [<Element c>, <Element c>]
            >>> a.c[1].d
            <Element d>
            >>> a.c[1].d.text
            'Hello'
            >>> ET.tostring(a)
            '<a b="blah"><c id="1" /><c id="2"><d>Hello</d></c></a>'
            """
            if name == 'xml':
                return object.__getattribute__(self, name)

            elements = self.xml.findall(name)
            l = len(elements)
            if l == 1:
                return Accessor(elements[0])
            elif l > 1:
                return map(Accessor, elements)

            if self.xml.attrib.has_key(name):
                return self.xml.attrib[name]

            if hasattr(self.xml, name):
                return getattr(self.xml, name)
            raise AttributeError


Look at the examples and run doctests.

[et-accessor]: http://gist.github.com/108704