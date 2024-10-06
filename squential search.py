def sequential_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def main():
    books = ["buku gambar", "buku tulis", "buku cerita", "buku komik", "buku novel"]
    
    while True:
        print("Daftar buku di toko buku:")
        for i, book in enumerate(books):
            print(f"{i + 1}. {book}")

        x = input("Masukkan jenis buku yang akan dicari: ").strip().lower()

        result = sequential_search(books, x)

        if result != -1:
            print(f"'{x}' ditemukan pada indeks {result}")
        else:
            print(f"'{x}' tidak ditemukan dalam daftar")

        ulangi = input("Apakah Anda ingin mencari buku lain? (y/n): ").strip().lower()
        if ulangi != 'y':
            break

if __name__ == "__main__":
    main()
