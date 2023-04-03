def R(k):
  if(k > 0):
    result = k + R(k - 1)
    print(result)
  else:
    result = 0
  return result
R(6)