import json
class JsonActions:
    @staticmethod
    def add(ibn,author,title):
        json3 = JsonActions.read_all()
        if not JsonActions.read('ibn',ibn):
            json3['books'].append({'ibn':ibn,'author':author,'title':title})
        else:
            raise ValueError('that ibn already exists.')
        with open('books.json', 'w', encoding='utf-8') as file:
            json.dump(json3, file, indent=4)

    @staticmethod
    def remove(ibn):
        json3 = JsonActions.read_all()
        for x,i in enumerate(json3['books']):
            if i['ibn'] == int(ibn):
                json3['books'].pop(x)
        with open('books.json','w',encoding='utf-8') as file:
            json.dump(json3,file,indent=4)
    @staticmethod
    def read(key,value):
        json3 = JsonActions.read_all()
        e = True
        for i in json3['books']:
            if i[key] == value:
                return i
        return  False

    @staticmethod
    def read_all():
        with open('books.json','r',encoding='utf-8') as file:
            json3 = json.load(file)
        return json3