from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

 # Initialize frontier with the root node
# Apply objective test
# si el nodo raíz es el objetivo, devuelve la solución
        if grid.objective_test(root.state):
            return Solution(root, reached)
# si no, agrega el nodo raíz a la frontera
        cola=QueueFrontier()
        nodo = root
        cola.add(nodo)

        while True:    
            if cola.is_empty():
                return NoSolution(reached)
            nodo = cola.remove()

            for i in grid.actions(nodo.state):
                sucesor=grid.result(nodo.state, i)
                if sucesor in reached:
                    continue
                else:
                    nodo1 = Node(i, state=sucesor, cost=grid.individual_cost(nodo.state, i)+nodo.cost, parent=nodo, action=i)
                    if grid.objective_test(sucesor):
                        return Solution(nodo1, reached)
                    reached[sucesor] = True
                    cola.add(nodo1)
                    
        return NoSolution(reached)
