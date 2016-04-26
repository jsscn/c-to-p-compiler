from AbstractSyntaxTree import *
from SymbolTable import *

class ASTSymbolTableFiller:
    def __init__(self, ast:AbstractSyntaxTree, table:SymbolTable):
        self.ast = ast
        self.table = table

    def fill(self, node=None): # call without arguments initially
        if node is None:
            node = self.ast.root

        openedScope = False
        if isinstance(node, (ASTStatementsNode, ASTFunctionDeclarationNode, ASTVariableDeclarationNode)):
            if isinstance(node, (ASTFunctionDeclarationNode)):
                if self.table.retrieveSymbol(node.identifier) is not None:
                    raise Excpetion("'" + node.identifier + "' has a previous declaration")
                self.table.insertSymbol(node.identifier, "function")
            openedScope = True
            self.table.openScope()

        if isinstance(node, ASTParameterNode):
            self.table.insertSymbol(node.identifier, node.type)

        for child in node.getChildren():
            self.fill(child)

        if openedScope:
            self.table.closeScope()