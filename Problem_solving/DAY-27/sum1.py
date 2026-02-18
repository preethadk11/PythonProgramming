string1,string2=input().split()
if sorted(string1)==sorted(string2):
    print("Anagram")
else:
    print("Not anagram")