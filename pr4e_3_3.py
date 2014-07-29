Score = raw_input('Enter Score:')
try: score = float(Score)
except: score = -1
    
if (score < 0 or score > 100): print('Enter Score range between 0 and 100')
elif (score >= 90): print ('A')
elif (score >= 80): print ('B')
elif (score >= 70): print ('C')
elif (score >= 60): print ('D')
else: print ('F')
