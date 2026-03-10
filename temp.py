import numpy as np

E: float = 1.602176634e-19
SPEED_OF_LIGHT: float = 299792458

class Muon():
    def __init__(self):
        self.MASS: float = 1.883531627e-28
        self.VELOCITY: float = SPEED_OF_LIGHT
        self.MOMENTUM: float = self.MASS * self.VELOCITY
        self.CHARGE: float = -E
        self.vector = np.array([1, 0])

class Material:
    def __init__(self, atomic_number: int, atomic_mass: float, radiation_length: float, thickness: float):
        self.atomic_number = atomic_number
        self.atomic_mass = atomic_mass
        self.radiation_length = radiation_length
        self.thickness = thickness

particle = Muon()

material = Material(13, 26.9815385, 24.01, 26.99) # 5.389

angle = -E * ( 13.6 / ( particle.MOMENTUM * SPEED_OF_LIGHT) ) \
        * np.sqrt( material.thickness / material.radiation_length ) \
        * (1 + ( 0.038 * np.log( (material.thickness * E**2)/ material.radiation_length )))

variance = angle ** 2

def probability_of_angle(angle):
    return (1 / (np.sqrt( 2 * np.pi * variance ))) * np.e ** ( - ( angle**2 ) / (2 * variance))

print(angle)

