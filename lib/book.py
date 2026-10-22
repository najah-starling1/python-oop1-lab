#!/usr/bin/env python3


class Book:
    """A book that can be read one page at a time."""

    def __init__(self, title, page_count):
        self.title = title
        # Start with no value, then go through the property setter so the
        # same validation runs whether the value is set here or later.
        self._page_count = None
        self.page_count = page_count

    @property
    def page_count(self):
        """Number of pages in the book."""
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        # bool is a subclass of int in Python, so exclude it explicitly.
        if isinstance(page_count, int) and not isinstance(page_count, bool):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        """Turn to the next page."""
        print("Flipping the page...wow, you read fast!")