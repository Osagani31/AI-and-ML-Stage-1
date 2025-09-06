marks = []

for i in range(10):
    mark = float(input(f"Enter mark for student {i+1}: "))
    marks.append(mark)

max_mark = max(marks)
min_mark = min(marks)
avg_mark = sum(marks) / len(marks)

print(f"\nMaximum mark: {max_mark}")
print(f"Minimum mark: {min_mark}")
print(f"Average mark: {avg_mark:.2f}")
