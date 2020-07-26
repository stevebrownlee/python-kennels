from uuid import uuid1

class Giraffe(object):

    def __init__(self) -> None:
        self.id = uuid1()

    def __repr__(self) -> str:
        # https://ascii.co.uk/art/giraffe
        return f"""
       .-",
       `~||
         ||___
         (':.)`
         || ||
         || ||
         ^^ ^^

Hi, I am giraffe {self.id}
            """
