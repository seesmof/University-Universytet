package gen;// Generated from D:/University-Universytet/42SI Stvorennja IDE/3/src/src/Main.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link MainParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface MainVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link MainParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(MainParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(MainParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#forStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForStatement(MainParser.ForStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#letBinding}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLetBinding(MainParser.LetBindingContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#structDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStructDecl(MainParser.StructDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#structField}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStructField(MainParser.StructFieldContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#functionDecl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionDecl(MainParser.FunctionDeclContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#parameters}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameters(MainParser.ParametersContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#parameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameter(MainParser.ParameterContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(MainParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#ifStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStatement(MainParser.IfStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#loopStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLoopStatement(MainParser.LoopStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#breakStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBreakStmt(MainParser.BreakStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#continueStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitContinueStmt(MainParser.ContinueStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType(MainParser.TypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code GroupExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitGroupExpr(MainParser.GroupExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code IdExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdExpr(MainParser.IdExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code StringLiteral}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStringLiteral(MainParser.StringLiteralContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BoolLiteral}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBoolLiteral(MainParser.BoolLiteralContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CompareExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCompareExpr(MainParser.CompareExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code MethodExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethodExpr(MainParser.MethodExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code FloatLiteral}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFloatLiteral(MainParser.FloatLiteralContext ctx);
	/**
	 * Visit a parse tree produced by the {@code BinaryExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBinaryExpr(MainParser.BinaryExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code CallExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCallExpr(MainParser.CallExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code IntLiteral}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIntLiteral(MainParser.IntLiteralContext ctx);
	/**
	 * Visit a parse tree produced by the {@code IndexExpr}
	 * labeled alternative in {@link MainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIndexExpr(MainParser.IndexExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#arguments}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArguments(MainParser.ArgumentsContext ctx);
}