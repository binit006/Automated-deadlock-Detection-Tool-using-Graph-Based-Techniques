import networkx as nx 

class DeadlockDetector: 
    def __init__(self): 
        self.graph = nx.DiGraph() 

    def add_process(self, process_id, resource_id): 
        self.graph.add_edge(process_id, resource_id) 

    def add_resource(self, resource_id, process_id): 
        self.graph.add_edge(resource_id, process_id) 

    def detect_deadlock(self): 
        try: 
            cycle = nx.find_cycle(self.graph, orientation='original') 
            return True, cycle 
        except nx.NetworkXNoCycle: 
            return False, [] 

    def get_graph_structure(self): 
        return { 
            "nodes": [{"id": node} for node in self.graph.nodes()], 
            "links": [{"source": edge[0], "target": edge[1]} for edge in self.graph.edges()] 
        } 
