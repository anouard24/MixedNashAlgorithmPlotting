from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def getDeriv(eq1,eq2):
	u = []
	for x,y in zip(eq1,eq2):
		u.append(x-y)
	return u

def print_eq(eq):
	var_s=[" ","r","q","p"]

	str_to_print = ""

	for x,z in zip(eq,var_s):
		if x!=0:
			str_to_print += "+("+str(x)+")"+z

	return str_to_print

def getXYZ(u,delta=0.01):
	x = y = np.arange(0, 1, delta)
	X, Y = np.meshgrid(x, y)
	Z = X+0*Y
	xshape = X.shape
	for i in range(xshape[0]):
		for j in range(xshape[1]):
			ind = u[0] + X[i][j]*u[1] + Y[i][j]*u[2]
			if ind > 0:
				Z[i][j] = 1
			elif ind < 0:
				Z[i][j] = 0

	return X, Y, Z

def getU_game(game,exi=5000):

	uo1 = [game[0][1][0][0]+game[0][1][1][0]+game[0][1][1][0]+game[0][0][1][0],0,game[0][0][0][0]+game[0][0][1][0]-game[0][1][0][0]-game[0][1][1][0], game[0][0][0][0]-game[0][0][1][0]+game[0][1][0][0]-game[0][1][1][0]]
	uf1 = [game[1][1][0][0]+game[1][1][1][0]+game[1][1][1][0]+game[1][0][1][0],0,game[1][0][0][0]+game[1][0][1][0]-game[1][1][0][0]-game[1][1][1][0], game[1][0][0][0]-game[1][0][1][0]+game[1][1][0][0]-game[1][1][1][0]]

	print "Les utilites des joueurs :"
	print "U(j1,s1) =",print_eq(uo1)
	print "U(j1,s2) =",print_eq(uf1)


	uo2 = [game[1][0][1][1]+game[0][0][1][1]+game[1][0][0][1]+game[1][0][1][1],  game[0][0][0][1]+game[0][0][1][1]-game[1][0][0][1]-game[1][0][1][1], 0 ,game[0][0][0][1]-game[0][0][1][1]+game[1][0][0][1]-game[1][0][1][1]]
	uf2 = [game[1][1][1][1]+game[0][1][1][1]+game[1][1][0][1]+game[1][1][1][1],  game[0][1][0][1]+game[0][1][1][1]-game[1][1][0][1]-game[1][1][1][1], 0 ,game[0][1][0][1]-game[0][1][1][1]+game[1][1][0][1]-game[1][1][1][1]]

	print "-"*40
	print "U(j2,s1) =",print_eq(uo2)
	print "U(j2,s2) =",print_eq(uf2)

	uo3 = [game[1][0][0][2]+game[0][1][0][2]+game[1][1][0][2]+game[1][1][0][2],  game[0][1][0][2]+game[0][0][0][2]-game[1][0][0][2]-game[1][1][0][2],  game[0][0][0][2]-game[0][1][0][2]+game[1][0][0][2]-game[1][1][0][2] ,0]
	uf3 = [game[1][0][1][2]+game[0][1][1][2]+game[1][1][1][2]+game[1][1][1][2],  game[0][1][1][2]+game[0][0][1][2]-game[1][0][1][2]-game[1][1][1][2],  game[0][0][1][2]-game[0][1][1][2]+game[1][0][1][2]-game[1][1][1][2] ,0]

	print "-"*40
	print "U(j3,s1) =",print_eq(uo3)
	print "U(j3,s2) =",print_eq(uf3)

	u_indif_1 = getDeriv(uo1,uf1)
	u_indif_2 = getDeriv(uo2,uf2)
	u_indif_3 = getDeriv(uo3,uf3)
	print "-"*40
	print "U1' =",print_eq(u_indif_1)
	print "U2' =",print_eq(u_indif_2)
	print "U3' =",print_eq(u_indif_3)
	
	return u_indif_1, u_indif_2, u_indif_3



def get_all_xyz(game):
	u, v, w = getU_game(game)
	u.pop(1)
	v.pop(2)
	w.pop(3)
	xyz1 = getXYZ(u)
	xyz2 = getXYZ(v)
	xyz3 = getXYZ(w)

	return xyz1, xyz2 , xyz3




def wireframe(xyz1,xyz2,xyz3):	
	# first
	fig = plt.figure()
	x, y, z = xyz1
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_wireframe(x, y, z, rstride=3, cstride=3, color="blue")
	plt.title('le plan du Joueur 1')
	plt.xlabel('Joueur 2', fontsize=14)
	plt.ylabel('Joueur 3', fontsize=14)

	print "affiche joueur 1"
	plt.show()

	# second
	fig = plt.figure()
	x, y, z = xyz2
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_wireframe(x, y, z, rstride=3, cstride=3, color="green")
	plt.title('le plan du Joueur 2')
	plt.xlabel('Joueur 1', fontsize=14)
	plt.ylabel('Joueur 3', fontsize=14)

	print "affiche joueur 2"
	plt.show()

	# third
	fig = plt.figure()
	x, y, z = xyz3
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_wireframe(x, y, z, rstride=3, cstride=3, color="red")
	plt.title('le plan du Joueur 3')
	plt.xlabel('Joueur 1', fontsize=14)
	plt.ylabel('Joueur 2', fontsize=14)

	print "affiche joueur 3"
	plt.show()


def wireframe3(xyz1, xyz2, xyz3):
	fig = plt.figure()
	x, y, z = xyz1
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_wireframe(z, x, y, rstride=2, cstride=2, color="blue")

	x, y, z = xyz2
	ax.plot_wireframe(x, z, y, rstride=2, cstride=2, color="green")

	x, y, z = xyz3
	ax.plot_wireframe(x, y, z, rstride=2, cstride=2, color="red")

	plt.show()


def surface(xyz1, xyz2, xyz3):
	
	# first
	fig = plt.figure()
	x, y, z = xyz1
	ax = fig.add_subplot(111, projection='3d')
	surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
	fig.colorbar(surf, shrink=0.5, aspect=10)
	print "affiche joueur 1"
	plt.show()
	# second
	fig = plt.figure()
	x, y, z = xyz2
	ax = fig.add_subplot(111, projection='3d')
	surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
	fig.colorbar(surf, shrink=0.5, aspect=10)
	print "affiche joueur 2"
	plt.show()
	# third
	fig = plt.figure()
	x, y, z = xyz3
	ax = fig.add_subplot(111, projection='3d')
	surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)
	fig.colorbar(surf, shrink=0.5, aspect=10)
	print "affiche joueur 3"
	plt.show()
