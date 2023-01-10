'''
dataclass 使用方式
    - 使用dataclasses時，__init__() 會呼叫 __post_init__()
    - Dataclasses 搭配 DataFrame

Reference:
    - https://www.maxlist.xyz/2022/04/30/python-dataclasses/
'''
from typing import List
from dataclasses import dataclass, field


# 一般宣告方式
class CommonDeclareProduct:
    def __init__(self, name: str, qty: int) -> None:
        self.name = name
        self.qty = qty



# 使用dataclass 方式
@dataclass
class DataClassProduct:
    name: str
    qty: int
    price: int
    amount: int = field(init=False)
    
    def __post_init__(self):
        self.amount = self.price * self.qty
    

@dataclass
class CustomPurchase:
    products: List[DataClassProduct]
    
    def revenue(self):
        total_revenue = 0
        for p in self.products:
            total_revenue += p.qty * p.price
        return total_revenue
        
        

if __name__ == '__main__':
    cdp = DataClassProduct(name='item-1', price=100, qty=10)
    print(cdp) # DataClassProduct(name='item-1', qty=10, price=100, amount=1000)
    print('amount', cdp.amount) # amount 1000    
    
    cp = CustomPurchase(
        products=[
            DataClassProduct(name='item-1', qty=1, price=100),
            DataClassProduct(name='item-2', qty=2, price=20),
        ]
    )
    
    print(cp.revenue()) # 140