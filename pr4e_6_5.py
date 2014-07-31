# Slice example

text = "X-DSPAM-Confidence:    0.8475";
atpos = text.find(':') + 1
f = float(text[atpos:])
print f

