sScore=raw_input('Enter Score:')

try:
    
    score=float(sScore)

except:
    score=-1
    
if (score>=90):
    print ('A')
  
elif (score>=80):
    print ('B')

elif (score>=70):
    print ('C')
    
elif (score>=60):
    print ('D')
    
elif (score>=0 and score<60):
    print ('F')
    
else:
    print ('Enter Score range between 0 and 100.')
    

