### Comment one problem code to run other  

#Day 2 q1

def check(q,z):

    green=0
    blue=0
    red=0
    for p in range(len(q)):
        print("game  ",z)
        z=int(z)
        if "blue" in q[p] and  int(q[p-1])>14:
            g.remove(z)
            break
        elif "green" in q[p] and int(q[p-1])>13:
            g.remove(z)
            break
        elif "red" in q[p] and int(q[p-1])>12:
            g.remove(z)
            break
        else:
            if z not in g:
                g.append(z)
    print(sum(g))   
       
g=[] 
with open('D:/test.txt') as f:
    n=0
    
    game=0
    for  i in f:
        z=i.split(':')
        q=z[1].split(" ")
        z=z[0].split(" ")

        check(q,z[1])
    print(g)



# Day 2 q 2
def check(q,z):
    green=0
    blue=0
    red=0
    for p in range(len(q)):
        if "blue" in q[p] and int(q[p-1])>blue:
            blue=int(q[p-1])
        if "green" in q[p] and int(q[p-1])>green:
            green = int(q[p-1])
        if "red" in q[p] and int(q[p-1])>red:
            red=int(q[p-1])

    tt=blue*red*green

    g.append(tt)
    
       
g=[] 

with open('D:/test.txt') as f:
    n=0
    game=0
    for  i in f:
        z=i.split(':')
        # print(z)
        q=z[1].split(" ")
        z=z[0].split(" ")
        
        check(q,z[1])
    print("total game",sum(g))