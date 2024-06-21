import os
import sys
sys.path.append(os.pardir)
from random import random
from pycomponents.draw import Draw

if __name__ == "__main__":  
    draw = Draw()
    dat = [random() for _ in range(10)]
    draw.plot_metrics(dat, label="random")

    draw.set_title(xlabel="index", ylabel="random")

    # SAVE
    # draw.show()
    # draw.save(fname="test.png")
    draw.save_as_pdf(fname="test.pdf")