import re

print("=" * 50)

pattern = r"[+\d]{1,3}-[\d]{2,2}-[\d]{2,2}"
text = "Hello, my phone number is 251-65-23."
result = re.findall(pattern=pattern, string=text)
print(result)

print("=" * 50)

pattern = r"[\wd\.]{1,255}@\w+\.+[\wd\.]{1,255}"
text = 'zagrebelnyivitalii@gmail.com'
result = re.findall(pattern=pattern, string=text)

print(result)

print("=" * 50)

pattern = r"([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])[.]([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])[.]" \
          r"([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])[.]([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])"
text = '000.000.000.000'

regex = re.findall(pattern=pattern, string=text)
regex2 = ', '.join('.'.join(tup) for tup in regex)
ip_address = re.sub(r'\b0+(\d)', r'\1', regex2)
print(ip_address)
print("=" * 50)

pattern = r'^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$'
text = "153.192.238.84"
result = re.match(pattern=pattern, string=text)

print(result)
