import pygame
import random
import sys

# ---------- Configuration ----------
WIDTH, HEIGHT = 600, 800
FPS = 60

CAR_WIDTH, CAR_HEIGHT = 50, 90
CAR_SPEED = 5

OBSTACLE_WIDTH_RANGE = (40, 120)
OBSTACLE_HEIGHT = 30
OBSTACLE_MIN_GAP = 120
OBSTACLE_SPAWN_INTERVAL = 1200  # milliseconds
OBSTACLE_BASE_SPEED = 4
OBSTACLE_SPEED_INCREMENT = 0.002  # per frame (makes it gradually harder)

BG_COLOR = (30, 30, 30)
ROAD_COLOR = (50, 50, 50)
LANE_MARK_COLOR = (220, 220, 220)
CAR_COLOR = (200, 30, 30)
OBSTACLE_COLOR = (20, 120, 200)
TEXT_COLOR = (240, 240, 240)
# -----------------------------------

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Moving Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)
big_font = pygame.font.SysFont(None, 56)

# Custom events
SPAWN_OBSTACLE = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_OBSTACLE, OBSTACLE_SPAWN_INTERVAL)


def draw_text(surf, text, x, y, font, color=TEXT_COLOR, center=False):
    img = font.render(text, True, color)
    rect = img.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surf.blit(img, rect)


class Car:
    def __init__(self, x, y):
        self.rect = pygame.Rect(0, 0, CAR_WIDTH, CAR_HEIGHT)
        self.rect.centerx = x
        self.rect.centery = y

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -CAR_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = CAR_SPEED
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -CAR_SPEED
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = CAR_SPEED

        # Move and clamp to screen bounds
        self.rect.x += dx
        self.rect.y += dy
        self.rect.left = max(self.rect.left, 50)     # keep inside road
        self.rect.right = min(self.rect.right, WIDTH - 50)
        self.rect.top = max(self.rect.top, 50)
        self.rect.bottom = min(self.rect.bottom, HEIGHT - 50)

    def draw(self, surf):
        pygame.draw.rect(surf, CAR_COLOR, self.rect, border_radius=6)
        # simple windows (just for visuals)
        win_h = int(CAR_HEIGHT * 0.25)
        win_w = int(CAR_WIDTH * 0.6)
        win_rect = pygame.Rect(0, 0, win_w, win_h)
        win_rect.centerx = self.rect.centerx
        win_rect.centery = self.rect.centery - 12
        pygame.draw.rect(surf, (220, 220, 255), win_rect, border_radius=3)


class Obstacle:
    def __init__(self, x, y, w, speed):
        self.rect = pygame.Rect(x, y, w, OBSTACLE_HEIGHT)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def draw(self, surf):
        pygame.draw.rect(surf, OBSTACLE_COLOR, self.rect, border_radius=6)


def draw_road(surf):
    # background
    surf.fill(BG_COLOR)
    # road
    road_rect = pygame.Rect(50, 50, WIDTH - 100, HEIGHT - 100)
    pygame.draw.rect(surf, ROAD_COLOR, road_rect, border_radius=8)
    # lane markings (dashed vertical center)
    lane_x = WIDTH // 2
    dash_h = 30
    gap = 20
    y = 70
    while y < HEIGHT - 70:
        pygame.draw.rect(surf, LANE_MARK_COLOR, (lane_x - 5, y, 10, dash_h))
        y += dash_h + gap


def main():
    # Initial game state
    car = Car(WIDTH // 2, HEIGHT - 160)
    obstacles = []
    running = True
    game_over = False
    score = 0
    frames = 0
    obstacle_speed = OBSTACLE_BASE_SPEED

    while running:
        dt = clock.tick(FPS)
        frames += 1
        if not game_over:
            score += dt / 1000.0  # score = seconds survived
            # gradually increase difficulty
            obstacle_speed += OBSTACLE_SPEED_INCREMENT

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == SPAWN_OBSTACLE and not game_over:
                # spawn a new obstacle near the top, random width and x within road
                w = random.randint(*OBSTACLE_WIDTH_RANGE)
                road_left = 50
                road_right = WIDTH - 50
                x = random.randint(road_left + 10, road_right - w - 10)
                obstacles.append(Obstacle(x, -OBSTACLE_HEIGHT - 10, w, obstacle_speed))
            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_r:
                    # restart
                    return main()
                if event.key == pygame.K_ESCAPE:
                    running = False

        if not game_over:
            car.handle_keys()

            # update obstacles
            for obs in obstacles:
                obs.update()

            # remove off-screen obstacles
            obstacles = [o for o in obstacles if o.rect.top <= HEIGHT + 50]

            # collision detection
            for obs in obstacles:
                if car.rect.colliderect(obs.rect):
                    game_over = True
                    break

        # draw everything
        draw_road(screen)

        for obs in obstacles:
            obs.draw(screen)

        car.draw(screen)

        # HUD
        draw_text(screen, f"Score: {int(score)}", 12, 12, font)
        draw_text(screen, "Move: Arrow keys or WASD   Restart: R   Quit: Esc", 12, HEIGHT - 30, font)

        if game_over:
            draw_text(screen, "GAME OVER", WIDTH // 2, HEIGHT // 2 - 40, big_font, center=True)
            draw_text(screen, f"Final score: {int(score)}", WIDTH // 2, HEIGHT // 2 + 10, font, center=True)
            draw_text(screen, "Press R to restart or Esc to quit", WIDTH // 2, HEIGHT // 2 + 50, font, center=True)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
