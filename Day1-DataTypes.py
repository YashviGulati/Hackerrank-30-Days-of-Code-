i = 4
d = 4.0
s = 'HackerRank '
c = []
while True:
    try:
        line = raw_input("")
    except EOFError:
        break
    c.append(line)
string=""

for k in range(2,len(c)):
    string=string.join(c[k])
print(i+int(c[0]))
print(d+float(c[1]))
print(s+string)
