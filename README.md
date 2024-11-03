# ClickJacking-Find-tool
I have created a script in python with which you could find if a website is vulnerable to clickjacking or not by simply putting the website name.
Firstly you will enter the domain name.
The urlopen will fetch the content of html page with headers.
The soup variable will extract the headers part from the urlopen.
and then check for X-Frame-Options.
If it is present then it shows that the page is not vulnerable if not its shows that it is vulnerable.

