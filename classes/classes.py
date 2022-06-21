#%% method
class Matematik:
    def __init__(self,sayi1,sayi2):
        self.sayi1 = sayi1
        self.sayi2 = sayi2
        print("Çalıştı")
        
        
    def topla(self):
        return self.sayi1 + self.sayi2
    
    def cıkar(self):
        return self.sayi1 - self.sayi2
    
    def carp(self):
        return self.sayi1 * self.sayi2
    
    def bol(self):
        return self.sayi1 / self.sayi2
    

matematik = Matematik(2,78) 
matematik2 = Matematik(3,76)
 
print("Toplam = " + str(matematik2.topla()))


#%% Property

class Person:
    def __init__(self, firstName, lastName, age): 
        self.firstName = firstName 
        self.lastName = lastName
        self.age = age
        

person1 = Person("Yeşim", "Doğan", 22)
print(person1.firstName + " " + person1.lastName + " " + str(person1.age))
        

