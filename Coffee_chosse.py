coffe_list = {1 : "Espresso", 2 : "Americano", 3 : "Latte", 4 : "Raf", 5 : "Capucino" }
coffe_price = {"Espresso" : 15, "Americano" : 20, "Latte" : 30, "Raf" : 35, "Capucino" : 25 }
print(coffe_list)
choose_coffe = int(input("Будьласка виберіть каву з списку: "))
pay_sum = 0
give_back = 0
tmp = 0 
try :
  for key, value in coffe_list.items():
    if choose_coffe == key:
      x = value
      print(value)
  for coffe, price in coffe_price.items():
    if coffe == x:
      print("Ви маєте заплатити :", price, "grn")
      while give_back == 0 and tmp == 0 and pay_sum < price:
        pay = float(input("внесіть суму: "))
        
        if pay >= price:
          pay_sum = pay
          give_back = pay_sum - price
          print("Тримайте здачу:", give_back, "grn")
          tmp += 1
        
        elif pay < price:
          pay_sum  += pay
          y = price - pay_sum  
          if y < 0 :
            print("Тримайте здачу: ",abs(y))
            break
          print("Ви внесли: ", pay)
          print("маєте внести ще: ", y, " грн" )
         
except:
  print("Цієї кави немає в списку")
finally:
  print("Бажаємо гарного дня")
