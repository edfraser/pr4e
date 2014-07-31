# Calculate pay with and without overtime

Hrs = raw_input('Enter Hours:')
Rate = raw_input('Enter Rate:')

try:
    hrs = float(Hrs)
    rate = float(Rate)
except: hrs = -1
    
if (hrs < 0): print ("Enter only positive numbers for Hours and Rate.")
elif (hrs == 0): print ('No pay this period.')
elif(hrs <= 40):
    pay = hrs * rate
    print pay
else:
    pay = (40 * rate) + (1.5 * rate * (hrs-40))
    print pay
