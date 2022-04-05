class Dough:
    def __init__(self, flour_type, baking_technique, weight):
        self.weight = weight
        self.baking_technique = baking_technique
        self.flour_type = flour_type

    @property
    def weight(self):
        return self.__w

    @weight.setter
    def weight(self, w):
        if w <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__w = w

    @property
    def baking_technique(self):
        return self.__technique

    @baking_technique.setter
    def baking_technique(self, technique):
        if technique == "":
            raise ValueError("The baking technique cannot be an empty string")
        self.__technique = technique

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, flour_type):
        if flour_type == "":
            raise ValueError("The flour type cannot be an empty string")
        self.__flour_type = flour_type
