# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
phone=dict()
for i in range(n):
    data=input()
    data=data.split()
    phone[data[0]] = phone.get(data[0],data[1])

while(1):
    try:
        q=input()
        if q in phone:
            print(str(q)+"="+str(phone[q]))
        else:
            print("Not found")
    except:
        break
