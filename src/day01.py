import re
from loadfile import read_file

def day01task01_02():
    file_lines = read_file("input/day01.txt")
    first_numbers = list()
    second_numbers = list()
    for line in file_lines:
        numbers = re.findall(r'\d+', line)
        if len(numbers) >= 2:
            first_numbers.append(int(numbers[0]))
            second_numbers.append(int(numbers[1]))

            first_numbers.sort()
            second_numbers.sort()
    
    difference = 0   
    for x in range(len(first_numbers)):
        difference = difference + abs(first_numbers[x] - second_numbers[x])
    
    similarity_score = 0
    for x in range(len(first_numbers)):
        similarity_score += first_numbers[x] * second_numbers.count(first_numbers[x])

    print("Difference:" + str(difference))
    print("Similarity Score:" + str(similarity_score))
