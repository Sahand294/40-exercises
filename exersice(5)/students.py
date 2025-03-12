import json
class ReadingJson:
    @staticmethod
    def returning_the_data():
        with open('students.json','r',encoding='Utf-8') as file:
            json3 = json.load(file)['students']
            return json3