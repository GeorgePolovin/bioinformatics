'''
In a weighted alphabet, every symbol is assigned a positive real number called a weight. A string formed from a weighted alphabet is called a weighted string, and its weight is equal to the sum of the weights of its symbols.

The standard weight assigned to each member of the 20-symbol amino acid alphabet is the monoisotopic mass of the corresponding amino acid.

Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
'''

protein_mass_table='''A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333
water   18.01056'''

def calc_prot_mass(prot_seq):
    mass_dict=dict(zip(protein_mass_table.split()[0::2],[float(i) for i in protein_mass_table.split()[1::2]])) #convert mass table to dictionary, make sure to convert masses to float
    prot_mass=mass_dict['water'] #start with mass of water
    for aa in prot_seq:
        prot_mass+=mass_dict[aa]
    return prot_mass

with open('protein_mass/protein_mass.txt','r') as rfile:
    protein_sequence=rfile.read().strip('\n')
with open('protein_mass/protein_mass_result.txt','w+') as wfile:
    wfile.write(str(calc_prot_mass(protein_sequence)))
