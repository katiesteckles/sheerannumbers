import itertools # for generating list of permutations
import csv # for output
albums=[1.0,3.0,4.0,4.0,5.0,7.0,13.0,13.0,18.0,19.0,21.0,25.0,25.0,50.0,1977.0,1989.0,8701.0] # .0 forces floats
# initialise lists
ptd=[]
pdt=[]
dpt=[]
dtp=[]
tpd=[]
tdp=[]

perms = list(itertools.permutations(albums,4)) # generate all possible orderings of 4 things from the 17

for i in perms: # iterate over all the sets of four things and work out all the different numbers using the three symbols
	ptd.append(i[0]+(i[1]*(i[2]/i[3])))
	pdt.append(i[0]+((i[1]/i[2])*i[3]))
	dpt.append((i[0]/i[1])+(i[2]*i[3]))
	dtp.append(((i[0]/i[1])*i[2])+i[3])
	tpd.append((i[0]*i[1])+(i[2]/i[3]))
	tdp.append((i[0]*(i[1]/i[2]))+i[3])

# output to csv
with open('sheeran-numbers.csv', 'wb') as csvfile:
    sheeran = csv.writer(csvfile, delimiter=',')
    for i in range(len(perms)):
		sheeran.writerow(list(perms[i]) + [ptd[i], pdt[i], dtp[i], dpt[i], tdp[i], tpd[i]]) # include the four albums used also
