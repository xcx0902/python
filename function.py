def code(x):
    p = x % 10
    if p == 1:
        return "st"
    elif p == 2:
        return "nd"
    elif p == 3:
        return "rd"
    else:
        return "th"

def find(x, a):
    pos = 1
    for i in a:
        if i == x:
            return f"Find {x} in {pos}{code(pos)} number in {a}!"
        pos += 1
    return f"Not find {x} in {a}!"

a = list(map(int, input().split()))
x = int(input())
print(find(x, a))