code = {'a': '+-','b': '-+++','c': '-+-+','d': '-++','e': '+','f': '++-+',
    'g': '--+','h': '++++','i': '++','j': '+---','k': '-+-','l': '+-++',
    'm': '--','n': '-+','o': '---','p': '+--+','q': '--+-','r': '+-+','s': '+++',
    't': '-','u': '++-','v': '+++-','w': '+--','x': '-++-','y': '-+--','z': '--++',
    '1': '+----','2': '++---','3': '+++--','4': '++++-','5': '+++++','6': '-++++',
    '7': '--+++','8': '---++','9': '----+','0': '-----'}

user_input = str(input("Please input anything you'd like, except for symbols:\n"))
convert = []

try:
    for i in user_input:
        if i == ' ':
            n = ' '
        else:
            n = i.replace(i, code[i])
        convert.append(n)
except:
    print('no symbols')

translated = ''.join(convert)
print(translated)