#1
import random
seznam = random.sample(range(1, 51), 6)
print("puvodni seznam:", seznam)
del seznam[2]
print("novy seznam:", seznam)
soucet = sum(seznam)
print("Celkovy soucet cisel je:", soucet)
print("delka seznamu je::", len(seznam))

#2
data = [1945, 1889, 2006, 2001, 1999, 2015, 1212]
minimalni_hodnota = min(data)
maximalni_hodnota = max(data)
print("minimalni hodnota je:", minimalni_hodnota)
print("maximalni hodnota je:", maximalni_hodnota)
data[0], data[1] = data[1], data[0]
data[5], data[6] = data[6], data[5]
print("novy seznam dat:", data)

#3
salary = [16000, 18000, 20000, 25000, 30000, 45500]
high_salary = salary[4:]
print("vysoke platy:", high_salary)
salary[2] = 23458
print("platy:", salary)
salary.sort(reverse=True)
print("serazeny seznam platu:", salary)

#4
cisla = [2, 4, 6, 8]
cisla_na_druhou = [4, 16, 36, 64]
vysledny_seznam = cisla + cisla_na_druhou
print(vysledny_seznam)