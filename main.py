'''
Project Name: Human Pyramid
Author: Tanner Hancock
Due Date: 2/11/20
Course: CS1410

This program will construct a human pyramid using recursive functions. You can add a paramater in command line to specify the # of rows you would like the pyramid to be. If you do not specify another parameter it will default to 7 rows. Part2.txt is for the function not using cache, and part3.txt is for the function using cache. 
'''
from pyramid import *
from hashmap import HashMap
import sys

#call all functions
def main():
    if  int(len(sys.argv)) == 2:
        num = sys.argv[1]
        part2(num)
        part3(num)
    else:
        num = 7
        part2(num)
        part3(num)

#start main
if __name__ == "__main__":
    main()