class Base62:
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    BASE = len(ALPHABET)
    
    @staticmethod
    def encode(num: int) -> str:
        """Convert number to base62 string"""
        if num == 0:
            return Base62.ALPHABET[0]
        
        result = []
        while num > 0:
            result.append(Base62.ALPHABET[num % Base62.BASE])
            num //= Base62.BASE
        
        return ''.join(reversed(result))
    
    @staticmethod
    def decode(string: str) -> int:
        """Convert base62 string back to number (optional, for reverse lookup)"""
        num = 0
        for char in string:
            num = num * Base62.BASE + Base62.ALPHABET.index(char)
        return num