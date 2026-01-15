def calculate_checksum(nine_digits: str):
    # Step 1: Apply Luhn doubling to the 9 digits
    # (Starting from the right, so indices 0, 2, 4, 6, 8 are doubled)
    digits = [int(d) for d in nine_digits]
    for i in range(len(digits) - 1, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    # Step 2: Sum all digits and find the remainder
    total_sum = sum(digits)

    # Step 3: Checksum is the number needed to reach the next multiple of 10
    return (10 - (total_sum % 10)) % 10


# Example: Birth date 900101 and serial 123
# print(calculate_checksum("900101123"))

if __name__ == "__main__":
    test_number = "900101123"
    checksum = calculate_checksum(test_number)
    print(f"The checksum for {test_number} is: {checksum}")
    print(f"Full number: {test_number}{checksum}")
