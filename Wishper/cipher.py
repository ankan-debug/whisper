# cipher.py

# Simple Substitution Map (customize this!)
substitution_map = {
    'A': 'R3', 'B': '@Z', 'C': 'x9', 'D': 'M4', 'E': '2L',
    'F': 'Q7', 'G': 'S1', 'H': '#K', 'I': '0V', 'J': 'P2',
    'K': 'N8', 'L': 'T5', 'M': 'Z0', 'N': 'B3', 'O': '$W',
    'P': 'E6', 'Q': 'J9', 'R': 'L4', 'S': 'D1', 'T': 'F8',
    'U': 'A7', 'V': 'G2', 'W': 'C3', 'X': 'Y5', 'Y': 'H6', 'Z': 'U0'
}

# Reverse map for decryption
reverse_map = {v: k for k, v in substitution_map.items()}

def encrypt_message(message):
    encrypted = []
    for char in message.upper():
        if char in substitution_map:
            encrypted.append(substitution_map[char])
        else:
            encrypted.append(char)  # keep spaces, symbols, numbers
    return ' '.join(encrypted)

def decrypt_message(encrypted_message):
    decrypted = []
    parts = encrypted_message.split()
    for part in parts:
        if part in reverse_map:
            decrypted.append(reverse_map[part])
        else:
            decrypted.append(part)
    return ''.join(decrypted)


