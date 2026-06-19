def naive_waf_filter(user_input):
    """Simulates a basic WAF rule blocking raw tags and common script strings."""
    blocked_chars = ["<", ">"]
    # Blocks if raw less-than/greater-than signs or explicit lowercase strings appear
    if any(char in user_input for char in blocked_chars) or "script" in user_input.lower():
        return "BLOCKED"
    return "ALLOWED"
