total = 0

while True:
    num = float(input("Enter a number (-999 to stop): "))
    if num == -999:
        break
    total += num

print(f"\nSum of numbers entered: {total}")

