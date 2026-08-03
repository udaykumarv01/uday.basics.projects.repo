A=[8,5,2]
B=[9,6,3]

num_A=0
for n in A:
    num_A=num_A*10 + int(n)

rev_A=0
while num_A>0:
    rev_A = rev_A*10 + num_A%10
    num_A//=10
print(rev_A)

num_B=0
for n in B:
    num_B = num_B*10 + int(n)

rev_B=0
while num_B>0:
    rev_B = rev_B*10 + num_B%10
    num_B//=10
print(rev_B)

total=int(rev_A)+int(rev_B)
result=[int(x) for x in list(str(total))]
print(result)