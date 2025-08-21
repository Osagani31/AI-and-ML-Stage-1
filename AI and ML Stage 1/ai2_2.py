for i in range(5):
    mark = float(input(f"Enter mark {i+1}: "))

    if mark > 75:
        grade = "A"
    elif 65 <= mark <= 75:
        grade = "B"
    elif 55 <= mark <= 64:
        grade = "C"
    elif 45 <= mark <= 54:
        grade = "S"
    else:
        grade = "F"
    
    print(f"Mark: {mark} → Grade: {grade}")
