import random
#TODO check __call__ in python
import pandas as pd
from operator import attrgetter

def check_overlapping(x, y):
    return [False if ((x.start == x.stop) or (oth.start == oth.stop)) else ((x.start < oth.stop  and x.stop > oth.start) or (x.stop  > oth.start and oth.stop > x.start)) for oth in y]

class Gene:
    def __init__(self, resources, time_weights,max_time=None, start_time=None ) -> None:
        super().__init__()
        self.resources:list = resources 
        self.time_weights:list = time_weights
        # self.finish = sum([time for time in self.time_weights])
        self.finish = self.time_weights[-1]
        if not start_time:
            if not max_time:
                self.start_time:int = random.choice(range(self.finish*50 - self.finish))
            else:
                self.start_time:int = random.choice(range(max_time - self.finish))


    def sequence_time(self, protein):
        return self.start_time , self.start_time + self.time_weights.get(protein)

    def init_time(self, max_time):
        self.start_time:int = random.choice(range(max_time- self.finish))

class Chromosome():
    def __init__(self, tasks:pd.DataFrame) -> None:
        super().__init__()
        self.genes = []
        self.damage = 0
        
        for i in range(50):
            self.genes.append(Gene(tasks[f"R.{i}"].to_list(), tasks[f"T.{i}"].to_list()))
        self.max_time:int = sum([gene.finish for gene in self.genes])
        for gene in self.genes:
            gene.init_time(self.max_time)

        self.current_time_value:int = self.max_time 
        self.mutated = []
        

    def check_integrity(self, max_num_overlaps):
        """
        if any tasks for some resource overlap dies
        """
        for protein in range(11):
            ranges = []
            for gene in self.genes:
                start_time, end_time = gene.sequence_time(protein)
                ranges.append(range(start_time, end_time+1))

            for index, sth in ranges:
                damages = check_overlapping(sth, ranges[:index] + ranges[index+1:])
                if any(damages):
                    self.damage +=1

        if self.damage > max_num_overlaps:
            return False
        else:
            return True

    def mutate(self, number_of_mutations):
        """
        exchange places at random
        """
        self.mutated.clear()
        mutations = []
        for i in range(number_of_mutations+1):
            old_gene = random.choice(self.genes)
            while old_gene in mutations:
                old_gene = random.choice(self.genes)
            # print(self.max_time)
            old_gene.start_time = random.choice(range(self.max_time - old_gene.finish))
            self.mutated.append(self.genes.index(old_gene))

    def fitness(self):
        """
        calculate how much time tasks take in this chromosome
        """
        # for gene in self.genes:
        starting_gene = min(self.genes, key=lambda x: x.start_time)
        # print(starting_gene.start_time) 
        finishing_gene = max(self.genes, key=lambda x: x.start_time + x.finish)
        # print(finishing_gene.start_time)
        self.current_time_value:int = finishing_gene.finish + finishing_gene.start_time - starting_gene.start_time
        return self.current_time_value
    
    def copy(self):
        return self
