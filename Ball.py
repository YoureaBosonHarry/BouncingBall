# Create a pygame simple bouncing ball
import random , pygame , math
# Create the settings

(width , height) = 600 , 600
background_color = (255 , 255 , 255)

class Particle():
    """simulate a bouncing ball"""
    
    def __init__(self , radius, x , y):
        self.color = (0 , 0 , 0)
        self.thickness = 0
        self.speed = 0
        self.angle = 0
        self.radius = radius
        self.x = x
        self.y = y
    
    def display_particle(self):
        pygame.draw.circle(screen , self.color ,
                           (int(self.x) , int(self.y))
                           , self.radius , self.thickness)
        
    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y -= self.speed * math.sin(self.angle)
        
    def boundary(self):
        if self.x >= width - self.radius:
            self.x = 2*(width - self.radius) - self.x
            self.angle = math.pi - self.angle
        elif self.x <= self.radius:
            self.x = 2*self.radius - self.x
            self.angle = math.pi - self.angle
            
        if self.y >= height - self.radius:
            self.y = 2*(height - self.radius) - self.y
            self.angle = -self.angle
        elif self.y <= self.radius:
            self.y = 2*self.radius - self.y
            self.angle = -self.angle
    
screen = pygame.display.set_mode((width , height))
pygame.display.set_caption("Balls")

number_of_balls = 1
particle_list = []

for n in range(number_of_balls):
    radius = random.randint(10 , 20)
    x = random.randint(radius , width - radius)
    y = random.randint(radius , height - radius)
    particle = Particle(radius , x , y)
    particle.speed = random.random()
    particle.angle = random.uniform(0 , math.pi * 2)
    particle_list.append(particle)
    
running = True
while running:
    
    for particle in particle_list:
        particle.move()
        particle.display_particle()
        particle.boundary()
        
    pygame.display.flip()
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

