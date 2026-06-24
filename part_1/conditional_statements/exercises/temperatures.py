fahren = int(input("Please type in a temperature (F): "))

celsius = (fahren - 32) / 1.8

print(f"{fahren} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print("Brr! It's cold in here!")