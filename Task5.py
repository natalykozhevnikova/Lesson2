import random

test_list = [2, 4, 6, 8, 1]
print("The original list is : " + str(test_list))
res = random.sample(test_list, len(test_list))
print("The shuffled list is : " + str(res))