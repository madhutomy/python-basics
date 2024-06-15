line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
vertical_pos = position[0]
horizontal_pos = int(position[1])
if horizontal_pos == 1:
    if vertical_pos == "A":
        line1[0] = 'X'
    elif vertical_pos == "B":
        line1[1] = 'X'
    else:
        line1[2] = 'X'
elif horizontal_pos == 2:
    if vertical_pos == "A":
        line2[0] = 'X'
    elif vertical_pos == "B":
        line2[1] = 'X'
    else:
        line2[2] = 'X'
elif horizontal_pos == 3:
    if vertical_pos == "A":
        line3[0] = 'X'
    elif vertical_pos == "B":
        line3[1] = 'X'
    else:
        line3[2] = 'X'
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
