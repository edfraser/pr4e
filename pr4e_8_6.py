numlst = list()

while True:
    mynum = raw_input('Enter a number: ')
    
    if len(mynum) == 0:
        continue
        
    elif mynum == 'done':
        break
        
    else:
        try:
            numlst.append(int(mynum))
            continue
        except:
            print 'Enter a number, or "done" to finish: '
            continue
    
try:
    numlst.sort()
    #list.sort(numlst)
    print numlst
    print 'Minimum: ', min(numlst)
    print 'Maximum: ', max(numlst)
except:
    exit()
