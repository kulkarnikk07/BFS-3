# BFS-3

## Problem1 Remove Invalid Parentheses(https://leetcode.com/problems/remove-invalid-parentheses/)

from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Use depth-first search (DFS) to explore possibilities
        def dfs(index: int, left_to_remove: int, right_to_remove: int, left_count: int, right_count: int, path: str):
            # Base case: if we have reached the end of the string
            if index == length:
                # Check if we no longer have any parentheses to remove and the parentheses are balanced
                if left_to_remove == 0 and right_to_remove == 0:
                    # Add the current path to the answer set
                    valid_expressions.add(path)
                return
          
            # Pruning: if there are more parentheses to remove than remaining characters
            # or more right parentheses used than left
            if length - index < left_to_remove + right_to_remove or left_count < right_count:
                return
          
            # Choose to ignore the current character if it's a parenthesis and we need to remove it
            if s[index] == '(' and left_to_remove > 0:
                dfs(index + 1, left_to_remove - 1, right_to_remove, left_count, right_count, path)
            elif s[index] == ')' and right_to_remove > 0:
                dfs(index + 1, left_to_remove, right_to_remove - 1, left_count, right_count, path)
          
            # Choose to keep the current character, updating the count of used parentheses
            dfs(index + 1, left_to_remove, right_to_remove, left_count + (s[index] == '('), right_count + (s[index] == ')'), path + s[index])
      
        # Initial preparations
        left_to_remove, right_to_remove = 0, 0
        # First pass to find out the number of unmatched '(' and ')'
        for char in s:
            if char == '(':
                left_to_remove += 1
            elif char == ')':
                # Only decrease the count of left parentheses if there's an unmatched left parenthesis
                if left_to_remove:
                    left_to_remove -= 1
                else:
                    right_to_remove += 1
      
        # A set to keep the unique valid expressions
        valid_expressions = set()
        length = len(s)
      
        # Start the DFS with the initial parameters
        dfs(0, left_to_remove, right_to_remove, 0, 0, '')
      
        # Convert the set into a list and return it
        return list(valid_expressions)
# TC = O(n), SC= O(n)

## Problem2 Clone graph (https://leetcode.com/problems/clone-graph/)

from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Dictionary to keep track of visited nodes and their clones.
        visited = defaultdict(Node)

        def clone(node: 'Node') -> 'Node':
            """
            clone is a helper function which performs a depth-first traversal
            of the graph to create a deep copy of it.

            :param node: The graph node to be cloned
            :return: The cloned copy of the input node
            """
            # Return None for a non-existent node
            if node is None:
                return None
          
            # If the node has already been visited, return the cloned node
            if node in visited:
                return visited[node]
          
            # Create a new Node clone with the value of the original node
            clone_node = Node(node.val)
          
            # Map the original node to the cloned one in visited dictionary
            visited[node] = clone_node
          
            # For every adjacent node, create a clone copy to the neighbors of the cloned node
            for neighbor in node.neighbors:
                clone_node.neighbors.append(clone(neighbor))

            return clone_node

        # Start the graph cloning process from the input node
        return clone(node)
# TC = O(N+M), SC= O(n)
