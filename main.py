import numpy as np
import statistics

E: float = 1.602176634e-19 # charge of an electron
SPEED_OF_LIGHT: float = 299792458


class Muon():
    def __init__(self):
        self.MASS: float = 1.883531627e-28 # kg
        self.VELOCITY: float = 0.99999 * SPEED_OF_LIGHT # m/s
        self.BETA = self.VELOCITY / SPEED_OF_LIGHT
        self.MOMENTUM: float = 4.806529461e-10 / SPEED_OF_LIGHT
        # self.MOMENTUM: float = 4.806529461e-10 # J (3 GeV)
        self.CHARGE: float = -E

    def calculate_momentum(self):
        gamma = 1 / ( np.sqrt( 1 - self.BETA**2 ) )
        momentum = gamma * self.MASS * self.VELOCITY

        return momentum
    #
    #     # Above is now ignored as the beam's momentum can be set

class Material:
    def __init__(self, name, atomic_number: int, atomic_mass: float, radiation_length: float, thickness: float):
        self.name = name # alphabet
        self.atomic_number = atomic_number
        self.atomic_mass = atomic_mass
        self.radiation_length = radiation_length # cm
        self.thickness = thickness # cm


def calculate_variance(particle: Muon, materials: list[Material]):
    outer_part = 2.178961128e-12 / ( particle.BETA * particle.MOMENTUM * SPEED_OF_LIGHT) # calculations done in Joules (SI) instead of eV

    sum = float()
    for material in materials:
        ratio = material.thickness / material.radiation_length
        log_part = 1 + (0.038 * np.log(ratio))

        sum += ratio * log_part**2

    return outer_part**2 * sum

def run_simulation(particle, materials, amount_to_simulate=1, detail=False, simulation_number=0, write=True):
    if detail:
        for material in materials:
            variance = calculate_variance(particle, [material])
            deviation = np.sqrt(variance)


            print(f"--- {material.name} ---")
            print(f"Atomic Number: {material.atomic_number}")
            print(f"Thickness: {material.thickness}")
            print(f"Radiation length: {material.radiation_length}")
            print(f"x/X0: {material.thickness / material.radiation_length}")
            print(f"Standard deviation:  {deviation}")
            print(f"Variance:  {variance}")
            print()

    print(f"--- Initial Calculations ---")

    variance = calculate_variance(particle, materials)
    standard_deviation = np.sqrt(variance)

    print(f"Materials: {', '.join([material.name for material in materials])}")
    print(f"Total thickness: {sum([material.thickness for material in materials])}")
    print(f"Variance: {variance}")
    print(f"Standard deviation:  {standard_deviation}")
    print()

    print(f"--- Simulation of {amount_to_simulate} particles ---")

    output_file_name = "simulation_output_"

    with open(f"{output_file_name}{simulation_number}.txt", "w") as file:
        angles = list()
        for i in range(amount_to_simulate):
            angle = np.random.normal(0, standard_deviation)
            angles.append(angle)

            if write:
                file.write(f"{angle}\n")

    mean = statistics.fmean(angles)
    absolute_mean = np.sqrt(statistics.fmean([angle**2 for angle in angles]))

    print(f"Mean angle: {mean}")
    print(f"Absolute mean: {absolute_mean}")
    print()

def main():
    particle = Muon()

    aluminum = Material(name="Aluminium",
                        atomic_number=13,
                        atomic_mass=26.9815385,
                        radiation_length=8.897,
                        thickness=1)

    lead = Material(name="Lead",
                    atomic_number=82,
                    atomic_mass=207.2,
                    radiation_length=0.5612,
                    thickness=1)

    amount_to_simulate = int(input("How many particles should be simulated? "))

    if amount_to_simulate < 1:
        raise ValueError("At least one particle must be simulated.")
    if type(amount_to_simulate) != type(int()):
        raise TypeError("Amount must be an integer.")

    run_simulation(particle, [aluminum, lead, aluminum], amount_to_simulate, simulation_number=2)
    run_simulation(particle, [aluminum, aluminum, aluminum], amount_to_simulate, simulation_number=3)


if __name__ == "__main__":
    main()

