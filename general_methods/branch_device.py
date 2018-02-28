class BranchDevice:
    def __init__(self, name):
        """
        Mother class for all branch devices
        :param name:
        """
        self.name = name

    def __repr__(self):
        return self.name


class Resistor(BranchDevice):
    def __init__(self, name, resistance):
        super().__init__(name)
        self.resistance = resistance
        self.conductance = 1.0 / resistance


class IndependentCurrentSource(BranchDevice):
    def __init__(self, name, current):
        super().__init__(name)
        self.current = current


class VoltageDependentCurrentSource(BranchDevice):
    def __init__(self, name, coefficient, referenceBranch):
        super().__init__(name)
        self.coefficient = coefficient
        self.referenceBranch = referenceBranch
