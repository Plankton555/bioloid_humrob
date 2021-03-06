class AbstractFunctionClass:

    def initializeGenome(self):
        # Should return a genome, that is, an array/list with floating values
        raise NotImplementedError()

    def getGenomeRange(self):
        # Should return a list of [min, max] ranges for each parameter in the genome
        # For example, if parameter 1 in the genome has an allowed range of (-2, 3) 
        # and parameter 2 in the genome has the allowed range (3, 5), then this function
        # should return the list [[-2, 3], [3, 5], ...]
        raise NotImplementedError()

    def getFitness(self, genome):
        # Should calculate the fitness of the specified genome and return it
        raise NotImplementedError()