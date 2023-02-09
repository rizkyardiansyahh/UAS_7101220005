def main():
    price = int(input(f"{'Harga Satuan':<18}{':':<3}"))
    piece = int(input(f"{'Jumlah Pembelian':<18}{':':<3}"))
    discount = int(input(f"{'Diskon':<18}{':':<3}"))
    
    totalPrice = toCurrency((price * piece) - (price * piece * discount / 100))
    price = toCurrency(price)

    print("\n======PROGRAM PENJUALAN BUKU======")
    print(f"{'Harga Satuan':<18}{':':<3}Rp. {price}")
    print(f"{'Jumlah Pembelian':<18}{':':<3}{piece}")
    print(f"{'Diskon':<18}{':':<3}{discount} %")
    print(f"{'Total Harga':<18}{':':<3}Rp. {totalPrice}")
    print("----------------------------------")

def toCurrency(value):
    return f"{value:,.2f}".replace('.', ' ').replace(',', '.').replace(' ', ',')

if __name__ == "__main__": main()