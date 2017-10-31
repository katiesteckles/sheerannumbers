import itertools
import csv
albums=[1.0,3.0,4.0,4.0,5.0,7.0,13.0,13.0,18.0,19.0,21.0,25.0,25.0,50.0,1977.0,1989.0,8701.0]
ptd=[]
pdt=[]
dpt=[]
dtp=[]
tpd=[]
tdp=[]

perms = list(itertools.permutations(albums,4))

for i in perms:
	ptd.append(i[0]+(i[1]*(i[2]/i[3])))
	pdt.append(i[0]+((i[1]/i[2])*i[3]))
	dpt.append((i[0]/i[1])+(i[2]*i[3]))
	dtp.append(((i[0]/i[1])*i[2])+i[3])
	tpd.append((i[0]*i[1])+(i[2]/i[3]))
	tdp.append((i[0]*(i[1]/i[2]))+i[3])

with open('sheeran-numbers.csv', 'wb') as csvfile:
    sheeran = csv.writer(csvfile, delimiter=',')
    for i in range(len(perms)):
		sheeran.writerow(list(perms[i]) + [ptd[i], pdt[i], dtp[i], dpt[i], tdp[i], tpd[i]])
