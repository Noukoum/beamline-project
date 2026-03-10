import numpy as np

E: float = 1.602176634e-19 # charge of an electron
SPEED_OF_LIGHT: float = 299792458

class Muon():
    def __init__(self):
        self.MASS: float = 1.883531627e-28 # kg
        self.VELOCITY: float = 0.99999 * SPEED_OF_LIGHT # m/s
        self.BETA = self.VELOCITY / SPEED_OF_LIGHT
        self.MOMENTUM: float = self.calculate_momentum()
        self.CHARGE: float = -E
        self.vector = np.array([1, 0])

    def calculate_momentum(self):
        gamma = 1 / ( np.sqrt( 1 - self.BETA**2 ) )
        momentum = gamma * self.MASS * self.VELOCITY

        return momentum

class Material:
    def __init__(self, atomic_number: int, atomic_mass: float, radiation_length: float, thickness: float):
        self.atomic_number = atomic_number
        self.atomic_mass = atomic_mass
        self.radiation_length = radiation_length # cm
        self.thickness = thickness # cm

particle = Muon()

material = Material(atomic_number=13,
                    atomic_mass=26.9815385,
                    radiation_length=8.897,
                    thickness=5)

angle = ( 2.178961128e-12 / ( particle.BETA * particle.MOMENTUM * SPEED_OF_LIGHT) ) \
        * np.sqrt( material.thickness / material.radiation_length ) \
        * (1 + ( 0.038 * np.log( material.thickness / material.radiation_length )))
        # radians (absolute value)

variance = angle ** 2

def probability_of_angle(angle):
    return (1 / (np.sqrt( 2 * np.pi * variance ))) * np.e ** ( - ( angle**2 ) / (2 * variance))

print(angle)

