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
