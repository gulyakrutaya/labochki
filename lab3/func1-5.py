
st=input("enter a word: ")

def perm(s):

    if len(s)==1:
        return [s]
    
    else:
        permList=[]
        for ind, ch in enumerate(s):
            for miniS in perm(s[:ind]+s[ind+1:]):
                permList.append(ch+miniS)
    return permList

print(perm(st))