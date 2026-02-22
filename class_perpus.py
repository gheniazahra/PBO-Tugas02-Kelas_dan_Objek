import datetime

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False 

    def borrow(self): # status peminjaman buku
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"[BUKU] Status '{self.title}': Sedang Dipinjam.")
        else:
            print(f"[BUKU] Gagal: Status '{self.title}' sudah dipinjam orang lain.")

    def return_book(self):  # status ketersediaan buku
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"[BUKU] Status '{self.title}': Tersedia.")
        else:
            print(f"[BUKU] Status '{self.title}': Tidak Tersedia / Sedang Dipinjam.")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = [] 


class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id


class BorrowTransaction:
    def __init__(self, book, member, staff):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = datetime.date.today().strftime("%Y-%m-%d") #--> tahun-bulan-hari 
        self.returned = False 

    def borrow_book(self, book, staff):
        print(f"\nMEMPROSES PEMINJAMAN")
        print(f"Staff bertugas : {staff.name}")
        print(f"Peminjam       : {self.member.name}")
        
        if not book.is_borrowed:
            book.borrow() 
            self.returned = False
            self.member.borrowed_books.append(self) 
            print(f"-> Transaksi SUKSES pada tanggal {self.borrow_date}.")
        else:
            print("-> Transaksi GAGAL. Buku tidak tersedia.")

    def return_book(self, book, staff):
        print(f"\nMEMPROSES PENGEMBALIAN")
        print(f"Staff bertugas : {staff.name}")
        print(f"Peminjam       : {self.member.name}")

        if not self.returned:
            book.return_book() 
            self.returned = True
            print(f"-> Pengembalian '{book.title}' oleh {self.member.name} SUKSES.")
        else:
            print("-> Buku ini sudah dikembalikan sebelumnya.")