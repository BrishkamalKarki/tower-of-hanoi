import pygame
import gameState, ToHScene

class EventSession:
  def __init__(self, game_state, game_scene):
    self.game_state: gameState.gameState = game_state
    self.game_scene: ToHScene.Scene = game_scene

  def checkEvent(self):
    if (self.game_state.HANOI_BOARD['C'] == [i for i in range(1, self.game_state.DISC_NO+1)]):
      self.game_state.GAME_WON = True
      self.game_state.GAME_STATE_CHANGED = True
      self.game_state.SOLVING_CONTENT = "SOLVED"
      self.game_state.DISC_MOVED_FROM = False
      self.game_state.SOLVING_CONTENT = "BOT SOLVED"
      self.game_state.DISC_NO_BEING_MOVED = -1
      self.game_state.GAME_HISTOTY.clear()

    if self.game_state.BOT_SOLVING and not self.game_state.GAME_WON:
      self.game_state.SRC = self.game_state.MOVE_SEQ[self.game_state.MOVE][0]
      self.game_state.DES = self.game_state.MOVE_SEQ[self.game_state.MOVE][1]
      self.game_state.DISC_BEING_MOVED = True
      self.game_state.DISC_MOVED_FROM = self.game_state.PEG_ALIAS[self.game_state.SRC]
      self.to_go = self.game_state.PEG_ALIAS[self.game_state.DES]
      self.game_state.DISC_NO_BEING_MOVED = self.game_state.HANOI_BOARD[self.game_state.PEG_ALIAS[self.game_state.SRC]][-1]


    self.game_state.MOUSE_BTN_BEING_PRESSED = pygame.mouse.get_pressed()[0]
    self.game_scene.click.rect.center = (pygame.mouse.get_pos())

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.game_state.RUNNING = False

      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.game_scene.restart_btn.rect.collidepoint(pygame.mouse.get_pos()):
          self.game_state.USER_SOLVING = False
          self.game_state.GAME_STATE_CHANGED = True
          self.game_state.BOT_SOLVING = False
          self.game_state.updateState()
          self.game_scene.game_sound.btn_sound.play()

        if (self.game_scene.bot_speed_up.rect.collidepoint(pygame.mouse.get_pos()) and self.game_state.BOT_SOLVING and not self.game_state.GAME_WON): 
          self.game_state.BOT_SOLVING_SPEED += 2
          self.game_scene.game_sound.btn_sound.play()

        if (self.game_scene.bot_speed_down.rect.collidepoint(pygame.mouse.get_pos()) and self.game_state.BOT_SOLVING and not self.game_state.GAME_WON): 
          if self.game_state.BOT_SOLVING_SPEED > 1:
            self.game_state.BOT_SOLVING_SPEED -= 1
            self.game_scene.game_sound.btn_sound.play()

        if (self.game_scene.return_btn.rect.collidepoint(pygame.mouse.get_pos()) and self.game_state.USER_SOLVING and not self.game_state.BOT_SOLVING and not self.game_state.GAME_WON): 
          history = self.game_state.GAME_HISTOTY
          if len(history) > 1:
            history.pop()
            self.game_state.HANOI_BOARD = {'A': history[-1]['A'][:], 'B': history[-1]['B'][:], 'C': history[-1]['C'][:]}
          elif len(history) == 1:
            history.pop()
            self.game_state.HANOI_BOARD = {'A': [i for i in range(1, self.game_state.DISC_NO+1)], 'B': [], 'C': []}
          self.game_scene.game_sound.btn_sound.play()

        if (self.game_scene.up_btn.rect.collidepoint(pygame.mouse.get_pos()) and not self.game_state.USER_SOLVING and not self.game_state.BOT_SOLVING and not self.game_state.GAME_WON): 
          if (self.game_state.DISC_NO < self.game_state.MAX_DISC): 
            self.game_state.DISC_NO += 1 
            self.game_state.GAME_STATE_CHANGED = True 
            self.game_state.BOT_RESTART = True
            self.game_scene.game_sound.btn_sound.play()

        if (self.game_scene.down_btn.rect.collidepoint(pygame.mouse.get_pos()) and not self.game_state.USER_SOLVING and not self.game_state.BOT_SOLVING and not self.game_state.GAME_WON):
          if (self.game_state.DISC_NO > self.game_state.STARTING_DISC):
            self.game_state.DISC_NO -= 1
            self.game_state.GAME_STATE_CHANGED = True 
            self.game_state.BOT_RESTART = True
            self.game_scene.game_sound.btn_sound.play()

        if (self.game_scene.solve_rect.collidepoint(pygame.mouse.get_pos()) and not self.game_state.USER_SOLVING and not self.game_state.BOT_SOLVING and not self.game_state.GAME_WON):
          self.game_state.BOT_SOLVING = True
          self.game_state.SOLVING_CONTENT = "BOT SOLVING"
          self.game_state.GAME_STATE_CHANGED = True
          self.game_scene.game_sound.btn_sound.play()

    if pygame.mouse.get_just_pressed():
      if not self.game_state.GAME_WON and not self.game_state.BOT_SOLVING:
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

    if self.game_state.USER_SOLVING:
      board = self.game_state.HANOI_BOARD

      board_snap = {'A': board['A'][:], 'B': board['B'][:], 'C': board['C'][:]}
      if not self.game_state.GAME_HISTOTY:
        self.game_state.GAME_HISTOTY.append(board_snap)
      elif (self.game_state.GAME_HISTOTY[-1] != board_snap):
        self.game_state.GAME_HISTOTY.append(board_snap)

    if pygame.mouse.get_just_released()[0]:
      if not self.game_state.GAME_WON and not self.game_state.BOT_SOLVING:
        self.upadateBoard()
    if self.game_state.BOT_SOLVING:
      self.upadateBoard()

  def upadateBoard(self):
    if self.game_state.DISC_BEING_MOVED:
      right = self.game_scene.disc_list[self.game_state.DISC_NO_BEING_MOVED - 1].rect.right
      left = self.game_scene.disc_list[self.game_state.DISC_NO_BEING_MOVED - 1].rect.left
      up = self.game_scene.disc_list[self.game_state.DISC_NO_BEING_MOVED - 1].rect.top
      down = self.game_scene.disc_list[self.game_state.DISC_NO_BEING_MOVED - 1].rect.bottom

      if right > self.game_scene.disc_range_hor['left_A'] and left < self.game_scene.disc_range_hor['right_A'] and up < self.game_scene.disc_range_ver['down'] and down > self.game_scene.disc_range_ver['up']:
        if (self.game_state.DISC_MOVED_FROM != 'A'):
          if (self.game_state.BOT_SOLVING and self.to_go == 'A') or not self.game_state.BOT_SOLVING:
            if len(self.game_state.HANOI_BOARD['A']) == 0:
              self.game_state.HANOI_BOARD['A'].append(self.game_state.DISC_NO_BEING_MOVED)
              self.game_state.HANOI_BOARD[f'{self.game_state.DISC_MOVED_FROM}'].pop()
              self.game_state.MOVE += 1
              self.game_scene.game_sound.disc_sound.play()
            elif self.game_state.HANOI_BOARD['A'][-1] < self.game_state.DISC_NO_BEING_MOVED:
              self.game_state.HANOI_BOARD['A'].append(self.game_state.DISC_NO_BEING_MOVED)
              self.game_state.HANOI_BOARD[f'{self.game_state.DISC_MOVED_FROM}'].pop()
              self.game_state.MOVE += 1
              self.game_scene.game_sound.disc_sound.play()
      elif right > self.game_scene.disc_range_hor['left_B'] and left < self.game_scene.disc_range_hor['right_B'] and up < self.game_scene.disc_range_ver['down'] and down > self.game_scene.disc_range_ver['up']:
        if (self.game_state.DISC_MOVED_FROM != 'B'):
          if (self.game_state.BOT_SOLVING and self.to_go == 'B') or not self.game_state.BOT_SOLVING:
            if len(self.game_state.HANOI_BOARD['B']) == 0:
              self.game_state.HANOI_BOARD['B'].append(self.game_state.DISC_NO_BEING_MOVED)
              self.game_state.HANOI_BOARD[f'{self.game_state.DISC_MOVED_FROM}'].pop()
              self.game_state.MOVE += 1
              self.game_scene.game_sound.disc_sound.play()
            elif self.game_state.HANOI_BOARD['B'][-1] < self.game_state.DISC_NO_BEING_MOVED:
              self.game_state.HANOI_BOARD['B'].append(self.game_state.DISC_NO_BEING_MOVED)
              self.game_state.HANOI_BOARD[f'{self.game_state.DISC_MOVED_FROM}'].pop()
              self.game_state.MOVE += 1
              self.game_scene.game_sound.disc_sound.play()
      elif right > self.game_scene.disc_range_hor['left_C'] and left < self.game_scene.disc_range_hor['right_C'] and up < self.game_scene.disc_range_ver['down'] and down > self.game_scene.disc_range_ver['up']:
        if (self.game_state.DISC_MOVED_FROM != 'C'):
          if (self.game_state.BOT_SOLVING and self.to_go == 'C') or not self.game_state.BOT_SOLVING:
            if len(self.game_state.HANOI_BOARD['C']) == 0:
              self.game_state.HANOI_BOARD['C'].append(self.game_state.DISC_NO_BEING_MOVED)
              self.game_state.HANOI_BOARD[f'{self.game_state.DISC_MOVED_FROM}'].pop()
              self.game_state.MOVE += 1
              self.game_scene.game_sound.disc_sound.play()
            elif self.game_state.HANOI_BOARD['C'][-1] < self.game_state.DISC_NO_BEING_MOVED:
              self.game_state.HANOI_BOARD['C'].append(self.game_state.DISC_NO_BEING_MOVED)
              self.game_state.HANOI_BOARD[f'{self.game_state.DISC_MOVED_FROM}'].pop()
              self.game_state.MOVE += 1
              self.game_scene.game_sound.disc_sound.play()

      if not self.game_state.GAME_WON and not self.game_state.BOT_SOLVING:
        self.game_state.DISC_NO_BEING_MOVED= -1
        self.game_state.DISC_BEING_MOVED = False
        if self.game_state.MOVE >= 1:
          self.game_state.USER_SOLVING = True
          self.game_state.SOLVING_CONTENT = "SOLVING"
      self.game_state.GAME_STATE_CHANGED = True

