t = int(input())
for i in range(1, t + 1):
    nestingDepth = 0
    s = ""
    digits = input()
    digitsArray = list(map(int, digits))
    for j in range(0, len(digitsArray)):
        if digitsArray[j] > nestingDepth:
            s += ('(' * (digitsArray[j] - nestingDepth)) + digits[j]
            nestingDepth = digitsArray[j]
        elif digitsArray[j] < nestingDepth:
            s += (')' * (nestingDepth - digitsArray[j])) + digits[j]
            nestingDepth = digitsArray[j]
        else:
            s += digits[j]
    s += ')' * nestingDepth
    print("Case #{}: {}".format(i, s))