s=[1,2,3,4,5]
i=[]
c=[]
def hanoi(n, s, c, i):
    if (n != 0):
        hanoi(n-1, s, i, c)
        c.append(s.pop())
        hanoi(n-1, i, c, s)
    hanoi(3,i, c, s)
print(s, i, c)

     #def factoriel(n):
    #if (n == 1):
     #   return 1
    #else:
    
       # return n * factoriel (n-1)

       # def fibo(n):
   # if (n == 0) or (n == 1):
       # return 1
   # else:
      #  return fibo(n-1)+fibo(n-2) 

