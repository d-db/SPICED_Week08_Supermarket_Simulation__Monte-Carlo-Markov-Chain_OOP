import pickle
import random
import time
from datetime import datetime
from cv2 import cv2
import numpy as np

from customer_class import Customer, test_probability_matrix
from supermarket_class import Supermarket
from customer_for_animation import CustomerForAnimation
from tiles_skeleton import SupermarketMap, MARKET, TILE_SIZE

# Load necessary data
with open('./data/full_df.bin', 'rb') as f:
    df = pickle.load(f)

with open('./data/probabilities.bin', 'rb') as f:
    probabilities = pickle.load(f)

with open('./data/initial_state.bin', 'rb') as f:
    initial_state_probabilities = pickle.load(f)

# Instantiating the supermarket
lidl = Supermarket(initial_state_probabilities, probabilities)

# Preparation for the supermarket animation
background = np.zeros((500, 700, 3), np.uint8)
tiles = cv2.imread("tiles.png")
market = SupermarketMap(MARKET, tiles)
avatar = market.extract_tile(7,0)

# Get the current time in order to asses whether the market is open
current_time = datetime.now().strftime("%H")

# Start while-loop if the current time is within the opening hours
while 6 < int(current_time) < 23:
    # If there are customers, push them to the next state
    lidl.remove_exitsting_customers()
    lidl.next_minute()
    lidl.add_new_customers()
    lidl.print_customers()
    print(lidl)

    # Create the frame for the animation
    frame = background.copy()
    # Draw the supermarket
    market.draw(frame)

    rc_list = []

    # Draw the customers to the animation
    for customer in lidl.customers:
        while True:
            row_and_columns = market.get_row_and_column(customer.state)
            if row_and_columns not in rc_list:
                cust = CustomerForAnimation(market, avatar, row_and_columns[0], row_and_columns[1])
                cust.draw(frame)
                rc_list.append(row_and_columns)
                break

    # https://www.ascii-code.com/
    key = cv2.waitKey(2)

    if key == 113: # 'q' key
        break

    cv2.imshow("frame", frame)
    # Wait for a a couple of seconds and then simulate the next minute
    time.sleep(1)

cv2.destroyAllWindows()