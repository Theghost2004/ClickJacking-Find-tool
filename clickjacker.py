from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request

domain = input("Enter target domain (e.g., example.com): ")

# Request the security headers page for the target domain
req = Request(
    url=f'https://securityheaders.com/?q={domain}&followRedirects=on',
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()

# Parse the page content
soup = bs(webpage, 'html.parser')

# Find the X-Frame-Options result in the page content
def check_clickjacking_vulnerability():
    if "X-Frame-Options" in soup.get_text():
        print(f"{domain} is not vulnerable to clickjacking attack.")
    else:
        print(f"{domain} is vulnerable to clickjacking attack.")

check_clickjacking_vulnerability()
