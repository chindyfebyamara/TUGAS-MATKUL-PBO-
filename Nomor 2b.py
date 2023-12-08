# Program menentukan bilangan ganjil atau genap tanpa input pengguna
batas = 10
counter = 1

while counter <= batas:
    if counter % 2 == 0:
        print(f"{counter} adalah bilangan genap")
    else:
        print(f"{counter} adalah bilangan ganjil")
    
    counter += 1
