#Returns a list containing the factorials of a chosen integer
def factorialList(n):
    factorial = []
    for i in range(1, n+1):
        if n%i == 0:
            factorial.append(i)
    return factorial

#Returns whether a chosen integer is prime or not
def prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
            break
        else:
            return True

#Returns whether a chosen number is perfect or not
def perfectNumber(n):
    perfectList = []
    for i in range(1, n):
        if n%i == 0:
            perfectList.append(i)
    if sum(perfectList) == n:
        return True
    else:
        return False

