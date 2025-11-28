# Yanlış Kullanım
class Machine:
    def print(self, document):
        pass
    def scan(self, document):
        pass
    def fax(self, document):
        pass
# Burada her cihaz tüm metodları uygulamak zorunda → ISP ihlali

# Doğru Kullanım
class Printer:
    def print(self, document):
        print("Belge yazdırılıyor:", document)

class Scanner:
    def scan(self, document):
        print("Belge taranıyor:", document)

# Test
printer = Printer()
printer.print("Rapor.pdf")

scanner = Scanner()
scanner.scan("Makale.docx")

