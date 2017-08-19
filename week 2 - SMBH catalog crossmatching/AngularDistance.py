import math
import numpy as np
def angular_dist(r1,d1,r2,d2):
  r1_rad=np.radians(r1)
  d1_rad=np.radians(d1)
  r2_rad=np.radians(r2)
  d2_rad=np.radians(d2)
  a = math.pow(np.sin(abs(d1_rad-d2_rad)/2.0),2)
  b=np.cos(d1_rad)*np.cos(d2_rad)*math.pow(np.sin(abs(r1_rad-r2_rad)/2.0),2)
  distance=2*np.arcsin(np.sqrt(a+b))
  dist_deg=np.degrees(distance)
  return dist_deg



# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  # Run your function with the second example in the question
  print(angular_dist(10.3, -3, 24.3, -29))
