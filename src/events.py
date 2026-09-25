import pygame
import gameState, ToHScene

class EventSession:
  def __init__(self, game_state, game_scene):
    self.game_state: gameState.gameState = game_state
    self.game_scene: ToHScene.Scene = game_scene

  def checkEvent(self):
    self.game_state.MOUSE_BTN_BEING_PRESSED = pygame.mouse.get_pressed()[0]
    self.game_scene.click.rect.center = (pygame.mouse.get_pos())

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.game_state.RUNNING = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.game_scene.restart_btn.rect.collidepoint(pygame.mouse.get_pos()):
          self.game_state.USER_SOLVING = False
          self.game_state.GAME_STATE_CHANGED = True
          self.game_state.updateState()

        if (self.game_scene.up_btn.rect.collidepoint(pygame.mouse.get_pos())): 
          if (self.game_state.DISC_NO < self.game_state.MAX_DISC): 
            self.game_state.DISC_NO += 1 
            self.game_state.GAME_STATE_CHANGED = True 

        if (self.game_scene.down_btn.rect.collidepoint(pygame.mouse.get_pos())):
          if (self.game_state.DISC_NO > self.game_state.STARTING_DISC):
            self.game_state.DISC_NO -= 1
            self.game_state.GAME_STATE_CHANGED = True 

    if pygame.mouse.get_just_pressed():
      if not self.game_state.DISC_BEING_MOVED:
        for disc in self.game_scene.disc_obj_A:

          if (len(self.game_state.HANOI_BOARD['A']) > 0):
            if disc.disc_no == self.game_state.HANOI_BOARD['A'][-1]:
              if (disc.rect.collidepoint(pygame.mouse.get_pos()) and self.game_state.MOUSE_BTN_BEING_PRESSED):
                self.game_state.DISC_NO_BEING_MOVED = disc.disc_no
                self.game_state.DISC_BEING_MOVED = True
                self.game_state.DISC_MOVED_FROM = 'A'
              else:
                self.game_state.DISC_NO_BEING_MOVED = -1

      if not self.game_state.DISC_BEING_MOVED:
        for disc in self.game_scene.disc_obj_B:

          if (len(self.game_state.HANOI_BOARD['B']) > 0):
            if disc.disc_no == self.game_state.HANOI_BOARD['B'][-1]:
              if (disc.rect.collidepoint(pygame.mouse.get_pos()) and self.game_state.MOUSE_BTN_BEING_PRESSED):
                self.game_state.DISC_NO_BEING_MOVED = disc.disc_no
                self.game_state.DISC_BEING_MOVED = True
                self.game_state.DISC_MOVED_FROM = 'B'
              else:
                self.game_state.DISC_NO_BEING_MOVED = -1
                
      if not self.game_state.DISC_BEING_MOVED:
        for disc in self.game_scene.disc_obj_C:

          if (len(self.game_state.HANOI_BOARD['C']) > 0):
            if disc.disc_no == self.game_state.HANOI_BOARD['C'][-1]:
              if (disc.rect.collidepoint(pygame.mouse.get_pos()) and self.game_state.MOUSE_BTN_BEING_PRESSED):
                self.game_state.DISC_NO_BEING_MOVED = disc.disc_no
                self.game_state.DISC_BEING_MOVED = True
                self.game_state.DISC_MOVED_FROM = 'C'
              else:
                self.game_state.DISC_NO_BEING_MOVED = -1

    if pygame.mouse.get_just_released()[0]:
      if self.game_state.DISC_BEING_MOVED:
        right = self.game_scene.disc_list[self.game_state.DISC_NO_BEING_MOVED - 1].rect.right
        left = self.game_scene.disc_list[self.game_state.DISC_NO_BEING_MOVED - 1].rect.left
        up = self.game_scene.disc_list[self.game_state.DISC_NO_BEING_MOVED - 1].rect.top
        down = self.game_scene.disc_list[self.game_state.DISC_NO_BEING_MOVED - 1].rect.bottom

        if right > self.game_scene.disc_range_hor['left_A'] and left < self.game_scene.disc_range_hor['right_A'] and up < self.game_scene.disc_range_ver['down'] and down > self.game_scene.disc_range_ver['up']:
          if (self.game_state.DISC_MOVED_FROM != 'A'):
            self.game_state.HANOI_BOARD['A'].append(self.game_state.DISC_NO_BEING_MOVED)
            self.game_state.HANOI_BOARD[f'{self.game_state.DISC_MOVED_FROM}'].pop()
        elif right > self.game_scene.disc_range_hor['left_B'] and left < self.game_scene.disc_range_hor['right_B'] and up < self.game_scene.disc_range_ver['down'] and down > self.game_scene.disc_range_ver['up']:
          if (self.game_state.DISC_MOVED_FROM != 'B'):
            self.game_state.HANOI_BOARD['B'].append(self.game_state.DISC_NO_BEING_MOVED)
            self.game_state.HANOI_BOARD[f'{self.game_state.DISC_MOVED_FROM}'].pop()
        elif right > self.game_scene.disc_range_hor['left_C'] and left < self.game_scene.disc_range_hor['right_C'] and up < self.game_scene.disc_range_ver['down'] and down > self.game_scene.disc_range_ver['up']:
          if (self.game_state.DISC_MOVED_FROM != 'C'):
            self.game_state.HANOI_BOARD['C'].append(self.game_state.DISC_NO_BEING_MOVED)
            self.game_state.HANOI_BOARD[f'{self.game_state.DISC_MOVED_FROM}'].pop()

        self.game_state.DISC_BEING_MOVED = False
        self.game_state.DISC_NO_BEING_MOVED= -1