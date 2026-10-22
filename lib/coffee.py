#!/usr/bin/env python3


class Coffee:
    """A coffee sold at the bookstore."""

    # The only sizes the store offers.
    VALID_SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, price):
        # Start with no value, then go through the property setter so the
        # same validation runs whether the value is set here or later.
        self._size = None
        self.size = size
        self.price = price

    @property
    def size(self):
        """Size of the coffee: Small, Medium, or Large."""
        return self._size

    @size.setter
    def size(self, size):
        if size in Coffee.VALID_SIZES:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        """Leave a tip, which adds 1 to the price of the coffee."""
        print("This coffee is great, here’s a tip!")
        self.price += 1