#Write a program to calculate the value of 'a' to the power of 'b'

def power(a,b):

    if b==1:
        return a
    
    return a * power(a,b-1)

if __name__ =="__main__":
    print(power(5,3))