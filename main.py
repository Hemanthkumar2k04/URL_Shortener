from Base62EncodeDecoder import Encoder, Decoder
from database import supabase_client

encoder = Encoder()
encoded_idx = encoder.encode(10000000)

decoder = Decoder()
decoded_idx = decoder.decode(encoded_idx)

print(decoded_idx)
