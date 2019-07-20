import sys
sys.setrecursionlimit(10**9)
# def check_rect(L):
# 	d = {}
# 	count = 0
# 	for i in L:
# 		d[i[0]] = []
# 	for i in L:
# 		d[i[0]].append(i[1])
# 	for i in d:
# 		d[i].sort()
# 	l = d.keys()
# 	for i in range(len(l)):
# 		s1 = set(d[l[i]])
# 		for j in range(i+1,len(l)):
# 			s2 = set(d[l[j]])
# 			s3 = s1.intersection(s2)
# 			if len(s3) >= 2:
# 				print l[i],l[j],s3
# 				count += 1
# 				return False
# 	print count
# 	return True


t = int(raw_input())
ans = []
for i in range(t):
	n = int(raw_input())
	mat = []
	for i in range(n):
		row = ['.']*n
		mat.append(row)
	coords =[]
	#d1
	for i in range(n):
		mat[i][i] ='O'
		#coords.append([i,i])
	#d2
	for i in range(1,n):
		mat[i][i-1] = 'O'
		#coords.append([i,i-1])
	#d3
	for i in range(2,n):
		mat[i-2][i] = 'O'
		#coords.append([i-2,i])
	#d4
	for i in range(5,n):
		mat[i][i-5] = 'O'
		#coords.append([i,i-5])
	#d5
	for i in range(8,n):
		mat[i-8][i] = 'O'
		#coords.append([i-8,i])
	#d6
	for i in range(15,n):
		mat[i][i-15] ='O'
		#coords.append([i,i-15])
	#d7
	for i in range(20,n):
		mat[i-20][i] = 'O'
		#coords.append([i-20,i])
	#d8
	for i in range(31,n):
		mat[i][i-31] = 'O'
		#coords.append([i,i-31])
	#d9
	for i in range(64,n):
		mat[i-64][i] = 'O'
		#coords.append([i-64,i])
	#d10
	for i in range(53,n):
		mat[i][i-53] = 'O'
		#coords.append([i,i-53])
	#d11
	for i in range(81,n):
		mat[i][i-81] = 'O'
		#coords.append([i,i-81])
	s = ''
	# for i in coords:
	# 	mat[i[0]][i[1]] = 'O'
	for i in mat:
		s += ''.join(i for i in i)+'\n'
	ans.append(s)
for i in ans:
	print i
