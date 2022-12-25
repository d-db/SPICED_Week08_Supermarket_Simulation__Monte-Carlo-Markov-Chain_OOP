import time
import random

import numpy as np
from cv2 import cv2

from customer_for_animation import CustomerForAnimation

TILE_SIZE = 32

MARKET = """
##################
##..............##
#O..ER..IF..TB..S#
#O..ER..IF..TB..S#
#O..ER..IF..TB..S#
#O..ER..IF..TB..S#
#O..ER..IF..TB..S#
##...............#
##..C#..C#..C#...#
##..##..##..##...#
##...............#
##############GG##
""".strip()


class SupermarketMap:
    """Visualizes the supermarket background"""

    def __init__(self, layout, tiles):
        """
        layout : a string with each character representing a tile
        tiles   : a numpy array containing all the tile images
        """
        self.tiles = tiles
        # split the layout string into a two dimensional matrix
        self.contents = [list(row) for row in layout.split("\n")]
        self.ncols = len(self.contents[0])
        self.nrows = len(self.contents)
        self.image = np.zeros(
            (self.nrows*TILE_SIZE, self.ncols*TILE_SIZE, 3), dtype=np.uint8
        )
        self.prepare_map()

    def extract_tile(self, row, col):
        """extract a tile array from the tiles image"""
        y = row*TILE_SIZE
        x = col*TILE_SIZE
        return self.tiles[y:y+TILE_SIZE, x:x+TILE_SIZE]

    def get_tile(self, char):
        """returns the array for a given tile character"""
        if char == "#":
            return self.extract_tile(0, 0)
        elif char == "G":
            return self.extract_tile(7, 3)
        elif char == "B":
            return self.extract_tile(0, 4)
        elif char == "C":
            return self.extract_tile(2, 8)
        elif char == "S":
            return self.extract_tile(1, 5)
        elif char == "T":
            return self.extract_tile(6, 3)
        elif char == "F":
            return self.extract_tile(1, 3)
        elif char == "I":
            return self.extract_tile(1, 6)
        elif char == "R":
            return self.extract_tile(2, 6)
        elif char == "E":
            return self.extract_tile(6, 13)
        elif char == "O":
            return self.extract_tile(3, 13)
        else:
            return self.extract_tile(1, 2)

    def prepare_map(self):
        """prepares the entire image as a big numpy array"""
        for row, line in enumerate(self.contents):
            for col, char in enumerate(line):
                bm = self.get_tile(char)
                y = row*TILE_SIZE
                x = col*TILE_SIZE
                self.image[y:y+TILE_SIZE, x:x+TILE_SIZE] = bm

    def draw(self, frame):
        """
        draws the image into a frame
        """
        frame[0:self.image.shape[0], 0:self.image.shape[1]] = self.image

    def write_image(self, filename):
        """writes the image into a file"""
        cv2.imwrite(filename, self.image)

    def get_row_and_column(self, state):
        """
        Returns row and column values for drawing the customers
        :param state: Current state of the customer
        :return: List with values for row and column which are necessary to draw the client
        """
        row_column = []

        dict_areas = {
            "drinks": [[1, 2, 3, 4, 5, 6, 7], [2, 3]],
            "dairy": [[1, 2, 3, 4, 5, 6, 7], [6, 7]],
            "spices": [[1, 2, 3, 4, 5, 6, 7], [10, 11]],
            "fruit": [[1, 2, 3, 4, 5, 6, 7], [14, 15]],
            "checkout": [[7], [4, 5, 8, 9, 12, 13]]
        }

        row = random.choice(dict_areas[state][0])
        row_column.append(row)
        column = random.choice(dict_areas[state][1])
        row_column.append(column)

        return row_column


if __name__ == "__main__":

    background = np.zeros((500, 700, 3), np.uint8)
    tiles = cv2.imread("tiles.png")

    market = SupermarketMap(MARKET, tiles)
    avatar = market.extract_tile(5,5)

    cust = CustomerForAnimation(market, avatar, 10, 15)

    while True:
        frame = background.copy()
        market.draw(frame)
        cust.draw(frame)
        cust.move("up")

        # https://www.ascii-code.com/
        key = cv2.waitKey(1)

        if key == 113: # 'q' key
            break

        cv2.imshow("frame", frame)
        time.sleep(1)

    cv2.destroyAllWindows()

    market.write_image("supermarket.png")
