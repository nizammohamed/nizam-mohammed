print '!-----------Calculator-----------!'
num1=long(input('enter first number'))
op=raw_input('select operator from (+,-,*,/)')
num2=long(input('enter second number'))


if(op=='*'):
  result=long(num1*num2)
  print result

elif(op=='/'):
  result=long(num1/num2)
  print result

elif(op=='+'):
  result=long(num1+num2)
  print result

elif(op=='-'):
result=long(num1-num2)
  print "result is",result


else:
   print 'select operator'
