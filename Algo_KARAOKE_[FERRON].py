class player:
def __init__ (self,ScoreMusic,MusicChoisit):
    self.score = ScoreMusic
    self.musique = MusicChoisit
def getMusique(self):
    return self.musique
def getScore(self):
    return self.score


class Karaoke:
def __init__(self,musique):


Musique1 = ("C'est un fameux trois-mâts, fin comme un oiseau...")
Musique2 = ("Sasageyo! sasageyo! shinzou wo sasageyo!...")
Musique3 = ("In my heart lies a desert...")
Musique4 = ("Like the legend of the phoenix...")
Musique5 = ("Somebody once told me the world is gonna roll me...")

karaoké = {1:Musique1,2:Musique2,3:Musique3,4:Musique4,5:Musique5}

Choix_de_la_musique = 0
print ("Choisissez une musique")
int(input(Choix_de_la_musique))

if input == 1:
    print(Musique1)
if input == 2:
    print (Musique2)
if input == 3:
    print (Musique3)
if input == 4:
    print (Musique4)
if input == 5:
    print (Musique5)

