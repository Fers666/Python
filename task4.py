def check (str1,str2) :
    for i in range(len(str2)):
        if str1[i] == str2[i] or str2[i]=='*':
            ok = 1
        else:
            ok = 0
            break
    return ok

str1=list(input())
str2=list(input())
if (len(str1)) != (len(str2)) and '*' not in str2 :
    ok=0
else :
    if (len(str1)) == (len(str2)) :
        ok=check(str1,str2)
    else :
        if len(str1) < len(str2) :
            while '*' in str2 :
                str2.remove('*')
                if len(str1)==len(str2) :
                    ok=check(str1,str2)
                    break
                else :
                    ok=0
        else :
            while len(str1)!=len(str2):
                str2.insert(str2.index('*'),'*')
                if len(str1)==len(str2) :
                    ok=check(str1,str2)
                    break

if ok==1 :
    print('OK')
else :
    print('KO')
