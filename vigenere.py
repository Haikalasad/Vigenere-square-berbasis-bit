def vigenere_encrypt(plaintext, key):
    teks_enkripsi = ""
    key_stream = generate_key_stream(plaintext, key)

    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key_stream[i]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        teks_enkripsi += encrypted_char
    
    return teks_enkripsi


def vigenere_decrypt(ciphertext, key):
    teks_deskripsi = ""
    key_stream = generate_key_stream(ciphertext, key)

    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key_stream[i]
        decrypted_char = chr(ord(char) ^ ord(key_char))
        teks_deskripsi += decrypted_char
        

    return teks_deskripsi

def generate_key_stream(text, key):
    key_stream = ""
    key_length = len(key)

    for i in range(len(text)):
        key_stream += key[i % key_length]

    return key_stream

def main():
    plaintext = "Muhammad Haikal Fikri Asad"
    key = "Rahasiadong"

    print("Plaintext:", plaintext)
    print("Key:", key)

    ciphertext = vigenere_encrypt(plaintext, key)
    print("Enkripsi:", ciphertext)

    teks_deskripsi = vigenere_decrypt(ciphertext, key)
    print("Deskripsi:", teks_deskripsi)

if __name__ == "__main__":
    main()
