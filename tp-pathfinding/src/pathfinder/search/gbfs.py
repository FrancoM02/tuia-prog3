from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        frontera = PriorityQueueFrontier()
        nodo = root
        frontera.add(nodo, grid.heuristica_manhattan(nodo.state))

        while True:
            if frontera.is_empty():
                return NoSolution(reached)
            
            nodo = frontera.pop()
            
            if grid.objective_test(nodo.state):
                return Solution(nodo, reached)
            
            for action in grid.actions(nodo.state):
                sucesor = grid.result(nodo.state, action)
                costo_sucesor = nodo.cost + grid.individual_cost(nodo.state, action)
                
                if sucesor not in reached or costo_sucesor < reached[sucesor]:
                    nodo_sucesor = Node(action, state=sucesor, cost=costo_sucesor, parent=nodo, action=action)
                    reached[sucesor] = costo_sucesor
                    frontera.add(nodo_sucesor, grid.heuristica_manhattan(sucesor))

        return NoSolution(reached)
