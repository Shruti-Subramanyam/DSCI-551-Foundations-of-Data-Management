# IMPORT LIBRARIES
import sys
import json
from lxml import etree


# Define any helper functions here
def author_hash_func(author_name):
    return sum(ord(c) for c in author_name) % 2


def add_book(book_id, book_json):  # check the book_id
    # INPUT : book json from command line
    # RETURN : 1 if successful, else 0
    # Assume JSON is well formed with no missing attributes
    try:
        book_data = json.loads(book_json)
        for auth_hash, file_xml in XML_FILES.items():
            try:
                with open(file_xml, "rb") as file:
                    tree = etree.parse(file)
                    root = tree.getroot()
                    for book_ele in root.findall("book"):
                        if book_ele.find("book_id").text == str(book_id):
                            return 0
            except FileNotFoundError:
                pass
        auth_hash = author_hash_func(book_data["author"])
        file_xml = XML_FILES[auth_hash]
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(file_xml, parser)
        root = tree.getroot()
        book = etree.SubElement(root, "book")
        etree.SubElement(book, "book_id").text = str(book_id)
        for key, value in book_data.items():
            subElem = etree.SubElement(book, key)
            subElem.text = str(value)
        with open(file_xml, "wb") as file:
            file.write(etree.tostring(root, pretty_print=True))
        return 1
    except Exception as e:
        return 0


def search_by_author(author_name):
    # INPUT: name of author
    # RETURN: list of strings containing only book titles
    # EXPECTED RETURN TYPE: ['book title 1', 'book title 2', ...]
    try:
        book_titles = []
        for file_xml in XML_FILES.values():
            tree = etree.parse(file_xml)
            root = tree.getroot()
            for book in root.findall("book"):
                if book.find("author").text == author_name:
                    book_titles.append(book.find("title").text)
        return book_titles
    except FileNotFoundError:
        return []
    except Exception as e:
        return []


def search_by_year(year):
    # INPUT: year of publication
    # RETURN: list of strings containing only book titles
    # EXPECTED RETURN TYPE: ['book name 1', 'book name 2', ...]
    try:
        book_titles = []
        for file_xml in XML_FILES.values():
            tree = etree.parse(file_xml)
            root = tree.getroot()
            for book in root.findall("book"):
                if int(book.find("year").text) == year:
                    book_titles.append(book.find("title").text)
        return book_titles
    except FileNotFoundError:
        return []
    except Exception as e:
        return []


# Use the below main method to test your code
if __name__ == "__main__":
    if len(sys.argv) < 5:
        sys.exit(
            "\nUsage: python3 script.py [path/to/file0.xml] [path/to/file1.xml] [operation] [arguments]\n"
        )

    xml0, xml1 = sys.argv[1], sys.argv[2]

    # Assume XML files exist at mentioned path and are initialized with empty <bib> </bib> tags
    global XML_FILES
    XML_FILES = {0: xml0, 1: xml1}

    operation = sys.argv[3].lower()

    if operation == "add_book":
        result = add_book(sys.argv[4], sys.argv[5])
        print(result)
    elif operation == "search_by_author":
        books = search_by_author(sys.argv[4])
        print(books)
    elif operation == "search_by_year":
        year = int(sys.argv[4])
        books = search_by_year(year)
        print(books)
    else:
        sys.exit("\nInvalid operation.\n")
