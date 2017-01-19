class Detector(object):
    """A detector takes in a timestamp and value and determines if the point
    is an anomaly or not."""

    def __init__(self):
        self.record = dict()

    def detect(timestamp, value):
        raise NotImplementedError()