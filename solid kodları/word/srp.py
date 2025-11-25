# (Yanlış Kullanım):
class DataManager:
    def read_file(self, filename):
        with open(filename, "r") as f:
            return f.read()

    def process_data(self, data):
        return data.upper()
# Burada tek sınıf hem dosya okuma hem veri işleme 
# sorumluluğunu üstleniyor → SRP ihlali

# (Doğru Kullanım):
class FileReader:
    def read_file(self, filename):
        with open(filename, "r") as f:
            return f.read()

class DataProcessor:
    def process_data(self, data):
        return data.upper()
# Burada her sınıf tek bir sorumluluk üstleniyor → SRP uyumlu


reader = FileReader()
data = reader.read_file("veri.txt")  # Bu dosya varsa içeriği okunur

processor = DataProcessor()
print(processor.process_data(data))