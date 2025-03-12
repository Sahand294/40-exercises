from students import ReadingJson
from puttting_in_csv import PuttingInAVGGrades
class CalculatingTheAVGGrade:
    def __init__(self):
        json3 = ReadingJson.returning_the_data()
        avg = []
        for i in json3:
            grade = self.calculate(i['grades'])
            avg.append({'name':i['name'],'avg grade':grade})
        for i in avg:
            PuttingInAVGGrades(i['name'],i['avg grade'])
    def calculate(self,grades):
        sum = 0
        n = 0
        for i in grades:
            sum += i
            n += 1
        avg = sum/n
        return avg
c = CalculatingTheAVGGrade
c()