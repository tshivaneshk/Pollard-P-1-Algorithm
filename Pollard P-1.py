import math
def main():
    a=int(input("Enter A Number: "))
    if (a<0):
        print("Enter a positive numbers!")
        return 0
    
    result= math.gcd(a,2)
    if result==1:
        Answer=pollard(a)
        print("\nFactors of {} are: {} , {}".format(a,Answer,a//Answer))

def factorial(B):
    X=1
    for i in range(2,B+1):
        X=X*i
    return X

def pollard(a):
    for i in range(1,a):
        power=factorial(i)
        value=pow(2,power,a)-1
        non_trivial=math.gcd(value,a)
        if non_trivial!=1:
            return non_trivial
            
main()