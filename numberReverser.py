def numberReverser(n):
    liste = list(n) #sayı listeye alınır
    liste.reverse() #sayı ters çevrilir
    listToStr = "".join(map(str, liste)) #listeden string hale geçer
    Number = int(listToStr) 
    print(Number)

while True:
	Number = input("Lütfen bir sayı giriniz : ")
	numberReverser(Number)
    
