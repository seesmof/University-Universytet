// Generated from d:/University-Universytet/42SI Stvorennja IDE/2/src/src/Main.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link MainParser}.
 */
public interface MainListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link MainParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(MainParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(MainParser.StartContext ctx);
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
	 * Enter a parse tree produced by {@link MainParser#vector}.
	 * @param ctx the parse tree
	 */
	void enterVector(MainParser.VectorContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#vector}.
	 * @param ctx the parse tree
	 */
	void exitVector(MainParser.VectorContext ctx);
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
	 * Enter a parse tree produced by {@link MainParser#for}.
	 * @param ctx the parse tree
	 */
	void enterFor(MainParser.ForContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#for}.
	 * @param ctx the parse tree
	 */
	void exitFor(MainParser.ForContext ctx);
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
	 * Enter a parse tree produced by {@link MainParser#params}.
	 * @param ctx the parse tree
	 */
	void enterParams(MainParser.ParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link MainParser#params}.
	 * @param ctx the parse tree
	 */
	void exitParams(MainParser.ParamsContext ctx);
}