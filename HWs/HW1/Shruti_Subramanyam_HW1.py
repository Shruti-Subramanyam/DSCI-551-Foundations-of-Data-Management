# IMPORT LIBRARIES
import json
import requests
import sys

# Firebase Database URLs (Replace these URLs with your actual Firebase URLs)
DATABASE_URLS = {
    0: "https://hw1-database0-bbd8e-default-rtdb.firebaseio.com/ .json",
    1: "https://hw1-database1-c5ae1-default-rtdb.firebaseio.com/ .json",
}

## Define any global methods
# HERE


def author_hash_func(author):
    data_hash = hash(author)
    return data_hash % 2


def add_book(book_id, book_json):
    # INPUT : book id and book json from command line
    # RETURN : status code after pyhton REST call to add book [response.status_code]
    # EXPECTED RETURN : 200
    book_details = json.loads(book_json)
    author = book_details.get("author", "")
    base_index = author_hash_func(author)
    url = DATABASE_URLS[base_index]
    response = requests.post(url, json={str(book_id): book_details})
    return response.status_code


def search_by_author(author_name):
    # INPUT: Name of the author
    # RETURN: JSON object having book_ids as keys and book information as value [book_json] published by that author
    # EXPECTED RETURN TYPE: {'102': {'author': ... , 'price': ..., 'title': ..., 'year': ...}, '104': {'author': , 'price': , 'title': , 'year': }}
    search_result = {}
    for db_index, url in DATABASE_URLS.items():
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for unique_id, book_data in data.items():
            for book_id, book_info in book_data.items():
                if book_info.get("author") == author_name:
                    search_result[book_id] = book_info
                    return search_result


def search_by_year(year):
    # INPUT: Year when the book published
    # RETURN: JSON object having book_ids as key and book information as value [book_json] published in that year
    # EXPECTED RETURN TYPE: {'102': {'author': ... , 'price': ..., 'title': ..., 'year': ...}, '104': {'author': , 'price': , 'title': , 'year': }}
    search_result = {}
    for db_index, url in DATABASE_URLS.items():
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        for unique_id, book_data in data.items():
            for book_id, book_info in book_data.items():
                if book_info.get("year") == year:
                    search_result["book_id"] = book_info
                    return search_result


# Use the below main method to test your code
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py [operation] [arguments]")

    operation = sys.argv[1].lower()
    if operation == "add_book":
        result = add_book(sys.argv[2], sys.argv[3])
        print(result)
    elif operation == "search_by_author":
        books = search_by_author(sys.argv[2])
        print(books)
    elif operation == "search_by_year":
        year = int(sys.argv[2])
        books = search_by_year(year)
        print(books)
