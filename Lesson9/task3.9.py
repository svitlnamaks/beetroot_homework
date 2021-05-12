#Потрібно доробити завдяння

# Task 3

# TV controller
# Create a simple prototype of a TV controller in Python.It’ll use
# the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel.
# If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
# if the channel N or 'name' exists in the list, or "No" - in the other case.
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.

# CHANNELS = ["BBC", "Discovery", "TV1000"]

# class TVController:

# pass

# controller = TVController(CHANNELS)
# controller.first_channel() == "BBC"
# controller.last_channel() == "TV1000"
# controller.turn_channel(1) == "BBC"
# controller.next_channel() == "Discovery"
# controller.previous_channel() == "BBC"
# controller.current_channel() == "BBC"
# controller.is_exist(4) == "No"
# controller.is_exist("BBC") == "Yes"


class TVController() :
    def __init__(self, channels) :
        self.channels = channels
        self.current_channel = 0

    def first_channel(self) :
        first = print(self.channels[0])
        return first

    def last_channel(self) :
        last = print(self.channels[-1])
        return last

    def turn_channel(self, N) :
        if N <= len(self.channels) :
            turn = print(self.channels[N - 1])
            return turn
        else :
            wrong_data = print('No such channel in a list ')
            return wrong_data

    # return next(my_next_channel
    def next_channel(self) :
        self.channels += 1
        if self.channels + 1 == len :
            self.channels = 0
        return self.channels

    def previous_channel(self) :
        self.channels -= 1
        pass

    def is_exist(self, N) :
        if N in self.channels or N <= len(self.channels) :
            return print('Yes')
        else :
            return print('No')

    def current_channel(self) :
        return self.channels[self.current_channel]


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)
controller.first_channel()  # == "BBC"
controller.last_channel()  # == "TV1000"
controller.turn_channel(2)  # == "BBC"
# controller.next_channel()  # == "Discovery"
# controller.previous_channel()  # "BBC"
# controller.current_channel()  # == "BBC"
controller.is_exist(4)  # == "No"
controller.is_exist("BBC")  # == "Yes"
