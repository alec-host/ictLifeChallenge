#!/usr/bin/python

"""
	author: alex
	date: 20-Sept-19
	name: cryptic arithmetic solver.
"""

from re import sub

"""
-.method to display formatted output.
"""
def displyTemplate(query):
  """
  -.defined constants.
  """
  LETTER_UPPER = "FUN"
  LETTER_LOWER = "BBQ"
  OPERATOR     = "x"
  EQUAL        = "------------"
  ANSWER       = "000000"
  SPACE        = " "
  """
  -.split by '=='.
  """
  str = query.split('==')
  
  """
  -.spit by '*'.
  """
  digit = str[0].split('*')
  
  output = "\t"+LETTER_UPPER.replace(LETTER_UPPER,digit[0])+"\n"+OPERATOR+"\t"+LETTER_LOWER.replace(LETTER_LOWER,digit[1])+"\n"+EQUAL+"\n"+SPACE+SPACE+SPACE+SPACE+SPACE+ANSWER.replace(ANSWER,str[1])
  
  return output

"""
-.method to solve the cryptic problem.
"""
def solveCrypticProblem(crypticQuery):
  try:
    n = (i for i in crypticQuery if i.isalpha()).next()
  except StopIteration:
    return crypticQuery if eval(sub(r'(^|[^0-9])0+([1-9]+)', r'\1\2', crypticQuery)) else False
  else: 
    for i in (str(i) for i in range(10) if str(i) not in crypticQuery):
      result = solveCrypticProblem(crypticQuery.replace(n,str(i)))
      if result:
        return result
    return False

if __name__ == "__main__":
  """
  -.defined input to solve.
  """
  inputProblem = "FUN*BBQ==SUMMER"
  """
  -.routine call to solve the cryptic arithmetic problem.
  """
  result = solveCrypticProblem(inputProblem)
  """
  -.display.
  """
  if(result):
    #print(result)
	print displyTemplate(result) 
  else:
    print("Solution not found.")
	