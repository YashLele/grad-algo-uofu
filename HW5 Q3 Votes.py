import random as r
import math as m

def take_sample_majority(vote_list, sample_size):
    majority_count = 0
    for i in range(100):
        sample_list = []
        for s in range(k):
            random_index = m.floor(r.random()*1000000)
            sample_list.append(vote_list[random_index])
        plus_one_count = sample_list.count(1)
        if plus_one_count > (sample_size / 2):
            majority_count += 1
    return majority_count/100
    
votes = [1]*520000 + [-1]*480000
r.shuffle(votes)
for k in [20, 50, 100, 200, 400, 800, 1000]:
    print('Sample size = ',k, '\tMajority probability of +1 votes = ', take_sample_majority(votes, k))