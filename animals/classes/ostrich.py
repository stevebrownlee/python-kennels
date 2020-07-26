from uuid import uuid1

class Ostrich(object):

    def __init__(self) -> None:
        self.id = uuid1()

    def __repr__(self) -> str:
        # https://ascii.co.uk/art/ostrich
        return f"""
           -O    /O
             \ __|/
              (_ )
                \\
               _/

Hi, I am ostrich {self.id}
            """
