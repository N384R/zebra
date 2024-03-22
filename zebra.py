import numpy as np

class QuantumCalculator:
    def __init__(self):
        self.energy = None
        self.eigenvectors = None

    def hartree_fock(self, mol):
        # Step 1: Initialize the molecular orbitals
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
    
    def print_results(self):   
        if self.energy is None or self.eigenvectors is None:
            print("No results to print.")
            return

        print("\nHartree-Fock energy:", self.energy)
        print("Molecular orbitals:")
        print(self.eigenvectors)
        

# Example usage
# mol = np.array([[1.0, 0.5], [0.5, 1.0]])  # Example molecular integrals
# qc = QuantumCalculator()
# energy, eigenvectors = qc.hartree_fock(mol)
# qc.print_results()
