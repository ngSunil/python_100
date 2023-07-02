# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
class MyGen():
    def divisible_by7(self, n):
        for i in range(0, n):
            if i % 7 == 0:
                yield i


mygen = MyGen()
for i in mygen.divisible_by7(int(input('Please enter a no...'))):
    print(i)
