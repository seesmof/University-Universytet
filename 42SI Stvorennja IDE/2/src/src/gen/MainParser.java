package gen;// Generated from D:/University-Universytet/42SI Stvorennja IDE/2/src/src/Main.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MainParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, ID=44, INT=45, STRING=46, 
		WS=47, COMMENT=48;
	public static final int
		RULE_program = 0, RULE_item = 1, RULE_function = 2, RULE_paramList = 3, 
		RULE_param = 4, RULE_type_ = 5, RULE_primitiveType = 6, RULE_structDef = 7, 
		RULE_fieldList = 8, RULE_field = 9, RULE_implBlock = 10, RULE_method = 11, 
		RULE_block = 12, RULE_statement = 13, RULE_letStmt = 14, RULE_ifStmt = 15, 
		RULE_forLoop = 16, RULE_whileLoop = 17, RULE_expr = 18, RULE_exprList = 19, 
		RULE_literal = 20, RULE_binOp = 21, RULE_unOp = 22;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "item", "function", "paramList", "param", "type_", "primitiveType", 
			"structDef", "fieldList", "field", "implBlock", "method", "block", "statement", 
			"letStmt", "ifStmt", "forLoop", "whileLoop", "expr", "exprList", "literal", 
			"binOp", "unOp"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'fn'", "'('", "')'", "'->'", "','", "':'", "'Vec'", "'<'", "'>'", 
			"'i32'", "'bool'", "'String'", "'struct'", "'{'", "'}'", "'impl'", "';'", 
			"'let'", "'='", "'if'", "'else'", "'for'", "'in'", "'..'", "'while'", 
			"'.'", "'vec!'", "'['", "']'", "'true'", "'false'", "'+'", "'-'", "'*'", 
			"'/'", "'%'", "'=='", "'!='", "'<='", "'>='", "'&&'", "'||'", "'!'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, "ID", "INT", "STRING", 
			"WS", "COMMENT"
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
	public String getGrammarFileName() { return "Main.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public MainParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(MainParser.EOF, 0); }
		public List<ItemContext> item() {
			return getRuleContexts(ItemContext.class);
		}
		public ItemContext item(int i) {
			return getRuleContext(ItemContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 73730L) != 0)) {
				{
				{
				setState(46);
				item();
				}
				}
				setState(51);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(52);
			match(EOF);
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
	public static class ItemContext extends ParserRuleContext {
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public StructDefContext structDef() {
			return getRuleContext(StructDefContext.class,0);
		}
		public ImplBlockContext implBlock() {
			return getRuleContext(ImplBlockContext.class,0);
		}
		public ItemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_item; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterItem(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitItem(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitItem(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ItemContext item() throws RecognitionException {
		ItemContext _localctx = new ItemContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_item);
		try {
			setState(57);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(54);
				function();
				}
				break;
			case T__12:
				enterOuterAlt(_localctx, 2);
				{
				setState(55);
				structDef();
				}
				break;
			case T__15:
				enterOuterAlt(_localctx, 3);
				{
				setState(56);
				implBlock();
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
	public static class FunctionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MainParser.ID, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ParamListContext paramList() {
			return getRuleContext(ParamListContext.class,0);
		}
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterFunction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitFunction(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitFunction(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(T__0);
			setState(60);
			match(ID);
			setState(61);
			match(T__1);
			setState(63);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(62);
				paramList();
				}
			}

			setState(65);
			match(T__2);
			setState(68);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__3) {
				{
				setState(66);
				match(T__3);
				setState(67);
				type_();
				}
			}

			setState(70);
			block();
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
	public static class ParamListContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public ParamListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_paramList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterParamList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitParamList(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitParamList(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParamListContext paramList() throws RecognitionException {
		ParamListContext _localctx = new ParamListContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_paramList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72);
			param();
			setState(77);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(73);
				match(T__4);
				setState(74);
				param();
				}
				}
				setState(79);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MainParser.ID, 0); }
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterParam(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitParam(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitParam(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(ID);
			setState(81);
			match(T__5);
			setState(82);
			type_();
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
	public static class Type_Context extends ParserRuleContext {
		public PrimitiveTypeContext primitiveType() {
			return getRuleContext(PrimitiveTypeContext.class,0);
		}
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public TerminalNode ID() { return getToken(MainParser.ID, 0); }
		public Type_Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type_; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterType_(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitType_(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitType_(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Type_Context type_() throws RecognitionException {
		Type_Context _localctx = new Type_Context(_ctx, getState());
		enterRule(_localctx, 10, RULE_type_);
		try {
			setState(91);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__9:
			case T__10:
			case T__11:
				enterOuterAlt(_localctx, 1);
				{
				setState(84);
				primitiveType();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 2);
				{
				setState(85);
				match(T__6);
				setState(86);
				match(T__7);
				setState(87);
				type_();
				setState(88);
				match(T__8);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 3);
				{
				setState(90);
				match(ID);
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
	public static class PrimitiveTypeContext extends ParserRuleContext {
		public PrimitiveTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitiveType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterPrimitiveType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitPrimitiveType(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitPrimitiveType(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PrimitiveTypeContext primitiveType() throws RecognitionException {
		PrimitiveTypeContext _localctx = new PrimitiveTypeContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_primitiveType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 7168L) != 0)) ) {
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
	public static class StructDefContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MainParser.ID, 0); }
		public FieldListContext fieldList() {
			return getRuleContext(FieldListContext.class,0);
		}
		public StructDefContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_structDef; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterStructDef(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitStructDef(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitStructDef(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StructDefContext structDef() throws RecognitionException {
		StructDefContext _localctx = new StructDefContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_structDef);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(T__12);
			setState(96);
			match(ID);
			setState(97);
			match(T__13);
			setState(99);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(98);
				fieldList();
				}
			}

			setState(101);
			match(T__14);
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
	public static class FieldListContext extends ParserRuleContext {
		public List<FieldContext> field() {
			return getRuleContexts(FieldContext.class);
		}
		public FieldContext field(int i) {
			return getRuleContext(FieldContext.class,i);
		}
		public FieldListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fieldList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterFieldList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitFieldList(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitFieldList(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FieldListContext fieldList() throws RecognitionException {
		FieldListContext _localctx = new FieldListContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_fieldList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			field();
			setState(108);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(104);
				match(T__4);
				setState(105);
				field();
				}
				}
				setState(110);
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

	@SuppressWarnings("CheckReturnValue")
	public static class FieldContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MainParser.ID, 0); }
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public FieldContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_field; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterField(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitField(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitField(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FieldContext field() throws RecognitionException {
		FieldContext _localctx = new FieldContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_field);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			match(ID);
			setState(112);
			match(T__5);
			setState(113);
			type_();
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
	public static class ImplBlockContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MainParser.ID, 0); }
		public List<MethodContext> method() {
			return getRuleContexts(MethodContext.class);
		}
		public MethodContext method(int i) {
			return getRuleContext(MethodContext.class,i);
		}
		public ImplBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_implBlock; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterImplBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitImplBlock(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitImplBlock(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ImplBlockContext implBlock() throws RecognitionException {
		ImplBlockContext _localctx = new ImplBlockContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_implBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(T__15);
			setState(116);
			match(ID);
			setState(117);
			match(T__13);
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__0) {
				{
				{
				setState(118);
				method();
				}
				}
				setState(123);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(124);
			match(T__14);
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
	public static class MethodContext extends ParserRuleContext {
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public MethodContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterMethod(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitMethod(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitMethod(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MethodContext method() throws RecognitionException {
		MethodContext _localctx = new MethodContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_method);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			function();
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
	public static class BlockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitBlock(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitBlock(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(T__13);
			setState(132);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 131953379901444L) != 0)) {
				{
				{
				setState(129);
				statement();
				}
				}
				setState(134);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(135);
			match(T__14);
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
	public static class StatementContext extends ParserRuleContext {
		public LetStmtContext letStmt() {
			return getRuleContext(LetStmtContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public ForLoopContext forLoop() {
			return getRuleContext(ForLoopContext.class,0);
		}
		public WhileLoopContext whileLoop() {
			return getRuleContext(WhileLoopContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitStatement(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitStatement(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_statement);
		try {
			setState(146);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__17:
				enterOuterAlt(_localctx, 1);
				{
				setState(137);
				letStmt();
				}
				break;
			case T__1:
			case T__26:
			case T__29:
			case T__30:
			case T__32:
			case T__42:
			case ID:
			case INT:
			case STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(138);
				expr(0);
				setState(140);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
				case 1:
					{
					setState(139);
					match(T__16);
					}
					break;
				}
				}
				break;
			case T__19:
				enterOuterAlt(_localctx, 3);
				{
				setState(142);
				ifStmt();
				}
				break;
			case T__21:
				enterOuterAlt(_localctx, 4);
				{
				setState(143);
				forLoop();
				}
				break;
			case T__24:
				enterOuterAlt(_localctx, 5);
				{
				setState(144);
				whileLoop();
				}
				break;
			case T__16:
				enterOuterAlt(_localctx, 6);
				{
				setState(145);
				match(T__16);
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
	public static class LetStmtContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MainParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Type_Context type_() {
			return getRuleContext(Type_Context.class,0);
		}
		public LetStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterLetStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitLetStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitLetStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LetStmtContext letStmt() throws RecognitionException {
		LetStmtContext _localctx = new LetStmtContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_letStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(148);
			match(T__17);
			setState(149);
			match(ID);
			setState(152);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__5) {
				{
				setState(150);
				match(T__5);
				setState(151);
				type_();
				}
			}

			setState(154);
			match(T__18);
			setState(155);
			expr(0);
			setState(156);
			match(T__16);
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
	public static class IfStmtContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<BlockContext> block() {
			return getRuleContexts(BlockContext.class);
		}
		public BlockContext block(int i) {
			return getRuleContext(BlockContext.class,i);
		}
		public IfStmtContext ifStmt() {
			return getRuleContext(IfStmtContext.class,0);
		}
		public IfStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifStmt; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterIfStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitIfStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitIfStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final IfStmtContext ifStmt() throws RecognitionException {
		IfStmtContext _localctx = new IfStmtContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_ifStmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(158);
			match(T__19);
			setState(159);
			expr(0);
			setState(160);
			block();
			setState(166);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__20) {
				{
				setState(161);
				match(T__20);
				setState(164);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__13:
					{
					setState(162);
					block();
					}
					break;
				case T__19:
					{
					setState(163);
					ifStmt();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
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
	public static class ForLoopContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(MainParser.ID, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ForLoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forLoop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterForLoop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitForLoop(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitForLoop(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ForLoopContext forLoop() throws RecognitionException {
		ForLoopContext _localctx = new ForLoopContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_forLoop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(168);
			match(T__21);
			setState(169);
			match(ID);
			setState(170);
			match(T__22);
			setState(171);
			expr(0);
			setState(172);
			match(T__23);
			setState(173);
			expr(0);
			setState(174);
			block();
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
	public static class WhileLoopContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public WhileLoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileLoop; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterWhileLoop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitWhileLoop(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitWhileLoop(this);
			else return visitor.visitChildren(this);
		}
	}

	public final WhileLoopContext whileLoop() throws RecognitionException {
		WhileLoopContext _localctx = new WhileLoopContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_whileLoop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(176);
			match(T__24);
			setState(177);
			expr(0);
			setState(178);
			block();
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
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VarExprContext extends ExprContext {
		public TerminalNode ID() { return getToken(MainParser.ID, 0); }
		public VarExprContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterVarExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitVarExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitVarExpr(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MethodCallExprContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ID() { return getToken(MainParser.ID, 0); }
		public ExprListContext exprList() {
			return getRuleContext(ExprListContext.class,0);
		}
		public MethodCallExprContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterMethodCallExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitMethodCallExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitMethodCallExpr(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class UnaryExprContext extends ExprContext {
		public UnOpContext unOp() {
			return getRuleContext(UnOpContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public UnaryExprContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterUnaryExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitUnaryExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitUnaryExpr(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FieldAccessContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ID() { return getToken(MainParser.ID, 0); }
		public FieldAccessContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterFieldAccess(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitFieldAccess(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitFieldAccess(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class BinaryExprContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public BinOpContext binOp() {
			return getRuleContext(BinOpContext.class,0);
		}
		public BinaryExprContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterBinaryExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitBinaryExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitBinaryExpr(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CallExprContext extends ExprContext {
		public TerminalNode ID() { return getToken(MainParser.ID, 0); }
		public ExprListContext exprList() {
			return getRuleContext(ExprListContext.class,0);
		}
		public CallExprContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterCallExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitCallExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitCallExpr(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VecLiteralContext extends ExprContext {
		public ExprListContext exprList() {
			return getRuleContext(ExprListContext.class,0);
		}
		public VecLiteralContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterVecLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitVecLiteral(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitVecLiteral(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LitExprContext extends ExprContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public LitExprContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterLitExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitLitExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitLitExpr(this);
			else return visitor.visitChildren(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParenExprContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ParenExprContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterParenExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitParenExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitParenExpr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 36;
		enterRecursionRule(_localctx, 36, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
			case 1:
				{
				_localctx = new UnaryExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(181);
				unOp();
				setState(182);
				expr(8);
				}
				break;
			case 2:
				{
				_localctx = new CallExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(184);
				match(ID);
				setState(185);
				match(T__1);
				setState(187);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 131953340710916L) != 0)) {
					{
					setState(186);
					exprList();
					}
				}

				setState(189);
				match(T__2);
				}
				break;
			case 3:
				{
				_localctx = new VecLiteralContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(190);
				match(T__26);
				setState(191);
				match(T__27);
				setState(193);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 131953340710916L) != 0)) {
					{
					setState(192);
					exprList();
					}
				}

				setState(195);
				match(T__28);
				}
				break;
			case 4:
				{
				_localctx = new LitExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(196);
				literal();
				}
				break;
			case 5:
				{
				_localctx = new VarExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(197);
				match(ID);
				}
				break;
			case 6:
				{
				_localctx = new ParenExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(198);
				match(T__1);
				setState(199);
				expr(0);
				setState(200);
				match(T__2);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(221);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(219);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
					case 1:
						{
						_localctx = new BinaryExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(204);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(205);
						binOp();
						setState(206);
						expr(10);
						}
						break;
					case 2:
						{
						_localctx = new MethodCallExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(208);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(209);
						match(T__25);
						setState(210);
						match(ID);
						setState(211);
						match(T__1);
						setState(213);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 131953340710916L) != 0)) {
							{
							setState(212);
							exprList();
							}
						}

						setState(215);
						match(T__2);
						}
						break;
					case 3:
						{
						_localctx = new FieldAccessContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(216);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(217);
						match(T__25);
						setState(218);
						match(ID);
						}
						break;
					}
					} 
				}
				setState(223);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprListContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public ExprListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exprList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterExprList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitExprList(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitExprList(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExprListContext exprList() throws RecognitionException {
		ExprListContext _localctx = new ExprListContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_exprList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			expr(0);
			setState(229);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__4) {
				{
				{
				setState(225);
				match(T__4);
				setState(226);
				expr(0);
				}
				}
				setState(231);
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

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(MainParser.INT, 0); }
		public TerminalNode STRING() { return getToken(MainParser.STRING, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterLiteral(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitLiteral(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitLiteral(this);
			else return visitor.visitChildren(this);
		}
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 105556337491968L) != 0)) ) {
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
	public static class BinOpContext extends ParserRuleContext {
		public BinOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_binOp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterBinOp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitBinOp(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitBinOp(this);
			else return visitor.visitChildren(this);
		}
	}

	public final BinOpContext binOp() throws RecognitionException {
		BinOpContext _localctx = new BinOpContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_binOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 8791798055680L) != 0)) ) {
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
	public static class UnOpContext extends ParserRuleContext {
		public UnOpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unOp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).enterUnOp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof MainListener) ((MainListener)listener).exitUnOp(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof MainVisitor ) return ((MainVisitor<? extends T>)visitor).visitUnOp(this);
			else return visitor.visitChildren(this);
		}
	}

	public final UnOpContext unOp() throws RecognitionException {
		UnOpContext _localctx = new UnOpContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_unOp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			_la = _input.LA(1);
			if ( !(_la==T__32 || _la==T__42) ) {
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 18:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 9);
		case 1:
			return precpred(_ctx, 6);
		case 2:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00010\u00ef\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0001\u0000\u0005\u00000\b\u0000\n\u0000\f\u0000"+
		"3\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0003\u0001:\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0003\u0002@\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002"+
		"E\b\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0005\u0003L\b\u0003\n\u0003\f\u0003O\t\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005\\\b\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007"+
		"d\b\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0005\bk\b\b"+
		"\n\b\f\bn\t\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n"+
		"\u0001\n\u0005\nx\b\n\n\n\f\n{\t\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0005\f\u0083\b\f\n\f\f\f\u0086\t\f\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\r\u0003\r\u008d\b\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003"+
		"\r\u0093\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e"+
		"\u0099\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f"+
		"\u00a5\b\u000f\u0003\u000f\u00a7\b\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00bc"+
		"\b\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0003\u0012\u00c2"+
		"\b\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0003\u0012\u00cb\b\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0003\u0012\u00d6\b\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0005\u0012\u00dc\b\u0012\n\u0012\f\u0012\u00df\t\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0005\u0013\u00e4\b\u0013\n\u0013\f\u0013\u00e7"+
		"\t\u0013\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0000\u0001$\u0017\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,\u0000\u0004\u0001"+
		"\u0000\n\f\u0002\u0000\u001e\u001f-.\u0002\u0000\b\t *\u0002\u0000!!+"+
		"+\u00f8\u00001\u0001\u0000\u0000\u0000\u00029\u0001\u0000\u0000\u0000"+
		"\u0004;\u0001\u0000\u0000\u0000\u0006H\u0001\u0000\u0000\u0000\bP\u0001"+
		"\u0000\u0000\u0000\n[\u0001\u0000\u0000\u0000\f]\u0001\u0000\u0000\u0000"+
		"\u000e_\u0001\u0000\u0000\u0000\u0010g\u0001\u0000\u0000\u0000\u0012o"+
		"\u0001\u0000\u0000\u0000\u0014s\u0001\u0000\u0000\u0000\u0016~\u0001\u0000"+
		"\u0000\u0000\u0018\u0080\u0001\u0000\u0000\u0000\u001a\u0092\u0001\u0000"+
		"\u0000\u0000\u001c\u0094\u0001\u0000\u0000\u0000\u001e\u009e\u0001\u0000"+
		"\u0000\u0000 \u00a8\u0001\u0000\u0000\u0000\"\u00b0\u0001\u0000\u0000"+
		"\u0000$\u00ca\u0001\u0000\u0000\u0000&\u00e0\u0001\u0000\u0000\u0000("+
		"\u00e8\u0001\u0000\u0000\u0000*\u00ea\u0001\u0000\u0000\u0000,\u00ec\u0001"+
		"\u0000\u0000\u0000.0\u0003\u0002\u0001\u0000/.\u0001\u0000\u0000\u0000"+
		"03\u0001\u0000\u0000\u00001/\u0001\u0000\u0000\u000012\u0001\u0000\u0000"+
		"\u000024\u0001\u0000\u0000\u000031\u0001\u0000\u0000\u000045\u0005\u0000"+
		"\u0000\u00015\u0001\u0001\u0000\u0000\u00006:\u0003\u0004\u0002\u0000"+
		"7:\u0003\u000e\u0007\u00008:\u0003\u0014\n\u000096\u0001\u0000\u0000\u0000"+
		"97\u0001\u0000\u0000\u000098\u0001\u0000\u0000\u0000:\u0003\u0001\u0000"+
		"\u0000\u0000;<\u0005\u0001\u0000\u0000<=\u0005,\u0000\u0000=?\u0005\u0002"+
		"\u0000\u0000>@\u0003\u0006\u0003\u0000?>\u0001\u0000\u0000\u0000?@\u0001"+
		"\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000AD\u0005\u0003\u0000\u0000"+
		"BC\u0005\u0004\u0000\u0000CE\u0003\n\u0005\u0000DB\u0001\u0000\u0000\u0000"+
		"DE\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000FG\u0003\u0018\f\u0000"+
		"G\u0005\u0001\u0000\u0000\u0000HM\u0003\b\u0004\u0000IJ\u0005\u0005\u0000"+
		"\u0000JL\u0003\b\u0004\u0000KI\u0001\u0000\u0000\u0000LO\u0001\u0000\u0000"+
		"\u0000MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000N\u0007\u0001"+
		"\u0000\u0000\u0000OM\u0001\u0000\u0000\u0000PQ\u0005,\u0000\u0000QR\u0005"+
		"\u0006\u0000\u0000RS\u0003\n\u0005\u0000S\t\u0001\u0000\u0000\u0000T\\"+
		"\u0003\f\u0006\u0000UV\u0005\u0007\u0000\u0000VW\u0005\b\u0000\u0000W"+
		"X\u0003\n\u0005\u0000XY\u0005\t\u0000\u0000Y\\\u0001\u0000\u0000\u0000"+
		"Z\\\u0005,\u0000\u0000[T\u0001\u0000\u0000\u0000[U\u0001\u0000\u0000\u0000"+
		"[Z\u0001\u0000\u0000\u0000\\\u000b\u0001\u0000\u0000\u0000]^\u0007\u0000"+
		"\u0000\u0000^\r\u0001\u0000\u0000\u0000_`\u0005\r\u0000\u0000`a\u0005"+
		",\u0000\u0000ac\u0005\u000e\u0000\u0000bd\u0003\u0010\b\u0000cb\u0001"+
		"\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000de\u0001\u0000\u0000\u0000"+
		"ef\u0005\u000f\u0000\u0000f\u000f\u0001\u0000\u0000\u0000gl\u0003\u0012"+
		"\t\u0000hi\u0005\u0005\u0000\u0000ik\u0003\u0012\t\u0000jh\u0001\u0000"+
		"\u0000\u0000kn\u0001\u0000\u0000\u0000lj\u0001\u0000\u0000\u0000lm\u0001"+
		"\u0000\u0000\u0000m\u0011\u0001\u0000\u0000\u0000nl\u0001\u0000\u0000"+
		"\u0000op\u0005,\u0000\u0000pq\u0005\u0006\u0000\u0000qr\u0003\n\u0005"+
		"\u0000r\u0013\u0001\u0000\u0000\u0000st\u0005\u0010\u0000\u0000tu\u0005"+
		",\u0000\u0000uy\u0005\u000e\u0000\u0000vx\u0003\u0016\u000b\u0000wv\u0001"+
		"\u0000\u0000\u0000x{\u0001\u0000\u0000\u0000yw\u0001\u0000\u0000\u0000"+
		"yz\u0001\u0000\u0000\u0000z|\u0001\u0000\u0000\u0000{y\u0001\u0000\u0000"+
		"\u0000|}\u0005\u000f\u0000\u0000}\u0015\u0001\u0000\u0000\u0000~\u007f"+
		"\u0003\u0004\u0002\u0000\u007f\u0017\u0001\u0000\u0000\u0000\u0080\u0084"+
		"\u0005\u000e\u0000\u0000\u0081\u0083\u0003\u001a\r\u0000\u0082\u0081\u0001"+
		"\u0000\u0000\u0000\u0083\u0086\u0001\u0000\u0000\u0000\u0084\u0082\u0001"+
		"\u0000\u0000\u0000\u0084\u0085\u0001\u0000\u0000\u0000\u0085\u0087\u0001"+
		"\u0000\u0000\u0000\u0086\u0084\u0001\u0000\u0000\u0000\u0087\u0088\u0005"+
		"\u000f\u0000\u0000\u0088\u0019\u0001\u0000\u0000\u0000\u0089\u0093\u0003"+
		"\u001c\u000e\u0000\u008a\u008c\u0003$\u0012\u0000\u008b\u008d\u0005\u0011"+
		"\u0000\u0000\u008c\u008b\u0001\u0000\u0000\u0000\u008c\u008d\u0001\u0000"+
		"\u0000\u0000\u008d\u0093\u0001\u0000\u0000\u0000\u008e\u0093\u0003\u001e"+
		"\u000f\u0000\u008f\u0093\u0003 \u0010\u0000\u0090\u0093\u0003\"\u0011"+
		"\u0000\u0091\u0093\u0005\u0011\u0000\u0000\u0092\u0089\u0001\u0000\u0000"+
		"\u0000\u0092\u008a\u0001\u0000\u0000\u0000\u0092\u008e\u0001\u0000\u0000"+
		"\u0000\u0092\u008f\u0001\u0000\u0000\u0000\u0092\u0090\u0001\u0000\u0000"+
		"\u0000\u0092\u0091\u0001\u0000\u0000\u0000\u0093\u001b\u0001\u0000\u0000"+
		"\u0000\u0094\u0095\u0005\u0012\u0000\u0000\u0095\u0098\u0005,\u0000\u0000"+
		"\u0096\u0097\u0005\u0006\u0000\u0000\u0097\u0099\u0003\n\u0005\u0000\u0098"+
		"\u0096\u0001\u0000\u0000\u0000\u0098\u0099\u0001\u0000\u0000\u0000\u0099"+
		"\u009a\u0001\u0000\u0000\u0000\u009a\u009b\u0005\u0013\u0000\u0000\u009b"+
		"\u009c\u0003$\u0012\u0000\u009c\u009d\u0005\u0011\u0000\u0000\u009d\u001d"+
		"\u0001\u0000\u0000\u0000\u009e\u009f\u0005\u0014\u0000\u0000\u009f\u00a0"+
		"\u0003$\u0012\u0000\u00a0\u00a6\u0003\u0018\f\u0000\u00a1\u00a4\u0005"+
		"\u0015\u0000\u0000\u00a2\u00a5\u0003\u0018\f\u0000\u00a3\u00a5\u0003\u001e"+
		"\u000f\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000\u00a4\u00a3\u0001\u0000"+
		"\u0000\u0000\u00a5\u00a7\u0001\u0000\u0000\u0000\u00a6\u00a1\u0001\u0000"+
		"\u0000\u0000\u00a6\u00a7\u0001\u0000\u0000\u0000\u00a7\u001f\u0001\u0000"+
		"\u0000\u0000\u00a8\u00a9\u0005\u0016\u0000\u0000\u00a9\u00aa\u0005,\u0000"+
		"\u0000\u00aa\u00ab\u0005\u0017\u0000\u0000\u00ab\u00ac\u0003$\u0012\u0000"+
		"\u00ac\u00ad\u0005\u0018\u0000\u0000\u00ad\u00ae\u0003$\u0012\u0000\u00ae"+
		"\u00af\u0003\u0018\f\u0000\u00af!\u0001\u0000\u0000\u0000\u00b0\u00b1"+
		"\u0005\u0019\u0000\u0000\u00b1\u00b2\u0003$\u0012\u0000\u00b2\u00b3\u0003"+
		"\u0018\f\u0000\u00b3#\u0001\u0000\u0000\u0000\u00b4\u00b5\u0006\u0012"+
		"\uffff\uffff\u0000\u00b5\u00b6\u0003,\u0016\u0000\u00b6\u00b7\u0003$\u0012"+
		"\b\u00b7\u00cb\u0001\u0000\u0000\u0000\u00b8\u00b9\u0005,\u0000\u0000"+
		"\u00b9\u00bb\u0005\u0002\u0000\u0000\u00ba\u00bc\u0003&\u0013\u0000\u00bb"+
		"\u00ba\u0001\u0000\u0000\u0000\u00bb\u00bc\u0001\u0000\u0000\u0000\u00bc"+
		"\u00bd\u0001\u0000\u0000\u0000\u00bd\u00cb\u0005\u0003\u0000\u0000\u00be"+
		"\u00bf\u0005\u001b\u0000\u0000\u00bf\u00c1\u0005\u001c\u0000\u0000\u00c0"+
		"\u00c2\u0003&\u0013\u0000\u00c1\u00c0\u0001\u0000\u0000\u0000\u00c1\u00c2"+
		"\u0001\u0000\u0000\u0000\u00c2\u00c3\u0001\u0000\u0000\u0000\u00c3\u00cb"+
		"\u0005\u001d\u0000\u0000\u00c4\u00cb\u0003(\u0014\u0000\u00c5\u00cb\u0005"+
		",\u0000\u0000\u00c6\u00c7\u0005\u0002\u0000\u0000\u00c7\u00c8\u0003$\u0012"+
		"\u0000\u00c8\u00c9\u0005\u0003\u0000\u0000\u00c9\u00cb\u0001\u0000\u0000"+
		"\u0000\u00ca\u00b4\u0001\u0000\u0000\u0000\u00ca\u00b8\u0001\u0000\u0000"+
		"\u0000\u00ca\u00be\u0001\u0000\u0000\u0000\u00ca\u00c4\u0001\u0000\u0000"+
		"\u0000\u00ca\u00c5\u0001\u0000\u0000\u0000\u00ca\u00c6\u0001\u0000\u0000"+
		"\u0000\u00cb\u00dd\u0001\u0000\u0000\u0000\u00cc\u00cd\n\t\u0000\u0000"+
		"\u00cd\u00ce\u0003*\u0015\u0000\u00ce\u00cf\u0003$\u0012\n\u00cf\u00dc"+
		"\u0001\u0000\u0000\u0000\u00d0\u00d1\n\u0006\u0000\u0000\u00d1\u00d2\u0005"+
		"\u001a\u0000\u0000\u00d2\u00d3\u0005,\u0000\u0000\u00d3\u00d5\u0005\u0002"+
		"\u0000\u0000\u00d4\u00d6\u0003&\u0013\u0000\u00d5\u00d4\u0001\u0000\u0000"+
		"\u0000\u00d5\u00d6\u0001\u0000\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000"+
		"\u0000\u00d7\u00dc\u0005\u0003\u0000\u0000\u00d8\u00d9\n\u0005\u0000\u0000"+
		"\u00d9\u00da\u0005\u001a\u0000\u0000\u00da\u00dc\u0005,\u0000\u0000\u00db"+
		"\u00cc\u0001\u0000\u0000\u0000\u00db\u00d0\u0001\u0000\u0000\u0000\u00db"+
		"\u00d8\u0001\u0000\u0000\u0000\u00dc\u00df\u0001\u0000\u0000\u0000\u00dd"+
		"\u00db\u0001\u0000\u0000\u0000\u00dd\u00de\u0001\u0000\u0000\u0000\u00de"+
		"%\u0001\u0000\u0000\u0000\u00df\u00dd\u0001\u0000\u0000\u0000\u00e0\u00e5"+
		"\u0003$\u0012\u0000\u00e1\u00e2\u0005\u0005\u0000\u0000\u00e2\u00e4\u0003"+
		"$\u0012\u0000\u00e3\u00e1\u0001\u0000\u0000\u0000\u00e4\u00e7\u0001\u0000"+
		"\u0000\u0000\u00e5\u00e3\u0001\u0000\u0000\u0000\u00e5\u00e6\u0001\u0000"+
		"\u0000\u0000\u00e6\'\u0001\u0000\u0000\u0000\u00e7\u00e5\u0001\u0000\u0000"+
		"\u0000\u00e8\u00e9\u0007\u0001\u0000\u0000\u00e9)\u0001\u0000\u0000\u0000"+
		"\u00ea\u00eb\u0007\u0002\u0000\u0000\u00eb+\u0001\u0000\u0000\u0000\u00ec"+
		"\u00ed\u0007\u0003\u0000\u0000\u00ed-\u0001\u0000\u0000\u0000\u001619"+
		"?DM[cly\u0084\u008c\u0092\u0098\u00a4\u00a6\u00bb\u00c1\u00ca\u00d5\u00db"+
		"\u00dd\u00e5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}