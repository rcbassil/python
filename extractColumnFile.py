#!/usr/bin/python3

with open("Flights.txt") as file:
    for line in file:
        print(line.rstrip().split()[-1])