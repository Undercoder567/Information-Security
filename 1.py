def encode(msg):
    # Determine the number of parity bits needed
    n = len(msg)
    k = 1
    while 2**k < n + k + 1:
        k += 1
    m = n + k
    
    # Initialize the encoded message
    code = [0] * m
    
    # Copy the message into the encoded message, skipping parity bit positions
    j = 0
    for i in range(m):
        if i+1 not in [2**p for p in range(k)]:
            code[i] = int(msg[j])
            j += 1
    
    # Calculate the parity bits
    for p in range(k):
        bit = 0
        for i in range(1, m+1):
            if i & (2**p) == (2**p):
                bit ^= code[-i]
        code[2**p - 1] = bit
    
    # Return the encoded message
    return ''.join(str(bit) for bit in code)


def decode(code):
    # Determine the number of parity bits used
    m = len(code)
    k = 1
    while 2**k < m + 1:
        k += 1
    n = m - k
    
    # Initialize the decoded message
    msg = [0] * n
    
    # Calculate the syndrome
    syndrome = []
    for p in range(k):
        bit = 0
        for i in range(1, m+1):
            if i & (2**p) == (2**p):
                bit ^= int(code[-i])
        syndrome.append(bit)
    syndrome.reverse()
    syndrome_num = int(''.join(str(bit) for bit in syndrome), 2)
    
    # Correct errors
    if syndrome_num != 0:
        code_list = list(code)
        code_list[syndrome_num-1] = str(int(code[syndrome_num-1]) ^ 1)
        code = ''.join(code_list)
    
    # Copy the message from the decoded code
    j = 0
    for i in range(m):
        if i+1 not in [2**p for p in range(k)]:
            msg[j] = int(code[i])
            j += 1
    
    # Return the decoded message
    return ''.join(str(bit) for bit in msg)

msg = '1011'
code = encode(msg)
print("Encoded Message:-",code)

decoded_msg = decode(code)
print("Decoded Message:-",decoded_msg)