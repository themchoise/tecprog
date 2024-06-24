import ast
import graphviz


class FlowchartGenerator(ast.NodeVisitor):
    def __init__(self):
        self.graph = graphviz.Digraph(format='png')
        self.counter = 0
        self.previous_node = None
        self.current_node = None

    def new_node(self, label, shape='box'):
        node_name = f'node{self.counter}'
        self.graph.node(node_name, label=label, shape=shape)
        self.counter += 1
        return node_name

    def add_edge(self, from_node, to_node):
        self.graph.edge(from_node, to_node)

    def visit_FunctionDef(self, node):
        func_node = self.new_node(f'Function: {node.name}')
        if self.previous_node:
            self.add_edge(self.previous_node, func_node)
        self.previous_node = func_node
        self.generic_visit(node)

    def visit_If(self, node):
        if_node = self.new_node('If', shape='diamond')
        self.add_edge(self.previous_node, if_node)
        self.previous_node = if_node
        self.visit(node.test)

        self.previous_node = if_node
        for stmt in node.body:
            self.visit(stmt)

        if node.orelse:
            else_node = self.new_node('Else', shape='diamond')
            self.add_edge(if_node, else_node)
            self.previous_node = else_node
            for stmt in node.orelse:
                self.visit(stmt)

        self.previous_node = if_node

    def visit_For(self, node):
        for_node = self.new_node('For', shape='diamond')
        self.add_edge(self.previous_node, for_node)
        self.previous_node = for_node
        self.generic_visit(node)

    def visit_While(self, node):
        while_node = self.new_node('While', shape='diamond')
        self.add_edge(self.previous_node, while_node)
        self.previous_node = while_node
        self.generic_visit(node)

    def visit_Assign(self, node):
        assign_node = self.new_node('Assign', shape='box')
        self.add_edge(self.previous_node, assign_node)
        self.previous_node = assign_node
        self.generic_visit(node)

    def visit_Expr(self, node):
        expr_node = self.new_node('Expr', shape='box')
        self.add_edge(self.previous_node, expr_node)
        self.previous_node = expr_node
        self.generic_visit(node)

    def generate(self, code):
        tree = ast.parse(code)
        self.visit(tree)
        return self.graph


if __name__ == "__main__":
    with open("./ejercicios/ej27.py", "r") as source_file:
        code = source_file.read()

    generator = FlowchartGenerator()
    graph = generator.gene rate(code)
    graph.render("flowchart")
