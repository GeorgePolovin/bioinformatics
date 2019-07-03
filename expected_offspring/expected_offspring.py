'''
Six nonnegative integers, each of which does not exceed 20,000.
The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor.
In order, the six given integers represent the number of couples having the following genotypes:

AA-AA: 100%
AA-Aa: 100%
AA-aa: 100%
Aa-Aa: 75%
Aa-aa: 50%
aa-aa: 0%

Return: The expected number of offspring displaying the dominant phenotype (AA or Aa) in the next generation, under the assumption that every couple has exactly two offspring.
'''

#!/usr/bin/python
def expected_value(list):
    dominant_prob=[1.0,1.0,1.0,0.75,0.5,0.0]
    prob_pairs=zip(dominant_prob,list)
    expected_values=[P*(2*N) for P,N in prob_pairs]
    return sum(expected_values)


with open('expected_offspring/expected_offspring.txt', 'r') as file:
    population_genotype=file.read().split()
    population_genotype=[int(x) for x in population_genotype]
    with open('expected_offspring/expected_offspring_results.txt','w+') as fh:
        fh.write(str(expected_value(population_genotype)))


###############OTHER USERS SOLUTIONS############

#!/usr/bin/python
filepath = r""
displayDominant = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]
offspring = 2

with open(filepath) as file:
    parentCounts = [int(x) for x in file.read().split()]

print sum([offspring * x[0] * x[1] for x in zip(displayDominant, parentCounts)])
