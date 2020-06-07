text = input("enter string ")
text = list(text)
# for i in range(len(text)):
#     y = text.count(text[i])
#     if y == 1:
#         print(text[i]+" "+str(i))
#         break
for i in range(len(text)):
    y = i+1
    if text[i] not in text[y:]:
        print(text[i])
        break
