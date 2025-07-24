def decimal_to_binary(n):
    return bin(n).replace("0b", "")

# Example usage:
decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print(f"Binary representation: {binary_number}")