import base64
from Crypto.Cipher import AES

def decrypt_savefile():

    input_file = r'C:\Users\User\AppData\LocalLow\Team Cherry\Hollow Knight\user2.dat'
    output_file = 'decrypted.json'

    CSHARP_HEADER = bytes([
        0, 1, 0, 0, 0, 255, 255, 255, 255, 1, 0, 0, 0, 0, 0, 0, 0, 6, 1, 0, 0, 0
    ])

    AES_KEY = b'UKu52ePUBwetZ9wNX88o54dnfKRu0T1l'
    BLOCK_SIZE = 16

    def pkcs7_unpad(data: bytes) -> bytes:
        pad_len = data[-1]
        if pad_len < 1 or pad_len > BLOCK_SIZE:
            return data
        return data[:-pad_len]

    def remove_header(data: bytes) -> bytes:
        if not data.startswith(CSHARP_HEADER):
            raise ValueError("Invalid or missing C# header in save data")
        data = data[len(CSHARP_HEADER):]

        length_count = 0
        for i in range(5):
            length_count += 1
            if (data[i] & 0x80) == 0:
                break
        data = data[length_count:]
        return data

    with open(input_file, 'rb') as f:
        file_data = f.read()

    data = remove_header(file_data)
    decoded = base64.b64decode(data)
    cipher = AES.new(AES_KEY, AES.MODE_ECB)
    decrypted = cipher.decrypt(decoded)
    decrypted = pkcs7_unpad(decrypted)

    json_text = decrypted.decode('utf-8')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(json_text)

    print(f"Decrypted save JSON written to {output_file}")


