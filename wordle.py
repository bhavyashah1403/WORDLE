word="pelsi"
g_word=input()
flag=0
res=[1,2,3,4,5]
for i in range(5):
    for j in range(5):
        if word[j]==g_word[i]:
            if i==j:
                res[i]="G"
            else:
                res[i]="Y"



for i in range(5):
    if str(res[i]).isdigit():
        res[i]='R'

print(res)
