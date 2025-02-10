# https://dmoj.ca/problem/ccc02s2
def find_gcf(x, y):
    gcf = 1
    for i in range(2, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            gcf = i

    return gcf


numerator = int(input())
denominator = int(input())

whole_number = numerator // denominator
new_numerator = numerator - whole_number * denominator

if new_numerator == 0:
    print(whole_number)
else:
    gcf = find_gcf(new_numerator, denominator)

    new_numerator /= gcf
    denominator /= gcf

    if whole_number == 0:
        print("{0}/{1}".format(int(new_numerator), int(denominator)))
    else:
        print("{0} {1}/{2}".format(whole_number, int(new_numerator), int(denominator)))
