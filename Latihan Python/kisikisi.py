# def timeconverter (second):
#     hour = second // 3600
#     if hour == 0:
#         hour = '00'
#     elif hour > 0 and hour < 10:
#         hour = '0'+str(hour)
#     else:
#         hour = str(hour)
#     sleft = second - (int(hour)*3600)
#     minute = sleft // 60
#     if minute == 0:
#         minute = '00'
#     elif minute > 0 and minute < 10:
#         minute = '0'+str(minute)
#     else:
#         minute = str(minute)
#     mleft = sleft - (int(minute)*60)
#     if mleft == 0:
#         mleft = '00'
#     elif mleft > 0 and mleft < 10:
#         mleft = '0'+str(mleft)
#     else:
#         mleft = str(mleft)
    
#     hasil = hour+':'+minute+':'+mleft
#     return hasil

# detik = int(input('Masukkan detik yang ingin diconvert: '))
# print(timeconverter(detik))


# def movelima(x):
#     for i in range(len(x)):
#         for a in range(i+1):
#             if type(lis[a])==int:
#                 if lis[a]>5:
#                     lis[i],lis[a]=lis[a],lis[i]
#             for j in range (a+1):
#                 if type(lis[j])==int and type(lis[a])==int:
#                     if lis[a]>5 and lis[j]>5 and lis[a]<lis[j]:
#                         lis[a],lis[j] = lis[j],lis[a]
#                 else:
#                     lis[a],lis[j] =lis[a],lis[j]
#     return lis

# lis = [1,4,20,6,10,0,'Test',True,False,'a',0]
# print(movelima(lis))


# def paskal (n):
#     num = 1
#     x=[]
#     for i in range (1,n+1):
#         temp=[]
#         for j in range (i):
#             temp.append(num)
#             num+=1
#         for k in range (i):
#             line=[]
#             if k>0:
#                 value = sum(temp)
#                 line.append(value)
#         temp.extend(line)
#         x.append(temp)
#     print(x)
    
#     z = '   '
#     for num, a in zip(x, range(len(x))) :
#         for b in range (n-a):
#             z += '  '
#         for c in num :
#             z += str(c).ljust(5, ' ')
#         z += '\n\n' 
#     print(z)

# paskal(5)

# x = [7,8,10,22,8,9]
# for i in range (len(x)):
#     y = []
#     for j in range (i+1):
#         if x[i]<x[j]:
#             x[i],x[j]=x[j],x[i]
#     for k in range (i):
#         temp =[]
#         if x[k] == 0 or x[k]%2 != 0:
#             temp.append(' ')
#         else:
#             temp.append(str(x[k]))
#         y.extend(temp)
# print(y)

# def tiket (lis):
#     harga = 25
#     dualima = 0
#     limapuluh = 0
#     for i in range (len(lis)):
#         if lis[i]==harga:
#             dualima +=1
#         elif lis[i]==50:
#             if dualima == 0:
#                 x = 'No'
#             else:
#                 dualima -=1
#                 limapuluh +=1
#         elif lis[i]-harga==75:
#             if dualima==0:
#                 x = 'No'
#             elif dualima<3 and limapuluh==0:
#                 x = 'No'
#             elif (dualima>0 and dualima<3) or limapuluh>0:
#                 dualima -=1
#                 limapuluh -=1
#                 x = 'Yes'
#             elif dualima>3 and limapuluh==0:
#                 dualima -=3
#                 x = 'Yes'
#         else:
#             x = 'Yes'
#         print('25 : '+str(dualima))
#         print('50 : '+str(limapuluh))
#     return x

# y = [50,25,100]
# y1 = [25,25,50,100]
# y2 = [25,50,50,100]
# print(tiket(y))
# print(tiket(y1))
# print(tiket(y2))

def pascal (n):
    mainlist = [1]
    newlist = []
    for i in range (n):
        newlist.append(mainlist)
        temp = []
        temp.append(1)
        if i == 0:
            for j in range (len(mainlist)):
                temp.append(mainlist[j]+mainlist[j])
        else:
            for j in range (len(mainlist)-1):
                temp.append(mainlist[j]+mainlist[j+1])
        temp.append(1)
        mainlist = temp
    print(newlist)
    
    z = '   '
    for a,b in zip(newlist, range(len(newlist))):
        for k in range (n-b):
            z +='  '
        for l in a:
            z +=str(l).ljust(5,' ')
        z +='\n\n'
    print(z)

num = int(input('Masukkan jumlah baris: '))
pascal(num)