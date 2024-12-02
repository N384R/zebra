from qc.hartree_fock import HartreeFock

H2 = 'H 0.0 0.0 0.0; H 0.0 0.0 1.4'
hf = HartreeFock(H2, 'sto-3g')
print(hf.overlap_integral)
print(hf.coordinates)
print(hf.basis_functions)
