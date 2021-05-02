# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(1,n+1):
    str=input()
    print(str[::2], str[1::2])
