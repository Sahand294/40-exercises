class OddSum:
    @staticmethod
    def d(numbers:list):
        sum = 0
        for i in numbers:
            division = i/2
            c = int(str(division).split('.')[1])
            if c != 0:
                sum += i
        return sum
o =OddSum
print(o.d([1,2,3,4,5]))