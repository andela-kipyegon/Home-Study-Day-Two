"""word count program
that splits words and counts them"""
def words(argument):
    """fxn defn words"""
    if isinstance(argument, str):
        wordcount = {}
        #splits the string
        for word in argument.split():
            #checks if string is in word count already
            if word.isdigit():
                digit = int(word)
                #checks if digit is in word count
                if digit in wordcount:
                    wordcount[digit] += 1
                else:
                    wordcount[digit] = 1
            else:
                #checks if digit is in word count
                if word in wordcount:
                    wordcount[word] += 1
                else:
                    wordcount[word] = 1
        return wordcount
print words("testing 1 2 1 3 1  testing")
