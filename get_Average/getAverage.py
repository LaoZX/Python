def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
encrypt = [1733,1695,1679,1694,1681]
encrypt_average = calculate_average(encrypt)
print(f"The encrypt_average is: {encrypt_average}")

#decrypt = [1,0,1,1,0]
#de_ave=calculate_average(decrypt)
#print(f"The decrypt_average is: {de_ave}")
