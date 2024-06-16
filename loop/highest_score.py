scores = input()
highest_score = 0
for i in range(0, len(scores)):
    scores[i] = int(scores[i])
    if scores[i] > highest_score:
        highest_score = scores[i]

print(f"The highest score in the class is: {highest_score}")
