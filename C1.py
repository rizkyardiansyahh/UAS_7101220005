def main():
    names, nims, grades, checkers = [], [], [], []

    for counter in range(1, 6):
        print(f"\nMahasiswa {counter}" if counter != 1 else f"Mahasiswa {counter}")
        names.append(input(f"{'Nama':<8}{':':<3}"))
        nims.append(input(f"{'Nim':<8}{':':<3}"))
        grades.append(int(input(f"{'Nilai':<8}{':':<3}")))

    dataAmount = len(names)
    average, passed, notPassed = 0, 0, 0
    maxCounter, maxGrade, maxPerson = 0, max(grades), "oleh: "
    minCounter, minGrade, minPerson = 0, min(grades), "oleh: "

    for index, value in enumerate(grades):
        if value >= 56: 
            passed += 1
            checkers.append("Lulus")
        else: 
            notPassed += 1
            checkers.append("Tidak Lulus")

        if maxCounter == 0:
            if value == maxGrade: 
                maxPerson += names[index]
                maxCounter += 1
        else:
            if value == maxGrade: maxPerson += ", " + names[index]
            
        if minCounter == 0:
            if value == minGrade: 
                minPerson += names[index]
                minCounter += 1
        else:
            if value == minGrade: minPerson += ", " + names[index]
        average += value
    average /= len(grades)

    print("\n====================PROGRAM PENGOLAHAN DATA MATKUL ALPRO====================")
    print("\n============================================================================")
    print(f"{'NO.':<7}{'NIM':<18}{'NAMA':<19}{'NILAI':<12}KETERANGAN")
    print("----------------------------------------------------------------------------")
    for index in range(len(names)):
        print(f"{index + 1:<5}{nims[index]:<15}{names[index]:<25}{grades[index]:<11}{checkers[index]}")
        print("----------------------------------------------------------------------------")
    print(f"\n{'Jumlah Mahasiswa':<18}{':':<3}{dataAmount}")
    print(f"{'Rata-rata Nilai':<18}{':':<3}{round(average, 2)}")
    print(f"{'Nilai Tertinggi':<18}{':':<3}{maxGrade} {maxPerson}")
    print(f"{'Nilai Terendah':<18}{':':<3}{minGrade} {minPerson}")
    print(f"{'Jumlah Lulus':<18}{':':<3}{passed}")
    print(f"{'Jumlah Gagal':<18}{':':<3}{notPassed}\n")

if __name__ == "__main__": main()