
from game2 import *

def pile_face():
	"""	Jeu de pile et face de 2 joueurs
		Si les joueurs jouent la meme strategie le joueur prend 1 et l'autre -1, l'inverse sinon
		(exemple dans le cours)
		"""
	game_pile_face = [[(1,-1),(-1,1)],[(-1,1),(1,-1)]]
	game = game_pile_face
	tracer(game)




if __name__ == '__main__':
	pile_face()
