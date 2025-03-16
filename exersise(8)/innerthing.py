def multiplyer_creater(x):
    def multiplyer(y):
        return x*y
    return multiplyer
a = multiplyer_creater(100)
print(a(8))