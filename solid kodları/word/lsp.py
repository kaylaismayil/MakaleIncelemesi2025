# Yanlış Kullanım
class Bird:
    def fly(self):
        print("Uçuyor...")

class Penguin(Bird):
    def fly(self):
        print("Penguen uçamaz!")  
# Burada alt sınıf üst sınıfın davranışını bozuyor → LSP ihlali

# Doğru Kullanım
class Bird:
    def move(self):
        raise NotImplementedError

class Sparrow(Bird):
    def move(self):
        print("Serçe uçuyor...")

class Penguin(Bird):
    def move(self):
        print("Penguen yüzüyor...")

# Test
birds = [Sparrow(), Penguin()]
for b in birds:
    b.move()

