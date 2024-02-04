
st=input("enter a string: ")

def rev(s):

    newSt=""  #new string for output

    ind=len(s)-1  #last letter

    while ind>=0:

        endInd=ind  #index of the end of the word

        while ind>=0 and s[ind]!=" ":
            ind-=1   #searching the index of whitespace

        newSt+=s[ind+1:endInd+1]+" "  #adding a word to new str

        ind-=1  #setting index to the end of the next word considering every word is sep by 1 space. if not while ind>=0 and s[ind]==" "

    print(newSt)

rev(st)