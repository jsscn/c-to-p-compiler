# Generated from smallc.g4 by ANTLR 4.5.2
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\17")
        buf.write("M\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4")
        buf.write("\6\4*\n\4\r\4\16\4+\3\5\3\5\3\5\3\5\3\5\3\5\3\6\6\6\65")
        buf.write("\n\6\r\6\16\6\66\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\6\16H\n\16\r\16\16\16I\3\16")
        buf.write("\3\16\2\2\17\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\3\2\5\3\2c|\3\2\62;\5\2\13\f\17")
        buf.write("\17\"\"O\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\3\35\3\2\2\2\5&\3\2\2\2\7)\3\2\2\2\t-\3\2")
        buf.write("\2\2\13\64\3\2\2\2\r8\3\2\2\2\17:\3\2\2\2\21<\3\2\2\2")
        buf.write("\23>\3\2\2\2\25@\3\2\2\2\27B\3\2\2\2\31D\3\2\2\2\33G\3")
        buf.write("\2\2\2\35\36\7%\2\2\36\37\7k\2\2\37 \7p\2\2 !\7e\2\2!")
        buf.write("\"\7n\2\2\"#\7w\2\2#$\7f\2\2$%\7g\2\2%\4\3\2\2\2&\'\7")
        buf.write("\60\2\2\'\6\3\2\2\2(*\t\2\2\2)(\3\2\2\2*+\3\2\2\2+)\3")
        buf.write("\2\2\2+,\3\2\2\2,\b\3\2\2\2-.\7*\2\2./\7\60\2\2/\60\7")
        buf.write(",\2\2\60\61\7A\2\2\61\62\7+\2\2\62\n\3\2\2\2\63\65\t\3")
        buf.write("\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3")
        buf.write("\2\2\2\67\f\3\2\2\289\7.\2\29\16\3\2\2\2:;\7*\2\2;\20")
        buf.write("\3\2\2\2<=\7+\2\2=\22\3\2\2\2>?\7>\2\2?\24\3\2\2\2@A\7")
        buf.write("@\2\2A\26\3\2\2\2BC\7}\2\2C\30\3\2\2\2DE\7\177\2\2E\32")
        buf.write("\3\2\2\2FH\t\4\2\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2")
        buf.write("\2\2JK\3\2\2\2KL\b\16\2\2L\34\3\2\2\2\6\2+\66I\3\b\2\2")
        return buf.getvalue()


class smallcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    ID = 3
    STRING = 4
    NUMBER = 5
    COMMA = 6
    LBRA = 7
    RBRA = 8
    LABRA = 9
    RABRA = 10
    LCBRA = 11
    RCBRA = 12
    WS = 13

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'#include'", "'.'", "'(.*?)'", "','", "'('", "')'", "'<'", 
            "'>'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "STRING", "NUMBER", "COMMA", "LBRA", "RBRA", "LABRA", 
            "RABRA", "LCBRA", "RCBRA", "WS" ]

    ruleNames = [ "T__0", "T__1", "ID", "STRING", "NUMBER", "COMMA", "LBRA", 
                  "RBRA", "LABRA", "RABRA", "LCBRA", "RCBRA", "WS" ]

    grammarFileName = "smallc.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


