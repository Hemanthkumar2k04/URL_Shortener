class Encoder:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.key = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._initialized = True

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
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self.key = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self._initialized = True

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
