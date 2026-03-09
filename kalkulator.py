def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Pembagian nol"

print("Pilih Operasi:")
print("1.Tambah\n2.Kurang\n3.Kali\n4.Bagi")

choice = input("Masukkan pilihan (1/2/3/4): ")

num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))

if choice == '1': print("Hasil:", add(num1, num2))
elif choice == '2': print("Hasil:", subtract(num1, num2))
elif choice == '3': print("Hasil:", multiply(num1, num2))
elif choice == '4': print("Hasil:", divide(num1, num2))
else: print("Input tidak valid")#please add your calculator function here
