import itertools
import string
import time

def brute_force_attack(target_password, max_length=8):
    # Define the character set to use (lowercase letters, uppercase letters, digits, and special characters)
    chars = string.ascii_letters + string.digits + string.punctuation

    # Start with a length of 1 and go up to max_length
    for length in range(1, max_length + 1):
        # Generate all possible combinations of the current length
        for attempt in itertools.product(chars, repeat=length):
            # Convert the tuple to a string
            attempt = ''.join(attempt)
            print(f"Trying: {attempt}")

            # Check if the attempt matches the target password
            if attempt == target_password:
                print(f"Password found: {attempt}")
                return attempt

    print("Password not found within the given length limit.")
    return None

# Example usage (for educational purposes only)
if __name__ == "__main__":
    # Simulate a target password (keep it short for demonstration purposes)
    target_password = input("Enter a target password (for simulation): ")

    # Start the brute force attack
    print("Starting brute force attack...")
    start_time = time.time()
    brute_force_attack(target_password, max_length=4)  # Limit max_length for quick demonstration
    end_time = time.time()

    print(f"Time taken: {end_time - start_time:.2f} seconds")
