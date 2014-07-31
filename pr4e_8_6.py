# Enter list of numbers
# Print sorted list, minimum and maximum values

numlst = list()
while True:
    mynum = raw_input('Enter a number: ')
    if mynum == 'done': break
    else:
        try: numlst.append(int(mynum))
        except: print 'Enter only numbers or "done" to finish'
    continue
            
numlst.sort()
print numlst
print 'Minimum: ', min(numlst)
print 'Maximum: ', max(numlst)
