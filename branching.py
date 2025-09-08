
kwh = int(input("Enter the KW hours used: "))
rate1 = 7.633
rate2 = 9.259
if kwh <= 1000:
    total = kwh * rate1
else:
    total = (1000 * rate1) + ((kwh - 1000) * rate2)
amount_owed = total / 100
print(f"Amount owed is ${amount_owed}")

