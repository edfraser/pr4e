# Create a distribution: number of emails sent each hour

name = raw_input('Enter file:')
if len(name) < 1 : name = 'mbox-short.txt'
try: fh = open(name)
except: 
    print 'File not found'
    exit()

count = {}
for line in fh:
    # parse line with email out of text file
    if not line.startswith('From '): continue
    
    # parse hour out of string
    atpos = line.find(':') - 2
    hour = line[atpos : atpos+2]
    
    # count occurrences of each hour
    count[hour] = count.get(hour,0) + 1
    
# make list of tuples, sort on key    
lst = count.items()
lst.sort()

# print distribution using an asterisk for each email occurrence / hour
for key, value in lst: print key, value, '*' * value
