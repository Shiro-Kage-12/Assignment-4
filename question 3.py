# program to make random multiplication tables
import random
i=1
while(i<=10):
    a = random.randint(1,10)
    b = random.randint(1,10)
    print(a,"x",b,"= ?")
    ans = int(input())
    if(ans == a*b):
        print("Correct!")
    else:
        print("Incorrect. The correct answer is ",a*b)
    i+=1