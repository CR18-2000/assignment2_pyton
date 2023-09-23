
def kmer_search(S, k, freq, x):
    #empty dictionary
    frequenza = {}
    pos = {}
    for j in range(0,len(S)-k+1):
        word = S[j:j+k]
        count = frequenza.get(word, 0)
        frequenza[word] = count +1
        position = pos.get(word, [])
        position.append(j)
        pos[word] = position
    L1 = []
    seq = []
    for word in sorted(pos, key=pos.get):
        if frequenza[word] >= freq:
            L1.append(pos[word])
            seq.append(word)
    L2 = []
    for i in range(0,len(L1)):
        word = seq[i]
        counter = 0
        if word[x] == "A":
            word = word[0:x] + "C" + word[x+1:len(word)]
            y = frequenza.get(word)
            if y != None:
                counter += y
            word = word[0:x] + "G" + word[x+1:len(word)]
            y = frequenza.get(word)
            if y != None:
                counter += y
            word = word[0:x] + "T" + word[x+1:len(word)]
            y = frequenza.get(word)
            if y != None:
                counter += y
        elif word[x] == "C":
            word = word[0:x] + "A" + word[x+1:len(word)]
            y = frequenza.get(word)
            if y != None:
                counter += y
            word = word[0:x] + "G" + word[x+1:len(word)]
            y = frequenza.get(word)
            if y != None:
                counter += y
            word = word[0:x] + "T" + word[x+1:len(word)]
            y = frequenza.get(word)
            if y != None:
                counter += y
        elif word[x] =="G":
            word = word[0:x] + "A" + word[x+1:len(word)]
            y = frequenza.get(word)
            if y != None:
                counter += y
            word = word[0:x] + "C" + word[x+1:len(word)]
            y = frequenza.get(word)
            if y != None:
                counter += y
            word = word[0:x] + "T" + word[x+1:len(word)]
            y = frequenza.get(word)
            if y != None:
                counter += y
        else: #T
            word = word[0:x] + "C" + word[x+1:len(word)]
            y = frequenza.get(word)
            if y != None:
                counter += y
            word = word[0:x] + "G" + word[x+1:len(word)]
            y = frequenza.get(word)
            if y != None:
                counter += y
            word = word[0:x] + "A" + word[x+1:len(word)]
            y = frequenza.get(word)
            if y != None:
                counter += y
        L2.append(counter)
    return L1, L2


def spet_location(S, k, p):
    frequenza = {}
    pos = {}
    for j in range(0,len(S)-k+1):
        word = S[j:j+k]
        count = frequenza.get(word, 0)
        frequenza[word] = count +1
        position = pos.get(word, [])
        position.append(j)
        pos[word] = position
    #non so se è più veloce scorrere sulle parole nel range e controllare
    #mi sa che è un for in meno
    freq = -1
    candidate = None
    for word in sorted(frequenza, key=frequenza.get):
        if frequenza[word] <= 5:
            if freq == -1 or freq == frequenza[word]:
                for i in pos[word]:
                    if i >= p-2*k and i < p-k:
                        counter = 0
                        for j in range(0, k):
                            if word[j] == "C" or word[j] == "G":
                                counter += 1
                        if counter >= 0.35*k and counter <= 0.65*k:
                            if candidate == None:
                                candidate = i
                                freq = frequenza[word]
                            else:
                                if abs(p-i) < abs(p-candidate):
                                    candidate = i
        else:
            break
    return candidate


def get_my_pqs():
    with open("seq.txt") as f: S = f.read().rstrip()
    k = 40
    #p va da 2*k a n
    found = False
    notFound = False
    p = 2*k
    list = []
    while (not found or not notFound) and p<len(S):
        if p != 180500:
            a = spet_location(S, k, p)
            if a == None and notFound == False:
                notFound = True
                list.append((p,a))
            elif a != None and found == False:
                found = True
                list.append((p,a))
        p +=1
    p = 180500
    list.append((p, spet_location(S, k, p)))
    return list

print(get_my_pqs())