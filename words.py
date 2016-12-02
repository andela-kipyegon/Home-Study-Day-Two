"""word count program
that splits words and counts them"""
def words(argument):
    """fxn defn words"""
    if isinstance(argument, str):
        wordcount = {}
        #splits the string
        for word in argument.split():
            #checks if string is in word count already
            if word in wordcount.keys():
                if word == int:
                    wordcount[word] += 1
                else:
                    wordcount[word] += 1
            else:
                #store digit item as int
                if word.isdigit():
                    word = int(word)
                    wordcount[word] = 1
                else:
                    wordcount[word] = 1
        return wordcount
    else:
        return "please enter a string"

