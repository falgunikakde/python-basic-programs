mylist=["prashant","ashish","komal","anushka","ashish",77,"sandip",60.53,"prashant"]
print(mylist)
print(type(mylist))
print(mylist[0])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:5])
print(mylist[1:8:2])
print(mylist[:])
print(mylist[::-1])

mylist=["prashant","ashish","komal","anushka","ashish",77,"sandip",60.53,"prashant"]
mylist.append('harsh')
mylist.append("laxman")
print(mylist)

mylist.insert(1,"sanket")
print(mylist)

mylist.remove("sandip")
print(mylist)

newlist= mylist.copy() #cloning a list
print(mylist)
print(newlist)
mylist = [['prashant', 'jha'],['85.56'],[440022,"yyy"]]
print("example of multidimensional list :")
print(mylist)
print (mylist)
#mylist [row] [col]
print(mylist[0][0])
print(mylist[0][1])
print(mylist[1][0])
print(mylist[2][0])
print(mylist[2][1])

list1=["prashant","jha"]
print(list1 *2) #it will print two times
list2=[50,25.50,'prashant']
del list2[2]#del  particular valur of list
print(list2)list2.clear() #clears all the value of the list
print(list2)

name= "prashant"
print(name)
myname=list(name) #typecasting
print(myname)

