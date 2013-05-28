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
cyan = (255, 255, 0)
orange = (255, 140, 0)
pileBlocks = []


class Block:
    def __init__(self):
        randomblock = random.randint(1, 7)
        self.position = self.randomBlock(randomblock)
        self.color = self.randomColor(randomblock)
        self.falling = True

    def draw(self):
        for block in self.position:
            self.drawBlock(self.color, black, getBlockLocation(block))

    def fall(self):
        #If bottom is reached, or will collide with another block next turn
        if any(block[1] > 17 for block in self.position) or any((block[0], block[1] + 1 ) in [blocks[0] for blocks in pileBlocks] for block in self.position):
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
        elif randomblock == 6: #Squigle Left
            return [(initpos[0], initpos[1]), (initpos[0]-1, initpos[1]), (initpos[0]+1, initpos[1]+1), (initpos[0], initpos[1]+1)]
        else: #Squigle Right
            return [(initpos[0], initpos[1]), (initpos[0]+1, initpos[1]), (initpos[0]-1, initpos[1]+1), (initpos[0], initpos[1]+1)]

    def randomColor(self, randomblock):
        if randomblock == 1:
            return red
        elif randomblock == 2:
            return orange
        elif randomblock == 3:
            return purple
        elif randomblock == 4:
            return cyan
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
        if all(block[0] >= 2 for block in self.position) and self.falling and not any((block[0] - 1, block[1]) in [blocks[0] for blocks in pileBlocks] for block in self.position):
            self.position = [(block[0] - 1, block[1]) for block in self.position]

    def moveRight(self):
        if all(block[0] <= 9 for block in self.position) and self.falling and not any((block[0] + 1, block[1]) in [blocks[0] for blocks in pileBlocks] for block in self.position):
            self.position = [(block[0] + 1, block[1]) for block in self.position]

def getBlockLocation(blockLoc):
    return (blockLoc[0]*30, blockLoc[1]*30, 30, 30)


def drawPile(pileBlocks):
    for block in pileBlocks:
        pygame.draw.rect(screen, block[1], getBlockLocation(block[0]), 0)
        pygame.draw.rect(screen, black, getBlockLocation(block[0]), 1)
    
def run():
    clocker = pygame.time.Clock()
    fallspeed = 50
    fallBlock = Block()
    time = 0
    
    while 1:
        clocker.tick()
        time += clocker.get_time()
        
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    fallBlock = Block()
                elif event.key == pygame.K_m:
                    fallBlock.showPos()
                elif event.key == pygame.K_LEFT:
                    fallBlock.moveLeft()
                elif event.key == pygame.K_RIGHT:
                    fallBlock.moveRight()

        if (float(time) /10 > fallspeed):
            time = 0
            if not fallBlock.fall():
                for block in fallBlock.position:
                    pileBlocks.append((block, fallBlock.color))
                fallBlock = Block()

        fallBlock.draw()
        drawPile(pileBlocks)
                                                                
        pygame.display.flip()
        
