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

def reverse_string(string):

  reversed_string = ""
  for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]
      
  return reversed_string
