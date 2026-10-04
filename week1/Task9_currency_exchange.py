amount_usd = float(input("Amount in USD: "))
exchange_rate = float(input("1 USD = "))

amount_birr = amount_usd * exchange_rate
width = 40

print("=" * width)
print("CURRENCY EXCHANGE".center(width))
print("=" * width)
print()
print(f"USD Amount: {amount_usd:.2f} USD")
print()
print(f"Exchange rate: 1 USD = {exchange_rate:.2f} ETB")
print()
print(f"ETB amount: {amount_birr:.2f} ETB")
print("=" * width)

