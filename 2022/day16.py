

class Pipe():

    def __init__(self, name, flow_rate, other_nodes, open):
        self.name = name
        self.flow_rate = flow_rate
        self.nodes = other_nodes

        self.open = open
    
    def open_pipe(self):
        self.open = True

class Tunnel():

    def __init__(self, valves:dict, time=0):
        
        self.valves = {name:Pipe(name, flow_rate, nodes, open) for name, (flow_rate, nodes, open) in valves.items()}
        self.total_pressure = 0
        self.time = time

    def release_pressure(self):

        for pipe in self.valves.keys():
            if self.valves[pipe].open:
                self.total_pressure += self.valves[pipe].flow_rate
    
    def ret_valves(self):
        return {pipe.name:(pipe.flow_rate, pipe.nodes, pipe.open) for pipe in self.valves.values()}
    

def most_pressure_releasable(tunnel:Tunnel, curr:str):
    


if __name__ == "__main__":

    fp = open("day16_input.txt", "r")

    start: Pipe
    valves = {}
    pipeline = fp.readline()
    while pipeline != "":
        pipeline = pipeline.split()

        pipe_name = pipeline[1]
        flow_rate = int(pipeline[4][pipeline[4].find("=")+1:pipeline[4].find(";")])
        other_pipes = [pipeline[i].strip(",") for i in range(9, len(pipeline))]
        
        valves[pipe_name] = (flow_rate, other_pipes, False)

        pipeline = fp.readline()

    tunnel = Tunnel(valves)
    print(most_pressure_releasable(tunnel, "AA"))

    fp.close()