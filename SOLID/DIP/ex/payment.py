from abc import ABC, abstractmethod

class IPayment(ABC):
  
    @abstractmethod
    def pay(self, amount: int) -> None:
        pass
      
      
class PaymentProcessor:
  
    def __init__(self, iPayment: IPayment) -> None:
        self.iPayment = iPayment

    def execute_payment(self, amount: int) -> object:
        ''' execute the process of payment. '''
        self.iPayment.pay(amount)


class CreditCardPayment(IPayment):
    ''' using credit card to pay money. '''
    def pay(self, amount: int) -> None:
        print(f'paid ${amount} via credit card.')
        return super().pay(amount)
      

class PayPalPayment(IPayment):
    ''' using PayPal to pay money. '''
    def pay(self, amount: int) -> None:
        print(f'paid ${amount} via PayPal.')
        return super().pay(amount)
      
      
if __name__ == '__main__':
    ccp = CreditCardPayment()
    pp = PaymentProcessor(ccp)
    pp.execute_payment(100) # paid $100 via credit card.
    
    ppp = PayPalPayment()
    pp2 = PaymentProcessor(ppp)
    pp2.execute_payment(50) # paid $50 via PayPal.
