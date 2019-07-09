'''
Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb.
Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level).
Assume that Mendel's second law holds for the factors.

Sample Dataset
2 1
Sample Output
0.684
'''

def import_numbers(data_filename):
    with open(data_filename,'r') as file:
        data_list=file.read().split(' ')
    return data_list[0], data_list[1].strip('\n')

def write_to_txt(result_filename, data_string):
    with open(result_filename,'w+') as fh:
        fh.write(data_string)

def hetero_prob_min(gen,min_num):
    total_offspring=2**gen
    frac_hetero_offspring=min_num/total_offspring
    prob_hetero=1
    for generation in range(1,gen+1):
        prob_hetero=prob_hetero*(generation*(1/4)*2/(2**generation))
        print(prob_hetero)
    return frac_hetero_offspring*prob_hetero




given_data=import_numbers('independent_alleles/independent_alleles.txt')
print(hetero_prob_min(int(given_data[0]),int(given_data[1])))
