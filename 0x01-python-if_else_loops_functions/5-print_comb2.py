#!/usr/bin/python3

"""Print number 0 to 99"""
for number in range(0, 99):
    print("{:0>2}, ".format(number), end="")
print("99")
