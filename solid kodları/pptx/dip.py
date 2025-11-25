#DIP ihlali
class EmailSender:
    def send(self, message):
        print("E-posta gönderildi:", message)

class NotificationService:
    def __init__(self):
        # Doğrudan EmailSender’a bağımlı → DIP ihlali
        self.sender = EmailSender()

    def notify(self, message):
        self.sender.send(message)

#DIP uyumlu
class MessageSender:
    def send(self, message):
        # Soyut arayüz, alt sınıflar kendi gönderim yöntemini tanımlar
        raise NotImplementedError

class EmailSender(MessageSender):
    def send(self, message):
        print("E-posta gönderildi:", message)

class SmsSender(MessageSender):
    def send(self, message):
        print("SMS gönderildi:", message)

class NotificationService:
    def __init__(self, sender: MessageSender):
        # Soyut arayüz üzerinden bağımlılık → DIP uyumlu
        self.sender = sender

    def notify(self, message):
        self.sender.send(message)

# Kullanım örneği
service = NotificationService(EmailSender())
service.notify("Merhaba Dünya!")