import pygame
import random
import array



#Set things
while True:
    WIDTH = 1216
    HEIGHT = 720
    TILESIZE = 32
    GRIDWIDTH = WIDTH / TILESIZE
    GRIDHEIGHT = HEIGHT / TILESIZE
    WHITE = (255,255,255)
    RED = (255,0,0)
    cube_gposX = []
    cube_gposY = []
    walkers = int(input("\n \n \n \nNumber of Walkers[4] : ") or 4 )
    steps = int(input("Number of Steps[90] : ") or 90)
    for x in range(walkers):
        cube_gposX.append(GRIDWIDTH / 2)
        cube_gposY.append(GRIDHEIGHT / 2)
    GEN_LIMIT = steps
    generated = False
    floormarkerX = array.array("i")
    floormarkerY = array.array("i")
    #initº1º1
    pygame.init()
    clock = pygame.time.Clock()
    #set screem
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    running = True

    #Icon + title
    pygame.display.set_caption("Window")

    #Set images
    testCube_img = pygame.image.load("empty.png")

    #def thimgs
    def testCube(index):
        screen.blit(testCube_img,(cube_gposX[index] * TILESIZE,cube_gposY[index] * TILESIZE))
        floormarkerX.append(int(cube_gposX[index]))
        floormarkerY.append(int(cube_gposY[index]))
        count = 0
        while count < len(floormarkerX):
            pygame.draw.rect(screen,RED,(floormarkerX[count] * TILESIZE,floormarkerY[count] * TILESIZE,32,32))
            count += 1

    def grid():
        for x in range(0,WIDTH,TILESIZE):
            pygame.draw.line(screen,WHITE,(x,0),(x,HEIGHT))

        for y in range(0,HEIGHT,TILESIZE):
            pygame.draw.line(screen,WHITE,(0,y),(WIDTH,y))

    def cubebound(index):
        global cube_gposX
        global cube_gposY
        if cube_gposX[index] > WIDTH - 1:
            cube_gposX[index] = WIDTH - 2
        if cube_gposY[index] > HEIGHT - 1:
            cube_gposY[index] = HEIGHT - 2
        if cube_gposX[index] < 1:
            cube_gposX[index] = 1
        if cube_gposY[index] < 1:
            cube_gposY[index] = 1


    def random_walk():

        global cube_gposX
        global cube_gposY
        global generated

        for x in range(0, len(cube_gposX)):
            DOWN = cube_gposY[x] + 1
            UP = cube_gposY[x] - 1
            LEFT = cube_gposX[x] + 1
            RIGHT = cube_gposX[x] - 1
            if generated == False:
                select_dir = random.random()
                if select_dir > 0 and select_dir < 0.25:
                    #print("LEFT")
                    cube_gposX[x] = LEFT
                if select_dir > 0.26 and select_dir < 0.5:
                    #print("RIGHT")
                    cube_gposX[x] = RIGHT
                if select_dir > 0.51 and select_dir < 0.75:
                    #print("UP")
                    cube_gposY[x] = UP
                if select_dir > 0.76 and select_dir < 1:
                    #print("DOWN")
                    cube_gposY[x] = DOWN



    #game loop
    while running == True:
        clock.tick(30)
        screen.fill((0,0,0))
        grid()
        random_walk()
        for x in range(0, len(cube_gposX)):
            testCube(x)
            cubebound(x)
        if GEN_LIMIT == 0:
            generated = True
        GEN_LIMIT -= 1
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
        pygame.display.update()
