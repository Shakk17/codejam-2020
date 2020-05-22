size = int(input())
strings = []
for i in range(size):
    text = input()
    string = ""
    # Insert parenthesis.
    for char in text:
        digit = int(char)
        string += '(' * digit + char + ')' * digit

    # Remove redundant parenthesis.
    while ")(" in string:
        string = string.replace(")(", "")

    strings.append(string)

for i, string in enumerate(strings):
    print("Case #{}: {}".format(i + 1, string))

