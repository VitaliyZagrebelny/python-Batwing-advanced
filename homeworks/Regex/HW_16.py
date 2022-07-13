import re

print("=" * 50)

pattern = r"[+\d]{1,3}-[\d]{2,2}-[\d]{2,2}"
text = "Hello, my phone number is 251-65-23."
result = re.findall(pattern=pattern, string=text)
print(result)

print("=" * 50)

pattern = r"(\b[A-Za-z0-9._%/+-]{1,255})+@([A-Za-z0-9]+.[A-Z|a-z]{1,255}\b)"
text = "zagrebelnyivitalii@gmail.com"
result = re.match(pattern=pattern, string=text)

print(result.groups())

print("=" * 50)

pattern = r"[0]"
text = "216.008.094.196"
result = re.sub(pattern=pattern, repl=" ", string=text)
print(result)

print("=" * 50)

pattern = r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,2}"
text = "153.192.392.84"
result = re.match(pattern=pattern, string=text)

print(result)
