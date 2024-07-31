# 1) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız

my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}

if "c" in my_dictionary.values():
    print("evet içinde")

# 2) Aşağıdaki listedeki sayılardan sadece çift sayı olanları başka bir listeye kaydeden bir kod yazınız.

my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]

other_list = []
for num in my_numbers:
    if num % 2 == 0:
        other_list.append(num)
print(other_list)

# 3) Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.

r_list = [3,2,5,8,4,6,9,12]
pi = 3.14
new_list = []
for r in r_list:
    new_list.append(2*pi*r)
print(new_list)

# 4) Aşağıdaki listede isim - yaş eşleşmelerinin bulunduğu yapılar mevcuttur. Sadece yaşların olduğu yeni ve ayrı bir liste oluşturunuz.

age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
age_list = []
for name,age in age_name_list:
    age_list.append(age)
print(age_list)

# 5) Aşağıdaki müzik gruplarından birini rastgele yazdıran bir kod yazınız

metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]
from random import randint
print(metal_list[randint(0,len(metal_list)-1)])

# 6) Aşağıdaki kodun çıktısı ne olacaktır?

number_list = [5,7,18,21,20,10,405,24]

print([num % 2 == 0 for num in number_list])

#7) Aşağıdaki string dizisinde, içinde sadece XYZ geçen barkodları gösterecek yeni bir liste oluşturunuz

barcodeList = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]
print(list(filter(lambda s: "XYZ" in s, barcodeList)))

#8) Aşağıda yazdırılan sınıfı incelediğinizde my_cat.multiply_age() kodunun çıktısı ne olacaktır?

class Cat:
    def __init__(self, name, age=5):
        self.name = name
        self.age = age

    def multiply_age(self):
        return self.age * 3

my_cat = Cat("Whiskers")
print(my_cat.multiply_age())
