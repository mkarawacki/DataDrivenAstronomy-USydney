def hms2dec(h,m,s):
  return 15*(h+m/60 + s/3600)
def dms2dec(d,m,s):
  sign=1
  if(d<0):
    dec= abs(d)+m/60 + s/3600
    return -1.0*dec
  else:
    dec=(d+m/60+s/3600)
    return dec
# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The first example from the question
  print(hms2dec(23, 12, 6))

  # The second example from the question
  print(dms2dec(22, 57, 18))

  # The third example from the question
  print(dms2dec(-66, 5, 5.1))