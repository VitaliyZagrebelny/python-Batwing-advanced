import re

print("=" * 50)

pattern = r"[+\d]{1,3}-[\d]{2,2}-[\d]{2,2}"
text = "Hello, my phone number is 251-65-23."
result = re.findall(pattern=pattern, string=text)
print(result)

print("=" * 50)

pattern = r"[\wd\.]{1,255}@\w+\.+[\wd\.]{1,255}"
text = 'zagrebelnyivitalii@gmail.com'
result = re.match(pattern=pattern, string=text)

print(result.groups())

print("=" * 50)

pattern = r"\.[0]*"
text = "216.008.094.190"
result = re.sub(pattern=pattern, repl=" ", string=text)
print(result)

print("=" * 50)

pattern = r"\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,2}"
text = "153.192.238.84"
result = re.match(pattern=pattern, string=text)

print(result)
