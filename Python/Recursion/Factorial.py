def fact(n):
    if n<0:
        return "This function only works for positive numbers"
    if n==0:  #base case, the factorial of 0 is 1
        return 1
    return n * fact(n-1)  #n*(n-1)*(n-2)*...(n-(n-1)

if __name__=='__main__':
    print(fact(-5))