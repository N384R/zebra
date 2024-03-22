import numpy as np
import zebra

# Test case 1: Identity matrix
mol1 = np.eye(3)
qc = zebra.QuantumCalculator()
energy1, eigenvectors1 = qc.hartree_fock(mol1)
print("Test case 1:")
print("Energy:", energy1)
print("Eigenvectors:")
print(eigenvectors1)

# Test case 2: Random matrix
mol2 = np.random.rand(3, 3)
energy2, eigenvectors2 = qc.hartree_fock(mol2)
print("Test case 2:")
print("Energy:", energy2)
print("Eigenvectors:")
print(eigenvectors2)

# Test case 3: Zero matrix
mol3 = np.zeros((3, 3))
energy3, eigenvectors3 = qc.hartree_fock(mol3)
print("Test case 3:")
print("Energy:", energy3)
print("Eigenvectors:")
print(eigenvectors3)