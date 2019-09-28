import networkx
import numpy
import scipy.stats

from bn.variable import Variable


class BayesianNetwork:
    NAME = "BayesianNetwork"

    def __init__(self, variables, adj):
        if not isinstance(variables, list):
            raise TypeError()
        if any(not isinstance(x, Variable) for x in variables):
            raise TypeError()

        self.__vars = numpy.array(variables)
        self.__n_var = len(variables)
        self.__varidx_map = {e.name: i for i, e in enumerate(self.vars)}
        self.__adj = adj

    @property
    def vars(self):
        return self.__vars

    @property
    def n_var(self):
        return self.__n_var

    @property
    def name(self):
        return BayesianNetwork.NAME

    def sample_data(self, n=1):
        topo = [x for x in networkx.topological_sort(self.as_graph(self.__adj))]
        print(topo)

    def as_graph(self, adj):
        graph = networkx.from_numpy_array(
          adj, create_using=networkx.DiGraph)
        graph = networkx.relabel_nodes(
          graph, {i: e for i, e in enumerate(self.vars)})
        return graph