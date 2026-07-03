#                         1 - misol

# n = int(input("Son kiriting : "))
# def fib_gener(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a+b
#         yield a
# fd = fib_gener(n)
# print(list(fd))

#                         3 - misol

# from collections import namedtuple
# cars = []
# car = namedtuple('car', ['brand', 'model', 'year' , 'mileage'])
# for i in range(5):
#     print(f"{i+1} - mashinaning ma'lumotlari : ")
#     brand = input("Enter brand: ")
#     model = input("Enter model: ")
#     year = int(input("Enter year: "))
#     try:
#         mileage = int(input("Enter mileage: "))
#     except :
#         print("Faqat integer kiriting ")
#         break
#
# cars.append(car(brand, model, year, mileage))
# min_mil = min(cars , key=lambda x: x.mileage)
# print(f"Eng kam milage : {min_mil.mileage} , brand nomi : {min_mil.brand}")

#                        4 - misol

# def ret_gen(text):
#     text = text.split()
#     for word in text:
#         yield word
#
# text = input("Matningizni kiriting : ")
# si  = ret_gen(text)
# for word in si:
#     print(word)

