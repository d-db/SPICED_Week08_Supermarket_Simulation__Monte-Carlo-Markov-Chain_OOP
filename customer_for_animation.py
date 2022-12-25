TILE_SIZE = 32

class CustomerForAnimation:

   def __init__(self, supermarket, avatar, row, col):
      """
      supermarket: A SuperMarketMap object
      avatar : a numpy array containing a 32x32 tile image
      row: the starting row
      col: the starting column
      """

      self.supermarket = supermarket
      self.avatar = avatar
      self.row = row
      self.col = col

   def draw(self, frame):
      x = self.col * TILE_SIZE
      y = self.row * TILE_SIZE
      frame[y:y+TILE_SIZE, x:x+TILE_SIZE] = self.avatar

   def move(self, direction):
      new_row = self.row
      new_col = self.col

      if direction == 'up':
         new_row -= 1

      if self.supermarket.contents[new_row][new_col] == '.':
         self.col = new_col
         self.row = new_row