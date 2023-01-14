babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
answer = 0
checkings = ["aya","ye","woo","ma"]

for word in babbling:
    for checking in checkings:
        word = word.replace(checking,"-")

    for i in range(len(word)):
        if word[i] == '-':
            if i == len(word)-1:
                answer+=1
        else:
            break
    #answer = [answer+1 for i in range(len(word)) if word[i] in '-']

print(answer)