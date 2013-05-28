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
            self.drawBlock(self.color, black, (block[0]*30, block[1]*30, 30, 30))

    def fall(self):
        if any(block[1] > 16 for block in self.position):
            self.falling = False
        if self.falling:
            self.position = [(block[0], block[1] + 1) for block in self.position]
        return self.falling
                
    def randomBlock(self, randomblock):
        initpos = [1,1]
        if randomblock == 1: #Block
            return [(initpos[0], initpos[1]), (initpos[0]+1, initpos[1]), (initpos[0], initpos[1]+1), (initpos[0]+1, initpos[1]+1)]
        elif randomblock == 2: #Straight
            return [(initpos[0], initpos[1]), (initpos[0], initpos[1]+1), (initpos[0], initpos[1]+2), (initpos[0], initpos[1]+3)]
        elif randomblock == 3: #LeftLong
            return [(initpos[0], initpos[1]), (initpos[0], initpos[1]+1), (initpos[0], initpos[1]+2), (initpos[0]+1, initpos[1]+2)]
        elif randomblock == 4: #RightLong
            return [(initpos[0], initpos[1]), (initpos[0], initpos[1]+1), (initpos[0], initpos[1]+2), (initpos[0]-1, initpos[1]+2)]
        elif randomblock == 5: #Middle
            return [(initpos[0], initpos[1]), (initpos[0]-1, initpos[1]), (initpos[0]+1, initpos[1]), (initpos[0], initpos[1]+1)]
        elif randomblock == 6:
            return [(initpos[0], initpos[1]), (initpos[0]-1, initpos[1]), (initpos[0]+1, initpos[1]+1), (initpos[0], initpos[1]+1)]
        else:
            return [(initpos[0], initpos[1]), (initpos[0]+1, initpos[1]), (initpos[0]-1, initpos[1]+1), (initpos[0], initpos[1]+1)]

    def randomColor(self, randomblock):
        if randomblock == 1:
            return red
        elif randomblock == 2:
            return black
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

    def showPos(self):
        print self.position

    def moveLeft(self):
        if all(block[0] >= 2 for block in self.position) and self.falling:
            self.position = [(block[0] - 1, block[1]) for block in self.position]

    def moveRight(self):
        if all(block[0] <= 9 for block in self.position) and self.falling:
            self.position = [(block[0] + 1, block[1]) for block in self.position]




def drawPile(pileBlocks):
    for block in pileBlocks:
        pygame.draw.rect(screen, block[1], (block[0][0]*30, block[0][1]*30, 30, 30), 0)
        pygame.draw.rect(screen, black, (block[0][0]*30, block[0][1]*30, 30, 30), 1)
    
def run():
    clocker = pygame.time.Clock()
    fallspeed = 50
    temp = Block()
    time = 0
    pileBlocks = []
        
    while 1:
        clocker.tick()
        time += clocker.get_time()
        #firstblock = (initpos[0], initpos[1] + fallspeed * float(time)/1000)
        
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    temp = Block()
                elif event.key == pygame.K_m:
                    temp.showPos()
                elif event.key == pygame.K_LEFT:
                    temp.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    temp.moveRight()
                
              #      initpos = (initpos[0] - 30, initpos[1])
               # elif event.key == pygame.K_RIGHT:
                #    initpos = (initpos[0] + 30, initpos[1])
        #print time
        #drawBlock(red, black, (initpos[0], initpos[1], 30,30))
        if (float(time) /10 > fallspeed):
            time = 0
            if not temp.fall():
                for block in temp.position:
                    pileBlocks.append((block,temp.color))
                    print pileBlocks
                temp = Block()

        temp.draw()
        drawPile(pileBlocks)
        #drawBlock(blue, black, (200, 320, 30, 30))
        pygame.display.flip()
        
