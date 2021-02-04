from typing import Optional


class Readme:
    def __init__(self, filename: Optional[str] = None, text: Optional[str] = None, fmt: Optional[str] = None):
        self.filename = filename
        self.text = text
        self.fmt = fmt

    def __eq__(self, other):
        return \
            self.filename == other.filename and \
            self.text == other.text and \
            self.fmt == other.fmt
