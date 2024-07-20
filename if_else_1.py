a = int(input("enter value of a: "))
if a < 10:
    b = 0
else:
    b = 99
print(b)
score = int(input("enter score: "))
if score >= 90:
  print('Your grade is A.')
else:
   if score >= 80:
      print('Your grade is B.')
   else:
      if score >= 70:
         print('Your grade is C.')
      else:
         if score >= 50:
           print('Your grade is D.')
         else:
            print('Your grade is F.')
