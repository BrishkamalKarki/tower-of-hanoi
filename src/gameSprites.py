import pygame, os, gameState

class Font:
  def __init__(self):
    self.reg_font = pygame.font.Font(os.path.join("..",  "assets", "fonts", "Cinzel", "static", "Cinzel-Regular.ttf"), 28)

class Sounds:
  def __init__(self):
    self.disc_sound = pygame.mixer.Sound(os.path.join("..",  "assets", "sounds", "disc_place.wav"))
    self.btn_sound = pygame.mixer.Sound(os.path.join("..",  "assets", "sounds", "clicked.mp3"))

class Base(pygame.sprite.Sprite):
  def __init__(self, game_state):
    super().__init__()

    self.game_state: gameState.gameState = game_state
    self.base_surf = pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "sprites", "ToHBase.png")), (0.8 * self.game_state.WIDTH, 0.8 * self.game_state.HEIGHT)).convert_alpha()
    self.image = self.base_surf
    self.rect = self.image.get_rect()

class TowerOfHanoi(pygame.sprite.Sprite):
  def __init__(self, game_state):
    super().__init__()

    self.game_state: gameState.gameState = game_state
    self.base_surf = pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "sprites", "TowerOfHanoi.png")), (460, 160)).convert_alpha()
    self.image = self.base_surf
    self.rect = self.image.get_rect()

class IncBtn(pygame.sprite.Sprite):
  def __init__(self, game_state):
    super().__init__()

    self.game_state: gameState.gameState = game_state
    self.base_surf = pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "sprites", "up.png")), (30,30)).convert_alpha()
    self.image = self.base_surf
    self.rect = self.image.get_rect()

class DecBtn(pygame.sprite.Sprite):
  def __init__(self, game_state):
    super().__init__()

    self.game_state: gameState.gameState = game_state
    self.base_surf = pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "sprites", "down.png")), (30, 30)).convert_alpha()
    self.image = self.base_surf
    self.rect = self.image.get_rect()

class Restart(pygame.sprite.Sprite):
  def __init__(self, game_state):
    super().__init__()

    self.game_state: gameState.gameState = game_state
    self.base_surf = pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "sprites", "restart.png")), (60, 60)).convert_alpha()
    self.image = self.base_surf
    self.rect = self.image.get_rect()

class Discs(pygame.sprite.Sprite):
  def __init__(self, disc_no):
    super().__init__()

    self.disc_no = disc_no
    self.image = pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "sprites", "discs", f"disc_{disc_no}.png")), (280 - disc_no * 16, 80 - disc_no * 2)).convert_alpha()
    self.rect = self.image.get_rect() 

def makeDisc() -> list:
  discs_sprite_group = pygame.sprite.Group()
  disc_list = []
  for i in range(1,11):
    disc_list.append(Discs(i))
  for disc in disc_list:
    discs_sprite_group.add(disc)
  return disc_list

class Click(pygame.sprite.Sprite):
  def __init__(self, game_state):
    super().__init__()

    self.game_state: gameState.gameState = game_state
    self.base_surf = pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "sprites", "click.png")), (30, 30)).convert_alpha()
    self.image = self.base_surf
    self.rect = self.image.get_rect()

class Return(pygame.sprite.Sprite):
  def __init__(self, game_state):
    super().__init__()

    self.game_state: gameState.gameState = game_state
    self.return_surf = pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "sprites", "undo.png")), (50, 50)).convert_alpha()
    self.image = self.return_surf
    self.rect = self.image.get_rect()

class SpeedUp(pygame.sprite.Sprite):
  def __init__(self, game_state):
    super().__init__()

    self.game_state: gameState.gameState = game_state
    self.speed_up_surf = pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "sprites", "speed.png")), (50, 50)).convert_alpha()
    self.image = self.speed_up_surf
    self.rect = self.image.get_rect()

class SpeedDown(pygame.sprite.Sprite):
  def __init__(self, game_state):
    super().__init__()

    self.game_state: gameState.gameState = game_state
    self.speed_down_surf = pygame.transform.scale(pygame.image.load(os.path.join("..", "assets", "sprites", "speed.png")), (50, 50)).convert_alpha()
    self.speed_down_surf = pygame.transform.flip(self.speed_down_surf, False, True)
    self.image = self.speed_down_surf
    self.rect = self.image.get_rect()