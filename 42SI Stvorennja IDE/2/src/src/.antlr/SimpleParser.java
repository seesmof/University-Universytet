// Generated from d:/University-Universytet/42SI Stvorennja IDE/2/src/src/Simple.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class SimpleParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, SELECT=11, FROM=12, WHERE=13, GROUP=14, BY=15, SUM=16, COUNT=17, 
		AND=18, OR=19, IDENTIFIER=20, NUMBER=21, STRING=22, WS=23;
	public static final int
		RULE_sql = 0, RULE_select_statement = 1, RULE_column_list = 2, RULE_column_expr = 3, 
		RULE_column_name = 4, RULE_aggregation_function = 5, RULE_table = 6, RULE_where_clause = 7, 
		RULE_condition = 8, RULE_comparison_operator = 9, RULE_logical_operator = 10, 
		RULE_value = 11, RULE_group_by_clause = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"sql", "select_statement", "column_list", "column_expr", "column_name", 
			"aggregation_function", "table", "where_clause", "condition", "comparison_operator", 
			"logical_operator", "value", "group_by_clause"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'*'", "','", "'('", "')'", "'='", "'<>'", "'<'", "'>'", "'<='", 
			"'>='", "'SELECT'", "'FROM'", "'WHERE'", "'GROUP'", "'BY'", "'SUM'", 
			"'COUNT'", "'AND'", "'OR'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, "SELECT", 
			"FROM", "WHERE", "GROUP", "BY", "SUM", "COUNT", "AND", "OR", "IDENTIFIER", 
			"NUMBER", "STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Simple.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SimpleParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SqlContext extends ParserRuleContext {
		public Select_statementContext select_statement() {
			return getRuleContext(Select_statementContext.class,0);
		}
		public SqlContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sql; }
	}

	public final SqlContext sql() throws RecognitionException {
		SqlContext _localctx = new SqlContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_sql);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(26);
			select_statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Select_statementContext extends ParserRuleContext {
		public TerminalNode SELECT() { return getToken(SimpleParser.SELECT, 0); }
		public Column_listContext column_list() {
			return getRuleContext(Column_listContext.class,0);
		}
		public TerminalNode FROM() { return getToken(SimpleParser.FROM, 0); }
		public TableContext table() {
			return getRuleContext(TableContext.class,0);
		}
		public Where_clauseContext where_clause() {
			return getRuleContext(Where_clauseContext.class,0);
		}
		public Group_by_clauseContext group_by_clause() {
			return getRuleContext(Group_by_clauseContext.class,0);
		}
		public Select_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_select_statement; }
	}

	public final Select_statementContext select_statement() throws RecognitionException {
		Select_statementContext _localctx = new Select_statementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_select_statement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			match(SELECT);
			setState(29);
			column_list();
			setState(30);
			match(FROM);
			setState(31);
			table();
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(32);
				where_clause();
				}
			}

			setState(36);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==GROUP) {
				{
				setState(35);
				group_by_clause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Column_listContext extends ParserRuleContext {
		public List<Column_exprContext> column_expr() {
			return getRuleContexts(Column_exprContext.class);
		}
		public Column_exprContext column_expr(int i) {
			return getRuleContext(Column_exprContext.class,i);
		}
		public Column_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_column_list; }
	}

	public final Column_listContext column_list() throws RecognitionException {
		Column_listContext _localctx = new Column_listContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_column_list);
		int _la;
		try {
			setState(47);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(38);
				match(T__0);
				}
				break;
			case SUM:
			case COUNT:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				column_expr();
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__1) {
					{
					{
					setState(40);
					match(T__1);
					setState(41);
					column_expr();
					}
					}
					setState(46);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Column_exprContext extends ParserRuleContext {
		public Column_nameContext column_name() {
			return getRuleContext(Column_nameContext.class,0);
		}
		public Aggregation_functionContext aggregation_function() {
			return getRuleContext(Aggregation_functionContext.class,0);
		}
		public Column_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_column_expr; }
	}

	public final Column_exprContext column_expr() throws RecognitionException {
		Column_exprContext _localctx = new Column_exprContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_column_expr);
		try {
			setState(55);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(49);
				column_name();
				}
				break;
			case SUM:
			case COUNT:
				enterOuterAlt(_localctx, 2);
				{
				setState(50);
				aggregation_function();
				setState(51);
				match(T__2);
				setState(52);
				column_name();
				setState(53);
				match(T__3);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Column_nameContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(SimpleParser.IDENTIFIER, 0); }
		public Column_nameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_column_name; }
	}

	public final Column_nameContext column_name() throws RecognitionException {
		Column_nameContext _localctx = new Column_nameContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_column_name);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Aggregation_functionContext extends ParserRuleContext {
		public TerminalNode SUM() { return getToken(SimpleParser.SUM, 0); }
		public TerminalNode COUNT() { return getToken(SimpleParser.COUNT, 0); }
		public Aggregation_functionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aggregation_function; }
	}

	public final Aggregation_functionContext aggregation_function() throws RecognitionException {
		Aggregation_functionContext _localctx = new Aggregation_functionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_aggregation_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			_la = _input.LA(1);
			if ( !(_la==SUM || _la==COUNT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TableContext extends ParserRuleContext {
		public TerminalNode IDENTIFIER() { return getToken(SimpleParser.IDENTIFIER, 0); }
		public TableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_table; }
	}

	public final TableContext table() throws RecognitionException {
		TableContext _localctx = new TableContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_table);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Where_clauseContext extends ParserRuleContext {
		public TerminalNode WHERE() { return getToken(SimpleParser.WHERE, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public Where_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_where_clause; }
	}

	public final Where_clauseContext where_clause() throws RecognitionException {
		Where_clauseContext _localctx = new Where_clauseContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_where_clause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(WHERE);
			setState(64);
			condition();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public Column_nameContext column_name() {
			return getRuleContext(Column_nameContext.class,0);
		}
		public Comparison_operatorContext comparison_operator() {
			return getRuleContext(Comparison_operatorContext.class,0);
		}
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public List<Logical_operatorContext> logical_operator() {
			return getRuleContexts(Logical_operatorContext.class);
		}
		public Logical_operatorContext logical_operator(int i) {
			return getRuleContext(Logical_operatorContext.class,i);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_condition);
		try {
			int _alt;
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(66);
				column_name();
				setState(67);
				comparison_operator();
				setState(68);
				value();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 2);
				{
				setState(70);
				match(T__2);
				setState(71);
				condition();
				setState(72);
				match(T__3);
				setState(78);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(73);
						logical_operator();
						setState(74);
						condition();
						}
						} 
					}
					setState(80);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Comparison_operatorContext extends ParserRuleContext {
		public Comparison_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison_operator; }
	}

	public final Comparison_operatorContext comparison_operator() throws RecognitionException {
		Comparison_operatorContext _localctx = new Comparison_operatorContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_comparison_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 2016L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Logical_operatorContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(SimpleParser.AND, 0); }
		public TerminalNode OR() { return getToken(SimpleParser.OR, 0); }
		public Logical_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_operator; }
	}

	public final Logical_operatorContext logical_operator() throws RecognitionException {
		Logical_operatorContext _localctx = new Logical_operatorContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_logical_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			_la = _input.LA(1);
			if ( !(_la==AND || _la==OR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(SimpleParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(SimpleParser.STRING, 0); }
		public TerminalNode IDENTIFIER() { return getToken(SimpleParser.IDENTIFIER, 0); }
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7340032L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Group_by_clauseContext extends ParserRuleContext {
		public TerminalNode GROUP() { return getToken(SimpleParser.GROUP, 0); }
		public TerminalNode BY() { return getToken(SimpleParser.BY, 0); }
		public List<Column_nameContext> column_name() {
			return getRuleContexts(Column_nameContext.class);
		}
		public Column_nameContext column_name(int i) {
			return getRuleContext(Column_nameContext.class,i);
		}
		public Group_by_clauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_group_by_clause; }
	}

	public final Group_by_clauseContext group_by_clause() throws RecognitionException {
		Group_by_clauseContext _localctx = new Group_by_clauseContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_group_by_clause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(GROUP);
			setState(90);
			match(BY);
			setState(91);
			column_name();
			setState(96);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__1) {
				{
				{
				setState(92);
				match(T__1);
				setState(93);
				column_name();
				}
				}
				setState(98);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0017d\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001\"\b\u0001\u0001\u0001\u0003\u0001"+
		"%\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002"+
		"+\b\u0002\n\u0002\f\u0002.\t\u0002\u0003\u00020\b\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u00038\b"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0005\bM\b\b\n\b\f"+
		"\bP\t\b\u0003\bR\b\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0005\f_\b\f\n\f\f\fb\t"+
		"\f\u0001\f\u0000\u0000\r\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012"+
		"\u0014\u0016\u0018\u0000\u0004\u0001\u0000\u0010\u0011\u0001\u0000\u0005"+
		"\n\u0001\u0000\u0012\u0013\u0001\u0000\u0014\u0016^\u0000\u001a\u0001"+
		"\u0000\u0000\u0000\u0002\u001c\u0001\u0000\u0000\u0000\u0004/\u0001\u0000"+
		"\u0000\u0000\u00067\u0001\u0000\u0000\u0000\b9\u0001\u0000\u0000\u0000"+
		"\n;\u0001\u0000\u0000\u0000\f=\u0001\u0000\u0000\u0000\u000e?\u0001\u0000"+
		"\u0000\u0000\u0010Q\u0001\u0000\u0000\u0000\u0012S\u0001\u0000\u0000\u0000"+
		"\u0014U\u0001\u0000\u0000\u0000\u0016W\u0001\u0000\u0000\u0000\u0018Y"+
		"\u0001\u0000\u0000\u0000\u001a\u001b\u0003\u0002\u0001\u0000\u001b\u0001"+
		"\u0001\u0000\u0000\u0000\u001c\u001d\u0005\u000b\u0000\u0000\u001d\u001e"+
		"\u0003\u0004\u0002\u0000\u001e\u001f\u0005\f\u0000\u0000\u001f!\u0003"+
		"\f\u0006\u0000 \"\u0003\u000e\u0007\u0000! \u0001\u0000\u0000\u0000!\""+
		"\u0001\u0000\u0000\u0000\"$\u0001\u0000\u0000\u0000#%\u0003\u0018\f\u0000"+
		"$#\u0001\u0000\u0000\u0000$%\u0001\u0000\u0000\u0000%\u0003\u0001\u0000"+
		"\u0000\u0000&0\u0005\u0001\u0000\u0000\',\u0003\u0006\u0003\u0000()\u0005"+
		"\u0002\u0000\u0000)+\u0003\u0006\u0003\u0000*(\u0001\u0000\u0000\u0000"+
		"+.\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000"+
		"\u0000-0\u0001\u0000\u0000\u0000.,\u0001\u0000\u0000\u0000/&\u0001\u0000"+
		"\u0000\u0000/\'\u0001\u0000\u0000\u00000\u0005\u0001\u0000\u0000\u0000"+
		"18\u0003\b\u0004\u000023\u0003\n\u0005\u000034\u0005\u0003\u0000\u0000"+
		"45\u0003\b\u0004\u000056\u0005\u0004\u0000\u000068\u0001\u0000\u0000\u0000"+
		"71\u0001\u0000\u0000\u000072\u0001\u0000\u0000\u00008\u0007\u0001\u0000"+
		"\u0000\u00009:\u0005\u0014\u0000\u0000:\t\u0001\u0000\u0000\u0000;<\u0007"+
		"\u0000\u0000\u0000<\u000b\u0001\u0000\u0000\u0000=>\u0005\u0014\u0000"+
		"\u0000>\r\u0001\u0000\u0000\u0000?@\u0005\r\u0000\u0000@A\u0003\u0010"+
		"\b\u0000A\u000f\u0001\u0000\u0000\u0000BC\u0003\b\u0004\u0000CD\u0003"+
		"\u0012\t\u0000DE\u0003\u0016\u000b\u0000ER\u0001\u0000\u0000\u0000FG\u0005"+
		"\u0003\u0000\u0000GH\u0003\u0010\b\u0000HN\u0005\u0004\u0000\u0000IJ\u0003"+
		"\u0014\n\u0000JK\u0003\u0010\b\u0000KM\u0001\u0000\u0000\u0000LI\u0001"+
		"\u0000\u0000\u0000MP\u0001\u0000\u0000\u0000NL\u0001\u0000\u0000\u0000"+
		"NO\u0001\u0000\u0000\u0000OR\u0001\u0000\u0000\u0000PN\u0001\u0000\u0000"+
		"\u0000QB\u0001\u0000\u0000\u0000QF\u0001\u0000\u0000\u0000R\u0011\u0001"+
		"\u0000\u0000\u0000ST\u0007\u0001\u0000\u0000T\u0013\u0001\u0000\u0000"+
		"\u0000UV\u0007\u0002\u0000\u0000V\u0015\u0001\u0000\u0000\u0000WX\u0007"+
		"\u0003\u0000\u0000X\u0017\u0001\u0000\u0000\u0000YZ\u0005\u000e\u0000"+
		"\u0000Z[\u0005\u000f\u0000\u0000[`\u0003\b\u0004\u0000\\]\u0005\u0002"+
		"\u0000\u0000]_\u0003\b\u0004\u0000^\\\u0001\u0000\u0000\u0000_b\u0001"+
		"\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000"+
		"a\u0019\u0001\u0000\u0000\u0000b`\u0001\u0000\u0000\u0000\b!$,/7NQ`";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}