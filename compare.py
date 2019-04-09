with open('output.txt') as o:
    content = o.readlines()
content = [ x.strip() for x in content]

with open('test.txt') as t:
    exp = t.readlines()
exp = [ x.strip() for x in exp]

for i in range(len(content)):
    if content[i] != exp[i]:
        print (i)

print(content == exp)
