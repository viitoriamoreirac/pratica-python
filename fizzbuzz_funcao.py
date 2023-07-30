def fizzbuzz(n):
    a = (n % 3 == 0)
    b = (n % 5 == 0)

    if a and not b:
        return "Fizz"
    if b and not a:
        return "Buzz"
    if a and b:
        return "FizzBuzz"
    if not a and not b:
        return n
