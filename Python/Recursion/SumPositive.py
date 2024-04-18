#Sum positive integers of n+(n-2)+(n-4)+... until n-x<=0

def SumPositive(n):
      if n<=0:
         return 0    
      return n + SumPositive(n-2)

if __name__=='__main__':
      print(SumPositive(5))