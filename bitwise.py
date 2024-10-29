bitwise = "hidup balmond"
print (bitwise)
# Mendefinisikan dua variabel
a = 12  # dalam biner: 1100
b = 5   # dalam biner: 0101

# Operator bitwise AND
and_result = a & b
print("Hasil a & b:", and_result)  # 4 (0100)

# Operator bitwise OR
or_result = a | b
print("Hasil a | b:", or_result)    # 13 (1101)

# Operator bitwise XOR
xor_result = a ^ b
print("Hasil a ^ b:", xor_result)    # 9 (1001)

# Operator bitwise NOT
not_result = ~a
print("Hasil ~a:", not_result)        # -13 (invers bit)

# Operator pergeseran ke kiri
left_shift = a << 2
print("Hasil a << 2:", left_shift)    # 48 (110000)

# Operator pergeseran ke kanan
right_shift = a >> 2
print("Hasil a >> 2:", right_shift)   # 3 (0011)
