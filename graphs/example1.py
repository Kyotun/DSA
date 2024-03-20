class Graph:
    def __init__(self, edges) -> None:
        self.edges = edges
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        
    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path=path)
                for path in new_paths:
                    paths.append(path)
                
        return paths
    
    def get_shortest_path(self, start, end, path=[]):
        pass