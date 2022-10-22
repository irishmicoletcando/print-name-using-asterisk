# letter I
for row in range(7):
  for column in range(5):
    if column == 2 or ((row == 0 or row == 6) and column!=2):
      print("*", end="")
    else:
      print(end=" ")
  print()