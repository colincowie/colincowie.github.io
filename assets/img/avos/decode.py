import sys

def decode(encoded_str, xor_key):
    decoded_str = ""
    key_len = len(xor_key)
    for i in range(0, len(encoded_str), 2):
        encoded_byte = int(encoded_str[i:i+2], 16) # Convert the hexadecimal byte to an integer
        xor_key_byte = ord(xor_key[i//2 % key_len]) # Get the corresponding byte from the XOR key
        decoded_byte = encoded_byte ^ xor_key_byte # Perform the XOR operation
        decoded_str += chr(decoded_byte) # Convert the result back to a character and append to the decoded string
    return decoded_str

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <encoded_str> <xor_key>")
    else:
        encoded_str = sys.argv[1]
        xor_key = sys.argv[2]
        decoded_str = decode(encoded_str, xor_key)
        print(decoded_str)
