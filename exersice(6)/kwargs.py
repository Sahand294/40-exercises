class AVGAndSum:
    @staticmethod
    def doesit(list_of_numbers:list,dict:dict):
        """

        list_of_numbers as many numbers as you want can be in it
        the dict needs to have words and numbers
        """
        sums = 0
        sum = 0
        avg = 0
        n = 0
        for i in list_of_numbers:
            sum += i
        for i in dict.values():
            if isinstance(i,int):
                sums += i
                n += 1
        avg = sums/n
        return {'avg of all the numbers in the dict':avg,'sum of the numbers in the list':sum}
mixed_dict = {
    "apple": 12,"banana": "yellow","cherry": 45,"date": "sweet","elephant": 78,
    "flower": "beautiful","grape": 23,"hat": "red","ice": 56,"jacket": "warm"}
numbers = [12, 45, 78, 23, 56, 89, 34, 67, 90, 21, 43, 76, 88, 99, 54, 32]
print(AVGAndSum.doesit(numbers,mixed_dict))

