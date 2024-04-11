'''
Basis set module to load basis set from a file and store it in a dictionary.
'''

class BasisSet:
    '''
    Class to load basis set from a file and store it in a dictionary.
    
    Attributes:
    basis_set_name (str): Name of the basis set.
    basis_set_file (str): File containing the basis set.
    basis_set (dict): Dictionary containing the basis set.
    '''

    def __init__(self, basis_set_name):
        self.basis_set_name = basis_set_name
        self.basis_set_file = f"basis_set/{basis_set_name}"
        self.basis_set = self.load_basis_set()

    def load_basis_set(self):
        '''Load basis set from a file and store it in a dictionary.'''
        basis_set_dict = {}
        with open(self.basis_set_file, 'r', encoding="UTF-8") as f:
            lines = f.readlines()
            for line in lines:
                if line.strip().startswith('#') or line.strip() == '':
                    continue
                data = line.split()

                if data[0] == '!':
                    element = data[1]
                    basis_set_dict[element] = {}
                elif data[0].isalpha():
                    orbital_type = data[0]
                    if orbital_type not in basis_set_dict[element]:
                        basis_set_dict[element][orbital_type] = []
                else:
                    basis_set_dict[element][orbital_type].append(list(map(float, data)))

        return basis_set_dict

    def show_basis_set(self):
        '''Print the basis set.'''
        print(f"Basis set: {self.basis_set_name}")
        for element, basis_function in self.basis_set.items():
            print(f"{element}: {basis_function}")

    def __str__(self):
        return f"Basis set: {self.basis_set_name}"

if __name__ == "__main__":
    basis_set = BasisSet("STO-3G")
    basis_set.show_basis_set()
    print(basis_set)