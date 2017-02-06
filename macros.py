"""
[up.py]

Cool aliases.
"""

import os

def up(env, args, kwargs):
    """[N]@Move up a directory N times."""
    for i in range(args[0]):
        os.chdir("..")
        env.directory = os.getcwd()


        
verbs = {"up":up,
        }
