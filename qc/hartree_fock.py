'''
Hartree-Fock calculations are a way to approximate the wavefunction of a molecule. 
The wavefunction is approximated as a single Slater determinant, 
which is a product of molecular orbitals. 

The molecular orbitals are obtained by solving the Hartree-Fock equations, 
which are a set of self-consistent field equations.
The Hartree-Fock equations are solved iteratively until convergence is reached.

The Hartree-Fock method is a mean-field theory,
which means that it does not include electron correlation effects. 
However, it is a good starting point for more advanced quantum chemistry methods 
that do include electron correlation effects.
'''

import numpy as np
from basis_set.basis_set import BasisSet

class HartreeFock:
    '''
    Class to perform Hartree-Fock calculations.

    Attributes:
    molecule (str): Molecule string.
    basis_set (BasisSet): Basis set object.
    overlap (np.ndarray): Overlap matrix.
    one_electron (np.ndarray): One-electron matrix.
    two_electron (np.ndarray): Two-electron matrix.
    energy (float): Energy of the molecule.
    eigenvectors (np.ndarray): Eigenvectors of the molecule.
    '''

    def __init__(self, molecule, basis_set_name):
        self.molecule = molecule
        self.basis_set = BasisSet(basis_set_name)
        self.overlap = None
        self.one_electron = None
        self.two_electron = None
        self.energy = None
        self.eigenvectors = None

    def coordinates(self, molecule):
        '''Parse the molecule string and return the coordinates of the atoms.'''

        coordinates = []
        for atom in molecule.split(';'):
            atom = atom.strip()
            symbol = atom.split()[0]
            x, y, z = atom.split()[1:]
            coordinates.append((symbol, float(x), float(y), float(z)))
        return coordinates

    @staticmethod
    def print_results(func):   
        def wrapper(*args, **kwargs):
            instance = args[0]
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            if instance.energy is None or instance.eigenvectors is None:
                print("No results to print.")
                return
            print("Calculated energy: %.6f" %instance.energy)
            print("eigen vectors:")
            print(instance.eigenvectors)
            print("Execution time: %.3f seconds" %(end - start))
            return result
        return wrapper
    
    def __hartree_fock(self, mol):
            # Step 1: Initialize the molecular orbitals
            print("Preforming SCF calculation...")
            n = mol.shape[0]
            fock = np.zeros((n, n))
            density = np.zeros((n, n))
            energy = 0.0

            # Step 2: Iterate until convergence
            max_iter = 100
            for iteration in range(max_iter):
                print("Iteration", (iteration + 1))
                # Step 3: Build the Fock matrix
                for i in range(n):
                    for j in range(n):
                        fock[i, j] = mol[i, j] + np.sum(density * (2 * mol[i, j] - mol[j, i]))

                # Step 4: Diagonalize the Fock matrix
                eigenvalues, eigenvectors = np.linalg.eigh(fock)

                # Step 5: Build the new density matrix
                new_density = np.zeros((n, n))
                for i in range(n):
                    for j in range(n):
                        for k in range(n):
                            new_density[i, j] += 2 * eigenvectors[i, k] * eigenvectors[j, k]

                # Step 6: Calculate the electronic energy
                energy_new = np.sum(density * (mol + fock))
                if np.abs(energy_new - energy) < 1e-6:
                    print("Converged in", (iteration + 1), "iterations.")
                    break
                elif iteration == max_iter - 1:
                    print("Did not converge in", max_iter, "iterations.")
                    break

                # Step 7: Update the density matrix and energy
                density = new_density
                energy = energy_new

            self.energy = energy
            self.eigenvectors = eigenvectors

            return energy, eigenvectors

    @print_results
    def hartree_fock(self, mol):
        return self.__hartree_fock(mol)
    
if __name__ == "__main__":
    H2 = 'H 0.0 0.0 0.0; H 0.0 0.0 1.4'
    hf = HartreeFock(H2, 'sto-3g')
    print(hf.coordinates(H2))