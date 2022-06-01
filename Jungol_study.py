while True:
    s,e= map(int,input().split())
    if 2<=s<=9 and 2<=e<=9:
        break
    else:
        print("INPUT ERROR!")

for i in range(1,10):
    tmp=s
    if s>e:
        while tmp>=e:
            ans=tmp*i
            print(f"{tmp} * {i} =""{:>3}".format(ans), end= "   ")
            tmp-=1
    else:
        while tmp<=e:
            ans=tmp*i
            print(f"{tmp} * {i} =""{:>3}".format(ans), end= "   ")
            tmp+=1
    print()