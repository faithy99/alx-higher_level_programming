#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum1 = 0
    sum2 = 0
    t1 = tuple_a + (0, 0)
    t2 = tuple_b + (0, 0)

    sum1 += t1[0] + t2[0]
    sum2 += t1[1] + t2[1]

    return (sum1, sum2)
