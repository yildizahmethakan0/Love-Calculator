print("Your love calculator is calculating your score")
name1 = input("what is your name ")
name2 = input("What is their name ")
###
combined_name = name1 + name2
lower_names = combined_name.lower()

t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
print(f"your love score is {score}.")
