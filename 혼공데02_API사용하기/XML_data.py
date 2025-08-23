x_str = """
<book>
    <name>혼공데</name>
    <author>박해선</author>
    <year>2022</year>
</book>
"""

import xml.etree.ElementTree as et
book = et.fromstring(x_str) # str -> element clas obj
print(type(book))

print(book.tag) # parents tag(element name)

name = book.findtext('name') # extract child tag
print(name) 

# more complex example
x2_str = """
<books>
    <book>
        <name>혼공데</name>
        <author>박해선</author>
        <year>2022</year>
    </book>
    <book>
        <name>혼공머</name>
        <author>박해선</author>
        <year>2020</year>
    </book>
</books>

"""

books = et.fromstring(x2_str)

for book in books.findall('book'):
    name = book.findtext('name')
    author = book.findtext('author')
    year = book.findtext('year')
    print(name)
    print(author)
    print(year)
    print()