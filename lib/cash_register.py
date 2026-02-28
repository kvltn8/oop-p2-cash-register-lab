#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0
    
    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.last_transaction = price * quantity
        
        # Add each item to the list (quantity times)
        for i in range(quantity):
            self.items.append(item)
    
    def apply_discount(self):
        if self.discount > 0:
            # Calculate discount amount
            discount_amount = self.total * (self.discount / 100)
            self.total = int(self.total - discount_amount)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
    
    def void_last_transaction(self):
        # Subtract last transaction from total
        self.total -= self.last_transaction
        
        # Remove the last item(s) from items list
        if len(self.items) > 0:
            self.items.pop()
        
        # Reset last transaction
        self.last_transaction = 0