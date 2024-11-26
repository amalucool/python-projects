class Books:
    def __init__(self, title, author, year,):
        self.title = title 
        self.author = author 
        self.year = year
        pass

class Harry_Potter(Books):
    pass

class Wimpy_Kid(Books):
    pass

class Three_Musketeers(Books):
    pass

class Things_Fall_Apart(Books):
    pass

Hp = Harry_Potter("Harry Potter", "J.K Rowling", "2000")
Wk = Wimpy_Kid("Diary of a wimpy kid", "Jeff Kinney", "1999")
Tm = Three_Musketeers("The Three Musketeers", "Hans Zimmer", "1878")
Tf = Things_Fall_Apart("Things Fall Apart", "Chinua Achebe", "1974")

for x in (Hp, Wk, Tm, Tf):
    print(x.title)
    print(x.author)
    print(x.year)

    y = sorted(x.year)
    print(y)
