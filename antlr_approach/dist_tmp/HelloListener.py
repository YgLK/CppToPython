# Generated from Hello.g4 by ANTLR 4.7.2
import autopep8
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser


# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):
    out_path = "out.py"

    def __init__(self, out_path="out.py"):

        self.out_path = out_path

    output = ""
    indent = 0
    tab = "\t"

    def getIndent(self):
        return self.indent * self.tab

    def addNewLine(self):
        self.output += '\n'

    # Enter a parse tree produced by HelloParser#program.
    def enterProgram(self, ctx: HelloParser.ProgramContext):
        pass

    # Exit a parse tree produced by HelloParser#program.
    def exitProgram(self, ctx: HelloParser.ProgramContext):
        # compilation_theory.antlr_approach.main.CppToPython.output_string = self.output
        self.output = autopep8.fix_code(self.output)
        with open(f'{self.out_path}', 'w') as file:
            file.write(self.output)
        pass

    # Enter a parse tree produced by HelloParser#block.
    def enterBlock(self, ctx: HelloParser.BlockContext):
        pass

    # Exit a parse tree produced by HelloParser#block.
    def exitBlock(self, ctx: HelloParser.BlockContext):
        pass

    # Enter a parse tree produced by HelloParser#block_part.
    def enterBlock_part(self, ctx: HelloParser.Block_partContext):
        pass

    # Exit a parse tree produced by HelloParser#block_part.
    def exitBlock_part(self, ctx: HelloParser.Block_partContext):
        pass

    # Enter a parse tree produced by HelloParser#main_func.
    def enterMain_func(self, ctx: HelloParser.Main_funcContext):
        self.output += "if __name__ == '__main__':\n"
        self.indent += 1

    # Exit a parse tree produced by HelloParser#main_func.
    def exitMain_func(self, ctx: HelloParser.Main_funcContext):
        self.indent -= 1
        pass

    # Enter a parse tree produced by HelloParser#using_namespace_std.
    def enterUsing_namespace_std(self, ctx: HelloParser.Using_namespace_stdContext):
        pass

    # Exit a parse tree produced by HelloParser#using_namespace_std.
    def exitUsing_namespace_std(self, ctx: HelloParser.Using_namespace_stdContext):
        pass

    # Enter a parse tree produced by HelloParser#class_object.
    def enterClass_object(self, ctx: HelloParser.Class_objectContext):
        self.output += f'class {ctx.VARNAME()}:'
        self.addNewLine()
        self.indent += 1

        pass

    # Exit a parse tree produced by HelloParser#class_object.
    def exitClass_object(self, ctx: HelloParser.Class_objectContext):
        self.indent -= 1
        self.addNewLine()
        self.addNewLine()
        pass

    # Enter a parse tree produced by HelloParser#class_variable.
    def enterClass_variable(self, ctx: HelloParser.Class_variableContext):

        pass

    # Exit a parse tree produced by HelloParser#class_variable.
    def exitClass_variable(self, ctx: HelloParser.Class_variableContext):

        pass

    # Enter a parse tree produced by HelloParser#class_functions.
    def enterClass_functions(self, ctx: HelloParser.Class_functionsContext):

        pass

    # Exit a parse tree produced by HelloParser#class_functions.
    def exitClass_functions(self, ctx: HelloParser.Class_functionsContext):

        self.addNewLine()
        pass

    # Enter a parse tree produced by HelloParser#function.
    def enterFunction(self, ctx: HelloParser.FunctionContext):

        self.output += f'{self.getIndent()}def '
        if isinstance(ctx.parentCtx, HelloParser.Class_functionsContext):
            if ctx.parentCtx.access_modifier() is not None:
                self.output += f'{self.enterAccess_modifier(ctx.parentCtx.access_modifier())}'
            self.output += f'{ctx.VARNAME()}('
            self.output += "self"
        else:
            self.output += f'{ctx.VARNAME()}('
        if ctx.parameters() is not None:
            self.output += f'{ctx.parameters()}):'
        else:
            self.output += f'):'

        self.indent += 1
        self.addNewLine()

    # Exit a parse tree produced by HelloParser#function.
    def exitFunction(self, ctx: HelloParser.FunctionContext):
        self.indent -= 1
        self.addNewLine()
        self.addNewLine()
        pass

    # Enter a parse tree produced by HelloParser#parameters.
    def enterParameters(self, ctx: HelloParser.ParametersContext):
        pass

    # Exit a parse tree produced by HelloParser#parameters.
    def exitParameters(self, ctx: HelloParser.ParametersContext):
        pass

    # Enter a parse tree produced by HelloParser#access_modifier.
    def enterAccess_modifier(self, ctx: HelloParser.Access_modifierContext):
        if ctx.PRIVATE() is not None:
            return "__"
        if ctx.PUBLIC() is not None:
            return ""
        if ctx.PROTECTED() is not None:
            return "_"

    # Exit a parse tree produced by HelloParser#access_modifier.
    def exitAccess_modifier(self, ctx: HelloParser.Access_modifierContext):
        pass

    # Enter a parse tree produced by HelloParser#statement.
    def enterStatement(self, ctx: HelloParser.StatementContext):
        if ctx.VARNAME() is not None and ctx.EQUAL() is not None and ctx.calculation() is not None:
            self.output += f'{self.getIndent()}{ctx.VARNAME()} = {self.enterCalculation(ctx.calculation())}'
            self.addNewLine()
            pass

    # Exit a parse tree produced by HelloParser#statement.
    def exitStatement(self, ctx: HelloParser.StatementContext):
        pass

    # Enter a parse tree produced by HelloParser#assign_var.
    def enterAssign_var(self, ctx: HelloParser.Assign_varContext):
        self.output += f'{self.getIndent()}{ctx.VARNAME(0)} = '
        if ctx.var_value() is not None:
            self.output += self.enterVar_value(ctx.var_value())
        # --------------------
        if ctx.PLUS() is not None:
            self.output += " + "
        # --------------------
        if ctx.calculation() is not None:
            self.output += self.enterCalculation(ctx.calculation())
        if ctx.VARNAME(1) is not None:
            self.output += str(ctx.VARNAME(1))

        pass

    # Exit a parse tree produced by HelloParser#assign_var.
    def exitAssign_var(self, ctx: HelloParser.Assign_varContext):
        self.addNewLine()
        pass

    def enterFor_statement(self, ctx: HelloParser.For_statementContext):
        self.output += f'{self.getIndent()}{ctx.VARNAME(0)} = {ctx.INTVAR(0)}'
        self.addNewLine()
        self.output += f'{self.getIndent()}while {ctx.VARNAME(1)} {self.enterComparator(ctx.comparator())} {ctx.INTVAR(1)}:'
        self.addNewLine()
        self.indent += 1

    # Exit a parse tree produced by HelloParser#for_statement.
    def exitFor_statement(self, ctx: HelloParser.For_statementContext):
        self.output += f'{self.getIndent()}{ctx.VARNAME(2)}{self.enterMath_operator(ctx.math_operator())}={ctx.INTVAR(2)}'
        self.addNewLine()
        self.indent -= 1
        pass

    # Enter a parse tree produced by HelloParser#while_statement.
    def enterWhile_statement(self, ctx: HelloParser.While_statementContext):
        self.output += f'{self.getIndent()}while {self.enterCondition(ctx.condition())}:\n'
        self.indent += 1

    # Exit a parse tree produced by HelloParser#while_statement.
    def exitWhile_statement(self, ctx: HelloParser.While_statementContext):
        self.indent -= 1

    # Enter a parse tree produced by HelloParser#if_statement.
    def enterIf_statement(self, ctx: HelloParser.If_statementContext):
        self.output += f'{self.getIndent()}if {self.enterCondition(ctx.condition())}:\n'
        self.indent += 1

    # Exit a parse tree produced by HelloParser#if_statement.
    def exitIf_statement(self, ctx: HelloParser.If_statementContext):
        self.indent -= 1
        pass

    # Enter a parse tree produced by HelloParser#else_block.
    def enterElse_block(self, ctx: HelloParser.Else_blockContext):
        self.indent -= 1
        self.output += f'{self.getIndent()}else:\n'
        self.indent += 1

    # Exit a parse tree produced by HelloParser#else_block.
    def exitElse_block(self, ctx: HelloParser.Else_blockContext):

        pass

    # Enter a parse tree produced by HelloParser#func_block.
    def enterFunc_block(self, ctx: HelloParser.Func_blockContext):

        pass

    # Exit a parse tree produced by HelloParser#func_block.
    def exitFunc_block(self, ctx: HelloParser.Func_blockContext):
        pass

    # Enter a parse tree produced by HelloParser#return_statement.
    def enterReturn_statement(self, ctx: HelloParser.Return_statementContext):

        if isinstance(ctx.parentCtx.parentCtx, HelloParser.Main_funcContext) is not True:
            self.output += self.getIndent() + 'return ' + ctx.getText().removeprefix('return').removesuffix(';')

        pass

    # Exit a parse tree produced by HelloParser#return_statement.
    def exitReturn_statement(self, ctx: HelloParser.Return_statementContext):
        self.addNewLine()

        pass

    # Enter a parse tree produced by HelloParser#condition.
    def enterCondition(self, ctx: HelloParser.ConditionContext):

        return ctx.getText()

    # Exit a parse tree produced by HelloParser#condition.
    def exitCondition(self, ctx: HelloParser.ConditionContext):
        pass

    # Enter a parse tree produced by HelloParser#variable_def.
    def enterVariable_def(self, ctx: HelloParser.Variable_defContext):

        pass

    # Exit a parse tree produced by HelloParser#variable_def.
    def exitVariable_def(self, ctx: HelloParser.Variable_defContext):
        pass

    # Enter a parse tree produced by HelloParser#declare_var.
    def enterDeclare_var(self, ctx: HelloParser.Declare_varContext):
        self.output += f'{self.getIndent()}{ctx.VARNAME()} = {self.enterData_type(ctx.data_type())}'
        self.addNewLine()
        pass

    # Exit a parse tree produced by HelloParser#declare_var.
    def exitDeclare_var(self, ctx: HelloParser.Declare_varContext):
        pass

    # Enter a parse tree produced by HelloParser#declare_assign_var.
    def enterDeclare_assign_var(self, ctx: HelloParser.Declare_assign_varContext):
        self.output += f'{self.getIndent()}'

        pa_parent = ctx.parentCtx.parentCtx
        if isinstance(pa_parent, HelloParser.Class_variableContext) and pa_parent.access_modifier() is not None:
            self.output += f'{self.enterAccess_modifier(pa_parent.access_modifier())}'

        if ctx.var_value() is not None:
            self.output += f'{ctx.VARNAME(0)} = {self.enterVar_value(ctx.var_value())}'
        if ctx.calculation() is not None:
            self.output += f'{ctx.VARNAME(0)} = {self.enterCalculation(ctx.calculation())}'
        if ctx.VARNAME(1) is not None and ctx.VARNAME(2) is not None:
            self.output += f'{ctx.VARNAME(0)} = {ctx.VARNAME(1)}{self.enterMath_operator(ctx.math_operator())}{ctx.VARNAME(2)}'

    # Exit a parse tree produced by HelloParser#declare_assign_var.
    def exitDeclare_assign_var(self, ctx: HelloParser.Declare_assign_varContext):
        self.addNewLine()
        pass

    # Enter a parse tree produced by HelloParser#print_out.
    def enterPrint_out(self, ctx: HelloParser.Print_outContext):
        pass

    # Exit a parse tree produced by HelloParser#print_out.
    def exitPrint_out(self, ctx: HelloParser.Print_outContext):
        pass

    # Enter a parse tree produced by HelloParser#cout_expression_string.
    def enterCout_expression_string(self, ctx: HelloParser.Cout_expression_stringContext):

        pass

    # Exit a parse tree produced by HelloParser#cout_expression_string.
    def exitCout_expression_string(self, ctx: HelloParser.Cout_expression_stringContext):

        pass

    # --------------------
    # Enter a parse tree produced by HelloParser#func_call.
    def enterFunc_call(self, ctx:HelloParser.Func_callContext):
        self.output += f'{self.getIndent()}{ctx.VARNAME()}()\n'
        pass

    # Exit a parse tree produced by HelloParser#func_call.
    def exitFunc_call(self, ctx:HelloParser.Func_callContext):
        pass


    # Enter a parse tree produced by HelloParser#func_call_parameters.
    def enterFunc_call_parameters(self, ctx:HelloParser.Func_call_parametersContext):
        pass

    # Exit a parse tree produced by HelloParser#func_call_parameters.
    def exitFunc_call_parameters(self, ctx:HelloParser.Func_call_parametersContext):
        pass

    # --------------------

    # Enter a parse tree produced by HelloParser#cout_expression.
    def enterCout_expression(self, ctx: HelloParser.Cout_expressionContext):
        self.output += f'{self.getIndent()}print({self.enterPrintable(ctx.printable())})\n'
        pass

    # Exit a parse tree produced by HelloParser#cout_expression.
    def exitCout_expression(self, ctx: HelloParser.Cout_expressionContext):
        pass

    # Enter a parse tree produced by HelloParser#printable.
    def enterPrintable(self, ctx: HelloParser.PrintableContext):

        if (ctx.getText() == "endl"):
            return "\"\\n\""
        return ctx.getText()

        pass

    # Exit a parse tree produced by HelloParser#printable.
    def exitPrintable(self, ctx: HelloParser.PrintableContext):
        pass

    # Enter a parse tree produced by HelloParser#calculation.
    def enterCalculation(self, ctx: HelloParser.CalculationContext):
        return ctx.getText()

    # Exit a parse tree produced by HelloParser#calculation.
    def exitCalculation(self, ctx: HelloParser.CalculationContext):
        pass

    # Enter a parse tree produced by HelloParser#include.
    def enterInclude(self, ctx: HelloParser.IncludeContext):
        pass

    # Exit a parse tree produced by HelloParser#include.
    def exitInclude(self, ctx: HelloParser.IncludeContext):
        pass

    # Enter a parse tree produced by HelloParser#cin_in.
    def enterCin_in(self, ctx: HelloParser.Cin_inContext):

        self.output += f'{self.indent * self.tab}{ctx.VARNAME()} = input()\n'
        pass

    # Exit a parse tree produced by HelloParser#cin_in.
    def exitCin_in(self, ctx: HelloParser.Cin_inContext):
        pass

    # Enter a parse tree produced by HelloParser#number.
    def enterNumber(self, ctx: HelloParser.NumberContext):
        return ctx.getText()
        pass

    # Exit a parse tree produced by HelloParser#number.
    def exitNumber(self, ctx: HelloParser.NumberContext):
        pass

    # Enter a parse tree produced by HelloParser#return_type.
    def enterReturn_type(self, ctx: HelloParser.Return_typeContext):
        pass

    # Exit a parse tree produced by HelloParser#return_type.
    def exitReturn_type(self, ctx: HelloParser.Return_typeContext):
        pass

    # Enter a parse tree produced by HelloParser#data_type.
    def enterData_type(self, ctx: HelloParser.Data_typeContext):
        if ctx.INT() is not None:
            return 0
        if ctx.CHAR() or ctx.STRING() is not None:
            return "\"\""
        if ctx.BOOL() is not None:
            return False

    # Exit a parse tree produced by HelloParser#data_type.
    def exitData_type(self, ctx: HelloParser.Data_typeContext):
        pass

    # Enter a parse tree produced by HelloParser#math_operator.
    def enterMath_operator(self, ctx: HelloParser.Math_operatorContext):
        return ctx.getText()

    # Exit a parse tree produced by HelloParser#math_operator.
    def exitMath_operator(self, ctx: HelloParser.Math_operatorContext):
        pass

    # Enter a parse tree produced by HelloParser#comparator.
    def enterComparator(self, ctx: HelloParser.ComparatorContext):
        return ctx.getText()
        pass

    # Exit a parse tree produced by HelloParser#comparator.
    def exitComparator(self, ctx: HelloParser.ComparatorContext):
        pass

    # Enter a parse tree produced by HelloParser#var_value.
    def enterVar_value(self, ctx: HelloParser.Var_valueContext):
        if ctx.bool_value() is not None:
            return self.enterBool_value(ctx.bool_value())
        return ctx.getText()
        pass

    # Exit a parse tree produced by HelloParser#var_value.
    def exitVar_value(self, ctx: HelloParser.Var_valueContext):
        pass

    # Enter a parse tree produced by HelloParser#bool_value.
    def enterBool_value(self, ctx: HelloParser.Bool_valueContext):

        res = True if ctx.TRUE() is not None else False
        return res

    # Exit a parse tree produced by HelloParser#bool_value.
    def exitBool_value(self, ctx: HelloParser.Bool_valueContext):
        pass
