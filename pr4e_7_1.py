# Using methods, example

fname = raw_input("Enter file name: ")
if len(fname) == 0: fname = 'words.txt'

try: fh = open(fname)
except:
    print 'File cannot be opened:', fname
    exit()

for line in fh: print line.rstrip().upper()

