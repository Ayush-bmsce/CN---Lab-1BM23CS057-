# CRC-CCITT (16-bit) polynomial
POLY = 0x1021

def crc_ccitt(data):
    crc = 0xFFFF   # initial value
    
    for byte in data:
        crc ^= (byte << 8)
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ POLY
            else:
                crc <<= 1
            crc &= 0xFFFF   # keep crc 16-bit
    return crc


def str_to_bytes(bin_str):
    return [int(bin_str[i:i+8], 2) for i in range(0, len(bin_str), 8)]


# ------------------------- MAIN PROGRAM -------------------------
# Input message in binary
data_bits = input("Enter binary data: ")

# Convert to byte array
byte_data = str_to_bytes(data_bits)

# Compute CRC
crc = crc_ccitt(byte_data)

# Append CRC to message
crc_bits = format(crc, '016b')
codeword = data_bits + crc_bits

print("\nCRC (16-bit):", crc_bits)
print("Transmitted Codeword:", codeword)

# --------- Simulate transmission and error checking -------------
received = input("\nEnter received codeword: ")

recv_data = str_to_bytes(received)
recv_crc = crc_ccitt(recv_data)

print("\nReceiver CRC Check Value:", format(recv_crc, '04x'))

if recv_crc == 0:
    print("Status: NO ERROR (Data Received Correctly)")
else:
    print("Status: ERROR DETECTED!")
