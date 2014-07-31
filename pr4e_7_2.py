# From email server header file
# Count, accumulate and calculate average spam confidence level

fname = raw_input("Enter file name: ")
if len(fname) == 0: fname = 'mbox-short.txt'
try: fh = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()
    
count = 0
value = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    atpos = line.find(":") + 1
    value = value + float(line[atpos:])
    
average = value/count
print "Average spam confidence:", average
