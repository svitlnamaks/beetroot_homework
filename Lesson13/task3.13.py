#Task 3

#Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one

def choose_func(nums: list, func1, func2) :
    nums1=list(filter(lambda it:it>0, nums))
    if len(nums)==len(nums1):
        return func1(nums)
    else:
        return func2(nums)

def square_nums(nums) :
    return [num ** 2 for num in nums]


def remove_negatives(nums) :
    return [num for num in nums if num > 0]


if __name__ =='__main__':
    # Assertions
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]

    print(choose_func(nums1, square_nums, remove_negatives)) #== [1, 4, 9, 16, 25]
    print(choose_func(nums2, square_nums, remove_negatives)) #== [1, 3, 5]

