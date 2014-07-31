# Create function: convert previous letter grade calculator

def computegrade(score):
    try: score = float(score)
    except: score = -1

    if (score < 0 or score > 100): return ('Enter number in range: 0 to 100')               
    elif (score >= 90): return ('A')
    elif (score >= 80): return ('B')
    elif (score >= 70): return ('C')
    elif (score >= 60): return ('D')
    else: return ('F')

# Use function:
print computegrade(raw_input('Enter Score:'))
