def main():
    print("\n======PROGRAM PERHITUNGAN GAJI KARYAWAN PT. XYZ======")
    print("-----------------------------------------------------")
    print("                    DATA  PEGAWAI                    ")
    print("-----------------------------------------------------")

    name = input(f"{'Nama':<20}{':':<3}")
    jobClass = input(f"{'Golongan':<20}{':':<3}")
    workTime = int(input(f"{'Total Jam Kerja':<20}{':':<3}"))

    if workTime > 200: overTime = workTime - 200
    if jobClass.upper() == 'A':
        salary = 1_200_000
        allowance = salary * .1
        overTime *= 5_000
    elif jobClass.upper() == 'B':
        salary = 1_600_000
        allowance = salary * .15
        overTime *= 7_500
    elif jobClass.upper() == 'C':
        salary = 2_000_000
        allowance = salary * .2
        overTime *= 10_000
    total = salary + allowance + overTime
    
    salary = toCurrency(salary)
    allowance = toCurrency(allowance)
    overTime = toCurrency(overTime)
    total = toCurrency(total)

    print("-----------------------------------------------------")
    print("                  PERHITUNGAN  GAJI                  ")
    print("-----------------------------------------------------")
    print(f"{'Gaji Pokok':<20}{':':<3}Rp. {salary}")
    print(f"{'Tunjangan':<20}{':':<3}Rp. {allowance}")
    print(f"{'Lembur':<20}{':':<3}Rp. {overTime}")
    print("-----------------------------------------------------")
    print(f"{'Total':<20}{':':<3}Rp. {total}")
    print("-----------------------------------------------------")

def toCurrency(value):
    return f"{value:,.2f}".replace('.', ' ').replace(',', '.').replace(' ', ',')

if __name__ == "__main__": main()