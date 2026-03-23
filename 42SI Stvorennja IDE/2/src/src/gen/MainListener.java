package gen;// Generated from D:/University-Universytet/42SI Stvorennja IDE/2/src/src/Main.g4 by ANTLR 4.13.2
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
	 * Enter a parse tree produced by {@link MainParser#item}.
	 * @param ctx the parse tree
	 */
	void enterItem(MainParser.ItemContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#item}.
	 * @param ctx the parse tree
	 */
	void exitItem(MainParser.ItemContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(MainParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(MainParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#paramList}.
	 * @param ctx the parse tree
	 */
	void enterParamList(MainParser.ParamListContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#paramList}.
	 * @param ctx the parse tree
	 */
	void exitParamList(MainParser.ParamListContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(MainParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(MainParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#type_}.
	 * @param ctx the parse tree
	 */
	void enterType_(MainParser.Type_Context ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#type_}.
	 * @param ctx the parse tree
	 */
	void exitType_(MainParser.Type_Context ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#primitiveType}.
	 * @param ctx the parse tree
	 */
	void enterPrimitiveType(MainParser.PrimitiveTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#primitiveType}.
	 * @param ctx the parse tree
	 */
	void exitPrimitiveType(MainParser.PrimitiveTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#structDef}.
	 * @param ctx the parse tree
	 */
	void enterStructDef(MainParser.StructDefContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#structDef}.
	 * @param ctx the parse tree
	 */
	void exitStructDef(MainParser.StructDefContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#fieldList}.
	 * @param ctx the parse tree
	 */
	void enterFieldList(MainParser.FieldListContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#fieldList}.
	 * @param ctx the parse tree
	 */
	void exitFieldList(MainParser.FieldListContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#field}.
	 * @param ctx the parse tree
	 */
	void enterField(MainParser.FieldContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#field}.
	 * @param ctx the parse tree
	 */
	void exitField(MainParser.FieldContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#implBlock}.
	 * @param ctx the parse tree
	 */
	void enterImplBlock(MainParser.ImplBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#implBlock}.
	 * @param ctx the parse tree
	 */
	void exitImplBlock(MainParser.ImplBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#method}.
	 * @param ctx the parse tree
	 */
	void enterMethod(MainParser.MethodContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#method}.
	 * @param ctx the parse tree
	 */
	void exitMethod(MainParser.MethodContext ctx);
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
	 * Enter a parse tree produced by {@link MainParser#letStmt}.
	 * @param ctx the parse tree
	 */
	void enterLetStmt(MainParser.LetStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#letStmt}.
	 * @param ctx the parse tree
	 */
	void exitLetStmt(MainParser.LetStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void enterIfStmt(MainParser.IfStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#ifStmt}.
	 * @param ctx the parse tree
	 */
	void exitIfStmt(MainParser.IfStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#forLoop}.
	 * @param ctx the parse tree
	 */
	void enterForLoop(MainParser.ForLoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#forLoop}.
	 * @param ctx the parse tree
	 */
	void exitForLoop(MainParser.ForLoopContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void enterWhileLoop(MainParser.WhileLoopContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#whileLoop}.
	 * @param ctx the parse tree
	 */
	void exitWhileLoop(MainParser.WhileLoopContext ctx);
	/**
	 * Enter a parse tree produced by the {@code varExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVarExpr(MainParser.VarExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code varExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVarExpr(MainParser.VarExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code methodCallExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMethodCallExpr(MainParser.MethodCallExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code methodCallExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMethodCallExpr(MainParser.MethodCallExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unaryExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpr(MainParser.UnaryExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unaryExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpr(MainParser.UnaryExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code fieldAccess}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFieldAccess(MainParser.FieldAccessContext ctx);
	/**
	 * Exit a parse tree produced by the {@code fieldAccess}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFieldAccess(MainParser.FieldAccessContext ctx);
	/**
	 * Enter a parse tree produced by the {@code binaryExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBinaryExpr(MainParser.BinaryExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code binaryExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBinaryExpr(MainParser.BinaryExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code callExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterCallExpr(MainParser.CallExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code callExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitCallExpr(MainParser.CallExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code vecLiteral}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVecLiteral(MainParser.VecLiteralContext ctx);
	/**
	 * Exit a parse tree produced by the {@code vecLiteral}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVecLiteral(MainParser.VecLiteralContext ctx);
	/**
	 * Enter a parse tree produced by the {@code litExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLitExpr(MainParser.LitExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code litExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLitExpr(MainParser.LitExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parenExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParenExpr(MainParser.ParenExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parenExpr}
	 * labeled alternative in {@link MainParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParenExpr(MainParser.ParenExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#exprList}.
	 * @param ctx the parse tree
	 */
	void enterExprList(MainParser.ExprListContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#exprList}.
	 * @param ctx the parse tree
	 */
	void exitExprList(MainParser.ExprListContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(MainParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(MainParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#binOp}.
	 * @param ctx the parse tree
	 */
	void enterBinOp(MainParser.BinOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#binOp}.
	 * @param ctx the parse tree
	 */
	void exitBinOp(MainParser.BinOpContext ctx);
	/**
	 * Enter a parse tree produced by {@link MainParser#unOp}.
	 * @param ctx the parse tree
	 */
	void enterUnOp(MainParser.UnOpContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#unOp}.
	 * @param ctx the parse tree
	 */
	void exitUnOp(MainParser.UnOpContext ctx);
}