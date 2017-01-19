import csv


class Runner(object):
    """Run the anomaly detection algorithm."""

    def __init__(self):
        self.data_folder = '../data/ydata-labeled-time-series-anomalies-v1_0/A1Benchmark/'
        self.filename = 'real_1.csv'
        # key is timestamp, value is 1 | 0
        self.truths = dict()

    def run(self):
        f = open(self.data_folder + self.filename)
        datareader = csv.reader(f)
        next(datareader)
        for row in datareader:
            timestamp = row[0]
            value = float(row[1])
            truth = int(row[2])
            self.truths[timestamp] = truth


if __name__ == '__main__':
    r = Runner()
    r.run()
