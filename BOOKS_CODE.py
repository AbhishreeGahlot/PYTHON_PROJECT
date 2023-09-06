# MAIN SOURCE CODE
import tkinter as tk
from tkinter import messagebox
import csv

def recommend_books():
    username = username_entry.get()
    author_name = author_entry.get()
    
    # Loading the CSV data into a dictionary
    book_recommendations = {}
    with open('Books.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for row in reader:
            book_title, author = row[0], row[1]
            if author not in book_recommendations:
                book_recommendations[author] = []
            book_recommendations[author].append(book_title)

    if author_name in book_recommendations:
        books = ", ".join(book_recommendations[author_name])
        messagebox.showinfo("Book Recommendations", f"Hi {username}, here are some books by {author_name}: {books}")
    else:
        messagebox.showinfo("Book Recommendations", f"Sorry, we don't have book recommendations for {author_name}.")

#main window
window = tk.Tk()
window.title("Book Recommendation System")
window.geometry("400x200")
window.configure(bg="#FFC0CB")
window.configure(cursor="hand2")

capital_label=tk.Label(window, text="FILL IN CAPITAL LETTERS",bg="#ADD8E6",fg="white")
capital_label.pack()
username_label = tk.Label(window, text="Enter your username:",bg="#D3D3D3",fg="white")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

author_label = tk.Label(window, text="Enter author's name:",bg="#D3D3D3",fg="white")
author_label.pack()
author_entry = tk.Entry(window)
author_entry.pack()

recommend_button = tk.Button(window, text="Recommend Books", command=recommend_books , bg="black",fg="white")
recommend_button.pack()

# main loop
window.mainloop()
