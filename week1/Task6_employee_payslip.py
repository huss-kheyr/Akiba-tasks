
employee_name = input("Employee name: ")
basic_salary = float(input("Basic salary: "))
transport_allowance = float(input("Transport allowance: "))
food_allowance = float(input("Food allowance: "))

gross_salary = basic_salary + transport_allowance + food_allowance
width = 50

print("=" * width)
print("EMPLOYEE PAYSLIP".center(width))
print("=" * width)
print()
print(f"Employee: {employee_name}")
print()
print(f"{'Basic Salary:':<16} {basic_salary:>10.2f}")
print(f"{'Transport allowance:':<16} {transport_allowance:>10.2f}")
print(f"{'Food allowance:':<16} {food_allowance:>10.2f}")
print("-" * width)
print(f"{'Gross salary(ETB):'}: {gross_salary:>10.2f}")
print("=" * 60)


