# Задача 5. (дополнительно) Есть текст. Пользователь ничего не вводит.
# На выходе указать, сколько различных слов было в тексте
text = "My mother bought me a nice suit and new shoes. \
We went to the shop together and chose a grey suit. I tried it on. \
It was my size and suited me well. I looked great. \
Mother paid money for the suit and we brought it home. \
It's a pity I didn't try the shoes on. They were the wrong size. \
So my mother changed them for the bigger size. \
And now they are OK. Frankly speaking, I don't like shopping. \
There are more interesting things.".lower()
text = text.split(" ")
j = 0
for i in text:
    if i[-1] in '''.,:;"?!-()''':
        text[j] = i[:-1]
    elif i[0] in '''.,:;"?!-()''':
        text[j] = i[1:]
    j += 1
text_set = set(text)
print(len(text_set))