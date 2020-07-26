from uuid import uuid1

class Rhino(object):

    def __init__(self) -> None:
        self.id = uuid1()

    def __repr__(self) -> str:
        # https://ascii.co.uk/art/rhino
        return f"""
              /))_
             /   .\/)
    _."```'-'  \___/
   '/           |
    \          /
     | ||~~~| ||
     ^^^`   ^^^`

Hi, I am rhino {self.id}
            """
