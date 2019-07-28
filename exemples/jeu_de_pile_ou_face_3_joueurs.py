from game3 import *


if __name__ == '__main__':
	print("Jeu de pile ou face avec un 3eme joueur ")
	tab1C = [[(1,-1,2),(1,-1,6)],[(-1,1,1),(-1,1,1)]]
	tab1F = [[(-1,1,1),(-1,1,5)],[(1,-1,5),(1,-1,1)]]
	
	jeu = [tab1C,tab1F]

	f1, f2, f3 = get_all_xyz(jeu)
	wireframe(f1, f2, f3)
	wireframe3(f1, f2, f3)
