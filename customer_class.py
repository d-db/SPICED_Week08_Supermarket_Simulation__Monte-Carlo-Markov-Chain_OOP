import sys
import pandas as pd

import random

class Customer:
    """
    a single customer that moves through the supermarket
    in a MCMC simulation
    """
    def __init__(self, name, initial_state_probs, transition_probs, budget=100):
        self.name = name
        self.state = self._initial_state(initial_state_probs)
        self.budget = budget
        self.transition_probs = transition_probs

    def __repr__(self):
        return f'<Customer {self.name} in {self.state}>'

    def _initial_state(self, initial_state_probs):
        areas = [i for i in initial_state_probs.keys()]
        probs = [i for i in initial_state_probs.values()]

        return random.choices(areas, weights=probs, k=1)[0]

    def next_state(self):
        '''
        Propagates the customer to the next state.
        Returns nothing.
        '''
        if self.state != "checkout":
            # Slice the column with the probabilities for the next area
            column = self.transition_probs.loc[:,self.state]
            # Remove the row with probability 0
            column = column[column.iloc[:] > 0]

            list_state = list()
            list_prop = list()

            # Extract the name of the area and the probability and add the two values to different lists
            for i, j in zip(column.index, column.iloc[:]):
                list_state.append(i)
                list_prop.append(round(j, 2))

            # Pass the list to random.choices and generate a new state
            self.state = random.choices(list_state, weights=list_prop, k=1)[0]

    def is_active(self):
        """Returns True if the customer has not reached the checkout yet."""
        return self.state != "checkout"


def test_probability_matrix(no_of_customers, probability_matrix):

    sum_of_areas_visited = 0

    for _ in range(no_of_customers):

        list_states = ["spices", "fruit", "drinks", "dairy"]
        cust = Customer("Mrs. X", random.choice(list_states), probability_matrix)

        while cust.is_active():
            cust.next_state()
            sum_of_areas_visited += 1

    print(f"With this probability matrix visits the average customer {round(sum_of_areas_visited/no_of_customers, 1)} areas before checkout.\n"
          f"In the original data average customers visit 3.3 areas before checkout.")