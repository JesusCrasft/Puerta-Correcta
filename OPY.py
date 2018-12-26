import pygame
import random
import Tkinter
def quit():
	global ayuda
   	ayuda.destroy()
  	
ayuda = Tkinter.Tk()
ayuda.title("Intrucciones")
ITN = Tkinter.Label(ayuda,text="Tienes 3 Vidas No Choques Con Los Monstruos")
ITN.pack()
ITNb = Tkinter.Label(ayuda,text="Ve Hacia La LLave Y Despues Descubre De Que Puerta Es")
ITNb.pack()
nombre = Tkinter.Label(ayuda,text="Introduzca Un Nombre Siquiere")
nombre.pack()
name = Tkinter.Entry(ayuda)
name.pack()
print(name.get())
Iniciar = Tkinter.Button(ayuda,text="Iniciar Juego",command=quit)
Iniciar.pack()
ayuda.mainloop()



pygame.init()
pantalla = pygame.display.set_mode((1024,600))
salir = False
relog1 = pygame.time.Clock()
vidas = ["3","2","1","0"]
ju = ""
vidai = 3
imagena = pygame.image.load("img/man.png")
imagenb = pygame.image.load("img/door.png")
imagene = pygame.image.load("img/door_blue.png")
imagenf = pygame.image.load("img/door_red.png")
imagenc = pygame.image.load("img/key.png")
imagend = pygame.image.load("img/monster.png")
fuente1 = pygame.font.SysFont("Arial", 20, True, False)
info = fuente1.render("Vidas: "+vidas[0], 0, (0,0,0))
jugador = fuente1.render("Jugador: "+ju, 0, (0,0,0))
gris = (145,145,145)
blanco = (255,255,255)
negro = (0,0,0)
rojo = (200,20,50)
listasp = []
spritea = pygame.sprite.Sprite()
spritea.image = imagena
spritea.rect = imagena.get_rect()
spritea.rect.top = 50
spritea.rect.left = 50
spriteb = pygame.sprite.Sprite()
spriteb.image = imagenb
spriteb.rect = imagenb.get_rect()
spriteb.rect.top = 500
spriteb.rect.left = 970
spritef = pygame.sprite.Sprite()
spritef.image = imagenf
spritef.rect = imagenf.get_rect()
spritef.rect.top = 10
spritef.rect.left = 970
spritee = pygame.sprite.Sprite()
spritee.image = imagene
spritee.rect = imagene.get_rect()
spritee.rect.top = 10
spritee.rect.left = 5
spritec = pygame.sprite.Sprite()
spritec.image = imagenc
spritec.rect = imagenc.get_rect()
spritec.rect.top = 500
spritec.rect.left = 0
sprited = pygame.sprite.Sprite()
sprited.image = imagend
sprited.rect = imagend.get_rect()
(x,y) = (0,0)
llave = False

for x in range(60):
	w = random.randrange(5,25)
	h = random.randrange(5,25)
	x = random.randrange(998)
	y = random.randrange(500)
	listasp.append(pygame.Rect(x,y,w,h))	

while salir != True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			salir = True
		for sprite in listasp:
			if spritea.rect.colliderect(sprite):
				spritea.rect.top = 50
				spritea.rect.left = 50
				info = fuente1.render("Vidas: "+vidas[1], 0, (0,0,0))
				vidai = vidai - 1
				if vidai == 1:
					info = fuente1.render("Vidas: "+vidas[2], 0, (0,0,0))
				if vidai == 0:
					info = fuente1.render("Vidas: "+vidas[3], 0, (0,0,0))
					salir = True
					ventana = Tkinter.Tk()
					ventana.title("Game Over")
					label = Tkinter.Label(ventana,text="Game Over")
					label.pack()
					ventana.mainloop()	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				spritea.rect.move_ip(0,-10)
			if event.key == pygame.K_DOWN:
				spritea.rect.move_ip(0,+10)
			if event.key == pygame.K_LEFT:
				spritea.rect.move_ip(-10,0)
			if event.key == pygame.K_RIGHT:
				spritea.rect.move_ip(+10,0)		
		if spritea.rect.colliderect(spritec.rect):
		 	llave = True
		 	spritec.rect.top = 1000
		 	spritec.rect.left = 2000
		if spritea.rect.colliderect(spriteb.rect) and llave == True:
			ganaste = Tkinter.Tk()
			ganaste.title("Felicidades")
			felicidades = Tkinter.Label(ganaste,text="Tu Tiempo Es De: "+segundos+" Segundos")
			felicidades.pack()
			ganaste.mainloop()
			salir = True

 	oldx = spritea.rect.left
 	oldy = spritea.rect.top
	relog1.tick(20)
	pantalla.fill(gris)
	for sprite in listasp:
		pantalla.blit(sprited.image,sprite)	
		pantalla.blit(info,(300,5))	
		pantalla.blit(jugador,(800,5))	
	if spritea.rect.top > 500 or spritea.rect.top < 0:	
		spritea.rect.top = oldy
	if spritea.rect.left > 998 or spritea.rect.left < 0:	
		spritea.rect.left = oldx		
	pantalla.blit(spritea.image,spritea.rect)
	pantalla.blit(spriteb.image,spriteb.rect)
	pantalla.blit(spritec.image,spritec.rect)
	pantalla.blit(spritee.image,spritee.rect)
	pantalla.blit(spritef.image,spritef.rect)
	segundosint = pygame.time.get_ticks()/1000
	segundos = str(segundosint)
	contador = fuente1.render(segundos,0,(0,0,0))	
	pantalla.blit(contador,(500,5))
	pygame.display.update()

pygame.quit()	

def level2():
	print("aaa")