# From email server header source file
# Count the number of times "From " occures

fname = raw_input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'

try: fh = open(fname)
except:
    print 'File not found: ', fname
    exit()

count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    emails = line.split()
    print emails[1] #2nd word is email
    count = count +1

print 'There were', count, 'lines in the file with From as the first word'

