from re import *

D = dict()
s = input()

while s:
    #print(s.find('int'))
    #print(D)
    s = s.replace(' ', '')
    if s[0] == '#':
        s = input()
        continue

    if findall('[^A-Za-z_][0-9]+E[-+]',s):
        #print(findall('[^A-Za-z_][0-9]+E[-+]',s))
        print("Syntax error")
        s = input()
        continue

    if '.' in s or s.find('**') >= 0 or s.find('int') >= 0 or s.find('//') >= 0:
        print("Syntax error")
        #print("mda")
        s = input()
        continue

    if '/' in s:
        s = sub('/', '//', s)

    s = sub(r'([A-Za-z_]+[A-Za-z_0-9]*)', r'_c_\1', s)

    if '=' in s:
        match_name = search('(.*?)=', s)
        name = match_name.groups()[0]

        if not findall('[A-Za-z_]+[A-Za-z_0-9]*', name):
            print('Assignment error')
            s = input()
            continue
        ind = s.index('=')
        #name = '_c_' + name

        try:
            D[name] = eval(s[ind+1:], None, D)
        except NameError:
            #print("tut")
            print('Name error')
            s = input()
            continue
        except SyntaxError:
            print('Syntax error')
            #print("tut")
            s = input()
            continue
        except TypeError:
            print('Syntax error')
            #print('kek')
            s = input()
            continue
        except:
            print('Runtime error')
            s = input()
            continue

    else:
        try:
            print(eval(s, None, D))
        except NameError:
            #s = sub('[A-Za-z_]+[A-Za-z_0-9]*', '_c_[A-Za-z_]+[A-Za-z_0-9]*', s)
            print('Name error')
            #print('tam')
        except SyntaxError:
            print('Syntax error')
            #print('tam')
        except TypeError:
            print('Syntax error')
            #print('lala')
        except:
            print('Runtime error')

    s = input()
