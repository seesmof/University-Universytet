// Generated from D:/University-Universytet/42SI Stvorennja IDE/3/src/src/Main.g4 by ANTLR 4.13.2
package gen;
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MainParser}.
 */
public interface MainListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MainParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(MainParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(MainParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(MainParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(MainParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void enterForStatement(MainParser.ForStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#forStatement}.
	 * @param ctx the parse tree
	 */
	void exitForStatement(MainParser.ForStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileStatement(MainParser.WhileStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#whileStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileStatement(MainParser.WhileStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#printStatement}.
	 * @param ctx the parse tree
	 */
	void enterPrintStatement(MainParser.PrintStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#printStatement}.
	 * @param ctx the parse tree
	 */
	void exitPrintStatement(MainParser.PrintStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#letBinding}.
	 * @param ctx the parse tree
	 */
	void enterLetBinding(MainParser.LetBindingContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#letBinding}.
	 * @param ctx the parse tree
	 */
	void exitLetBinding(MainParser.LetBindingContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#structDecl}.
	 * @param ctx the parse tree
	 */
	void enterStructDecl(MainParser.StructDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#structDecl}.
	 * @param ctx the parse tree
	 */
	void exitStructDecl(MainParser.StructDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#structField}.
	 * @param ctx the parse tree
	 */
	void enterStructField(MainParser.StructFieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#structField}.
	 * @param ctx the parse tree
	 */
	void exitStructField(MainParser.StructFieldContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDecl(MainParser.FunctionDeclContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#functionDecl}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDecl(MainParser.FunctionDeclContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#parameters}.
	 * @param ctx the parse tree
	 */
	void enterParameters(MainParser.ParametersContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#parameters}.
	 * @param ctx the parse tree
	 */
	void exitParameters(MainParser.ParametersContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(MainParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(MainParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#block}.
	 * @param ctx the parse tree
	 */
	void enterBlock(MainParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#block}.
	 * @param ctx the parse tree
	 */
	void exitBlock(MainParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfStatement(MainParser.IfStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#ifStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfStatement(MainParser.IfStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#loopStatement}.
	 * @param ctx the parse tree
	 */
	void enterLoopStatement(MainParser.LoopStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#loopStatement}.
	 * @param ctx the parse tree
	 */
	void exitLoopStatement(MainParser.LoopStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void enterBreakStmt(MainParser.BreakStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#breakStmt}.
	 * @param ctx the parse tree
	 */
	void exitBreakStmt(MainParser.BreakStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#continueStmt}.
	 * @param ctx the parse tree
	 */
	void enterContinueStmt(MainParser.ContinueStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#continueStmt}.
	 * @param ctx the parse tree
	 */
	void exitContinueStmt(MainParser.ContinueStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#type}.
	 * @param ctx the parse tree
	 */
	void enterType(MainParser.TypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#type}.
	 * @param ctx the parse tree
	 */
	void exitType(MainParser.TypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code GroupExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterGroupExpr(MainParser.GroupExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code GroupExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitGroupExpr(MainParser.GroupExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IdExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterIdExpr(MainParser.IdExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IdExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitIdExpr(MainParser.IdExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code StringLiteral}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterStringLiteral(MainParser.StringLiteralContext ctx);
	/**
	 * Exit a parse tree produced by the {@code StringLiteral}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitStringLiteral(MainParser.StringLiteralContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BoolLiteral}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterBoolLiteral(MainParser.BoolLiteralContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BoolLiteral}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitBoolLiteral(MainParser.BoolLiteralContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CompareExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterCompareExpr(MainParser.CompareExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CompareExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitCompareExpr(MainParser.CompareExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MethodExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterMethodExpr(MainParser.MethodExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MethodExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitMethodExpr(MainParser.MethodExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code FloatLiteral}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterFloatLiteral(MainParser.FloatLiteralContext ctx);
	/**
	 * Exit a parse tree produced by the {@code FloatLiteral}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitFloatLiteral(MainParser.FloatLiteralContext ctx);
	/**
	 * Enter a parse tree produced by the {@code BinaryExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterBinaryExpr(MainParser.BinaryExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code BinaryExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitBinaryExpr(MainParser.BinaryExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CallExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterCallExpr(MainParser.CallExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CallExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitCallExpr(MainParser.CallExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IntLiteral}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterIntLiteral(MainParser.IntLiteralContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IntLiteral}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitIntLiteral(MainParser.IntLiteralContext ctx);
	/**
	 * Enter a parse tree produced by the {@code IndexExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterIndexExpr(MainParser.IndexExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code IndexExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitIndexExpr(MainParser.IndexExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#arguments}.
	 * @param ctx the parse tree
	 */
	void enterArguments(MainParser.ArgumentsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#arguments}.
	 * @param ctx the parse tree
	 */
	void exitArguments(MainParser.ArgumentsContext ctx);
}