# Who sent the most email messages?

# Using email server header source file
# Count email addresses, print largest

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
try: fh = open(name)
except:
    print 'File not found: ', name
    exit()
    
count = {}
for line in fh:
    if not line.startswith('From '): continue
    words = line.split() 
    count[words[1]] = count.get(words[1],0) + 1 # 2nd word is email
    
largest = None
for key in count: 
    if largest is None or count[largest] < count[key]: largest = key
    
print largest, count[largest]
