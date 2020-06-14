#solve1
z=''
for item in range (5,0,-1):
    for item1 in range (0,item):
        z+=' * '
    z+='\n'
print('Solve 1\n'+z)

#solve2
z = ''
for item in range(5,0,-1):
    for item1 in range (0,item):
        z+=' * '
    z+='\n'
for item2 in range (1,5,1):
    for item3 in range (0,item2+1):
        z+=' * '
    z+='\n'
print('\nSolve 2\n'+z)


# #solve3
z = ''
for item in range (0,10):
    for item1 in range (0,9-item):
        z+='   '
    for item2 in range (0,2*item+1):
        z+=' * '
    z+='\n'
print('\nSolve 3\n'+z)

#solve4
z=''
for item in range (10,0,-1):
    for item1 in range (0,10-item):
        z+='   '
    for item2 in range (0,2*item-1):
        z+=' * '
    z+='\n'
print('\nSolve 4\n'+z)

#solve5
z=''
for item in range (0,5):
    for item1 in range (0,4-item):
        z+='   '
    for item2 in range (0,2*item+1):
        z+=' * '
    z+='\n'
for item3 in range (5,0,-1):
    for item in range (0,5-item3):
        z+='   '
    for item in range (0,2*item3-1):
        z+=' * '
    z+='\n'
print('\nSolve 5\n'+z)
