1.wap to accept any digit and check that pos, neg , zero
 no= int(input("enter any digit:"))
if no>0:
    print('positive')
    
if no<0:
    print('negative')
if no==0:
     print('zero')

2.#wap to accept days and check the working dat and weekend
day=input("enter a day: ")
if day == "saturday" or day == "sunday" :
    print('weekend')
    
else :
    print('working')


3.wap tp accept 3 paper marks to calculate total, percentage and if percentage is greater than or equal to 60 then he /she is eligible for placment
 p1_marks=input("enter marks")
 p2_marks=input("enter marks")
 p3_marks=input("enter marks")
 total=p1_marks+p2_marks+p3_marks
 percentage = total / 150*100
 if percentage > 60:
     print('eligible ')
 else:
     print ('you deserve better')

4.wap tp accpept five diffent valu in 5 different var and check max value and print by using "simple if statemnet"
n1=input('enter num')
n2 = input('enter num')
n3=input('enter num')
n4=input('enter num')
n5=input('enter num')
if n1 >n2 and n1>n3 and n1>n4 and n1> n5 :
    print('p1 is greater')
    
if n2>n1 and n2>n3 and n2>n4 and n2>n5 :
    print('p2 is greater')
   




