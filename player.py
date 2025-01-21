import pygame
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt        
       
    def shoot(self):
        if self.timer <= 0:
            new_shot = Shot(self.position.x, self.position.y)
            shot_velocity = pygame.Vector2(0,1)
            shot_velocity = shot_velocity.rotate(self.rotation)
            shot_velocity *= PLAYER_SHOOT_SPEED
            new_shot.velocity = shot_velocity
            self.timer = PLAYER_SHOOT_COOLDOWN

            

    def update(self, dt):
        self.timer -= dt       
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

# Further learning with boots
#    def get_position_info(self):
#        print(f"Position vector: {self.position}")
#        print(f"X coordinate: {self.position.x}")
#        print(f"Y coordinate: {self.position.y}")    

