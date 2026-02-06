words=["one","two","three","four","five","six","seven","eight","nine","ten"]
num=int(input())
n=num
new=[]
digit=0
while(n>0):
    rem=n%10
    new.append(words[rem-1])
    n=n//10
new.reverse()
for i in new:
    print(i,end=" ")

    