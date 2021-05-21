# Task 4

# Custom exception
# Create your custom exception named `CustomException`, you can inherit from base Exception class,
# but extend its functionality to log every error message to a file named `logs.txt`.
# Tips: Use __init__ method to extend functionality for saving messages to file


class CustomException(Exception) :
    def __init__(self, name, msg='Your input is not correct!') :
        self.name = name
        self.msg = msg
        super().__init__(self.msg)

with open('logs.txt','w') as logs:
