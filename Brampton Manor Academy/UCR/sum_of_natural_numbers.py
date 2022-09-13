def brute_force(n):
    sum = 0
    for i in range(n+1):
        sum+=i
    return sum

def formula(n):
    sum = (n**2+n)/2
    return sum

n = int(input("enter a number: "))
print(brute_force(n))
print(formula(n))
