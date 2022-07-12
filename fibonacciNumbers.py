def FibonacciNumbers(n):
    a = 1;
    b = 1;
    i = 3;
    while(i<=n):
        c = a+b;
        a = b;
        b = c;
        i+=1;
    return(a,b);
def FibonacciNumbersRecursion(n):
    if(n == 0):
        return n;
    elif(n == 1):
        return n;
    else:
        return FibonacciNumbersRecursion(n-1)+FibonacciNumbersRecursion(n-2);
FibonacciNumbers(77);
FibonacciNumbersRecursion(7);


