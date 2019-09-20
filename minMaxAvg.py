def s_min(numbers):
    minNumber=numbers[0]
    for i in range(1,len(numbers)):
        if minNumber>numbers[i]:
            minNumber=numbers[i]
    return minNumber

def s_max(numbers):
    maxNumber=numbers[0]
    for i in range(1,len(numbers)):
        if maxNumber<numbers[i]:
            maxNumber=numbers[i]
    return maxNumber

def s_avg(numbers):
    avgNumber=0
    for i in range(len(numbers)):
        avgNumber+=numbers[i]
    avgNumber/=len(numbers)
    return avgNumber

def examine():
    try:
        num=int(input(""))
        return num
    except:
        return "NO"

N=input("How much number do you want? ")
while not(N.isdigit()):
        print("Give a number instead!")
        N=input("")

N=int(N)
nums=[]
print("Give the numbers by hitting ENTER!")
for i in range(N):
    boolean=examine()
    while boolean=="NO":
        boolean=examine()
    nums.append(boolean)
    
print("The min:",s_min(nums),"The max:",s_max(nums),"The avg:",s_avg(nums))

