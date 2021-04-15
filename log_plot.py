import matplotlib.pyplot as plt
f = open ('log10_4.txt','r')
log_matrix=f.read().split('\n')
x=list()
y=list()
for log_vector in log_matrix:
	log_lines=log_vector.split('\t')
	try:
		x.append(float(log_lines[1]))
		y.append(float(log_lines[2]))
	except:
		pass
plt.plot(x,y)
plt.show()

