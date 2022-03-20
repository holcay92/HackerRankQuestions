# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
TrueFalseArray = []
for n in range(0, T):

    number_of_A: int = input()
    A = set(map(int, input().split()))
    number_of_B: int = input()
    B = set(map(int, input().split()))
    if A.issubset(B): TrueFalseArray.append("True")
    else: TrueFalseArray.append("False")

for i in TrueFalseArray:
    print(i)