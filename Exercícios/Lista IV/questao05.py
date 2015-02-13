# coding=utf-8
texto = '''The Python Software Foundation and the global Python community
 welcome and encourage participation by everyone. Our community is based on
 mutual respect, tolerance, and encouragement, and we are working to help each
 other live up to these principles. We want our community to be more diverse:
 whoever you are, and whatever your background, we welcome you.'''
lista = texto.split()
palavras = 0
for x in lista:
    x = x.lower()
    if x[-1:] in ", . :":
        x = x[:-1]
    y = 0
    while y < len(x) and len(x) > 4:
        if x[y] in "python":
            palavras += 1
        y += 1
print(palavras)
