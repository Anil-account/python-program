#to find power
# d=dict()
# for x in range(1,5):
#     d[x]=x**2
#     print(d)


#copy
# d1 = {'a':100, 'b':200}
# d2 = {'x':300, 'y':200}
# d = d1.copy()
# d.update(d2)
# print(d)


a=[]
dict ={'roll no' : [1,2,3,4,5], 'name' : ['ali','katy','sam','hasley','poppey'],'mark' : [55.0,99.8,78.0,67.0,45.0],'sex':['male','female','male','female','male']}
x = dict['sex']
for i in range(len(x)):
    if (dict['sex'][i])=='male':

        print("the roll of male is ", dict['roll no'][i] )
        print("the name of student is ", dict['name'][i])
