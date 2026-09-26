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
    self.MIN_MOVES = 0
    self.NO_DISC_SOLVED = -1
    self.SOLVED = False
    self.GAME_STATE_CHANGED = False
    self.USER_SOLVING = False
    self.HANOI_BOARD = {'A': [i for i in range(1, self.DISC_NO+1)], 'B': [], 'C': []}
    self.DISC_NO_BEING_MOVED = -1
    self.DISC_MOVED_FROM = 'n'
    self.DISC_BEING_MOVED = False
    self.MOUSE_BTN_BEING_PRESSED = False
    self.GAME_WON = False
    self.MOVE = 0
    self.MOVE_SEQ = []
    self.SOLVING_CONTENT = "UNSOLVED"
    self.BOT_SOLVING = False
    self.BOT_RESTART = True
    self.BOT_THINKED = False
    self.PREV_SRC = -1
    self.PREV_DES = -1
    self.SRC, self.DES = -1, -1
    self.PEG_ALIAS = {0:'A', 1:'B', 2:'C'}
    self.GAME_HISTOTY = []
    self.BOT_SOLVING_SPEED = 8 # px/frame

  def updateState(self):
    if (not self.USER_SOLVING and not self.BOT_SOLVING):
      self.HANOI_BOARD = {'A': [i for i in range(1, self.DISC_NO+1)], 'B': [], 'C': []}
      self.DISC_NO_BEING_MOVED = -1
      self.DISC_MOVED_FROM = 'n'
      self.DISC_BEING_MOVED = False
      self.MOUSE_BTN_BEING_PRESSED = False
      self.RUNNING = True
      self.NO_DISC_SOLVED = -1
      self.USER_SOLVING = False
      self.GAME_WON = False
      self.MOVE = 0
      self.SOLVING_CONTENT = "UNSOLVED"
      self.BOT_SOLVING = False
      self.PREV_SRC = -1
      self.PREV_DES = -1
      self.SRC, self.DES = -1, -1


