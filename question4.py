# program to guess the amount of candies in a jar
candies = 1
while(candies<200):
    if (candies % 5== 2):
        if (candies % 6 == 3):
           if (candies % 7 == 2):
              print("The number of candies is ",candies)
              break
    candies+=1
