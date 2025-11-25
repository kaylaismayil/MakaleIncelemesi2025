#LSP ihlali
class Bird:
    def fly(self):
        print("Uçuyor...")

class Penguin(Bird):
    def fly(self):
        # Penguen uçamaz → LSP ihlali
        raise Exception("Penguenler uçamaz!")

class Bird:
    def move(self):
 # Alt sınıflar kendi davranışını tanımlar
        raise NotImplementedError

class Sparrow(Bird):
    def move(self):
        # Serçe uçabilir
        print("Serçe uçuyor...")

class Penguin(Bird):
    def move(self):
        # Penguen yüzebilir
        print("Penguen yüzüyor...")      