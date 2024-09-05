p = input()
all_g = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
count = 0
for i in p:
    if i in all_g:
        count += 1

print('Кол-во гласных:', count)