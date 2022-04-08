from importlib.resources import path


def silaHasla(haslo):
    duza = False
    mala = False
    wykrzyknik = False
    if len(haslo) >= 10:
        for i in range(len(haslo)):
            if ord(haslo[i]) <= 90 and ord(haslo[i]) >= 50:
                duza = True
            elif ord(haslo[i]) == 33:
                wykrzyknik = True
            else:
                mala = True
        if mala and duza and wykrzyknik:
            return True
        else:
            return False
    else:
        return False


print(silaHasla("asjdA!sfsdfsdfsdf"))

lista = [1, 2, 99, 4, 5]
for i in range(len(lista)):
    if lista[i] == 99:
        continue
    print(lista[i])


def czyNalezy(lista, e):
    wynik = False
    i = 0
    while(i < len(lista)):
        if(lista[i] == e):
            wynik = True
            break
        i += 1
    return wynik


with open("C:\\Users\\kacpe\\Desktop\\minzwiedzy\\lab2\\plik.txt", "r") as file:
    for x in file:
        print(x, end="")
jezyki = ['python', 'java', 'javaScript', 'C++', 'C']


with open("C:\\Users\\kacpe\\Desktop\\minzwiedzy\\lab2\\plik.txt", "w") as file:
    for x in jezyki:
        print(x)
        file.write(x+"\n")

miasta = ["Olsztyn", "Warszawa", "Kraków", "Łódź"]

print(list(map(lambda napis: napis[:3], miasta)))

nazwyPlikow = ["tekst.txt", "main.py", "xd.txt", "zadania.py", "run.exe"]


def rozszerzenie(lista, e):
    lista2 = []
    for i in lista:
        if i.endswith(e):
            lista2.append(i)
    print(lista2)


rozszerzenie(nazwyPlikow, "txt")
rozszerzenie(nazwyPlikow, ".py")
