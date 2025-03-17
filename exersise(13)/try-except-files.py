with open('hi','r') as file:
    text = file.read()
    if text == '':
        raise ValueError("file can't be empty")
    if '.' in text:
        raise TypeError('integer values only.')
    text = list(text)
    for i in text:
        if i not in '0123456789 ':
            raise TypeError('integer values only.')