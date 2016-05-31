import unittest
import logging

# insert the parent directory into this path to get antlr files
import sys
sys.path.insert(0, '..')

from antlr4_generated.SmallCLexer import SmallCLexer
from antlr4_generated.SmallCParser import SmallCParser

from AbstractSyntaxTree import *
from Listener import *
from CompilerErrorHandler import *
from SymbolTable import *
from VisitorDefinitionProcessor import *
from VisitorDeclarationProcessor import *
from VisitorTypeChecker import *
from VisitorCodeGenerator import *

import copy
# import re to remove all whitespace from strings
import re

# set this to True to overwrite ALL test .txt files with output from c2p.py
set = False

class ASTTest():
    def setUp(self):
        self.errorHandler = None

    def parseFile(self, filename):
        input_file = FileStream(filename)
        lexer = SmallCLexer(input_file)
        stream = CommonTokenStream(lexer)
        parser = SmallCParser(stream)
        programContext = parser.program()

        walker = ParseTreeWalker()
        abstractSyntaxTree = AbstractSyntaxTree();
        self.errorHandler = CompilerErrorHandler(filename)
        listener = Listener(abstractSyntaxTree)
        walker.walk(listener, programContext)

        symbolTable = SymbolTable()
        functionFiller = VisitorDefinitionProcessor(symbolTable, self.errorHandler)
        functionFiller.visitProgramNode(abstractSyntaxTree.root)
        symbolTable.traverseOn()
        symbolTable.resetToRoot()
        tableFiller = VisitorDeclarationProcessor(symbolTable, self.errorHandler)
        tableFiller.visitProgramNode(abstractSyntaxTree.root)

        typeCheck = VisitorTypeChecker(self.errorHandler)
        typeCheck.visitProgramNode(abstractSyntaxTree.root)

    def generateErrorsAndCompare(self, filename):
        self.parseFile(filename + ".c")
        self.assertTrue(self.errorHandler.errorCount() > 0)

        # if there is error output generated, compare with txt file
        try:
            with open(filename + ".txt", 'r') as myfile:
                correctOutput = myfile.read()
        except:
            with open(filename + ".txt", 'w') as myfile:
                correctOutput = "blabla"

        errorMessage = self.errorHandler.errorsToString()
        errorMessageWithWhitespace = copy.copy(errorMessage)

        # remove all whitespace
        errorMessage  = re.sub('[ \t\n\r]', '', errorMessage)
        correctOutput = re.sub('[ \t\n\r]', '', correctOutput)

        expectedOutputFound = errorMessage.find(correctOutput) != -1

        if set and not expectedOutputFound:
            f = open(filename + ".txt", "w")
            f.write(errorMessageWithWhitespace)
            f.close()

        # if not expectedOutputFound:
        #     log = logging.getLogger("ASTTest")
        #     log.debug(__name__ + ": expected:\n" + correctOutput + "\ngot:\n" + errorMessage)

        self.assertTrue(expectedOutputFound)
        self.errorHandler = None

    def generateNoError(self, filename):
        self.parseFile(filename)

        self.assertTrue(self.errorHandler.errorCount() == 0)

class UnaryOperatorsTypeTests(ASTTest, unittest.TestCase):
    # unary operators: ++, --, *, &, !, [], can be prefix or postfix
    # unary logic operator: ! only works with type int
    def testUnaryOperatorTypes1(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/1")

    def testUnaryOperatorTypes2(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/2")

    def testUnaryOperatorTypes3(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/3")

    def testUnaryOperatorTypes4(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/4")

    def testUnaryOperatorTypes5(self):
        self.generateNoError("testfiles/unary-operators/5.c")

    def testUnaryOperatorTypes6(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/6")

    def testUnaryOperatorTypes7(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/7")

    def testUnaryOperatorTypes8(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/8")

    def testUnaryOperatorTypes9(self):
        self.generateNoError("testfiles/unary-operators/9.c")

    def testUnaryOperatorTypes10(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/10")

    def testUnaryOperatorTypes11(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/11")

    def testUnaryOperatorTypes12(self):
        self.generateErrorsAndCompare("testfiles/unary-operators/12")

    def testUnaryOperatorTypes13(self):
        self.generateNoError("testfiles/unary-operators/13.c")

    def testUnaryOperatorTypes14(self):
        self.generateNoError("testfiles/unary-operators/14.c")


class BinaryOperatorsTypeTests(ASTTest, unittest.TestCase):

    def testAllBinaryOperatorTypesLiteralsCorrect(self):
        self.generateNoError("testfiles/binary-operators/correct-literals.c")

    def testBinaryOperatorTypes1(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/1")

    def testBinaryOperatorTypes2(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/2")

    def testBinaryOperatorTypes3(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/3")

    def testBinaryOperatorTypes4(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/4")

    def testBinaryOperatorTypes5(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/5")

    def testBinaryOperatorTypes6(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/6")

    def testBinaryOperatorTypes7(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/7")

    def testBinaryOperatorTypes8(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/8")

    def testBinaryOperatorTypes9(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/9")

    def testBinaryOperatorTypes10(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/10")

    def testBinaryOperatorTypes11(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/11")

    def testBinaryOperatorTypes12(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/12")

    def testBinaryOperatorTypes13(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/13")

    def testBinaryOperatorTypes14(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/14")

    def testBinaryOperatorTypes15(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/15")

    def testBinaryOperatorTypes16(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/16")

    def testBinaryOperatorTypes17(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/17")

    def testBinaryOperatorTypes18(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/18")

    def testBinaryOperatorTypes19(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/19")

    def testBinaryOperatorTypes20(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/20")

    def testBinaryOperatorTypes21(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/21")

    def testBinaryOperatorTypes22(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/22")

    def testBinaryOperatorTypes23(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/23")

    def testBinaryOperatorTypes24(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/24")

    def testBinaryOperatorTypes25(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/25")

    def testBinaryOperatorTypes26(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/26")

    def testBinaryOperatorTypes27(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/27")

    def testBinaryOperatorTypes28(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/28")

    def testBinaryOperatorTypes29(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/29")

    def testBinaryOperatorTypes30(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/30")

    def testBinaryOperatorTypes31(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/31")

    def testBinaryOperatorTypes32(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/32")

    def testBinaryOperatorTypes33(self):
        self.generateNoError("testfiles/binary-operators/33.c")

    def testBinaryOperatorTypes34(self):
        self.generateErrorsAndCompare("testfiles/binary-operators/34")


class TernaryOperatorTypeTests(ASTTest, unittest.TestCase):
    # ternary operator test: needs int as first operator and alternatives should be of same type
    # (expression with type int) ? (expression with type T) : (expression with same type T);
    def test1(self):
        self.generateErrorsAndCompare("testfiles/ternary-operator/1")

    def test2(self):
        self.generateErrorsAndCompare("testfiles/ternary-operator/2")

    def test3(self):
        self.generateNoError("testfiles/ternary-operator/3.c")

    def test3(self):
        self.generateNoError("testfiles/ternary-operator/4.c")

    def test3(self):
        self.generateErrorsAndCompare("testfiles/ternary-operator/5")

    def test6(self):
        self.generateErrorsAndCompare("testfiles/ternary-operator/6")


class FunctionCallTypeTests(ASTTest, unittest.TestCase):

    def testFunctionCallParameterType1(self):
        self.generateErrorsAndCompare("testfiles/function-calls/1")

    def testFunctionCallParameterType2(self):
        self.generateErrorsAndCompare("testfiles/function-calls/2")

    def testFunctionCallParameterType3(self):
        self.generateErrorsAndCompare("testfiles/function-calls/3")

    def testFunctionCallParameterType4(self):
        self.generateErrorsAndCompare("testfiles/function-calls/4")

    def testFunctionCallParameterType5(self):
        self.generateErrorsAndCompare("testfiles/function-calls/5")

    def testFunctionCallParameterType6(self):
        self.generateErrorsAndCompare("testfiles/function-calls/6")

    def testFunctionCallParameterType7(self):
        self.generateErrorsAndCompare("testfiles/function-calls/7")

    def testFunctionCallParameterType8(self):
        self.generateErrorsAndCompare("testfiles/function-calls/8")

    def testFunctionCallParameterTypeCorrect(self):
        self.generateNoError("testfiles/function-calls/correct.c")

    def testFunctionCallParameterType9(self):
        self.generateErrorsAndCompare("testfiles/function-calls/9")

    def testFunctionCallParameterType10(self):
        self.generateNoError("testfiles/function-calls/10.c")

    def testFunctionCallParameterType11(self):
        self.generateErrorsAndCompare("testfiles/function-calls/11")

    def testFunctionCallParameterType12(self):
        self.generateNoError("testfiles/function-calls/12.c")

    def testFunctionCallParameterType13(self):
        self.generateErrorsAndCompare("testfiles/function-calls/13")


class VariableDeclarationTests(ASTTest, unittest.TestCase):

    def testStrangeBrackets(self):
        self.generateNoError("testfiles/variable-declarations/strange-brackets.c")

    def testVariableDeclaration1(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/1")

    def testVariableDeclaration2(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/2")

    def testVariableDeclaration3(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/3")

    def testVariableDeclaration4(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/4")

    def testVariableDeclaration5(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/5")

    def testVariableDeclaration6(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/6")

    def testVariableDeclaration7(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/7")

    def testVariableDeclaration8(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/8")

    def testVariableDeclaration9(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/9")

    def testVariableDeclaration10(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/10")

    def testVariableDeclarations11(self):
        self.generateNoError("testfiles/variable-declarations/11.c")

    def testVariableDeclaration12(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/12")

    def testVariableDeclarations13(self):
        self.generateNoError("testfiles/variable-declarations/13.c")

    def testVariableDeclaration14(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/14")

    def testVariableDeclarations15(self):
        self.generateNoError("testfiles/variable-declarations/15.c")

    def testVariableDeclaration16(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/16")

    def testVariableDeclarations17(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/17")

    def testVariableDeclaration18(self):
        self.generateNoError("testfiles/variable-declarations/18.c")

    def testVariableDeclarations19(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/19")

    def testVariableDeclarations20(self):
        self.generateErrorsAndCompare("testfiles/variable-declarations/20")


class FunctionDeclarationTests(ASTTest, unittest.TestCase):

    def testFunctionDeclaration1(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/1")

    def testFunctionDeclaration2(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/2")

    def testFunctionDeclaration3(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/3")

    def testFunctionDeclaration4(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/4")

    def testFunctionDeclaration5(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/5")

    def testFunctionDeclaration6(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/6")

    def testFunctionDeclaration7(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/7")

    def testFunctionDeclaration8(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/8")

    def testFunctionDeclaration9(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/9")

    def testFunctionDeclaration10(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/10")

    def testFunctionDeclaration11(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/11")

    def testFunctionDeclaration12(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/12")

    def testFunctionDeclaration13(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/13")

    def testFunctionDeclaration14(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/14")

    def testFunctionDeclaration15(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/15")

    def testFunctionDeclaration16(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/16")

    def testFunctionDeclaration17(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/17")

    def testFunctionDeclaration18(self):
        self.generateErrorsAndCompare("testfiles/function-declarations/18")


class ConstTests(ASTTest, unittest.TestCase):
    def testConst1(self):
        self.generateNoError("testfiles/const/1.c")

    def testConst2(self):
        self.generateErrorsAndCompare("testfiles/const/2")

    def testConst3(self):
        self.generateErrorsAndCompare("testfiles/const/3")

    def testConst4(self):
        self.generateErrorsAndCompare("testfiles/const/4")

    def testConst5(self):
        self.generateErrorsAndCompare("testfiles/const/5")


class SymbolTableTests(unittest.TestCase):
    def testInsertionAndRetrieval(self):
        table = SymbolTable()
        inttype = TypeInfo(rvalue=False, basetype="int")
        floattype = TypeInfo(rvalue=False, basetype="float")
        chartype = TypeInfo(rvalue=False, basetype="char")
        a = ASTVariableNode("a")
        a.typeInfo = inttype

        b = ASTVariableNode("b")
        b.typeInfo = floattype

        c = ASTVariableNode("c")
        c.typeInfo = chartype

        d = ASTVariableNode("d")
        d.typeInfo = floattype

        b_bis = ASTVariableNode("b")
        b_bis.typeInfo = inttype

        # d_bis = ASTVariableNode("d")
        # d_bis.type = floattype

        table.insertVariableSymbol(a)
        table.insertVariableSymbol(b)
        table.openScope()
        table.insertVariableSymbol(c)
        self.assertTrue(table.retrieveSymbol("a", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("b", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("c", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("d", requireSeen=False) is None)
        table.closeScope()
        table.openScope()
        table.insertVariableSymbol(d)
        table.insertVariableSymbol(b_bis)
        self.assertTrue(table.retrieveSymbol("a", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("b", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("c", requireSeen=False) is None)
        self.assertTrue(table.retrieveSymbol("d", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("b", requireSeen=False).typeInfo.basetype == "int")

        table.closeScope()

        self.assertTrue(table.retrieveSymbol("b", requireSeen=False).typeInfo.basetype == "float")
        self.assertTrue(table.retrieveSymbol("a", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("b", requireSeen=False) is not None)
        self.assertTrue(table.retrieveSymbol("c", requireSeen=False) is None)
        self.assertTrue(table.retrieveSymbol("d", requireSeen=False) is None)


class MiscellaneousTests(ASTTest, unittest.TestCase):

    # expressions.c has many combinations of binary operators
    def testExpressions(self):
        self.generateNoError("testfiles/expressions.c")

    # tests different usages of if, else, while, do while, if without else
    def testFlowControl(self):
        self.generateNoError("testfiles/flow_control.c")

    # many scopes and many variables and some more complex initializers
    def testVariables(self):
        self.generateNoError("testfiles/variables.c")

    # functions, forward declarations, weird parameters to functions and printf
    def testFunctions(self):
        self.generateNoError("testfiles/functions.c")

    # a file with some includes, functions, expressions and flow control
    def testHelloWorld(self):
        self.generateNoError("testfiles/hello_world.c")

class EvalutationTests(ASTTest, unittest.TestCase):

    def testTypes(self):
        self.generateNoError("testfiles/assistant-tests/1types2.c")

    def testIO(self):
        self.generateNoError("testfiles/assistant-tests/2io1.c")

    def testExpressions(self):
        self.generateNoError("testfiles/assistant-tests/3expressions3.c")

    def testFunction(self):
        self.generateNoError("testfiles/assistant-tests/7function2.c")

    def testArrays(self):
        self.generateNoError("testfiles/assistant-tests/8arrays2.c")

def testAll():
    unittest.main()

if __name__=="__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("ASTTest").setLevel(logging.DEBUG)
    testAll()
