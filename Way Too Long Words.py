num=int(input("Enter number of words: "))
for i in range (0, num+1):
    arr=input("Enter the word: ")
    length=len(arr)
    if(length<=10):
        print(arr)
    else:
        wordlist= list(arr)
        print(wordlist[0], end="")
        print(length-2, end="")
        print(wordlist[length-1])
