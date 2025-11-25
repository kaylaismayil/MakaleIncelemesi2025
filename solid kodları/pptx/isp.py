#ISP ihlali
class Machine:
    def print(self, document):
        # Yazıcı için uygun
        raise NotImplementedError

    def scan(self, document):
        # Tarayıcı için uygun
        raise NotImplementedError

    def fax(self, document):
        # Faks için uygun
        raise NotImplementedError

class SimplePrinter(Machine):
    def print(self, document):
        print("Belge yazdırılıyor:", document)

    def scan(self, document):
        # Bu cihazda tarayıcı yok → gereksiz metod
        raise Exception("Tarayıcı özelliği yok!")

#ISP uyumlu
class Printer:
    def print(self, document):
        # Yazıcı için gerekli metod
        raise NotImplementedError

class Scanner:
    def scan(self, document):
        # Tarayıcı için gerekli metod
        raise NotImplementedError

class SimplePrinter(Printer):
    def print(self, document):
        print("Belge yazdırılıyor:", document)

class MultiFunctionDevice(Printer, Scanner):
    def print(self, document):
        print("Belge yazdırılıyor:", document)

    def scan(self, document):
        print("Belge taranıyor:", document)