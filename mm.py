class flashcard:

    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning

    def __str__(self):
        return self.word+' ( '+self.meaning+' )'

flash=[]
print("welcome to the flashcard ")

while(True):

    word=input('enter word')
    meaning=input('add meaning')
    flash.append(flashcard(word,meaning))
    option=int(input('if you would like to continue press 0 if not press 1'))

    if (option):
        break
print("\n your flashcards")
for i in flash:
    print("<", i)