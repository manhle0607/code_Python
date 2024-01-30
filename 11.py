import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome_prime(num):
    if not is_prime(num) or num == int(str(num)[::-1]):
        return False
    return True

def generate_palindrome_primes(upper_limit):
    palindrome_primes = [str(num) for num in range(11, upper_limit + 1) if is_palindrome_prime(num) and int(str(num)[::-1]) <= upper_limit]
    return " ".join(palindrome_primes)

def main():
    test_cases = int(input("Enter the number of test cases: "))
    for _ in range(test_cases):
        upper_limit = int(input())
        result = generate_palindrome_primes(upper_limit)
        print(result)

if __name__ == "__main__":
    main()