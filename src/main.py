import events, gameState, engine.solver as solver, gameSprites, ToHScene
import pygame
import threading

class Game: 

  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()

    # loading the game state
    self.game_state = gameState.gameState() 
    self.screen = pygame.display.set_mode((self.game_state.HEIGHT * self.game_state.ASPECT_RATIO, self.game_state.HEIGHT), pygame.RESIZABLE | pygame.SCALED) 
    self.game_scene = ToHScene.Scene(self.game_state, self.screen) 
    self.game_event = events.EventSession(self.game_state, self.game_scene) 
    self.solver = solver.Solver(self.game_state) 

    self.solver_thread = threading.Thread(target=self.solver.startThinking)

    pygame.mouse.set_visible(False)
    self.gameLoop()

  def gameLoop(self):
    while (self.game_state.RUNNING):

      # checking for the event
      self.game_event.checkEvent()
        
      if self.game_state.GAME_STATE_CHANGED:
        self.game_scene.updateContent()

      if (not self.game_state.SOLVED): 
        if not self.solver_thread.is_alive():
          self.solver_thread.start()
        self.game_state.SOLVED = True

      if (self.game_state.GAME_STATE_CHANGED):
        self.game_state.updateState()
        self.game_state.GAME_STATE_CHANGED = False

      self.screen.fill("#b3b3b3")
      self.game_scene.makeScene()

      pygame.display.flip()

      self.clock.tick(self.game_state.FPS)

    pygame.quit()


if __name__ == "__main__":
  toh = Game()
