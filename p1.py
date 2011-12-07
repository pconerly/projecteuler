#p1.py
#exactly like the fizzbuzz problem


def fizzbuzz():
    c = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            c += i
    return c

print fizzbuzz()
