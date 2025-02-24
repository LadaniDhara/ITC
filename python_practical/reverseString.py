string="hello"
reverse_string = string[::-1]


def reverse (input):
    reverse = ""
    for a in input:
        reverse = a + reverse
    return reverse

input = "hello"
reverse = reverse(input)
print(reverse)