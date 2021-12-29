



def counter(text,word):
    count = 0
    for a in text:
        if a == word:
            count += 1
    return count

def countWords(input):    
    result={}
    for word in input:
        if word not in result.keys():
            result[word] = counter(input,word)           
    print(f"Map: {result}")

#banana

if __name__ == '__main__':
    countWords('banana')