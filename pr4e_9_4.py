name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

try:
    fh = open(name)
    
except:
    print 'File not found: ', name
    exit()
    
words = []
count = {}
for line in fh:
    if not line.startswith('From '): continue
    line.rstrip()
    words = line.split()
    count[words[1]] = count.get(words[1],0) + 1
    
largest = None
name = None
for key in count:
    if largest is None or largest < count[key]:
        name = key
        largest = count[key]
        
print name, largest
