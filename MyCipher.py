import math
listofprimes=[0]*26
smalllistofprimes=[0]*26
smalllistofnos=[0]*10
listofalphabets=[None]*62

for i in range(26):
    listofalphabets[i] = chr(65+i)
j=0
for i in range(26,52,1):
    listofalphabets[i] = chr(97+j)
    j=j+1
j=0
for i in range(52,62,1):
    listofalphabets[i] = chr(48+j)
    j=j+1

z=0
j=1
count = 23
i=6
listofprimes[0]=102
listofprimes[1]=103
listofprimes[2]=105
while(count!=0):
    flag = 0
    for j in range(1, int(math.sqrt(i))+1, 1):
        if i%j ==0:
            flag = flag+1
    if flag ==1:
        if int(len(str(i)))==2 or int(len(str(i)))==1 :
            x = i+100
        else:
            x=i
        listofprimes[z+3]=x
        z=z+1
        count = count-1
    i=i+1
listofprimes.reverse()
#Removing the 0s
# while(0 in listofprimes):
#     listofprimes.remove(0)
countdown=26
i=0
while(countdown!=0):
    smalllistofprimes[i]=listofprimes[i]+100
    countdown = countdown-1
    i= i+1
for i in range(10):
    smalllistofnos[i]=chr(65+i)+chr(65+i)+chr(65+i)

keys=listofprimes+smalllistofprimes+smalllistofnos

sbox=dict(zip(listofalphabets, keys))
print(sbox)
#Sbox created.
PT=[]
RevPT=[]
CT=[]
PT=input("Enter the Plaintext here:")
RevPT=PT[::-1]

for i in RevPT:
    for j in sbox.keys():
        if i==j:
            CT.append(sbox[j])
print("The Cipher Text is:")
print(CT)
#Encryption Completed

rev_ans=[]
sbox_key_list=list(sbox.keys())
sbox_value_list=list(sbox.values())

for i in CT:
    for j in sbox.values():
        if i==j:
            rev_ans.append(sbox_key_list[sbox_value_list.index(j)])

rev_ans.reverse()
PT=[]
PT=rev_ans
print("The Plain Text is:")
print(PT)
