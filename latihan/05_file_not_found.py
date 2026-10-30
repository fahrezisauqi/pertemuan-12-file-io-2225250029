
input_file = "data/tidak_ada.txt"

try:
    with open(input_file, "r", encoding="utf-8") as file:
        isi = file.read()
        print(isi)

except FileNotFoundError:
    print(f"File tidak ditemukan: {input_file}")
