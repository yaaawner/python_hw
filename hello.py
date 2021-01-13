s = input()
h, m, s = s[s.rfind(" "):].split(":")
h, m, s = int(h), int(m), int(s)

print(h, m, s)
print(type(h))