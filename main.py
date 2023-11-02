data = []
num = int(input('ведіть кількість повтореннь'))
for i in range(num):
   name = input('Введить назву товара')
   price = float(input('цена tovara'))
   amount = int(input('kilckist tovara'))
   data.append([name,price,amount])
   print(data)
   suma = 0
for i in data:
   suma = suma + i[1]*i[2]
print("suma pokupok", suma)
print("podatok" ,suma*0.18)
print("reestr")
print(name, price, amount)
