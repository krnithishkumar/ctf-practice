import base64

hex_str = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Decode hex to bytes
byte_data = bytes.fromhex(hex_str)

print(byte_data)

# Encode bytes to Base64
base64_str = base64.b64encode(byte_data).decode()
print(base64_str)
