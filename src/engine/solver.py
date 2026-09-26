import gameState
import copy
import sys
from collections import deque

class Solver:

  def __init__(self, game_state):
    self.game_state: gameState.gameState = game_state
    # sys.setrecursionlimit(100000)

  def startThinking(self):
    virtual_hanoi_board = (tuple(i for i in range(1, self.game_state.DISC_NO+1)), (), ())
    solve_hanoi_board = ((), (), tuple(i for i in range(1, self.game_state.DISC_NO+1)))
    self.curr_move = 0

    self.local_solved = False
    self.move_sequence = self.bfs(virtual_hanoi_board, solve_hanoi_board)
    self.game_state.MIN_MOVES = len(self.move_sequence)
    self.game_state.SOLVED = True
    self.game_state.MOVE_SEQ.clear()
    self.game_state.MOVE_SEQ = self.move_sequence[:]
    self.game_state.GAME_STATE_CHANGED = True
    self.game_state.BOT_THINKED = True

  def checkValidMoves(self, local_hanoi_board) -> tuple:
    valid_moves = ()

    src = 0
    des = 0
    for peg in local_hanoi_board:
      if peg: 
        last_of_peg = peg[-1]

        for peg in local_hanoi_board:
          if peg:
            if peg[-1] < last_of_peg:
              valid_moves += ((src, des),)
          else:
            valid_moves += ((src, des),)
          des += 1
      src += 1
      des = 0

    return valid_moves

  def applyMove(self, local_hanoi_board, src, des):
    local_hanoi_board = list(local_hanoi_board)
    local_hanoi_board[des] += (local_hanoi_board[src][-1],)
    local_hanoi_board[src] = local_hanoi_board[src][:-1]
    return tuple(local_hanoi_board)

  def bfs(self, local_haoi_board, solved_hanoi_board): # breadth first search
    board_queue = deque([(local_haoi_board, [])]) 
    visited = {local_haoi_board}

    while board_queue:  
      current_state, move_seq = board_queue.popleft()

      if current_state == solved_hanoi_board:
        return move_seq

      possible_moves = self.checkValidMoves(current_state)
      for pm in possible_moves:
        new_state = self.applyMove(current_state[:], pm[0], pm[1])

        if new_state not in visited:
          new_move_seq = move_seq + [pm]
          visited.add(new_state)
          board_queue.append((new_state, new_move_seq))

    return None
  