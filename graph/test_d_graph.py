from direct_graph import DirectedGraph
import unittest

class TestDirectedGraph(unittest.TestCase):

    def test_add(self):
        expected = [
            (0, 1, 10), (1, 4, 15), (2, 1, 23), (3, 1, 5), (3, 2, 7),
             (4, 0, 12), (4, 3, 3)
        ]
        g = DirectedGraph()
        for _ in range(5):
            g.add_vertex()

        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        for src, dst, weight in edges:
            g.add_edge(src, dst, weight)
        actual = g.get_edges()
        self.assertEqual(expected, actual)

    def test_get_edge(self):
        g = DirectedGraph()
        expected = [], []
        actual = g.get_edges(), g.get_vertices()
        self.assertEqual(expected, actual)
        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g = DirectedGraph(edges)
        expected = [
            [(0, 1, 10), (1, 4, 15), (2, 1, 23), (3, 1, 5), (3, 2, 7),
             (4, 0, 12), (4, 3, 3)],
            [0, 1, 2, 3, 4]
        ]
        actual = [g.get_edges(), g.get_vertices()]
        self.assertEqual(expected, actual)

    def valid_path(self):
        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g = DirectedGraph(edges)
        expected = [True, False, False, True, True, True]
        test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
        for i in range (0, len(test_cases)):
            self.assertEqual(expected[i], g.is_valid_path(test_cases[i]))

    def test_dfs(self):
        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g = DirectedGraph(edges)
        expected = [
            [0, 1, 4, 3, 2],
            [1, 4, 0, 3, 2],
            [2, 1, 4, 0, 3],
            [3, 1, 4, 0, 2],
            [4, 0, 1, 3, 2]
        ]
        for start in range(5):
            self.assertEqual(expected[start], g.dfs(start))

    def test_bfs(self):
        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g = DirectedGraph(edges)
        expected = [
            [0, 1, 4, 3, 2],
            [1, 4, 0, 3, 2],
            [2, 1, 4, 0, 3],
            [3, 1, 2, 4, 0],
            [4, 0, 3, 1, 2]
        ]
        for start in range(5):
            self.assertEqual(expected[start], g.bfs(start))

    def test_cycle(self):
        edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
                 (3, 1, 5), (2, 1, 23), (3, 2, 7)]
        g = DirectedGraph(edges)

        edges_to_remove = [(3, 1), (4, 0), (3, 2)]
        expected = [True, True, False, False, False, False, True]
        count = 0
        for src, dst in edges_to_remove:
            g.remove_edge(src, dst)
            self.assertEqual(expected[count], g.has_cycle())
            count += 1

        edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
        for src, dst in edges_to_add:
            g.add_edge(src, dst)
            self.assertEqual(expected[count], g.has_cycle())
            count += 1


if __name__ == "__main__":
    unittest.main()