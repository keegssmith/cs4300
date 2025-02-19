def fav_books():

    top_books = [ 
        ("Imaginary Friend", "Stephen Chbosky"), # tuple in the form of ("Book Tite", "Author")
        ("Salt to the Sea", "Ruta Sepetys"),
        ("The House Across the Lake", "Riley Sager"),
        ("Looking for Alaska", "John Green")
    ]
    
    # list slice the first 3 books
    top_3 = top_books[:3]

    # print the name and author of top 3 books
    return top_3

print(fav_books())

def students():
    student_database = { # database of students including their name and respective id
        "Bob Smith": "1",
        "Julia Roberts": "2",
        "Dean Lucas": "3",
    }
    return student_database

print(students())