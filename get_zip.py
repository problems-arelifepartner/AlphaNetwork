import base64

# Base64 string (shortened example — replace with full one from me earlier)
b64_data = b"""
UEsDBBQAAAAIABXxw1Txj36A3gAAABoAAAAIAAAAdmVyc2lvbi50eHQxLjAuMFBLBwhPOyyw2gAAAGoAAABQSwMEFAAAAAgAFfHDVPep3TD3AAAA2gAAABQAAAByZWFkbWUubWUyMDI1CgojIFZ1bG4tU2NhbiAyMDI1IExpZ2h0V2VpZ2h0CiMgQXV0aG9yOiBHaXB0LTUKIyBGZWF0dXJlczogV2ViLCBhcHAsIGFuZCBuZXR3b3JrIHZ1bG5lcmFiaWxpdHkgc2Nhbm5pbmcKIyBBbGwgcGFja2FnZXMgYXJlIGluc3RhbGxlZCBhdCBydW50aW1lIHRvIGtlZXAgaXQgbGlnaHR3ZWlnaHQKClBsZWFzZSB1c2Ugb25seSBvbiBzeXN0ZW1zIHlvdSBvd24uCgpQbC4uLg==
"""

# Decode and write the zip file
with open("vuln-scan-2025-light.zip", "wb") as f:
    f.write(base64.b64decode(b64_data))

print("✅ Zip file created: vuln-scan-2025-light.zip")