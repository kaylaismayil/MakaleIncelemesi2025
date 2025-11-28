# Yanlış Kullanim
class EmailSender:
    def send(self, message):
        print("Email gönderildi:", message)

class NotificationService:
    def __init__(self):
        self.sender = EmailSender()  # Doğrudan bağımlılık → DIP ihlali

    def notify(self, message):
        self.sender.send(message)

# Doğru Kullanım
class MessageSender:
    def send(self, message):
        raise NotImplementedError

class EmailSender(MessageSender):
    def send(self, message):
        print("Email gönderildi:", message)

class SmsSender(MessageSender):
    def send(self, message):
        print("SMS gönderildi:", message)

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender  # Soyutlamaya bağımlı → DIP uyumlu

    def notify(self, message):
        self.sender.send(message)

# Test
service1 = NotificationService(EmailSender())
service1.notify("Merhaba Kayla!")

service2 = NotificationService(SmsSender())
service2.notify("Test mesajı")

