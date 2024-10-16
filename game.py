import pygame
import random
import math
import os

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FPS Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player class
class Player:
    def __init__(self, x, y, controls):
        self.x = x
        self.y = y
        self.speed = 5
        self.health = 100
        self.damage = 30
        self.controls = controls
        self.invincible = False
        self.invincible_time = 1000  # 1秒無敵時間
        self.last_hit_time = 0

    def move(self, dx, dy):
        self.x = max(0, min(self.x + dx, WIDTH - 50))
        self.y = max(0, min(self.y + dy, HEIGHT - 50))

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 50, 50))

    def find_closest_enemy(self, enemies):
        if not enemies:
            return None
        return min(enemies, key=lambda enemy: math.hypot(enemy.x - self.x, enemy.y - self.y))

    def take_damage(self, damage):
        current_time = pygame.time.get_ticks()
        if not self.invincible:
            self.health -= damage
            self.invincible = True
            self.last_hit_time = current_time

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.invincible and current_time - self.last_hit_time > self.invincible_time:
            self.invincible = False

# Enemy class
class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.health = 50
        self.speed = 1  # 降低敵人速度

    def move_towards_player(self, players):
        closest_player = min(players, key=lambda player: math.hypot(player.x - self.x, player.y - self.y))
        dx = closest_player.x - self.x
        dy = closest_player.y - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist > 0:
            dx /= dist
            dy /= dist
            self.x += dx * self.speed
            self.y += dy * self.speed

    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, 40, 40))
        health_text = pygame.font.SysFont(None, 24).render(str(self.health), True, WHITE)
        screen.blit(health_text, (self.x + 10, self.y - 20))

# Boss class
class Boss:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.health = 500
        self.speed = 1
        self.attack_cooldown = 2000
        self.last_attack_time = pygame.time.get_ticks()
        self.direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

    def move(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]
        
        # 如果碰到邊界，改變方向
        if self.x <= 0 or self.x >= WIDTH - 60:
            self.direction = (-self.direction[0], self.direction[1])
        if self.y <= 0 or self.y >= HEIGHT - 60:
            self.direction = (self.direction[0], -self.direction[1])

    def attack(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time > self.attack_cooldown:
            self.last_attack_time = current_time
            # Boss 射擊，但不自動瞄準
            return Bullet(self.x + 30, self.y + 30, self.x + self.direction[0] * 100, self.y + self.direction[1] * 100, 10)
        return None

    def take_damage(self, damage):
        self.health -= damage
        return self.health <= 0

    def draw(self):
        pygame.draw.rect(screen, (255, 215, 0), (self.x, self.y, 60, 60))
        health_text = pygame.font.SysFont(None, 24).render(str(self.health), True, WHITE)
        screen.blit(health_text, (self.x + 10, self.y - 20))

# Bullet class
class Bullet:
    def __init__(self, x, y, target_x, target_y, damage):
        self.x = x
        self.y = y
        self.speed = 10
        self.dx = target_x - x
        self.dy = target_y - y
        dist = math.sqrt(self.dx ** 2 + self.dy ** 2)
        self.dx /= dist
        self.dy /= dist
        self.damage = damage

    def update(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def draw(self):
        pygame.draw.circle(screen, GREEN, (int(self.x), int(self.y)), 5)

# Load high scores
def load_high_scores():
    if not os.path.exists("high_scores.txt"):
        return []
    with open("high_scores.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

# Save high score
def save_high_score(score):
    high_scores = load_high_scores()
    high_scores.append(str(score))
    high_scores = sorted(map(int, high_scores), reverse=True)[:5]
    with open("high_scores.txt", "w") as f:
        for s in high_scores:
            f.write(f"{s}\n")

def game_over_screen(score):
    save_high_score(score)
    high_scores = load_high_scores()

    font = pygame.font.SysFont(None, 74)
    over_text = font.render('Game Over', True, WHITE)
    score_text = font.render(f'Score: {score}', True, WHITE)
    restart_text = font.render('Click to Restart', True, WHITE)

    screen.fill(BLACK)
    screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))

    font_small = pygame.font.SysFont(None, 36)
    for i, high_score in enumerate(high_scores):
        high_score_text = font_small.render(f"{i + 1}. {high_score}", True, WHITE)
        screen.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, HEIGHT // 2 + 100 + i * 30))
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

def mode_selection_screen():
    font = pygame.font.SysFont(None, 74)
    title_text = font.render('Select Game Mode', True, WHITE)
    single_text = font.render('1. Single Player', True, WHITE)
    multi_text = font.render('2. Two Players', True, WHITE)

    screen.fill(BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - 100))
    screen.blit(single_text, (WIDTH // 2 - single_text.get_width() // 2, HEIGHT // 2))
    screen.blit(multi_text, (WIDTH // 2 - multi_text.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if HEIGHT // 2 - 25 <= mouse_y <= HEIGHT // 2 + 25:
                    return 1  # Single player mode
                elif HEIGHT // 2 + 25 < mouse_y <= HEIGHT // 2 + 75:
                    return 2  # Two players mode

# 在文件開頭添加新的常量
BOSS_INTERVAL = 5  # 每5關生成一個boss

# Main game loop
def main():
    mode = mode_selection_screen()
    
    clock = pygame.time.Clock()
    if mode == 1:
        players = [Player(WIDTH // 2, HEIGHT // 2, "WASD")]
    else:
        players = [Player(WIDTH // 4, HEIGHT // 2, "WASD"), Player(WIDTH * 3 // 4, HEIGHT // 2, "ARROWS")]
    
    enemies = []
    bullets = []
    boss = None
    level = 1

    for _ in range(3):
        x = random.randint(0, WIDTH - 40)
        y = random.randint(0, HEIGHT - 40)
        while any(math.hypot(player.x - x, player.y - y) < 200 for player in players):
            x = random.randint(0, WIDTH - 40)
            y = random.randint(0, HEIGHT - 40)
        enemies.append(Enemy(x, y))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_result = pause_screen()
                    if pause_result == "main_menu":
                        return  # 返回主菜單

        screen.fill(BLACK)

        keys = pygame.key.get_pressed()
        
        for player in players:
            if player.controls == "WASD":
                if keys[pygame.K_a]:
                    player.move(-player.speed, 0)
                if keys[pygame.K_d]:
                    player.move(player.speed, 0)
                if keys[pygame.K_w]:
                    player.move(0, -player.speed)
                if keys[pygame.K_s]:
                    player.move(0, player.speed)
                if keys[pygame.K_g]:
                    closest_enemy = player.find_closest_enemy(enemies if not boss else [boss] + enemies)
                    if closest_enemy:
                        bullet = Bullet(player.x + 25, player.y + 25, closest_enemy.x + 20, closest_enemy.y + 20, player.damage)
                        bullets.append(bullet)
            elif player.controls == "ARROWS":
                if keys[pygame.K_LEFT]:
                    player.move(-player.speed, 0)
                if keys[pygame.K_RIGHT]:
                    player.move(player.speed, 0)
                if keys[pygame.K_UP]:
                    player.move(0, -player.speed)
                if keys[pygame.K_DOWN]:
                    player.move(0, player.speed)
                if keys[pygame.K_RETURN]:
                    closest_enemy = player.find_closest_enemy(enemies if not boss else [boss] + enemies)
                    if closest_enemy:
                        bullet = Bullet(player.x + 25, player.y + 25, closest_enemy.x + 20, closest_enemy.y + 20, player.damage)
                        bullets.append(bullet)

        for player in players:
            player.update()

        for enemy in enemies:
            enemy.move_towards_player(players)
            for player in players:
                if not player.invincible and (enemy.x < player.x + 50 and enemy.x + 40 > player.x and
                    enemy.y < player.y + 50 and enemy.y + 40 > player.y):
                    player.take_damage(1)

        if boss:
            boss.move()
            boss_bullet = boss.attack()
            if boss_bullet:
                bullets.append(boss_bullet)
            for player in players:
                if not player.invincible and (boss.x < player.x + 50 and boss.x + 60 > player.x and
                    boss.y < player.y + 50 and boss.y + 60 > player.y):
                    player.take_damage(2)

        for bullet in bullets[:]:
            bullet.update()
            if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
                bullets.remove(bullet)
            else:
                for enemy in enemies[:]:
                    if (bullet.x > enemy.x and bullet.x < enemy.x + 40 and
                            bullet.y > enemy.y and bullet.y < enemy.y + 40):
                        if enemy.take_damage(bullet.damage):
                            enemies.remove(enemy)
                        bullets.remove(bullet)
                        break
                if boss and (bullet.x > boss.x and bullet.x < boss.x + 60 and
                        bullet.y > boss.y and bullet.y < boss.y + 60):
                    if boss.take_damage(bullet.damage):
                        boss = None
                    bullets.remove(bullet)

        # 檢查是否需要進入下一關
        if not enemies and not boss:
            level += 1
            if level % BOSS_INTERVAL == 0:
                boss = Boss()
            else:
                for _ in range(3 + level):
                    x = random.randint(0, WIDTH - 40)
                    y = random.randint(0, HEIGHT - 40)
                    while any(math.hypot(player.x - x, player.y - y) < 200 for player in players):
                        x = random.randint(0, WIDTH - 40)
                        y = random.randint(0, HEIGHT - 40)
                    enemies.append(Enemy(x, y))

        if any(player.health <= 0 for player in players):
            mode = mode_selection_screen()
            if mode == 1:
                players = [Player(WIDTH // 2, HEIGHT // 2, "WASD")]
            else:
                players = [Player(WIDTH // 4, HEIGHT // 2, "WASD"), Player(WIDTH * 3 // 4, HEIGHT // 2, "ARROWS")]
            enemies = []
            bullets = []
            level = 1
            boss = None
            for _ in range(3):
                x = random.randint(0, WIDTH - 40)
                y = random.randint(0, HEIGHT - 40)
                while any(math.hypot(player.x - x, player.y - y) < 200 for player in players):
                    x = random.randint(0, WIDTH - 40)
                    y = random.randint(0, HEIGHT - 40)
                enemies.append(Enemy(x, y))

        for player in players:
            if not player.invincible or pygame.time.get_ticks() % 200 < 100:
                player.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
        if boss:
            boss.draw()

        font = pygame.font.SysFont(None, 36)
        for i, player in enumerate(players):
            health_text = font.render(f'P{i+1} Health: {player.health}', True, WHITE)
            screen.blit(health_text, (10, 10 + i * 40))
        level_text = font.render(f'Level: {level}', True, WHITE)
        screen.blit(level_text, (10, 10 + len(players) * 40))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
