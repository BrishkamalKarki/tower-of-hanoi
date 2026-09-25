import gameState
import copy
import sys

class Solver:

  def __init__(self, game_state):
    self.game_state: gameState.gameState = game_state
    sys.setrecursionlimit(100000)

  def startThinking(self):
    self.virtual_hanoi_board = copy.deepcopy(self.game_state.HANOI_BOARD)

    self.possible_move_way = []

    self.valid_moves = [()]
    self.curr_move = 0
    self.done_for = 0
    self.min_moves = float('inf')

    self.local_solved = False

    self.visited = []

    for disc in range(1, self.game_state.MAX_DISC):
      self.solve(0)
      print("the min move is : ", self.min_moves)
      # self.done_for += 1
      # print("the curr move is ", self.curr_move)
    self.game_state.SOLVED = True

  def solve(self, move) -> bool:
    if move >= self.min_moves:
      return False
    A = self.virtual_hanoi_board['A'][:]
    B = self.virtual_hanoi_board['B'][:]
    C = self.virtual_hanoi_board['C'][:]
    # print(A, B, C)
    local_hanoi_board = {'A': A, 'B': B, 'C': C}

    if not self.saveBoard(local_hanoi_board, move):
      return False


    # print("current board ",self.checkSolved(local_hanoi_board), local_hanoi_board)
    if self.checkGotOne(local_hanoi_board):
      # print("the move is ", move)
      self.min_moves = move
      return True

    valid_moves = self.checkValidMoves(local_hanoi_board)

    for valid_move in valid_moves:
      # print("the virtual hanoi board after the valid move is", self.virtual_hanoi_board[valid_move[0]], "for valid move ", valid_move, " at move ", move)
      self.virtual_hanoi_board[valid_move[1]].append(self.virtual_hanoi_board[valid_move[0]][-1])
      self.virtual_hanoi_board[valid_move[0]].pop()

      # print("\n\nrecurse finished")

      solved = self.solve(move+1)
      self.virtual_hanoi_board = {'A': A[:], 'B': B[:], 'C': C[:]} 
      
      # if solved: 
      #   return True 
    
    # return False

  def checkValidMoves(self, local_hanoi_board) -> dict[chr, chr]:
    valid_moves = []

    for src_stick, discs in local_hanoi_board.items():
      for des_stick, discs_ in local_hanoi_board.items():

        if src_stick == des_stick:
          continue

        if len(discs) == 0:
          continue

        if len(discs_) == 0:
          # print (src_stick, des_stick)
          valid_moves.append((src_stick, des_stick))
          continue

        if discs[-1] > discs_[-1]:
          valid_moves.append((src_stick, des_stick))

    # print(valid_moves)
    return valid_moves

  def checkGotOne(self, local_hanoi_board) -> bool:
    curr_disc = self.done_for + 1
    return local_hanoi_board['C'][:curr_disc] == list(range(1, curr_disc + 1))
  
  def checkSolved(self, local_hanoi_board) -> bool:
    return local_hanoi_board['C'] == list(range(1, self.game_state.DISC_NO + 1))

  def saveBoard(self, local_hanoi_board, move) -> bool:
    if (len(local_hanoi_board) == 0): 
      self.visited.append(local_hanoi_board)
      return True

    for state in self.visited:
      if state[0] == local_hanoi_board:
        if state[1] <= move:
          return False
        state[1] = move
        return True

    self.visited.append([local_hanoi_board, move])
    return True


    