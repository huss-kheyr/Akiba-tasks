customer_name = input("customer: ")
product_name = input("product_name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

total_price = price * quantity
width = 40

print("=" * width)
print("Receipt".center(width))
print("=" * width)
print(f"Customer: {customer_name}")
print("-" * width)
print(f"{'Product':<16}{'Price':>10}{'Qty':>5}{'Total':>9}")
print(f"{product_name:<16}{price:>10.2f}ETB{quantity:>5}{total_price:>9.2f}")
print("-"* width)
print(f"{'Total (ETB)':<16}{total_price:>24.2f}")
print("-" * width)