#problem 09: Special Pythagorean triplet
def find_pythagorean_triplet(sum_total):
    for a in range(1, sum_total // 3):
        for b in range(a + 1, sum_total // 2):
            c = sum_total - a - b
            if a**2 + b**2 == c**2:
                return a * b * c
    return None
print(find_pythagorean_triplet(1000))

