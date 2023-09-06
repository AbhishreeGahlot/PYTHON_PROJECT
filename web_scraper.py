#WEB SCRAPPING CODE
import requests
from bs4 import BeautifulSoup

url = "https://www.goodreads.com/list/show/13143.Best_Authors_Ever"
response = requests.get(url)

if response.status_code == 200:
    # Parsing the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    book_elements = soup.find_all("tr", itemtype="http://schema.org/Book")   
   
    books_info = []

    # Loop through the first 100 book elements
    for book_element in book_elements[:100]:
        # Finding the book title
        book_title = book_element.find("a", class_="bookTitle").get_text(strip=True)

        # Finding the author name
        author_names = [author.get_text(strip=True) for author in book_element.find_all("a", class_="authorName")]

        # Adding the book title and author names to the list
        books_info.append((book_title, author_names))
    
    for i, (book_title, author_names) in enumerate(books_info[:100], 1):
        print(f"{i}. Book Title: {book_title}")
        print(f"   Author: {', '.join(author_names)}\n")

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
