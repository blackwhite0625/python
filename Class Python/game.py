import pygame
import random
import math
import os

# 初始化Pygame
pygame.init()

# 設置屏幕
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("雙人FPS遊戲")

# 顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 玩家類
class Player:
    def __init__(self, x, y, controls):
        self.x = x
        self.y = y
        self.speed = 5
        self.health = 100
        self.damage = 30  # 降低初始傷害
        self.controls = controls

    def move(self, dx, dy):
        self.x = max(0, min(self.x + dx, WIDTH - 50))
        self.y = max(0, min(self.y + dy, HEIGHT - 50))

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, 50, 50))

# 敵人類
class Enemy:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 40)
        self.y = random.randint(0, HEIGHT - 40)
        self.health = 50
        self.speed = 2

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

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, 40, 40))
        health_text = pygame.font.SysFont(None, 24).render(str(self.health), True, WHITE)
        screen.blit(health_text, (self.x + 10, self.y - 20))

# BOSS類
class Boss:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.health = 200
        self.speed = 1
        self.attack_cooldown = 1000  # 攻擊冷卻時間（毫秒）
        self.last_attack_time = pygame.time.get_ticks()

    def move_towards_players(self, players):
        closest_player = min(players, key=lambda player: math.hypot(player.x - self.x, player.y - self.y))
        dx = closest_player.x - self.x
        dy = closest_player.y - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist > 0:
            dx /= dist
            dy /= dist
            self.x += dx * self.speed
            self.y += dy * self.speed

    def attack(self, players):
        current_time = pygame.time.get_ticks()
        for player in players:
            if current_time - self.last_attack_time > self.attack_cooldown:
                player.health -= 5  # BOSS 每次攻擊損失5點血量
                self.last_attack_time = current_time

    def draw(self):
        pygame.draw.rect(screen, (255, 215, 0), (self.x, self.y, 60, 60))  # 金色 BOSS
        health_text = pygame.font.SysFont(None, 24).render(str(self.health), True, WHITE)
        screen.blit(health_text, (self.x + 10, self.y - 20))

# 子彈類
class Bullet:
    def __init__(self, x, y, target, damage):
        self.x = x
        self.y = y
        self.speed = 10
        self.target = target
        self.dx = target.x - x
        self.dy = target.y - y
        dist = math.sqrt(self.dx ** 2 + self.dy ** 2)
        self.dx /= dist
        self.dy /= dist
        self.damage = damage

    def update(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed

    def draw(self):
        pygame.draw.circle(screen, GREEN, (int(self.x), int(self.y)), 5)

# 升級道具類
class Upgrade:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 20)
        self.y = random.randint(0, HEIGHT - 20)

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, 20, 20))

# 血量包類
class HealthPack:
    def __init__(self):
        self.x = random.randint(0, WIDTH - 20)
        self.y = random.randint(0, HEIGHT - 20)

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 255), (self.x, self.y, 20, 20))  # 粘粉色血量包

# 讀取排行榜
def load_high_scores():
    if not os.path.exists("high_scores.txt"):
        return []
    with open("high_scores.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

# 寫入排行榜
def save_high_score(score):
    high_scores = load_high_scores()
    high_scores.append(str(score))
    high_scores = sorted(map(int, high_scores), reverse=True)[:5]  # 只保留前5名
    with open("high_scores.txt", "w") as f:
        for s in high_scores:
            f.write(f"{s}\n")

def game_over_screen(score):
    save_high_score(score)  # 保存分數到排行榜
    high_scores = load_high_scores()  # 讀取排行榜

    font = pygame.font.SysFont(None, 74)
    over_text = font.render('Game Over', True, WHITE)
    score_text = font.render(f'Score: {score}', True, WHITE)
    restart_text = font.render('Press R to Restart', True, WHITE)

    screen.fill(BLACK)
    screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2 - 50))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 50))

    # 顯示排行榜
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # 按 R 鍵重新開始
                    waiting = False

# 主遊戲循環
def main():
    clock = pygame.time.Clock()
    players = [Player(WIDTH // 4, HEIGHT // 2, "WASD"), Player(WIDTH * 3 // 4, HEIGHT // 2, "ARROWS")]
    enemies = []
    bullets = []
    upgrades = []
    health_packs = []
    score = 0
    boss = None
    boss_phase = 0  # 0: 普通關卡，1: BOSS 關卡

    # 初始生成一些敵人
    for _ in range(3):  # 減少敵人的數量
        enemies.append(Enemy())

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # 玩家 1 控制（WASD）
        if keys[pygame.K_a]:  # 左
            players[0].move(-players[0].speed, 0)
        if keys[pygame.K_d]:  # 右
            players[0].move(players[0].speed, 0)
        if keys[pygame.K_w]:  # 上
            players[0].move(0, -players[0].speed)
        if keys[pygame.K_s]:  # 下
            players[0].move(0, players[0].speed)
        if keys[pygame.K_SPACE]:  # 玩家1攻擊
            mouse_x, mouse_y = pygame.mouse.get_pos()
            bullet = Bullet(players[0].x + 25, players[0].y + 25, mouse_x, mouse_y, players[0].damage)
            bullets.append(bullet)

        # 玩家 2 控制（箭頭）
          # 玩家 2 控制（箭頭）
        if keys[pygame.K_LEFT]:  # 左
            players[1].move(-players[1].speed, 0)
        if keys[pygame.K_RIGHT]:  # 右
            players[1].move(players[1].speed, 0)
        if keys[pygame.K_UP]:  # 上
            players[1].move(0, -players[1].speed)
        if keys[pygame.K_DOWN]:  # 下
            players[1].move(0, players[1].speed)
        if keys[pygame.K_RETURN]:  # 玩家 2 攻擊
         if enemies:  # 確保有敵人
            closest_enemy = min(enemies, key=lambda enemy: math.hypot(enemy.x - players[1].x, enemy.y - players[1].y))
            bullet = Bullet(players[1].x + 25, players[1].y + 25, closest_enemy, players[1].damage)
            bullets.append(bullet)




        # 更新敵人
        for enemy in enemies:
            enemy.move_towards_player(players)

            # 檢查敵人是否接觸玩家
            for player in players:
                if (enemy.x < player.x + 50 and enemy.x + 40 > player.x and
                    enemy.y < player.y + 50 and enemy.y + 40 > player.y):
                    player.health -= 1  # 每次接觸損失1點血量

        # 更新子彈
        for bullet in bullets[:]:
            bullet.update()
            if bullet.x < 0 or bullet.x > WIDTH or bullet.y < 0 or bullet.y > HEIGHT:
                bullets.remove(bullet)
            else:
                # 檢查是否擊中敵人
                for enemy in enemies[:]:
                    if (bullet.x > enemy.x and bullet.x < enemy.x + 40 and
                            bullet.y > enemy.y and bullet.y < enemy.y + 40):
                        enemy.health -= bullet.damage  # 子彈傷害
                        bullets.remove(bullet)
                        if enemy.health <= 0:
                            enemies.remove(enemy)
                            score += 10  # 增加分數
                            # 有機會掉落升級道具
                            if random.random() < 0.5:  # 50% 機率
                                upgrades.append(Upgrade())
                            # 有機會掉落血量包
                            if random.random() < 0.5:  # 50% 機率
                                health_packs.append(HealthPack())
                            enemies.append(Enemy())  # 增加新敵人
                        break

        # 檢查玩家是否撿到升級道具
        for upgrade in upgrades[:]:
            for player in players:
                if (upgrade.x < player.x + 50 and upgrade.x + 20 > player.x and
                        upgrade.y < player.y + 50 and upgrade.y + 20 > player.y):
                    player.damage += 10  # 增加傷害
                    upgrades.remove(upgrade)

        # 檢查玩家是否撿到血量包
        for health_pack in health_packs[:]:
            for player in players:
                if (health_pack.x < player.x + 50 and health_pack.x + 20 > player.x and
                        health_pack.y < player.y + 50 and health_pack.y + 20 > player.y):
                    player.health += 20  # 回復20點血量
                    health_packs.remove(health_pack)

        # 檢查是否進入 BOSS 關卡
        if score >= 50 and boss_phase == 0:
            boss_phase = 1
            boss = Boss()

        # 更新 BOSS
        if boss_phase == 1 and boss:
            boss.move_towards_players(players)
            boss.attack(players)  # BOSS 攻擊玩家

            # 檢查 BOSS 是否接觸玩家
            for player in players:
                if (boss.x < player.x + 50 and boss.x + 60 > player.x and
                    boss.y < player.y + 50 and boss.y + 60 > player.y):
                    player.health -= 1  # 每次接觸損失1點血量

            # 檢查子彈是否擊中 BOSS
            for bullet in bullets[:]:
                if (bullet.x > boss.x and bullet.x < boss.x + 60 and
                        bullet.y > boss.y and bullet.y < boss.y + 60):
                    boss.health -= bullet.damage  # 子彈傷害
                    bullets.remove(bullet)
                    if boss.health <= 0:
                        boss = None
                        score += 50  # 击败BOSS后增加分数
                        boss_phase = 0  # 结束BOSS阶段
                        enemies = []  # 清空敵人列表，進入下一關
                        for _ in range(3 + (score // 50) * 2):  # 增加敵人數量
                            enemies.append(Enemy())
                    break

        # 如果任一玩家的血量為0，顯示Game Over畫面
        if any(player.health <= 0 for player in players):
            game_over_screen(score)
            players = [Player(WIDTH // 4, HEIGHT // 2, "WASD"), Player(WIDTH * 3 // 4, HEIGHT // 2, "ARROWS")]  # 重新生成玩家
            enemies = []  # 清空敵人列表
            upgrades = []  # 清空升級道具列表
            health_packs = []  # 清空血量包列表
            boss = None
            score = 0  # 重置分數
            for _ in range(3):  # 重新生成敵人
                enemies.append(Enemy())

        # 畫出玩家、敵人、BOSS 和子彈
        for player in players:
            player.draw()
        for enemy in enemies:
            enemy.draw()
        for bullet in bullets:
            bullet.draw()
        if boss_phase == 1 and boss:
            boss.draw()
        for upgrade in upgrades:
            upgrade.draw()
        for health_pack in health_packs:
            health_pack.draw()

        # 顯示玩家血量和分數
        font = pygame.font.SysFont(None, 36)
        health_text = font.render(f'P1 Health: {players[0].health}', True, WHITE)
        health_text2 = font.render(f'P2 Health: {players[1].health}', True, WHITE)
        score_text = font.render(f'Score: {score}', True, WHITE)
        damage_text = font.render(f'P1 Damage: {players[0].damage}', True, WHITE)
        damage_text2 = font.render(f'P2 Damage: {players[1].damage}', True, WHITE)
        screen.blit(health_text, (10, 10))
        screen.blit(health_text2, (10, 40))
        screen.blit(score_text, (10, 70))
        screen.blit(damage_text, (10, 100))
        screen.blit(damage_text2, (10, 130))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
