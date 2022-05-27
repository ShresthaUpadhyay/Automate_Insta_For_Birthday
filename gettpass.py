
import base64

def decodeInitials(value):
    base64_string = value
    base64_bytes = base64_string.encode("ascii")
  
    sample_string_bytes = base64.b64decode(base64_bytes)
    final = sample_string_bytes.decode("ascii")
    return final
  

