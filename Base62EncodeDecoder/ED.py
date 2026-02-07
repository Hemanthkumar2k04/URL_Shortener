class Encoder:
    def __init__(self):
        self.key = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def encode(self, num):
        """
        Encode an integer to a base62 string.
        
        Args:
            num: Non-negative integer to encode
            
        Returns:
            Base62 encoded string
        """
        if num == 0:
            return self.key[0]
        
        encoded = ""
        while num > 0:
            encoded = self.key[num % 62] + encoded
            num //= 62
        
        return encoded


class Decoder:
    def __init__(self):
        self.key = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def decode(self, encoded_str):
        """
        Decode a base62 string back to an integer.
        
        Args:
            encoded_str: Base62 encoded string
            
        Returns:
            Decoded integer
        """
        num = 0
        for char in encoded_str:
            num = num * 62 + self.key.index(char)
        
        return num