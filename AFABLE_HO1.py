

def compute_average(numbers):
    return sum(numbers) / len(numbers)

def compare_avg_with_length(avg, word_length, word):
    if word_length > avg:
        print(f"The length of the word '{word}' is greater than the average.")
    elif word_length < avg:
        print(f"The length of the word '{word}' is less than the average.")
    else:
        print(f"The length of the word '{word}' is equal to the average.")

word = input("Enter a word: ")

word_length = len(word)

number = []
for j in range(word_length):
    num = int(input(f"Enter number {j+1}: "))
    number.append(num)
    
print(number)

avg = compute_average(number)

print(f"The length of the word is {word_length}")
print(f"The average of the numbers is {avg}")
compare_avg_with_length(avg, word_length, word)

