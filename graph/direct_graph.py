import heapq
from collections import deque

class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency matrix
        """
        self.v_count = 0
        self.adj_matrix = []

        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def add_vertex(self) -> int:
        """
        Adds a new vertex to the graph
        """
        # Add vertex to graph
        new_vertex = [0 for vert in range(0, self.v_count+1)]
        self.adj_matrix.append(new_vertex)
        self.v_count += 1

        # Adjust other vertices
        for vert in range(0, self.v_count):
            self.adj_matrix[vert].append(0)

        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Adds a new edge to the graph
        """
        if src in range(0, self.v_count) and dst in range(0, self.v_count):
            if src != dst:  # no loops allowed
                if weight > 0:
                    self.adj_matrix[src][dst] = weight  # add edge

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes edge from the graph
        """
        if src in range(0, self.v_count) and dst in range(0, self.v_count):
            self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        Returns list will all vertices
        """
        return [vert for vert in range(0, self.v_count)]

    def get_edges(self) -> []:
        """
        Returns a list of edges in the graph
        """
        edge_list = []

        for src in range(0, self.v_count):
            for dst in range(0, self.v_count):
                if self.adj_matrix[src][dst] != 0:
                    edge_list.append((src, dst, self.adj_matrix[src][dst]))

        return edge_list

    def is_valid_path(self, path: []) -> bool:
        """
        Returns true if given path is valid, false if not
        """
        if len(path) == 0:  # empty path valid
            return True

        if len(path) == 1:  # single item paths valid if vertex exists in graph
            if path[0] in range(0, len(self.adj_matrix)):
                return True
            else:
                return False

        cur_vert = 0
        next_vert = 1

        while next_vert < len(path):
            cur_loc = path[cur_vert]
            next_loc = path[next_vert]

            # edge exists from source to destination
            if self.adj_matrix[cur_loc][next_loc] > 0:
                cur_vert += 1
                next_vert += 1
            else:
                return False

        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Returns list of vertices visited in DFS order
        vertices are visited in ascending order
        """
        visit_verts = []

        if v_start in range(0, len(self.adj_matrix)):
            stack = deque()  # used to track search items
            stack.append(v_start)

            while len(stack) > 0:
                cur_vert = stack.pop()

                # end vertex reached, if applicable
                if cur_vert == v_end:
                    visit_verts.append(v_end)
                    return visit_verts

                # only search vertices not yet visited
                if cur_vert not in visit_verts:
                    visit_verts.append(cur_vert)

                    heap = []

                    # record successors in ascending order
                    for edge in range(0, len(self.adj_matrix[cur_vert])):
                        if self.adj_matrix[cur_vert][edge] > 0:
                            heapq.heappush(heap, edge)

                    count = 0
                    while len(heap) > 0:
                        direct_successor = heapq.heappop(heap)
                        # add successor if it has not been visited
                        if direct_successor not in visit_verts:
                            stack.insert(len(stack) - count, direct_successor)
                            count += 1

        return visit_verts

    def bfs(self, v_start, v_end=None) -> []:
        """
        Returns list of vertices visited in BFS order
        vertices are visited in ascending order
        """
        visit_verts = []

        if v_start in range(0, len(self.adj_matrix)):
            queue = deque()   # used to track search items
            queue.append(v_start)

            while len(queue) > 0:
                cur_vert = queue.popleft()

                if cur_vert == v_end:  # end vertex reached, if applicable
                    visit_verts.append(v_end)
                    return visit_verts

                # only search vertices not yet visited
                if cur_vert not in visit_verts:
                    visit_verts.append(cur_vert)

                    heap = []

                    # record successors in ascending order
                    for edge in range(0, len(self.adj_matrix[cur_vert])):
                        if self.adj_matrix[cur_vert][edge] > 0:
                            heapq.heappush(heap, edge)

                    count = 0
                    while len(heap) > 0:
                        direct_successor = heapq.heappop(heap)
                        # add successor if it has not been visited
                        if direct_successor not in visit_verts:
                            queue.append(direct_successor)
                            count += 1

        return visit_verts

    def has_cycle(self) -> bool:
        """
        Returns True if graph has a cycle, false is not
        """

        for vert in range(0, self.v_count):
            visit_verts = []
            stack = deque()
            stack.append(vert)

            while len(stack) > 0:
                cur_vert = stack.pop()
                visit_verts.append(cur_vert)
                heap = []

                # record successors in ascending order
                for edge in range(0, len(self.adj_matrix[cur_vert])):
                    if self.adj_matrix[cur_vert][edge] > 0:
                        heapq.heappush(heap, edge)

                count = 0
                while len(heap) > 0:
                    direct_successor = heapq.heappop(heap)
                    # add successor if it has not been visited
                    if direct_successor not in visit_verts:
                        stack.insert(len(stack) - count, direct_successor)
                        count += 1
                    # successor has been visited and is starting vertex (cycle)
                    elif direct_successor == vert:
                        return True

        return False  # no cycle found
