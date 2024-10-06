def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        middle = (left + right) // 2
        if sorted_list[middle][1] == target:
            return middle
        elif sorted_list[middle][1] < target:
            left = middle + 1
        else:
            right = middle - 1

    return None

def main():
    # Daftar barang beserta harganya, diurutkan berdasarkan harga
    sorted_items = [
        ["biskuit", 5000],
        ["roti", 5000],
        ["oreo", 6000],
        ["green tea", 6000],
        ["sosis", 10000]
    ]
    
    print("Daftar barang di toko:")
    for item in sorted_items:
        print(f"{item[0]}: Rp{item[1]}")

    try:
        target = int(input("Masukkan budget Anda: "))
    except ValueError:
        print("Masukkan nilai yang valid.")
        return

    index = binary_search(sorted_items, target)
    if index is not None:
        print(f"Barang dengan harga Rp{target} ditemukan: {sorted_items[index][0]}.")
    else:
        print(f"Tidak ada barang dengan harga Rp{target} dalam daftar.")

if __name__ == "__main__":
    main()
