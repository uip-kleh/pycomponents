import matplotlib.pyplot as plt 

class Draw:
    def __init__(self) -> None:
        pass

    def plot_metrics(self, dat: list, idx: list = [], label: str = ""):
        plt.figure()
        if not idx: idx = [i for i in range(len(dat))]
        plt.plot(idx, dat, label=label)

    def show(self):
        plt.show()

    def save(self, fname: str):
        plt.savefig(fname)
        self.close()

    def save_as_pdf(self, fname: str):
        plt.savefig(fname, transparent=True)
        self.close()

    def set_title(self, xlabel: str = "", ylabel: str = ""):
        if str: plt.xlabel(xlabel)
        if str: plt.ylabel(ylabel)
        plt.legend()
        plt.tight_layout()

    def close(self):
        plt.clf()
        plt.cla()
        plt.close()