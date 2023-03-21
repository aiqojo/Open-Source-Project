a, b = 0, 1
sum_even = 0
while b < 4000000:
    # If b is even, we add to sum
    if b % 2 == 0:
        sum_even += b
    # Continuing fibonacci sequence
    a, b = b, a+b

print(sum_even)

# answer should be 4613732
