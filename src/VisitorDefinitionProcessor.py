from antlr4 import *
from AbstractSyntaxTree import *
from VisitorSymbolTable import *

class VisitorDefinitionProcessor(VisitorSymbolTable):

    def visitBreakNode(self, node):
        breakFrom = node
        while not isinstance(breakFrom, (ASTForNode, ASTWhileNode)) and breakFrom is not None:
            breakFrom = breakFrom.parent

        if breakFrom is None:
            self.addError("'break' statement not in loop statement", node)

        node.breakFrom = breakFrom

    def visitContinueNode(self, node):
        continueTo = node
        while not isinstance(continueTo, (ASTForNode, ASTWhileNode)) and continueTo is not None:
            continueTo = continueTo.parent

        if continueTo is None:
            self.addError("'continue' statement not in loop statement", node)

        node.continueTo = continueTo

    # int a[myFun(5)] = {1, 2+"a", 3}
    # put variables and parameters into the currently open scope, but not parameters of a function declaration
    def visitDeclaratorInitializerNode(self, node):
        arrayLength = []
        for child in reversed(node.children):
            if isinstance(child, ASTIntegerLiteralNode):
                arrayLength.append(child)
        i = 0
        for j in range(len(node.indirections)):
            if node.indirections[j][0]:
                if i >= len(arrayLength):
                    # raise Exception("not enough array length nodes")
                    break

                node.indirections[j] = (arrayLength[i].value, node.indirections[j][1])
                i += 1


        if type(node.parent.parent) is not ASTFunctionDeclarationNode:
            if node.parent.basetype is None:
                node.parent.basetype = "int"
                # warning
                # TODO: test this
                self.addError("type specifier missing, defaults to 'int'", node)
            result = self.insertSymbol(node, isFunction=False)
            if result == False:
                return


        self.visitChildren(node)


    # insert function declaration into symbol table
    def visitFunctionDeclarationNode(self, node):
        result = self.insertSymbol(node, isFunction=True)
        if result == False:
            return

        self.visitChildren(node)


    # insert function definition into symbol table
    def visitFunctionDefinitionNode(self, node):
        result = self.insertSymbol(node, isFunction=True)
        if result == False:
            return
        self.table.openScope(True, node.identifier)
        self.visitChildren(node)
        self.table.closeScope()


    def visitParameterNode(self, node):
        # in a function definition, all parameters need to have identifiers
        parametersCount = len(node.parent.children)

        if node.basetype == "void":
            if node.identifier is None and parametersCount > 1:
                self.addError("‘void’ must be the only parameter", node)
                return

            elif node.identifier is not None and node.getType().nrIndirections() == 0:
                self.addError("parameter '{0}' has incomplete type".format(node.identifier), node)
                return

        elif node.identifier is None and isinstance(node.parent.parent, ASTFunctionDefinitionNode):
            self.addError("parameter name omitted", node)
            return

        elif node.basetype is None:
            node.basetype = "int"
            # warning
            # TODO: test this
            self.addError("type specifier missing, defaults to 'int'", node)

        if type(node.parent.parent) is not ASTFunctionDeclarationNode:
            result = self.insertSymbol(node, isFunction=False)
            if result == False:
                return

        self.visitChildren(node)
