# Enter your code here. Read input from STDIN. Print output to STDOUT
actual = list(map(int, input().split()))
d1, m1, y1 = actual

expected = list(map(int, input().split()))
d2, m2, y2 = expected

if y1 > y2:
    print("10000")
elif y1==y2:
    if(m1 > m2):
        print(500*(m1-m2))
    elif(m1==m2 and d1>d2):
        print(15*(d1-d2))
    else:
        print("0")
else:
    print("0")
        
