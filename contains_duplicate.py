nums = [1, 2, 3]

def contains_duplicate_dict(nums):
    dict = {}
    for i in nums:
        dict[i] = dict.get(i,0) + 1
    
    for key in dict:
        if dict[key] > 1:
            return True
    return False

print(contains_duplicate_dict(nums))