from class_perpus import Book, Member, Staff, BorrowTransaction
print("=== SISTEM PERPUSTAKAAN UIN SUSKA ===")

# Membuat Objek (sesuai urutan state di __init__)
buku1 = Book("Buku PBO", "Sinta", "10111")
buku2 = Book("Buku Kalkulus", "Dini", "10112")

staff1 = Staff("Admin Budi", "001")
staff2 = Staff("Admin Yusuf", "002")

member1 = Member("Ghenia", "M-1001")
member2 = Member("Zahra", "M-1002")

# Cek status awal buku dan member
print(f"\n---INFO STATUS BUKU DAN RIWAYAT ANGGOTA---")
print(f"Status Buku '{buku1.title}'= {buku1.is_borrowed}")
print(f"Status Buku '{buku2.title}'= {buku2.is_borrowed}")

buku_ghenia = [nota.book.title for nota in member1.borrowed_books] 
buku_zahra = [nota.book.title for nota in member2.borrowed_books]

print(f"\nStatus Anggota {member1.name} = Meminjam {len(member1.borrowed_books)} buku {buku_ghenia}")
print(f"Status Anggota {member2.name} = Meminjam {len(member2.borrowed_books)} buku {buku_zahra}")

# PEMINJAMAN BUKU
# Membuat objek transaksi
transaksi_01 = BorrowTransaction(buku1, member1, staff1) 
transaksi_02 = BorrowTransaction(buku2, member2, staff2) 

# Sistem memproses peminjaman
transaksi_01.borrow_book(buku1, staff1)
transaksi_02.borrow_book(buku2, staff2)

# Cek status buku setelah dipinjam
print(f"\n---INFO STATUS BUKU DAN RIWAYAT ANGGOTA SETELAH PEMINJAMAN---")
print(f"Status Buku '{buku1.title}'= {buku1.is_borrowed}")
print(f"Status Buku '{buku2.title}'= {buku2.is_borrowed}")

buku_ghenia = [nota.book.title for nota in member1.borrowed_books]
buku_zahra = [nota.book.title for nota in member2.borrowed_books]

print(f"\nStatus Anggota {member1.name} = Meminjam {len(member1.borrowed_books)} buku {buku_ghenia}")
print(f"Status Anggota {member2.name} = Meminjam {len(member2.borrowed_books)} buku {buku_zahra}")

# PENGEMBALIAN BUKU
# Sistem memproses pengembalian
transaksi_01.return_book(buku1, staff1)
transaksi_02.return_book(buku2, staff2)

# Cek status setelah dikembalikan
print(f"\n---INFO STATUS BUKU DAN RIWAYAT ANGGOTA SETELAH PENGEMBALIAN---")
print(f"Status Buku '{buku1.title}'= {buku1.is_borrowed}")
print(f"Status Buku '{buku2.title}'= {buku2.is_borrowed}")

buku_ghenia = [nota.book.title for nota in member1.borrowed_books]
buku_zahra = [nota.book.title for nota in member2.borrowed_books]

print(f"\nStatus Anggota {member1.name} = Meminjam {len(member1.borrowed_books)} buku {buku_ghenia}")
print(f"Status Anggota {member2.name} = Meminjam {len(member2.borrowed_books)} buku {buku_zahra}")