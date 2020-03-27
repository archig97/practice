#Homework Assignment 5
#Demonstration of understanding of loops

def prime(num):  #function to check for prime numbers
    #i=2
    flag=0
    for i in range(2,num):
        if((num%i)==0):
            flag=1
            break
        i+=1
    return flag


count = 2
print(1)
for i in range(2,101):
    if((count%3)==0) and ((count%5)==0):  #divisible by both 3 and 5
        print("FizzBuzz")
        count+=1
    elif((count%3)==0):  #divisible by 3
        print("Fizz")
        count+=1
    elif((count%5)==0):  #divisible by 5
        print("Buzz")
        count+=1
    elif(prime(count)==0):  #prime
       print("Prime")
       count+=1
    else:
        print(count)
        count+=1
