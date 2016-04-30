# -*- coding: utf-8 -*-
from yacc import yacc, lisp_str
import cmd

"""
This file has been edited for PLProject6 by Nich Osborn on April 29, 2016.
Changes begin on Line 41.
"""

class MiniLisp(cmd.Cmd):     # See https://docs.python.org/2/library/cmd.html
    """
    MiniLisp evalúa expresiones sencillas con sabor a lisp,
    más información en http://www.juanjoconti.com.ar
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "ml> "
        self.intro  = "Welcome to MiniLisp!"

    def do_exit(self, args):
        """Exits from the console"""
        return -1

    def do_EOF(self, args):
        """Exit on system end of file character"""
        print "Good bye!"
        return self.do_exit(args)

    def do_help(self, args):
        print self.__doc__

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
           In that case we execute the line as Python code.
        """
        print "\nParsing input with YACC:"
        result = yacc.parse(line)
        # This result is the Abstract Syntax Tree.
        print "The result is: ", result

        # Imports lis.py methods in the same folder, then passes the result for evaluation.
        import lis
        print ("\nEvaluating result with Lis.py:")
        print lis.eval(result)


if __name__ == '__main__':
        ml = MiniLisp()
        ml.cmdloop()     # See https://docs.python.org/2/library/cmd.html
