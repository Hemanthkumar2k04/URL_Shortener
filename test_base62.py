from utils.base62 import Base62

# Test encoding
print(Base62.encode(1))    # Should print: 1
print(Base62.encode(10))   # Should print: a
print(Base62.encode(61))   # Should print: Z
print(Base62.encode(62))   # Should print: 10
print(Base62.encode(125))  # Should print: 21

# Test decoding (optional)
print(Base62.decode("1"))   # Should print: 1
print(Base62.decode("a"))   # Should print: 10
print(Base62.decode("21"))  # Should print: 125