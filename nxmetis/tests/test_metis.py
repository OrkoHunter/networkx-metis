import itertools
import nose.tools

import networkx as nx

import nxmetis
from nxmetis import exceptions
from nxmetis import _metis
from nxmetis import types


def make_cycle(n):
    xadj = list(range(0, 2 * n + 1, 2))
    adjncy = list(
        itertools.chain.from_iterable(
            zip(itertools.chain([n - 1], range(n - 1)),
                itertools.chain(range(1, n), [0]))))
    return xadj, adjncy


class TestMetis(object):

    def setUp(self):
        self.node_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                     1, 2, 3, 4, 5, 6]
        self.G = nx.Graph()
        edges = [(self.node_list[i], self.node_list[i+1])
                 for i in range(len(self.node_list) - 1)]
        edges.append((6, 'a'))  # To complete the cycle
        self.G.add_edges_from(edges)

    def test_node_nested_dissection_unweighted(self):
        node_ordering = nxmetis.node_nested_dissection(self.G)
        nose.tools.assert_items_equal(self.node_list, node_ordering)

    def test_partition(self):
        partitioning = (96, [[1, 'c', 'b', 'j'], ['e', 'd', 'g', 'f'],
                        ['i', 'h', 3, 6], ['a', 2, 4, 5]])
        nose.tools.assert_equal(nxmetis.partition(self.G, 4), partitioning)

    def test_vertex_separator(self):
        bisection = ([1, 'c', 'e', 'g', 'f', 'h', 4],
                     ['a', 'b', 'd', 'i', 'j', 2, 3, 6, 5], [])
        nose.tools.assert_equal(nxmetis.vertex_separator(self.G), bisection)

    def test_MetisOptions(self):
        n = 16
        xadj, adjncy = make_cycle(n)
        options = types.MetisOptions(niter=-2)
        nose.tools.assert_raises_regexp(exceptions.MetisError,
                                        'Input Error: Incorrect niter.',
                                        _metis.part_graph, xadj, adjncy, 2,
                                        options=options)
