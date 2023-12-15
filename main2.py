import math
import time
from math import sqrt


def calculate():
    i = 0
    n = int(input("enter iteration depth as integer: "))
    st = time.time()  # start time in sec

    distance_total = 0
    for x1 in range(0, n):
        for y1 in range(0, n):
            for x2 in range(0, n):
                for y2 in range(0, n):
                    distance = sqrt(math.pow((x2 - x1), 2) + (math.pow((y2 - y1), 2)))
                    i = i + 1
                    distance_total = distance_total + distance

    et = time.time()  # end time in sec
    elapsed_time = et - st  # difference in sec
    print(f"execution time: {elapsed_time} sn")
    result = distance_total / i / n
    print(f"result is: {result}")


calculate()
