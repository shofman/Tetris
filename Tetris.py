import sys, pygame, math, string, random, operator
pygame.init()
screen = pygame.display.set_mode((480, 640))
black = (0,0,0)
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0,0,255)
green = (0,255,0)
yellow = (0, 255, 255)
purple = (255, 0, 255)
other = (255, 255, 0)


class Block:
    
    def __init__(self):
        randomblock = random.randint(1, 7)
        self.position = self.randomBlock(randomblock)
        self.color = self.randomColor(randomblock)
        self.falling = True

    def draw(self):
        for block in self.position:
            self.drawBlock(self.color, black, (block[0], block[1], 30, 30))

    def fall(self, fallspeed):
        self.position = [(block[0], block[1] + fallspeed) for block in self.position]            
                
    def randomBlock(self, randomblock):
        initpos = [240,0]
        if randomblock == 1: #Block
            return [(initpos[0], initpos[1]), (initpos[0]+30, initpos[1]), (initpos[0], initpos[1]+30), (initpos[0]+30, initpos[1]+30)]
        elif randomblock == 2: #Straight
            return [(initpos[0], initpos[1]), (initpos[0], initpos[1]+30), (initpos[0], initpos[1]+60), (initpos[0], initpos[1]+90)]
        elif randomblock == 3: #LeftLong
            return [(initpos[0], initpos[1]), (initpos[0], initpos[1]+30), (initpos[0], initpos[1]+60), (initpos[0]+30, initpos[1]+60)]
        elif randomblock == 4: #RightLong
            return [(initpos[0], initpos[1]), (initpos[0], initpos[1]+30), (initpos[0], initpos[1]+60), (initpos[0]-30, initpos[1]+60)]
        elif randomblock == 5: #Middle
            return [(initpos[0], initpos[1]), (initpos[0]-30, initpos[1]), (initpos[0]+30, initpos[1]), (initpos[0], initpos[1]+30)]
        elif randomblock == 6:
            return [(initpos[0], initpos[1]), (initpos[0]-30, initpos[1]), (initpos[0]+30, initpos[1]+30), (initpos[0], initpos[1]+30)]
        else:
            return [(initpos[0], initpos[1]), (initpos[0]+30, initpos[1]), (initpos[0]-30, initpos[1]+30), (initpos[0], initpos[1]+30)]

    def randomColor(self, randomblock):
        if randomblock == 1:
            return red
        elif randomblock == 2:
            return white
        elif randomblock == 3:
            return purple
        elif randomblock == 4:
            return other
        elif randomblock == 5:
            return blue
        elif randomblock == 6:
            return green
        else:
            return yellow

    def drawBlock(self, color, outline, location):
        pygame.draw.rect(screen, color, location, 0)
        pygame.draw.rect(screen, outline, location, 1)


def drawBlock(color, outline, location):
    pygame.draw.rect(screen, color, location, 0)
    pygame.draw.rect(screen, outline, location, 1)



def run():
    clocker = pygame.time.Clock()
    fallspeed = 50
    temp = Block()
    
    while 1:
        clocker.tick()
        time = clocker.get_time()
        #firstblock = (initpos[0], initpos[1] + fallspeed * float(time)/1000)
        
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    temp = Block()
              #      initpos = (initpos[0] - 30, initpos[1])
               # elif event.key == pygame.K_RIGHT:
                #    initpos = (initpos[0] + 30, initpos[1])

        #drawBlock(red, black, (initpos[0], initpos[1], 30,30))
        temp.fall(fallspeed * float(time)/1000)
        temp.draw()
        drawBlock(blue, black, (200, 320, 30, 30))
        pygame.display.flip()
        
