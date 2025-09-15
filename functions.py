def circle_area(pi, radius):
    return pi * (radius ** 2)
def total_due(money, tax_rate):
    return money + (money * tax_rate)
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5/9)
pi = 3.1416
radius = float(input("Enter radius of the circle: "))
area = circle_area(pi, radius)
print(f"Area of the circle: {area:.2f}")
money = float(input("Enter the money amount: "))
tax_rate = float(input("Enter tax rate (as a decimal, e.g. 0.06 for 6%): "))
total = total_due(money, tax_rate)
print(f"Total due: {total:.2f}")
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"Temperature in Celsius: {celsius:.5f}")