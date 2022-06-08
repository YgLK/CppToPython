# Generated from Hello.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):

    # Enter a parse tree produced by HelloParser#program.
    def enterProgram(self, ctx:HelloParser.ProgramContext):
        pass

    # Exit a parse tree produced by HelloParser#program.
    def exitProgram(self, ctx:HelloParser.ProgramContext):
        pass


    # Enter a parse tree produced by HelloParser#block.
    def enterBlock(self, ctx:HelloParser.BlockContext):
        pass

    # Exit a parse tree produced by HelloParser#block.
    def exitBlock(self, ctx:HelloParser.BlockContext):
        pass


    # Enter a parse tree produced by HelloParser#block_part.
    def enterBlock_part(self, ctx:HelloParser.Block_partContext):
        pass

    # Exit a parse tree produced by HelloParser#block_part.
    def exitBlock_part(self, ctx:HelloParser.Block_partContext):
        pass


    # Enter a parse tree produced by HelloParser#main_func.
    def enterMain_func(self, ctx:HelloParser.Main_funcContext):
        pass

    # Exit a parse tree produced by HelloParser#main_func.
    def exitMain_func(self, ctx:HelloParser.Main_funcContext):
        pass


    # Enter a parse tree produced by HelloParser#using_namespace_std.
    def enterUsing_namespace_std(self, ctx:HelloParser.Using_namespace_stdContext):
        pass

    # Exit a parse tree produced by HelloParser#using_namespace_std.
    def exitUsing_namespace_std(self, ctx:HelloParser.Using_namespace_stdContext):
        pass


    # Enter a parse tree produced by HelloParser#class_object.
    def enterClass_object(self, ctx:HelloParser.Class_objectContext):
        pass

    # Exit a parse tree produced by HelloParser#class_object.
    def exitClass_object(self, ctx:HelloParser.Class_objectContext):
        pass


    # Enter a parse tree produced by HelloParser#class_variable.
    def enterClass_variable(self, ctx:HelloParser.Class_variableContext):
        pass

    # Exit a parse tree produced by HelloParser#class_variable.
    def exitClass_variable(self, ctx:HelloParser.Class_variableContext):
        pass


    # Enter a parse tree produced by HelloParser#class_functions.
    def enterClass_functions(self, ctx:HelloParser.Class_functionsContext):
        print(ctx.getText())
        pass

    # Exit a parse tree produced by HelloParser#class_functions.
    def exitClass_functions(self, ctx:HelloParser.Class_functionsContext):
        pass


    # Enter a parse tree produced by HelloParser#function.
    def enterFunction(self, ctx:HelloParser.FunctionContext):
        print(ctx.getText())
        pass

    # Exit a parse tree produced by HelloParser#function.
    def exitFunction(self, ctx:HelloParser.FunctionContext):
        pass


    # Enter a parse tree produced by HelloParser#parameters.
    def enterParameters(self, ctx:HelloParser.ParametersContext):
        pass

    # Exit a parse tree produced by HelloParser#parameters.
    def exitParameters(self, ctx:HelloParser.ParametersContext):
        pass


    # Enter a parse tree produced by HelloParser#access_modifier.
    def enterAccess_modifier(self, ctx:HelloParser.Access_modifierContext):
        print(ctx.getText())
        pass

    # Exit a parse tree produced by HelloParser#access_modifier.
    def exitAccess_modifier(self, ctx:HelloParser.Access_modifierContext):
        pass


    # Enter a parse tree produced by HelloParser#statement.
    def enterStatement(self, ctx:HelloParser.StatementContext):
        pass

    # Exit a parse tree produced by HelloParser#statement.
    def exitStatement(self, ctx:HelloParser.StatementContext):
        pass


    # Enter a parse tree produced by HelloParser#assign_var.
    def enterAssign_var(self, ctx:HelloParser.Assign_varContext):
        pass

    # Exit a parse tree produced by HelloParser#assign_var.
    def exitAssign_var(self, ctx:HelloParser.Assign_varContext):
        pass


    # Enter a parse tree produced by HelloParser#for_statement.
    def enterFor_statement(self, ctx:HelloParser.For_statementContext):
        pass

    # Exit a parse tree produced by HelloParser#for_statement.
    def exitFor_statement(self, ctx:HelloParser.For_statementContext):
        pass


    # Enter a parse tree produced by HelloParser#while_statement.
    def enterWhile_statement(self, ctx:HelloParser.While_statementContext):
        pass

    # Exit a parse tree produced by HelloParser#while_statement.
    def exitWhile_statement(self, ctx:HelloParser.While_statementContext):
        pass


    # Enter a parse tree produced by HelloParser#if_statement.
    def enterIf_statement(self, ctx:HelloParser.If_statementContext):
        pass

    # Exit a parse tree produced by HelloParser#if_statement.
    def exitIf_statement(self, ctx:HelloParser.If_statementContext):
        pass


    # Enter a parse tree produced by HelloParser#else_block.
    def enterElse_block(self, ctx:HelloParser.Else_blockContext):
        pass

    # Exit a parse tree produced by HelloParser#else_block.
    def exitElse_block(self, ctx:HelloParser.Else_blockContext):
        pass


    # Enter a parse tree produced by HelloParser#func_block.
    def enterFunc_block(self, ctx:HelloParser.Func_blockContext):
        pass

    # Exit a parse tree produced by HelloParser#func_block.
    def exitFunc_block(self, ctx:HelloParser.Func_blockContext):
        pass


    # Enter a parse tree produced by HelloParser#return_statement.
    def enterReturn_statement(self, ctx:HelloParser.Return_statementContext):
        pass

    # Exit a parse tree produced by HelloParser#return_statement.
    def exitReturn_statement(self, ctx:HelloParser.Return_statementContext):
        pass


    # Enter a parse tree produced by HelloParser#condition.
    def enterCondition(self, ctx:HelloParser.ConditionContext):
        pass

    # Exit a parse tree produced by HelloParser#condition.
    def exitCondition(self, ctx:HelloParser.ConditionContext):
        pass


    # Enter a parse tree produced by HelloParser#variable_def.
    def enterVariable_def(self, ctx:HelloParser.Variable_defContext):
        pass

    # Exit a parse tree produced by HelloParser#variable_def.
    def exitVariable_def(self, ctx:HelloParser.Variable_defContext):
        pass


    # Enter a parse tree produced by HelloParser#declare_var.
    def enterDeclare_var(self, ctx:HelloParser.Declare_varContext):
        pass

    # Exit a parse tree produced by HelloParser#declare_var.
    def exitDeclare_var(self, ctx:HelloParser.Declare_varContext):
        pass


    # Enter a parse tree produced by HelloParser#declare_assign_var.
    def enterDeclare_assign_var(self, ctx:HelloParser.Declare_assign_varContext):
        pass

    # Exit a parse tree produced by HelloParser#declare_assign_var.
    def exitDeclare_assign_var(self, ctx:HelloParser.Declare_assign_varContext):
        pass


    # Enter a parse tree produced by HelloParser#print_out.
    def enterPrint_out(self, ctx:HelloParser.Print_outContext):
        pass

    # Exit a parse tree produced by HelloParser#print_out.
    def exitPrint_out(self, ctx:HelloParser.Print_outContext):
        pass


    # Enter a parse tree produced by HelloParser#cout_expression_string.
    def enterCout_expression_string(self, ctx:HelloParser.Cout_expression_stringContext):
        pass

    # Exit a parse tree produced by HelloParser#cout_expression_string.
    def exitCout_expression_string(self, ctx:HelloParser.Cout_expression_stringContext):
        pass


    # Enter a parse tree produced by HelloParser#cout_expression.
    def enterCout_expression(self, ctx:HelloParser.Cout_expressionContext):
        pass

    # Exit a parse tree produced by HelloParser#cout_expression.
    def exitCout_expression(self, ctx:HelloParser.Cout_expressionContext):
        pass


    # Enter a parse tree produced by HelloParser#printable.
    def enterPrintable(self, ctx:HelloParser.PrintableContext):
        pass

    # Exit a parse tree produced by HelloParser#printable.
    def exitPrintable(self, ctx:HelloParser.PrintableContext):
        pass


    # Enter a parse tree produced by HelloParser#calculation.
    def enterCalculation(self, ctx:HelloParser.CalculationContext):
        pass

    # Exit a parse tree produced by HelloParser#calculation.
    def exitCalculation(self, ctx:HelloParser.CalculationContext):
        pass


    # Enter a parse tree produced by HelloParser#include.
    def enterInclude(self, ctx:HelloParser.IncludeContext):
        pass

    # Exit a parse tree produced by HelloParser#include.
    def exitInclude(self, ctx:HelloParser.IncludeContext):
        pass


    # Enter a parse tree produced by HelloParser#cin_in.
    def enterCin_in(self, ctx:HelloParser.Cin_inContext):
        pass

    # Exit a parse tree produced by HelloParser#cin_in.
    def exitCin_in(self, ctx:HelloParser.Cin_inContext):
        pass


    # Enter a parse tree produced by HelloParser#number.
    def enterNumber(self, ctx:HelloParser.NumberContext):
        pass

    # Exit a parse tree produced by HelloParser#number.
    def exitNumber(self, ctx:HelloParser.NumberContext):
        pass


    # Enter a parse tree produced by HelloParser#return_type.
    def enterReturn_type(self, ctx:HelloParser.Return_typeContext):
        pass

    # Exit a parse tree produced by HelloParser#return_type.
    def exitReturn_type(self, ctx:HelloParser.Return_typeContext):
        pass


    # Enter a parse tree produced by HelloParser#data_type.
    def enterData_type(self, ctx:HelloParser.Data_typeContext):
        pass

    # Exit a parse tree produced by HelloParser#data_type.
    def exitData_type(self, ctx:HelloParser.Data_typeContext):
        pass


    # Enter a parse tree produced by HelloParser#math_operator.
    def enterMath_operator(self, ctx:HelloParser.Math_operatorContext):
        pass

    # Exit a parse tree produced by HelloParser#math_operator.
    def exitMath_operator(self, ctx:HelloParser.Math_operatorContext):
        pass


    # Enter a parse tree produced by HelloParser#comparator.
    def enterComparator(self, ctx:HelloParser.ComparatorContext):
        pass

    # Exit a parse tree produced by HelloParser#comparator.
    def exitComparator(self, ctx:HelloParser.ComparatorContext):
        pass


    # Enter a parse tree produced by HelloParser#var_value.
    def enterVar_value(self, ctx:HelloParser.Var_valueContext):
        # print(ctx.getText())
        pass

    # Exit a parse tree produced by HelloParser#var_value.
    def exitVar_value(self, ctx:HelloParser.Var_valueContext):
        pass


    # Enter a parse tree produced by HelloParser#bool_value.
    def enterBool_value(self, ctx:HelloParser.Bool_valueContext):
        print(ctx.getText())
        pass

    # Exit a parse tree produced by HelloParser#bool_value.
    def exitBool_value(self, ctx:HelloParser.Bool_valueContext):
        pass


