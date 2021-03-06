# Subtrees are referred to as nodes just for clarification, though the terms tree and node
# are really interchangeable

# For tree in which each node may have any number of children


class Tree:
    def __init__(self, val, children=None):
        self.val = val
        # This step is neccesary to ensure that an empty list is the
        # default value for the tree's children
        if children is None:
            self.children = []
        else:
            self.children = children

    # When a tree is printed, it prints the value stored in it
    def __str__(self):
        return str(self.val)

    # Recursively calculates the sum of the tree's value and all of its children's values
    def total(self):
        result = 0
        if len(self.children) < 1:
            result = self.val
        else:
            result += self.val
            for child in self.children:
                result += child.total()

        return result

    # Returns the number of edges the tree has
    def num_edges(self):
        result = 0
        if len(self.children) > 0:
            result += len(self.children)
            for child in self.children:
                result += child.num_edges()

        return result

    # Returns the total number of nodes under the tree
    def num_nodes(self):
        return self.num_edges() + 1

    # Adds a node to the parent tree. Will search for the first node in the parent tree
    # with the value parent and then adds a new node with value v to its children
    def add_node(self, parent, v):
        if self.val == parent:
            # Very handy print statement for clarification
            print("Adding node", v, "to node", self.val)
            self.children.append(Tree(v))
        else:
            for child in self.children:
                child.add_node(parent, v)

    # Removes a tree from the parent node.  Will search for the first node in the parent tree
    # with the value parent and then removes node with value v from its children
    def remove_node(self, parent, v):
        if self.val == parent:
            print("Removing node", v, "from node", self.val)
            for child in self.children:
                if child.val == v:
                    self.children.remove(child)
        else:
            for child in self.children:
                child.remove_node(child.val, v)

    # Searches a tree for a particular node within it
    def check_for_node(self, parent, v):
        # Print for clarification
        print("Checking", self.val, "for node", (parent, v))
        # If the tree's value matches that of the parent,
        # each of its children are checked to be the node
        if self.val == parent:
            if len(self.children) > 0:
                for child in self.children:
                    if child.val == v:
                        return True
                # If the loop completes without finding the node,
                # then we can conclude that it is not there at all
                return False
            else:
                return False
        # If the tree is not the parent, then the process is repeated for
        # each of its children (if any)
        else:
            if len(self.children) > 0:
                present = False
                for child in self.children:
                    present = child.check_for_node(parent, v)
                    if present:
                        return present
                # If none of the tree's children are the parent of the
                # target node, then we can conclude that this node is a dead-end
                return False
            else:
                return False


# Examples

a = Tree(1)

n = int(input())

for i in range(n - 1):
    u, v = map(int, input().split())
    a.add_node(u, v)

if max(a.children, key=lambda x: x.num_nodes()) == min(a.children, key=lambda x: x.num_nodes()):
    print(a.num_nodes() - a.children[0].num_nodes())
else:
    print(a.num_nodes(), a.num_edges())
