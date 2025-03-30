# Class for doing encryption and decryption using a Caesar cipher.
class CaesarCipher:
    # Construct Caesar cipher using given integer shift for rotation.
    def __init__(self, shift):
        encoder = [None] * 26 # temp array for encryption
        decoder = [None] * 26 # temp array for decryption
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder) # convert the encoder and
        self._backward = ''.join(decoder) # decoder arrays as strings

    # Return string representing encrypted message.
    def encrypt(self, message):
        return self._transform(message, self._forward)
    # Return decrypted message given encrypted secret."""
    def decrypt(self, secret):
        return self._transform(secret, self._backward)
    # Utility to perform transformation based on given code string.
    def _transform(self, original, code):
        msg = list(original)# convert msg into a list of characters
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - 65# index from 0 to 25
                msg[k] = code[j] # replace this character
        return ''.join(msg)
# Test code
cipher = CaesarCipher(3)
message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
coded = cipher.encrypt(message)
print('Secret: ', coded)
answer = cipher.decrypt(coded)
print('Message:', answer)
