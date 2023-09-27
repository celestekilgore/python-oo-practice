class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Make a new instance of SerialGenerator"""

        self.start = start
        self.tracker = start #often called next
        # can combine since they equal the same thing

    def __repr__(self):
        return f"<Serial Generator start={self.start}"

    def generate(self):
        """Update serial tracker, return current serial number"""

        self.tracker += 1
        return self.tracker - 1

    def reset(self):
        """Reset the serial tracker to the initial start number"""

        self.tracker = self.start
