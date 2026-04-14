from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        # Initialize frontier with the root node
        expanded = {}
        reached = {}
        reached[root.state] = True

        pila = StackFrontier()
        nodo = root
        pila.add(nodo)

        while True:    
            if pila.is_empty():
                return NoSolution(expanded)
            nodo = pila.remove()

            for i in grid.actions(nodo.state):
                sucesor=grid.result(nodo.state, i)
                if sucesor in expanded:
                    continue
                else:
                    nodo1 = Node(i, state=sucesor, cost=grid.individual_cost(nodo.state, i)+nodo.cost, parent=nodo, action=i)
                    if grid.objective_test(sucesor):
                        return Solution(nodo1, expanded)
                    expanded[sucesor] = True
                    pila.add(nodo1) 

        return NoSolution(expanded)
