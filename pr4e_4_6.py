# Create function: convert previous pay calculator program

def computepay(h,r):
    if h <= 40: p = h*r 
    else: p = 40*r + (h-40)*r*1.5
    return p

# Use function:
hrs = float(raw_input('Enter Hours: '))
rate = float(raw_input('Enter Rate: '))
p = computepay(hrs,rate)
print p
