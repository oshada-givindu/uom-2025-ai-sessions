#problrm 04: Largest palindrome product
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def largest_palindrome_product(digits):
    max_palindrome = 0
    lower_limit = 10**(digits-1)
    upper_limit = 10**digits
    for i in range(upper_limit-1, lower_limit-1, -1):
        for j in range(i, lower_limit-1, -1):
            product = i * j
            if product <= max_palindrome:
                break
            if is_palindrome(product):
                max_palindrome = product
    return max_palindrome
print(largest_palindrome_product(3))