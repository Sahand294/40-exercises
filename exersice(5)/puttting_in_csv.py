import csv
class PuttingInAVGGrades:
    def putting_it_in(self,data):
        with open('avg.csv','w',newline='') as file:
            fileheader = data[0]
            writer = csv.DictWriter(file,fileheader)
            writer.writeheader()
            writer.writerows(data)
    def __init__(self,name,grade):
        data = self.reading_it()
        data.append({'name':name,'grade':grade})
        self.putting_it_in(data)
    def reading_it(self):
        with open('avg.csv','r') as files:
            file = csv.DictReader(files)
            data = []
            for i in file:
                data.append({key:value for key,value in i.items()})
            return data