#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name=None, last_name=None, knowledge=None):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge if knowledge is not None else []

    def teach(self):
        return random.choice(self.knowledge)

# Instantiate a Teacher object with knowledge list
my_teacher = Teacher("My", "Teacher", knowledge=[
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    # Add other knowledge strings here
])