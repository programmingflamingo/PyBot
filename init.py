### Imports
###############################################################################
import cv2 as cv
import tensorflow as tf
import sklearn
import selenium
import numpy as np
import time
from PIL import ImageGrab
###############################################################################


### Classes
###############################################################################
class PyBot:
    """
    Takes in Sensory Input and returns Motor Output.
    """

    def __init__(self):
        self.my_input = SensoryInput()
        self.my_output = MotorOutput()

        return

    def what_am_i_looking_at(self, screen):
        cv.namedWindow('window', cv.WINDOW_NORMAL)
        cv.imshow('window',screen)
        if(cv.waitKey(25) & 0xFF == ord('q')):
            cv.destroyAllWindows()
        return

    def integration_loop(self):
        while(True):
            screen = self.my_input.screen_grab()
            self.what_am_i_looking_at(screen)

        return


class SensoryInput:
    """
    One Input: Vision
    """

    def __init__(self):
        return

    def roi(self):
        return

    def process_image(self, originalImage):
        processedImage = cv.cvtColor(originalImage,cv.COLOR_BGR2GRAY)
        #processedImage = cv.resize(processedImage, (80,45))
        #high_thresh, thresh_im = cv.threshold(processedImage, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
        #lowThresh = 0.5*high_thresh
        processedImage = cv.Canny(processedImage, 0, 255)
        return processedImage

    def screen_grab(self):
        last_time = time.time()
##      use win32gui, win32ui, win32con, win32api
        screen = np.array(ImageGrab.grab())
        new_screen = self.process_image(screen)
        loop_time = time.time()
        print('Loop took: {}'.format(loop_time-last_time))
        return new_screen
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
    myBot = PyBot()
    myBot.integration_loop()
    return
###############################################################################


### Entry Point
###############################################################################
if __name__ == "__main__":
    main()
###############################################################################



#image captioning
#object detection