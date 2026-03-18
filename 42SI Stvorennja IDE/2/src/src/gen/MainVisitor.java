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
	 * Visit a parse tree produced by {@link MainParser#start}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStart(MainParser.StartContext ctx);
	/**
	 * Visit a parse tree produced by {@link MainParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(MainParser.ExpressionContext ctx);
}