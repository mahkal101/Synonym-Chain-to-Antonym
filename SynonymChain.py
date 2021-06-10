from textblob import Word



def getAntonyms(word):
  for lemma in word.synsets[0].lemmas()[0].antonyms():
        return lemma.name()



def getSynonyms(word):
    synonyms = set()
    for synset in Word(word).synsets:
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    return synonyms
                
wordInput = Word(input('Enter a word: '))
answer = []
antonym = getAntonyms(wordInput)
if antonym == None:
    print("There are no antonyms for", wordInput)
else:
    synonyms = getSynonyms(wordInput)
    again = True
    answer = [antonym]
    while again:
        for syn in synonyms:
            synonyms = synonyms.union(getSynonyms(syn))
            if antonym in synonyms:
                answer.append(syn)
                antonym = syn
                synonyms = getSynonyms(wordInput)
                if antonym in synonyms:
                    answer.append(antonym)
                    again = False
                break
            
if len(answer) > 0:
    answer.pop()
print("\nThe word chain is:")
for chain in answer:
    print(chain)
