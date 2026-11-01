scores = []

print("Enter the quiz scores. Enter -1 to finish: ")

while True:
    score = int(input("Enter score (0-100)"))
    if score == -1:
        break
    if score <0 or score > 100:
        print("Invalid Sore. Try again")
        continue

    scores.append(score)

total = 0

for score in scores:
    total += score

    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "Fail"
    print(f"Score: {score} -> Grade: {grade}")

if(len(scores) == 0):
    pass
else:
    average = total / len(scores)
    print(f"\nAverage Score: {average:.2f}")

