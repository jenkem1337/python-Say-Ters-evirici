def reverseNumber(n):
    liste = list(n) #sayı listeye alınır
    liste.reverse() #sayı ters çevrilir
    listToStr = "".join(map(str, liste)) #listeden string hale geçer
    Str = int(listToStr) 
    print(Str)

while True:
	Number = input("Lütfen bir sayı giriniz : ")
	reverseNumber(Number)
    
