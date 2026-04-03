data = "Book 1;30000\nBook 2;50000\nBook 3;100000\nTong;900000"
with open("books.txt", "w") as f:
    f.write(data)
