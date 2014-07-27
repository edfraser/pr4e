fname = raw_input('Enter file name: ')
if len(fname) < 1 : fname = 'romeo.txt'
    
try:
    fh = open(fname) 

except:
    print 'File not found: ', fname
    sys.exit()

lst = list()
unique_lst = list()

for line in fh:
    lst = line.split()
    for i in range(len(lst)):
        if lst[i] in unique_lst: continue
        unique_lst.append(lst[i])
        
unique_lst.sort()
print unique_lst
