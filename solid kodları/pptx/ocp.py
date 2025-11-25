class PaymentProcessor:
    def pay(self, method, amount):
        # Burada her yeni ödeme yöntemi için kodu
        # değiştirmek gerekiyor → OCP ihlali
        if method == "credit":
            print("Kredi kartı ile ödeme:", amount)
        elif method == "paypal":
            print("PayPal ile ödeme:", amount)

class PaymentMethod:
    def pay(self, amount):
        # Soyut sınıf, alt sınıflar
        # kendi ödeme yöntemini tanımlar
        raise NotImplementedError

class CreditCard(PaymentMethod):
    def pay(self, amount):
        # Kredi kartı ile ödeme işlemi
        print("Kredi kartı ile ödeme:", amount)

class PayPal(PaymentMethod):
    def pay(self, amount):
        # PayPal ile ödeme işlemi
        print("PayPal ile ödeme:", amount)

# Yeni ödeme yöntemi eklemek için sadece
# yeni sınıf yazılır
class Bitcoin(PaymentMethod):
    def pay(self, amount):
        # Bitcoin ile ödeme işlemi
        print("Bitcoin ile ödeme:", amount)