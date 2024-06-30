class Tree:
    def __init__(self, root_node):
        """
        Initialize a new Tree instance with a root node.
        
        :param root_node: The root node of the tree.
        """
        self.root_node = root_node

    def get_element_by_id(self, id):
        """
        Recursively searches the tree for an element with the given ID and returns its details.
        
        :param id: The ID of the element to search for.
        :return: A dictionary containing the details of the element if found, otherwise None.
        """
        def traverse(node):
            if node['id'] == id:
                return node
            for child in node.get('children', []):
                result = traverse(child)
                if result:
                    return result
            return None
        
        return traverse(self.root_node)

# Example usage
# Define your tree structure here
root_node = {
    'id': 'root',
    'tag_name': 'div',
    'text_content': '',
    'children': [
        {
            'id': 'heading',
            'tag_name': 'h1',
            'text_content': 'Title',
            'children': []
        }
    ]
}

tree = Tree(root_node)
element = tree.get_element_by_id('heading')
print(element)
