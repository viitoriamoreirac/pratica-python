def fizzBuzz(n):
    i = 1
    while i <= n:
        a = (i % 3 == 0)
        b = (i % 5 == 0)
        if a and b:
            print ("FizzBuzz")
        if a and not b:
            print ("Fizz")
        if b and not a:
            print ("Buzz")
        if not a and not b:
            print (i)
            
        i += 1
