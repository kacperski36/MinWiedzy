# imie = input("Podaj swoje imie: ")
# print(f'witaj: {imie}')

from pickle import FALSE, TRUE


x = "zmienna string"
flt = 3.256
liczba = 2

print(f'{x} to  typ  {type(x)}, {flt} to  typ  {type(flt)}, {liczba} to  typ  {type(liczba)}')

lista = ['a', 'b', 'c']
print(lista)

hasz = '#'.join(lista)
print(hasz)

lista2 = ['x', 'y', 'z']

txt = "Metody Inżynierii Wiedzy Są Najlepsze"
print(f'{txt}, dlugość tego ciągu to {len(txt)}')

txt = txt.lower()
print(f'{txt}')

txtUsuniete = txt.replace('ż', 'z')
txtUsuniete = txt.replace('ą', 'a')
txtUsuniete = txt.replace(' ', '')

print(f'{txtUsuniete}, dlugość tego ciągu to {len(txtUsuniete)}')

set(txtUsuniete)

print(f'{txtUsuniete}, dlugość tego ciągu to {len(txtUsuniete)}')

x = (1, 2, 3)
y = ('raz', 'dwa', 'trzy')

print(f'{x} to  typ  {type(x)}')
print(f'{y} to  typ  {type(y)}')

jezyki = ['python', 'java', 'javaScript', 'C++', 'C']

print(f'{jezyki}, dlugość tego ciągu to {len(jezyki)}')

print(jezyki.index('python'))

lista3 = lista+lista2

print(lista)
print(lista2)
print(lista3)

lista.extend(lista3)
print(lista)


slownik = {"Litwa": "Wilno", "Rosja": "Moskwa", "Niemcy": "Berlin",
           "Ukraina": "Kijów", "Czechy": "Praga", "Białoruś": "Mińsk", "Słowacja": "Bratysława"}

print(slownik)
print(slownik.values())

print(sorted(slownik))

zdanie = "Ala ma kota a kot no jest kotem i ma ale"
secik = set(zdanie)

if len(secik) > 15:
    print('no jest wiecej')
else:
    print("nie ma")

if zdanie[0] == 'J':
    print('jest J')
else:
    print("nie ma j ")

for i in range(10):
    print(i)

hasz = str(hasz)
wynik = ""
for i in range(len(hasz)):
    if hasz[i] != '#':
        wynik += hasz[i]
print(wynik)


# Za tydzien wyznacznik macierzy i obliczanie macierzy odwrotnej
# Zadanie domowe sortowanie całego słownika
