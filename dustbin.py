from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:
    def __init__(self, color):
        self.color = color
        self.plastic_content = []
        self.paper_content = []
        self.house_waste_content = []

    def throw_out_garbage(self, garbage):
        if isinstance(garbage, PlasticGarbage):
            if garbage.is_clean is True:
                self.plastic_content.append(garbage)
            else:
                raise DustbinContentError("Clean it first!")
        elif isinstance(garbage, PaperGarbage):
            if garbage.is_squeezed is True:
                self.paper_content.append(garbage)
            else:
                raise DustbinContentError("Squeeze it first!")
        elif isinstance(garbage, Garbage):
            self.house_waste_content.append(garbage)
        else:
            raise DustbinContentError("This is not garbage!")

    def empty_contents(self):
        self.plastic_content = []
        self.paper_content = []
        self.house_waste_content = []
