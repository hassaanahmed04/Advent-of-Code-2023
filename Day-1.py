### Comment one problem code to run other  

#Day 1 q1

with open('D:/test.txt') as diary_file:
    n = 1
    result=0
    for line in diary_file:
       z=[]
       for i in line:
           if i.isnumeric():
               z.append(i)   
       print(z)
       print(z[0]+z[len(z)-1])
       result=result+int(z[0]+z[len(z)-1])
       
       n+=1
       
print(result)


#Day 1 q2

with open('D:/test.txt') as diary_file:
    p1=0
    p2=0

    for line in diary_file:
        p1_d=[]
        p2_d=[]
        for i,c in enumerate(line):
            if c.isdigit():
                p1_d.append(c)
                p2_d.append(c)
            for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    p2_d.append(str(d+1))
        # p1 += int(p1_d[0]+p1_d[-1])
        p2+=int(p2_d[0]+p2_d[-1])
print(p1)
print(p2)
