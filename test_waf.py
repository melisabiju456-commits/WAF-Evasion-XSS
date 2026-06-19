from mock_waf import naive_w_a_f_filter as naive_waf_filter # type: ignore
from xss_evador import generate_mixed_case, generate_html_entity, generate_double_url

def main():
    base_payload = "<script>alert('XSS')</script>"
    print("Testing payloads against mock WAF:\n")
    
    # Test Raw
    print(f"{base_payload}  ->  {naive_waf_filter(base_payload)}")
    
    # Test Mixed Case Obfuscation
    mixed = generate_mixed_case(base_payload)
    print(f"{mixed}  ->  {naive_waf_filter(mixed)}")
    
    # Test HTML Entity
    html_ent = generate_html_entity(base_payload)
    print(f"{html_ent}  ->  {naive_waf_filter(html_ent)}")

if __name__ == "__main__":
    main()
