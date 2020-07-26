from uuid import uuid1

class Toucan(object):

    def __init__(self) -> None:
        self.id = uuid1()

    def __repr__(self) -> str:
        # https://ascii.co.uk/art/toucan
        return f"""
                ,-,---.
             __/( ,----`
         _,-'    ;
       ;;.---..-'
             ""

Hi, I am toucan {self.id}
            """
