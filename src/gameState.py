import tomllib

class gameState:

  def __init__(self):    
    with open("../config.toml", "rb") as file:
      config_file = tomllib.load(file)

      self.WIDTH = config_file["window"]["width"]
      self.HEIGHT = config_file["window"]["height"]
      self.ASPECT_RATIO = config_file["window"]["aspect_ratio"]
      self.FULLSCREEN = config_file["window"]["fullscreen"]
      self.RESIZABLE = config_file["window"]["resizable"]
      
      self.FPS = config_file["game"]["fps"]
      self.STARTING_DISC = config_file["game"]["starting_disc"]
      self.MAX_DISC = config_file["game"]["max_disc"]

    self.RUNNING = True
    self.DISC_NO = self.STARTING_DISC
    self.MIN_MOVES = -1
    self.NO_DISC_SOLVED = -1
    self.SOLVED = False
    self.GAME_STATE_CHANGED = False
    self.USER_SOLVING = False
    self.HANOI_BOARD = {'A': [i for i in range(1, self.DISC_NO+1)], 'B': [], 'C': []}
    self.DISC_NO_BEING_MOVED = -1
    self.DISC_MOVED_FROM = 'n'
    self.DISC_BEING_MOVED = False
    self.MOUSE_BTN_BEING_PRESSED = False

  def updateState(self):
    if (not self.USER_SOLVING):
      # self.HANOI_BOARD = {'A':[2, 4, 5], 'B':[1, 3, 6], 'C':[9, 8, 10]}
      self.HANOI_BOARD = {'A': [i for i in range(1, self.DISC_NO+1)], 'B': [], 'C': []}
      self.DISC_NO_BEING_MOVED = -1
      self.DISC_MOVED_FROM = 'n'
      self.DISC_BEING_MOVED = False
      self.MOUSE_BTN_BEING_PRESSED = False
      self.RUNNING = True
      self.MIN_MOVES = -1
      self.NO_DISC_SOLVED = -1
      # self.SOLVED = False
      self.USER_SOLVING = False

