def calculate_discount(price, discount):
    final_price = price - ((discount/100) * price) # subtract the discount amount from the original
    return final_price

print(calculate_discount(100,50))