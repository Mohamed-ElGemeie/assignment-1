def calculate_sum(*args):
  """Calculates the sum of any number of arguments.

  Args:
    *args: Any number of integer or floating-point arguments.

  Returns:
    The sum of the input numbers.
  """

  sum = 0
  for arg in args:
    sum += arg
  return sum


def check_prime(number):
  """Checks if a given integer is prime or not.

  Args:
    number: A single integer argument.

  Returns:
    Display whether the input number is prime or not.
  """

  if number <= 1:
    print("The number is not prime.")
    return
  for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
      print("The number is not prime.")
      return
  print("The number is prime.")


def gcd(a, b):
  """Calculates the greatest common divisor (GCD) of two integers.

  Args:
    a: An integer.
    b: An integer.

  Returns:
    The greatest common divisor of the two input numbers.
  """

  while b:
    a, b = b, a % b
  return a

def check_pangram(string):
  """Checks if a given string is a pangram (contains all letters of the alphabet
  at least once).

  Args:
    string: A single string.

  Returns:
    Return True if the input string is a pangram, otherwise False.
  """

  alphabet = set("abcdefghijklmnopqrstuvwxyz")
  for letter in string.lower():
    alphabet.remove(letter)
  return not alphabet

def word_count(sentence):
  """Counts the number of words in a given sentence.

  Args:
    sentence: A single string (a sentence).

  Returns:
    The count of words in the input sentence.
  """

  words = sentence.split()
  return len(words)


def fahrenheit_to_celsius(fahrenheit):
  """Converts a temperature from Fahrenheit to Celsius.

  Args:
    fahrenheit: A single floating-point number representing a temperature in
      Fahrenheit.

  Returns:
    The temperature converted to Celsius.
  """

  celsius = (fahrenheit - 32) * 5 / 9
  return celsius

def generate_fibonacci(N):
    if N <= 0:
        return "Enter a positive number for N."

    fib_sequence = [0, 1]

    while len(fib_sequence) < N:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return " ".join(map(str, fib_sequence[:N]))
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

def prime_factorization(number):
  """Finds and returns the prime factors of a given positive integer.

  Args:
    number: A single positive integer.

  Returns:
    A list of prime factors of the input number.
  """

  prime_factors = []
  for i in range(2, int(number**0.5) + 1):
    while number % i == 0:
      prime_factors.append(i)
      number //= i
  if number > 1:
    prime_factors.append(number)
  return prime_factors

def calculate_average(*args):
    """
    Args:
        *args: Any number of integer or floating-point arguments.

    Returns:
        The average of the input numbers.
    """

    average = sum(args) / len(args)
    return average

def reverse_string(string):

  reversed_string = ""
  for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]
      
  return reversed_string
