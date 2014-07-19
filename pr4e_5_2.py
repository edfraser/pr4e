largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num in ("done", "exit", "quit", "adios", "bye", "bye bye") : break
        
    try:
        num = int(num)
    
    except:
        print "Invalid input"
        continue
           
    if smallest == None and largest == None :
        smallest = num
        largest = num
        
    if smallest > num :
        smallest = num
        
    if largest < num :
        largest = num
        
print "Maximum is", largest
print "Minimum is", smallest
