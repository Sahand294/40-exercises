class sorting:
    def __init__(self):
        with open('students','r') as file:
            t = file.read()
            u = list(t.split(','))
        y = set(u)
        s = []
        for i in y:
            s.append(i)
        s.sort()
        i = str(s)
        o = i[1:-1]
        o = o.replace('"','')
        o = o.replace("'","")
        o = o.replace(" ","")
        #for x,i in enumerate(o):
         #   if i == '"' or i == "'":
          #      o.remove(x)
        with open('students','w') as text:
            text.write(o)
sorting()