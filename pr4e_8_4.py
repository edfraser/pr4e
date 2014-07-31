# Generate and print list of unique words from text file

fname = raw_input('Enter file name: ')
if len(fname) < 1 : fname = 'romeo.txt'
try: fh = open(fname) 
except: 
    print 'File not found: ', fname
    exit()

unique_lst = []
for line in fh:
    lst = line.split()
    for word in range(len(lst)):
        if lst[word] in unique_lst: continue
        unique_lst.append(lst[word])
        
unique_lst.sort()
print unique_lst
