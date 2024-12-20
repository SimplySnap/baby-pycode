'''
Numerical Computations and Control Flow**

1. Factorial Function:
   - Write a recursive function factorial(n) that computes the factorial of a non-negative integer n.
   - Include error handling to raise an exception if n  is negative or not an integer.

2. List of Primes:
   - Write a function generate_primes(m) that returns a list of all prime numbers less than or equal to m.

2. Numerical Integration
   - Write a function trapezoidal_rule(f, a, b, n) that computes the numerical integral of a function f over the interval
     [a, b] using the trapezoidal rule with n subintervals.

   - Use this print statement once you have implemented the trapezoidal rule
        print(f"n = {n}, Approximate Integral = {approx}, Error = {error}")
    
        where "approx" is the result from your function and "Error" is the difference between the analytical result
        and the approximated result.

    - Use func as the function to intergrate over.

        def func(x):
            return x**3 + x**2 + x + 5 

    
Submit Python File into Gradescope 
'''

def factorial(n):
   '''Factorial function which computes the factorial of non-negative integer n.'''
   if type(n) != int:
      print("Please insert an integer")
   if n == 1:
     return 1
   elif n<1:
      print("This is not non-negative")
   else:
     return (n*factorial(n-1))


def generate_primes(m):
   '''We start with a prime number 2, and build up primes in a semi-clever'''
   if m == 1:
      return 1
   if m<1:
      return
   primes = [2]
   i = 3
   while i < m:
      isPrime = True
      for j in range(0,len(primes)):
         if i % primes[j] == 0:
            isPrime = False
      if isPrime:
         primes.append(i)
      i+=2 #As primes can only be odd numbers
   return primes

def trapezoidal_rule(f, a, b, n):
   interval = (b-a)/n+1
   total_sum = 0.5 * (f(a) + f(b))

   for i in range(1, n):
      x_i = a + i * interval
      total_sum += f(x_i)
   approx = total_sum * interval
   analytical = (1/4)*b**4 + (1/3)*b**3 + (1/2)*b**2 + 5*b - ((1/4)*a**4 + (1/3)*a**3 + (1/2)*a**2 + 5*a)
   error = abs(approx-analytical)
   print(f"n = {n}, Approximate Integral = {approx}, Error = {error}")
      

   
      



