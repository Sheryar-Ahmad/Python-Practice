from abc import ABC, abstractmethod


class PaymentProcessor(ABC):

    @abstractmethod
    def process_payment(self, amount: float):
        pass

    @abstractmethod
    def refund_payment(self, amount: float):
        pass

    def receipt_footer(self):
        print("Thank you for shopping with us! Have a great day.\n")


class CreditCardPayment(PaymentProcessor):

    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount: float):
        print(
            f"Processing credit card payment of ${amount:.2f} using card ending in {self.card_number[-4:]}..."
        )

    def refund_payment(self, amount: float):
        print(
            f"Refunding ${amount:.2f} back to credit card ending in {self.card_number[-4:]}..."
        )


class PayPalPayment(PaymentProcessor):

    def __init__(self, email):
        self.email = email

    def process_payment(self, amount: float):
        print(f"Connecting to PayPal portal for {self.email}...")
        print(f"Successfully processed ${amount:.2f} transaction.")

    def refund_payment(self, amount: float):
        print(f"Issuing PayPal refund of ${amount:.2f} to {self.email}...")


try:
    invalid_object = PaymentProcessor()
except TypeError as error:
    print(f"Error caught: {error}\n")

print("-- Using Credit Card Gateway --")
cc_gateway = CreditCardPayment("1234567890123456")
cc_gateway.process_payment(150.75)
cc_gateway.receipt_footer()

print("--- Using PayPal Gateway ---")
paypal_gateway = PayPalPayment("user@example.com")
paypal_gateway.process_payment(45.00)
paypal_gateway.refund_payment(45.00)
paypal_gateway.receipt_footer()
