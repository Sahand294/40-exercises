try:
    with open('his','r') as file:
        text = file.read()
        if text == '':
            raise ValueError('the file is empty')
except FileNotFoundError:
    raise FileNotFoundError('no such file')