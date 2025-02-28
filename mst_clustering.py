class MSTClustering:
    def calculate_similarity(self, book1, book2):
        """
        Calculate the similarity between two books based on genre and rating.

        Args:
            book1 (dict): The first book.
            book2 (dict): The second book.

        Returns:
            float: The similarity score between the two books.
        """
        similarity = 0
        if book1['genre'] == book2['genre']:
            similarity += 10  # High score for same genre
        similarity -= abs(float(book1['avg_rating']) - float(book2['avg_rating']))
        return similarity

    def construct_edge_list(self, books):
        """
        Construct a list of edges where each edge represents the similarity between two books.

        Args:
            books (list): List of book dictionaries.

        Returns:
            list: List of edges in the form (weight, book1_index, book2_index).
        """
        edges = []
        for i, book1 in enumerate(books):
            for j, book2 in enumerate(books):
                if i < j:
                    similarity = self.calculate_similarity(book1, book2)
                    edges.append((-similarity, i, j))  # Use negative similarity for MST
        return edges

    def find(self, parent, i):
        """
        Find the root of the set in which element i is located.

        Args:
            parent (list): List representing the parent of each element.
            i (int): The element to find.

        Returns:
            int: The root of the set containing element i.
        """
        if parent[i] == i:
            return i
        else:
            return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        """
        Perform the union of two sets.

        Args:
            parent (list): List representing the parent of each element.
            rank (list): List representing the rank of each element.
            x (int): The first element.
            y (int): The second element.
        """
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def build_mst(self, edges, num_books):
        """
        Build the Minimum Spanning Tree (MST) using Kruskal's algorithm.

        Args:
            edges (list): List of edges in the form (weight, book1_index, book2_index).
            num_books (int): The number of books (nodes).

        Returns:
            list: List of edges in the MST.
        """
        edges.sort()
        parent = list(range(num_books))
        rank = [0] * num_books
        mst = []

        for edge in edges:
            weight, u, v = edge
            if self.find(parent, u) != self.find(parent, v):
                self.union(parent, rank, u, v)
                mst.append(edge)

        return mst

    def apply_greedy(self, books, num_clusters):
        """
        Apply a greedy algorithm to form clusters by removing the highest-weight edges from the MST.

        Args:
            books (list): List of book dictionaries.
            num_clusters (int): The desired number of clusters.

        Returns:
            list: List of clusters, each cluster is a set of book indices.
        """
        edges = self.construct_edge_list(books)
        mst = self.build_mst(edges, len(books))

        # Sort edges of the MST by weight in descending order
        mst.sort(reverse=True, key=lambda x: x[0])

        # Greedy approach: Remove the highest-weight edges to form clusters
        for _ in range(num_clusters - 1):
            mst.pop(0)

        # Extract clusters
        parent = list(range(len(books)))
        for weight, u, v in mst:
            self.union(parent, [0] * len(books), u, v)

        clusters = {}
        for i in range(len(books)):
            root = self.find(parent, i)
            if root not in clusters:
                clusters[root] = []
            clusters[root].append(i)

        return list(clusters.values())