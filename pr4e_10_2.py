# Print out the distribution by hour of the day for each email message in a text file

name = raw_input('Enter file:')
if len(name) < 1 : name = 'mbox-short.txt'
try: fh = open(name)
except: 
    print 'File not found'
    exit()

count = {}
for line in fh:
    if not line.startswith('From '): continue
    
    # parse hour out of string
    atpos = line.find(':') - 2
    hour = line[atpos : atpos+2]
    
    # count occurances of each hour
    count[hour] = count.get(hour,0) + 1
    
# make list of tuples, sort on key    
lst = count.items()
lst.sort()

# print keys, values 
for key, value in lst: print key, value
