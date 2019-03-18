for i in range(1,40):
    try:
        txt = open('File_{}.txt'.format(i), 'r', encoding='cp1253') #encoding for greek
        txt.read()
        txt.close()
    except:
        txt = open('File_{}.txt'.format(i), 'a', encoding='cp1253')
        txt.write(str(i))
        txt.close()
        break

txt = open('File_1.txt', 'r', encoding='cp1253')
x = txt.read()
print(x)
txt.close()
