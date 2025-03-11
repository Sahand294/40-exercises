class CountingWords:
    def __init__(self,phrase:list):
        t = phrase
        count = {}
        duplictate = []
        for i in t:
            p = i.split(' ')
            for x in p:
                try:
                    if x in duplictate:
                        pass
                    else:
                        count[x] += i.split().count(x)
                        duplictate.append(x)
                except:
                    count[x] = i.count(x)
                    duplictate.append(x)
            duplictate = []
        print(count)
