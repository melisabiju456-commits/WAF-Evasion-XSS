# Task 8: WAF Evasion for XSS - Python Script

## Objective
The goal of this project is to research how Web Application Firewalls (WAFs) process input and write a Python script that automatically transforms standard strings into alternative formats (like mixed-case, URL-encoded, or hex-encoded) to illustrate filter evasion concepts.

## Techniques Implemented
* **Mixed Case:** Changing character casing to bypass basic string matching.
* **URL/Double URL Encoding:** Converting characters into hex codes to see if input parsers evaluate the data differently.
* **HTML Entity Hex:** Rebuilding the string using raw character values.
* **Alternative Elements:** Using modern HTML tags like `<img>` or `<svg>` instead of traditional `<script>` tags.
*
