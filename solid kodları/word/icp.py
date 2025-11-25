class PaymentProcessor:
    def pay(self, method, amount):
        if method == "credit":
            print("Kredi kartı ile ödeme:", amount)
        elif method == "paypal":
            print("PayPal ile ödeme:", amount)
# Burada her yeni ödeme yöntemi için mevcut kodu değiştirmek gerekiyor → OCP ihlali


class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print("Kredi kartı ile ödeme:", amount)

class PayPal(PaymentMethod):
    def pay(self, amount):
        print("PayPal ile ödeme:", amount)

class Bitcoin(PaymentMethod):
    def pay(self, amount):
        print("Bitcoin ile ödeme:", amount)
# Yeni ödeme yöntemi eklemek için sadece yeni sınıf yazılır → OCP uyumlu

payment = CreditCard()
payment.pay(100)
