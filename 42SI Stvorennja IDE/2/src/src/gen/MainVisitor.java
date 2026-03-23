package gen;// Generated from D:/University-Universytet/42SI Stvorennja IDE/2/src/src/Main.g4 by ANTLR 4.13.2
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
	 * Visit a parse tree produced by {@link MainParser#item}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitItem(MainParser.ItemContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#function}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction(MainParser.FunctionContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#paramList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParamList(MainParser.ParamListContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#param}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParam(MainParser.ParamContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#type_}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitType_(MainParser.Type_Context ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#primitiveType}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimitiveType(MainParser.PrimitiveTypeContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#structDef}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStructDef(MainParser.StructDefContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#fieldList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFieldList(MainParser.FieldListContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#field}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitField(MainParser.FieldContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#implBlock}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitImplBlock(MainParser.ImplBlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#method}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethod(MainParser.MethodContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#block}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock(MainParser.BlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(MainParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#letStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLetStmt(MainParser.LetStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#ifStmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfStmt(MainParser.IfStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#forLoop}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForLoop(MainParser.ForLoopContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#whileLoop}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileLoop(MainParser.WhileLoopContext ctx);
	/**
	 * Visit a parse tree produced by the {@code varExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVarExpr(MainParser.VarExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code methodCallExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethodCallExpr(MainParser.MethodCallExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code unaryExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnaryExpr(MainParser.UnaryExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code fieldAccess}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFieldAccess(MainParser.FieldAccessContext ctx);
	/**
	 * Visit a parse tree produced by the {@code binaryExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBinaryExpr(MainParser.BinaryExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code callExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCallExpr(MainParser.CallExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code vecLiteral}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVecLiteral(MainParser.VecLiteralContext ctx);
	/**
	 * Visit a parse tree produced by the {@code litExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLitExpr(MainParser.LitExprContext ctx);
	/**
	 * Visit a parse tree produced by the {@code parenExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParenExpr(MainParser.ParenExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#exprList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExprList(MainParser.ExprListContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#literal}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLiteral(MainParser.LiteralContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#binOp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBinOp(MainParser.BinOpContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#unOp}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnOp(MainParser.UnOpContext ctx);
}