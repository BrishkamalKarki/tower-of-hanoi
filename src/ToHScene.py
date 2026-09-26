import pygame
import gameSprites, gameState

class Scene():
  def __init__(self, game_state, game_screen):
    self.game_state: gameState.gameState = game_state
    self.game_screen: gameState.gameState = game_screen

    self.game_sound = gameSprites.Sounds()

    self.base = gameSprites.Base(self.game_state)
    self.TowerOfHanoi = gameSprites.TowerOfHanoi(self.game_state)
    self.up_btn = gameSprites.IncBtn(self.game_state)
    self.down_btn = gameSprites.DecBtn(self.game_state)
    self.restart_btn = gameSprites.Restart(self.game_state)
    self.click = gameSprites.Click(self.game_state)
    self.disc_list = gameSprites.makeDisc()
    self.return_btn = gameSprites.Return(self.game_state)
    self.bot_speed_up = gameSprites.SpeedUp(self.game_state)
    self.bot_speed_down = gameSprites.SpeedDown(self.game_state)

    self.font = gameSprites.Font()
    self.disc_txt = self.font.reg_font.render(f"DISC: {self.game_state.DISC_NO}", True, (255, 255, 255))
    self.min_move_txt = self.font.reg_font.render(f"MIN MOVES: {self.game_state.MIN_MOVES}", True, (255, 255, 255))
    self.move_txt = self.font.reg_font.render(f"MOVE: {self.game_state.MOVE}", True, (255, 255, 255))
    self.is_solved_txt = self.font.reg_font.render(f"{self.game_state.SOLVING_CONTENT}", True, (255, 255, 255))
    self.solve_txt = self.font.reg_font.render("SOLVE", True, (255, 255, 255))

    self.disc_factor = [0, 0.028, 0.0, 0.08, 0.0, 1.05, 0.3, 0.35, 0.4, 3]
    self.disc_range_ver = {'up': 200, 'down': 620}
    self.disc_range_hor = {'left_A': 290, 'right_A': 370, 'left_B': 610, 'right_B': 690, 'left_C': 940, 'right_C': 1010}

    self.disc_rect = pygame.Rect(430, 16, 160, 60)
    self.min_move_rect = pygame.Rect(760, 16, 290, 60)
    self.move_rect = pygame.Rect(70, 100, 260, 60)
    self.is_solved_rect = pygame.Rect(360, 100, 200, 60)
    self.solve_rect = pygame.Rect(590, 100, 160, 60)
    self.x_diff = {'A': 330, 'B': 655, 'C': 974}
    self.y_diff = (200, 600)

    self.disc_obj_A = []
    self.disc_obj_B = []
    self.disc_obj_C = []

  def makeScene(self):
    self.base.rect.center = (self.game_state.WIDTH/2, self.game_state.HEIGHT/1.6)
    self.game_screen.blit(self.base.image, self.base.rect)

    self.TowerOfHanoi.rect.topleft = (0,-40)
    self.game_screen.blit(self.TowerOfHanoi.image, self.TowerOfHanoi.rect)

    pygame.draw.rect(self.game_screen, "#1e1e1e", self.disc_rect, 0, 9)
    pygame.draw.rect(self.game_screen, "#1e1e1e", self.min_move_rect, 0, 9)
    pygame.draw.rect(self.game_screen, "#1e1e1e", self.move_rect, 0, 9)
    pygame.draw.rect(self.game_screen, "#1e1e1e", self.is_solved_rect, 0, 9)
    pygame.draw.rect(self.game_screen, "#1e1e1e", self.solve_rect, 0, 9)

    self.up_btn.rect.topleft = (630, 10)
    self.game_screen.blit(self.up_btn.image, self.up_btn.rect)
    self.down_btn.rect.topleft = (630, 50)
    self.game_screen.blit(self.down_btn.image, self.down_btn.rect)

    self.restart_btn.rect.topleft = (670, 14)
    self.game_screen.blit(self.restart_btn.image, self.restart_btn.rect)
    self.return_btn.rect.topleft = (780, 105)
    self.game_screen.blit(self.return_btn.image, self.return_btn.rect)
    if self.game_state.BOT_SOLVING and not self.game_state.GAME_WON:
      self.bot_speed_up.rect.topleft = (70, 200)
      self.game_screen.blit(self.bot_speed_up.image, self.bot_speed_up.rect)
      self.bot_speed_down.rect.topleft = (70, 270)
      self.game_screen.blit(self.bot_speed_down.image, self.bot_speed_down.rect)
    
    self.game_screen.blit(self.disc_txt, (self.disc_rect.centerx - self.disc_txt.width/2, 28))
    self.game_screen.blit(self.min_move_txt, (self.min_move_rect.centerx - self.min_move_txt.width/2, 28))
    self.game_screen.blit(self.move_txt, (self.move_rect.centerx - self.move_txt.width/2, 112))
    self.game_screen.blit(self.is_solved_txt, (self.is_solved_rect.centerx - self.is_solved_txt.width/2, 112))
    self.game_screen.blit(self.solve_txt, (self.solve_rect.centerx - self.solve_txt.width/2, 112))

    self.disc_in_A = self.game_state.HANOI_BOARD['A'][:]
    self.disc_in_B = self.game_state.HANOI_BOARD['B'][:]
    self.disc_in_C = self.game_state.HANOI_BOARD['C'][:]
    self.disc_obj_A.clear()
    self.disc_obj_B.clear()
    self.disc_obj_C.clear()
    for disc_no in self.disc_in_A:
      for disc in self.disc_list:
        if disc.disc_no == disc_no:
          self.disc_obj_A.append(disc)
    for disc_no in self.disc_in_B:
      for disc in self.disc_list:
        if disc.disc_no == disc_no:
          self.disc_obj_B.append(disc)
    for disc_no in self.disc_in_C:
      for disc in self.disc_list:
        if disc.disc_no == disc_no:
          self.disc_obj_C.append(disc)

    if (self.game_state.BOT_SOLVING and not self.game_state.GAME_WON):
      
        for disc in self.disc_list:
          if disc.disc_no == self.game_state.DISC_NO_BEING_MOVED:
            if self.game_state.SRC < self.game_state.DES:
              disc.rect.centerx += self.game_state.BOT_SOLVING_SPEED
            else:
              disc.rect.centerx -= self.game_state.BOT_SOLVING_SPEED
            disc.rect.centery -= self.game_state.BOT_SOLVING_SPEED/8
        self.game_state.PREV_DES = self.game_state.DES
        self.game_state.PREV_SRC = self.game_state.SRC
    
          
    for i, disc in enumerate(self.disc_obj_A):
      i += 1
      if (disc.disc_no == self.game_state.DISC_NO_BEING_MOVED):
        if (not self.game_state.BOT_SOLVING):
          disc.rect.center = pygame.mouse.get_pos()
      else:
        disc.rect.center = (325, 627 - i * 30)
      self.game_screen.blit(disc.image, disc.rect)

    for i, disc in enumerate(self.disc_obj_B):
      i += 1
      if (disc.disc_no == self.game_state.DISC_NO_BEING_MOVED):
        if (not self.game_state.BOT_SOLVING):
          disc.rect.center = pygame.mouse.get_pos()
      else:
        disc.rect.center = (650, 627 - i * 30) 
      self.game_screen.blit(disc.image, disc.rect)  

    for i, disc in enumerate(self.disc_obj_C):
      i += 1
      # if i in self.disc_in_C:
      if (disc.disc_no == self.game_state.DISC_NO_BEING_MOVED):
        if (not self.game_state.BOT_SOLVING):
          disc.rect.center = pygame.mouse.get_pos()
      else:
        disc.rect.center = (973, 627 - i * 30)
      self.game_screen.blit(disc.image, disc.rect)
        
    # making the copy of the stick layer
    disc_no_A = len(self.game_state.HANOI_BOARD['A'])
    disc_no_B = len(self.game_state.HANOI_BOARD['B'])
    disc_no_C = len(self.game_state.HANOI_BOARD['C'])
    if disc_no_A > 0:
      for disc in self.disc_obj_A:
        if disc.disc_no == self.game_state.DISC_NO_BEING_MOVED:
          if (self.game_state.DISC_BEING_MOVED and disc_no_A > 1):
            stickA_rect = stickA_rect = pygame.Rect(506, 0, 27, 434 - (disc_no_A - 2) * 30 - self.disc_factor[self.disc_obj_A[-2].disc_no - 1])
            self.game_screen.blit(self.base.image, (313, 162), stickA_rect) 
        else:
          stickA_rect = pygame.Rect(506, 0, 27, 434 - (disc_no_A - 1) * 30 - self.disc_factor[self.disc_obj_A[-1].disc_no - 1]) 
          self.game_screen.blit(self.base.image, (313, 162), stickA_rect) 

    if disc_no_B > 0:
      for disc in self.disc_obj_B:
        if disc.disc_no == self.game_state.DISC_NO_BEING_MOVED:
          if (self.game_state.DISC_BEING_MOVED and disc_no_B > 1):
            stickB_rect = stickB_rect = pygame.Rect(830, 0, 27, 434 - (disc_no_B - 2) * 30 - self.disc_factor[self.disc_obj_B[-2].disc_no - 1])
            self.game_screen.blit(self.base.image, (636, 162), stickB_rect) 
        else:
          stickB_rect = pygame.Rect(830, 0, 27, 434 - (disc_no_B - 1) * 30 - self.disc_factor[self.disc_obj_B[-1].disc_no - 1]) 
          self.game_screen.blit(self.base.image, (636, 162), stickB_rect) 

    if disc_no_C > 0:
      for disc in self.disc_obj_C:
        if disc.disc_no == self.game_state.DISC_NO_BEING_MOVED:
          if (self.game_state.DISC_BEING_MOVED and disc_no_C > 1):
            stickC_rect = pygame.Rect(830, 0, 27, 434 - (disc_no_C - 2) * 30 - self.disc_factor[self.disc_obj_C[-2].disc_no - 1])
            self.game_screen.blit(self.base.image, (960, 162), stickC_rect) 
        else:
          stickC_rect = pygame.Rect(830, 0, 27, 434 - (disc_no_C - 1) * 30 - self.disc_factor[self.disc_obj_C[-1].disc_no - 1]) 
          self.game_screen.blit(self.base.image, (960, 162), stickC_rect) 

    self.game_screen.blit(self.click.image, self.click.rect) 

  def updateContent(self):
    self.disc_txt = self.font.reg_font.render(f"DISC: {self.game_state.DISC_NO}", True, (255, 255, 255))
    self.min_move_txt = self.font.reg_font.render(f"MIN MOVES: {self.game_state.MIN_MOVES}", True, (255, 255, 255))
    self.move_txt = self.font.reg_font.render(f"MOVE: {self.game_state.MOVE}", True, (255, 255, 255))
    self.is_solved_txt = self.font.reg_font.render(f"{self.game_state.SOLVING_CONTENT}", True, (255, 255, 255))

    
