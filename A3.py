def main():
    hnormal = int(input(f"{'Harga Normal':<14}{':':<3}"))
    hkredit = hnormal * 1.2
    umuka = hkredit * .3
    ucicil = (hkredit - hnormal) / 12
    print(f"{'Uang Muka':<14}{':':<3}Rp. {toCurrency(umuka)}")
    print(f"{'Cicilan':<14}{':':<3}Rp. {toCurrency(ucicil)}")

def toCurrency(value):
    return f"{value:,.2f}".replace('.', ' ').replace(',', '.').replace(' ', ',')

if __name__ == "__main__": main() 