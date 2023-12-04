#Day 4 Q 1
def check_winnings(l1,l2):
    g=0
    for i in l1:
        for j in range(len(l2)):
            if i==l2[j]:
                if g<1:
                    g+=1
                else:
                    g=g*2
    print(g)
    ans.append(int(g))
ans=[]
with open("D:/test.txt") as f:
    n=0
    g=0
    for line in f:
        z=line.split("|")
        q=z[0].split(":")
        t=q[1].split(" ")
        c=z[1].split(" ")
        for i in t:
            if i =="":
                t.remove(i)
            if t[len(t)-1]=="":
                t.remove(t[len(t)-1])
        c = [j.strip() for j in c]
        for j in c:
            if j=="":
                c.remove(j)
        check_winnings(t,c)
    print(sum(ans))




