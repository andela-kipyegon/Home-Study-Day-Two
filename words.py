"""word count program
that splits words and counts them"""
def words(argument):
    """fxn defn words"""
    if isinstance(argument, str):
        wordcount = {}
        for word in argument.split():
            if word in wordcount.keys():
                if word == int:
                    wordcount[word] += 1
                else:
                    wordcount[word] += 1
            else:
                if word.isdigit():
                    word = int(word)
                    wordcount[word] = 1
                else:
                    wordcount[word] = 1
        return wordcount
    else:
        return "please enter a string"
print words("testing test testing 1 testing 1 day day 2")
