class geometri:
    def __init__(self,a,b,c,d):
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def tanı(self):
        self.a=input("Birinci Ölçüyü Giriniz:")
        self.b=input("ikinci Ölçüyü Giriniz:")
        self.c=input("Üçüncü Ölçüyü Giriniz:")

    def kare(self):
        if self.a == self.b== self.c:
            print("Girilen Ölçülerin tasvir ettiği Şekil=Karedir.")
        else:
            print("Uygun Bir Ölçü Giriniz!")

    def dikdörtgen(self):
        if self.a == self.b +self.c == self.d:
            print("Girilen Ölçülerin tasvir ettiği Şekil=Dikdörtgendir.")

        else:
            print("Uygun Bir Ölçü Giriniz:")


    def ucgen(self):
        if self.a == self.b == self.c:
            print("Girilen Ölçülerin tasvir ettiği Şekil=Dikdörtgendir.")

        else:
            print("Uygun Bir Ölçü Giriniz:")



