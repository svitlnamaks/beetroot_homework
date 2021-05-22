#Task 2

#Write a Python program to access a function inside a function (Tips: use function, which returns another function)
def my_func_1(a):
    def my_func_2(b):
        if a>0:
            return a+b
        else:
            return a*b
    return my_func_2

if __name__ == '__main__':
    num=my_func_1(10)(8)
    num_2=my_func_1(-10)(4)
    print(num,num_2)


