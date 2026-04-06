import string

char = "j"
index = string.ascii_lowercase.index(char)
output = [float(x) for x in "{:05b}".format(index)]
print(output)
