# We have received a text string in reverse
# solve it and return it as a text with the format
# "Name" "Last Name" got a grade of "Grade"
string = "zerep nauJ, 01"
string = string[::-1]

print(string[4:], "got a grade of ", string[:3])