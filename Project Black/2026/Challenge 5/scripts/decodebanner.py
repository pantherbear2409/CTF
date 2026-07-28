#!/usr/bin/env python3
import base64

# The decoded content you posted
content = """


      Ky0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tL
      S0tLS0tLS0tLS0tLS0tLS0tKwp8ICBQUkpCTEt7MS82Ol9mSVIkdF8wZl9tQG5ZX2ZMQGd6Ll
      93SEVyM19XMWxMX1kwdV9wVVRfVGgzTV9AMWw/fSAgICAgICB8CnwgICAgICAgICAgICAgICA
      gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg
      IHwKfCAgSGludDogL2FwaS9saXN0aW5nLnBocD9rZXk9VkdocGMwbHpWR2hsVm1WeWVWWmxjb
      mxXWlhKNVUyVmpjbVYwUzJWNSAgfAorLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS
      0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0r
    
    
"""

# Clean the content (remove whitespace at line starts)
cleaned = ''.join(line.strip() for line in content.split('\n') if line.strip())

# Decode from base64
decoded = base64.b64decode(cleaned).decode('utf-8')

print(decoded)
