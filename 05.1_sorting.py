import random
from collections import Counter

# sorting tuples in an array
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
student_tuples = sorted(student_tuples, key=lambda student: student[2])   # sort by age
print (student_tuples)

#sort list of numbers
numbers_list = [1,4,8,6,7,2,4,6,2,4,6,4,8]
print(sorted(numbers_list))
print(sorted(numbers_list, reverse=True))   #reverse sort 

#sort dict by key
counts2_dict = {4: 20, 6: 21, 5: 19, 1: 17, 3: 10, 2: 13}
print (counts2_dict)
print (type(counts2_dict))
print(sorted(counts2_dict.items()))  # sort by first element of tuple
print(sorted(counts2_dict.items(), reverse=True))   #reverse sort 

# sort by value of each tuple in the dict
print(sorted(counts2_dict.items(),key=lambda item: item[1])) 
