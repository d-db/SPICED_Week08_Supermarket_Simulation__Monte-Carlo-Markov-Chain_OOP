"""
Start with this to implement the supermarket simulator.
"""

import numpy as np
import pandas as pd
import random
import csv
from faker import Faker

from customer_class import Customer
from datetime import datetime


class Supermarket:
    """manages multiple Customer instances that are currently in the market.
    """

    def __init__(self, initial_state_probabilities, probabilities):
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.initial_state_probabilities = initial_state_probabilities
        self.probabilities = probabilities

    def __repr__(self):
        return f'Currently there are {len(self.customers)} customers in the supermarket'

    def _get_time(self):
        """current time in HH:MM format,
        """
        return datetime.now().strftime("%H:%M")

    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        for customer in self.customers:
            time = self._get_time()
            name = customer.name
            state = customer.state

            fields = [time, name, state]
            with open("./data/customer.csv", 'a') as f:
                writer = csv.writer(f)
                writer.writerow(fields)

        return None

    def next_minute(self):
        """propagates all customers to the next state.
        """
        for customer in self.customers:
            customer.next_state()

        return None

    def add_new_customers(self):
        """randomly creates new customers.
        """
        for i in range(random.randint(1, 3)):
            fake = Faker()
            name = fake.name()
            customer = Customer(name, self.initial_state_probabilities, self.probabilities)
            self.customers.append(customer)

        return None

    def remove_exitsting_customers(self):
        """removes every customer that is not active any more.
        """
        for customer in self.customers:
            if not customer.is_active():
                self.customers.remove(customer)

        return None