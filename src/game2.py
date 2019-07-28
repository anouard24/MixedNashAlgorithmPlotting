import numpy as np
import matplotlib.pyplot as plt

try:
	type(print_eq)
except Exception as e:
	def print_eq(eq,var_s):
		x,i = eq
		str_to_print = ""
		if i!=0:
			if i>0 and x!=0: str_to_print = str_to_print+"+"
		if x!=0:
			str_to_print = str(x)+var_s+str_to_print
			if i!=0:
				str_to_print = str_to_print+str(i)
		return str_to_print

def getXY_game(game):

	uo1 = [game[0][0][0]-game[0][1][0],1*game[0][1][0]]
	uf1 = [game[1][0][0]-game[1][1][0],1*game[1][1][0]]
	print("Les utilites des joueurs :")
	print("U(j1,s1) = "+print_eq(uo1,"q"))
	print("U(j1,s2) = "+print_eq(uf1,"q"))

	uf2 = [game[0][1][1]-game[1][1][1],1*game[1][1][1]]
	uo2 = [game[0][0][1]-game[1][0][1],1*game[1][0][1]]
	print("-"*40)
	print("U(j2,s1) = "+print_eq(uo2,"r"))
	print("U(j2,s2) = "+print_eq(uf2,"r"))

	u_indif_1 = [uo1[0]-uf1[0] , uo1[1]-uf1[1]]
	print("(U1)'= "+str(u_indif_1))

	
	x2 = np.linspace(0,1,5000)
	y2 = np.linspace(0,1,5000)
	
	for i,xi in enumerate(x2):
		if u_indif_1[0]*xi + u_indif_1[1] > 0:
			y2[i] = 1
		elif u_indif_1[0]*xi + u_indif_1[1] < 0:
			y2[i] = 0
	##########################################
	##########################################

	x1 = np.linspace(0,1,5000)
	y1 = np.linspace(0,1,5000)
	
	u_indif_2 = [uo2[0]-uf2[0] , uo2[1]-uf2[1]]
	print("(U2)'= "+str(u_indif_2))

	for i,yi in enumerate(y1):
		if u_indif_2[0]*yi + u_indif_2[1] > 0:
			x1[i] = 1
		elif u_indif_2[0]*yi + u_indif_2[1] < 0:
			x1[i] = 0


	ena,enb = (-float(u_indif_1[1])/float(u_indif_1[0]),-float(u_indif_2[1])/float(u_indif_2[0]))
	if(ena>=0 and ena<=1 and enb>=0 and enb<=1):
		print("Equilibre de Nash en strategie mixte :("+str(-(u_indif_1[1]))+"/"+str(u_indif_1[0])+"  ,  "+str(-(u_indif_2[1]))+"/"+str(u_indif_2[0])+")")
	else:
		print("Pas d'equilibre de Nash mixte")
	return x1,y1,x2,y2

def tracer(game):
	print("Le tableau du jeu :")
	for d in game:
		print(d)

	x1,y1,x2,y2 = getXY_game(game)
	plt.plot(x1, y1,".-")
	plt.plot(x2, y2,".-")

	plt.title("Representation graphique du jeu")

	plt.axis("equal")
	plt.show()


