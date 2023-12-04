# #Day 4 Q 1
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



#Day 4 Q 2

def total_scratchcards_from_file(file_path):
    def parse_card_line(line):
        parts = line.split('|')
        winning_numbers = list(map(int, parts[0].split()[2:]))
        your_numbers = list(map(int, parts[1].split()))
        return {"winning_numbers": winning_numbers, "your_numbers": your_numbers}
    def count_matching_numbers(winning, your):
        return len(set(winning) & set(your))
    cards = []
    with open(file_path, 'r') as file:
        for line in file:
            cards.append(parse_card_line(line.strip()))
    card_counts = [1] * len(cards)
    for i in range(len(cards)):
        matches = count_matching_numbers(cards[i]["winning_numbers"], cards[i]["your_numbers"])
        for j in range(i + 1, min(i + 1 + matches, len(cards))):
            card_counts[j] += card_counts[i]
    return sum(card_counts)
file_path = "D:/test.txt"
total_cards = total_scratchcards_from_file(file_path)
print(total_cards)