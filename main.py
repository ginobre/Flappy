#Criar o pássaro

Bird = sprites.create(img("""
  
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . b b b b b 5 5 5 5 5 5 5 b . . 
            . b d 5 b 5 5 5 5 5 5 5 5 b . . 
            . . b 5 5 b 5 d 1 f 5 d 4 f . . 
            . . b d 5 5 b 1 f f 5 4 4 c . . 
            b b d b 5 5 5 d f b 4 4 4 4 b . 
            b d d c d 5 5 b 5 4 4 4 4 4 4 b 
            c d d d c c b 5 5 5 5 5 5 5 b . 
            c b d d d d d 5 5 5 5 5 5 5 b . 
            . c d d d d d d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . .
    """),
    SpriteKind.player) #Definir o tipo de Sprite

Bird.set_position(10, 10) # posição inicial do pássaro

tiles.set_tilemap(tilemap("""level1"""))
scene.camera_follow_sprite(Bird)

#Função para o pássaro bater as asas "forever"
def baterasa():
    Bird.set_image(img("""

                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . . . . b b 5 d 1 f 5 d 4 c . . 
                . . . . b 5 5 1 f f d d 4 4 4 b 
                . . . . b 5 5 d f b 4 4 4 4 b . 
                . . . b d 5 5 5 5 4 4 4 4 b . . 
                . . b d d 5 5 5 5 5 5 5 5 b . . 
                . b d d d d 5 5 5 5 5 5 5 5 b . 
                b d d d b b b 5 5 5 5 5 5 5 b . 
                c d d b 5 5 d c 5 5 5 5 5 5 b . 
                c b b d 5 d c d 5 5 5 5 5 5 b . 
                . b 5 5 b c d d 5 5 5 5 5 d b . 
                b b c c c d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . .
    """))
    pause(200)
    Bird.set_image(img("""
     
                . . . . . . b b b b b b . . . . 
                . . . . . b b 5 5 5 5 5 b . . . 
                . b b b b b 5 5 5 5 5 5 5 b . . 
                . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                . . b d 5 5 b 1 f f 5 4 4 c . . 
                b b d b 5 5 5 d f b 4 4 4 4 4 b 
                b d d c d 5 5 b 5 4 4 4 4 4 b . 
                c d d d c c b 5 5 5 5 5 5 5 b . 
                c b d d d d d 5 5 5 5 5 5 5 b . 
                . c d d d d d d 5 5 5 5 5 d b . 
                . . c b d d d d d 5 5 5 b b . . 
                . . . c c c c c c c c b b . . .
    """))
    pause(200)
    #Aceleração do pássaro 
    Bird.ay = Bird.ay + 15  #aumentar aceleração de y de 15 em 15
    Bird.ax = Bird.ax + 3   #aumentar aceleração de x de 3 em 3

forever(baterasa)  # Rodar "forever" a função bater asa.

#Definir que a barra de espaço / botão A no video game, faz o pássaro ir para cima.
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

#função : quando A estiver apertado, o pássaro vai aumentar a velocidade de y
def on_a_pressed():
    Bird.vy = -35

#Condições para o fim do jogo
#Uma função para cada vez que o pássaro encostar em um cano ou no chão.
    def orverlaptile (sprite, location):
        game.over(False)
    scene.on_overlap_tile(SpriteKind.player, assets.tile("myTile"), sobreportile1)

    def sobreportile0 (sprite, location):
        game.over(False)
    scene.on_overlap_tile(SpriteKind.player,
    assets.tile("myTile0"), sobreportile0)

    def sobreportile1 (sprite, location):
        game.over(False)
    scene.on_overlap_tile(SpriteKind.player,
    assets.tile("myTile1"), sobreportile2)

    def sobreportile2 (sprite, location):
        game.over(False)
    scene.on_overlap_tile(SpriteKind.player,
    assets.tile("myTile2"), sobreportile2)

    def sobreportile3 (sprite, location):
        game.over(True)
    scene.on_overlap_tile(SpriteKind.player,
    assets.tile("myTile3"), sobreportile3)
