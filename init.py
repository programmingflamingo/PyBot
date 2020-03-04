### Imports
###############################################################################
import cv2 as cv
import tensorflow as tf
import sklearn
import selenium
import numpy as np
###############################################################################


### Classes
###############################################################################
class PyBot:
    """
    Takes in computer vision and returns computer action.
    """

    def __init__(self):
        self.my_input = SensoryInput()
        self.my_output = MotorOutput()

        return

    def integration_loop(self):


        return


class SensoryInput:
    """
    One Input: Vision
    """

    def __init__(self):
        return

    def roi(self):
        return

    def process_image(self):
        return

    def screen_grab(self):
        return


class MotorOutput:
    """
    One Output: Speech
    """

    def __init__(self):
        return
###############################################################################


### Functions
###############################################################################
def checkVersion():
    print(cv.__version__)
    print(tf.__version__)
    print(sklearn.__version__)
    print(selenium.__version__)
    print(np.__version__)
    return

def main():
    return
###############################################################################


### Entry Point
###############################################################################
if __name__ == "__main__":
    main()
###############################################################################



#image captioning
#object detection