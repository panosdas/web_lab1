import requests

url = input("Δώστε url: ")  # προσδιορισμός του url

if not url.startswith("https://"):
    url = "https://" + url



with requests.get(url) as response:  # το αντικείμενο response
    for key, value in response.headers.items():
        print(f"{key}: {value}\n")
    server = response.headers.get("Server", "Unknown")
    print(f"Server: {server}")
    cookies = response.cookies
    if cookies:
        print("\nΗ σελίδα χρησιμοποιεί cookies.")
        print("\nCookies:")
        for cookie in cookies:
            print(f"Όνομα: {cookie.name}, Διάρκεια: {cookie.expires if cookie.expires else 'Άγνωστη'}")
    else:
        print("\nΗ σελίδα δεν χρησιμοποιεί cookies.")