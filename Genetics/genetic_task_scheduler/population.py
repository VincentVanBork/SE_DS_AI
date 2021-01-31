from chromosome import Chromosome


class Population():
    """
    mutability how often mutations happen
    adaptability how much chromosome must be damaged to die (9-49) length of the chromosome
    survivability how many chromosomes are picked from the population as offspring (least 0-Npop) e.g. 5 with lowest time
    """
    def __init__(self, df, size=1000, mutability=1, surivability=0, adaptability=1) -> None:
        super().__init__()
        self.chromosomes:list[Chromosome] = []
        self.mutability = mutability
        self.surivability = surivability
        # self.next_generation = []
        for i in range(size):
            self.chromosomes.append(Chromosome(df))
        self.fitness:list[int] = []
        self.adaptability = adaptability
        self.size = size 
        self.best = None
    
    def mutate_generation(self):
        for chromosome in self.chromosomes:
            chromosome.mutate(self.mutability)

    def next_generation(self):
        self.fitness = [chromosome for chromosome in self.chromosomes]
        for chromosome in self.chromosomes:
            chromosome.fitness()
        self.fitness.sort(key=lambda x: x.current_time_value)
        self.chromosomes = self.fitness[:self.adaptability+1]
        print("BEST IN CHROME", self.chromosomes[0].current_time_value)
        #TODO BLAD Z WYBOREM NAJLEPSZEGO
        if self.best:
            if self.best.current_time_value > self.chromosomes[0].current_time_value:
                print("BEST IN POP", self.best.current_time_value)
                
                self.best = self.chromosomes[0]
        else:
            self.best = self.chromosomes[0]

    def repopulate_generation(self):
        while len(self.chromosomes) < self.size:
            for chromosome in self.chromosomes:
                # print(len(self.chromosomes))
                # print("CHROM", chromosome)
                if len(self.chromosomes) < self.size:
                    self.chromosomes.append(chromosome.copy())
                else:
                    break