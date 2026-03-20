// Generated from d:/University-Universytet/42SI Stvorennja IDE/2/src/src/Main.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MainLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		INT=10, UNT=11, FLOAT=12, BOOL=13, NUMBER=14, NAME=15, WS=16, STRING=17, 
		SEMICOLON=18, LEFT_CURLY_BRACE=19, RIGHT_CURLY_BRACE=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"INT", "UNT", "FLOAT", "BOOL", "NUMBER", "NAME", "WS", "STRING", "SEMICOLON", 
			"LEFT_CURLY_BRACE", "RIGHT_CURLY_BRACE"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'fn'", "'('", "')'", "'vec!['", "']'", "'impl'", "'for'", "'in'", 
			"'..'", null, null, null, "'bool'", null, null, null, null, "';'", "'{'", 
			"'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "INT", "UNT", 
			"FLOAT", "BOOL", "NUMBER", "NAME", "WS", "STRING", "SEMICOLON", "LEFT_CURLY_BRACE", 
			"RIGHT_CURLY_BRACE"
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


	public MainLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Main.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0014\u0093\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0003\tW\b\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\nh\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0003\u000bp\b\u000b\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\r\u0004\rx\b\r\u000b\r\f\ry\u0001\u000e\u0004\u000e}"+
		"\b\u000e\u000b\u000e\f\u000e~\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u0010\u0001\u0010\u0005\u0010\u0087\b\u0010\n\u0010\f\u0010"+
		"\u008a\t\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0088\u0000\u0014\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f"+
		"\u001f\u0010!\u0011#\u0012%\u0013\'\u0014\u0001\u0000\u0003\u0001\u0000"+
		"09\u0003\u0000AZ__az\u0003\u0000\t\n\r\r  \u009e\u0000\u0001\u0001\u0000"+
		"\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000"+
		"\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000"+
		"\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000"+
		"\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000"+
		"\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000"+
		"#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001"+
		"\u0000\u0000\u0000\u0001)\u0001\u0000\u0000\u0000\u0003,\u0001\u0000\u0000"+
		"\u0000\u0005.\u0001\u0000\u0000\u0000\u00070\u0001\u0000\u0000\u0000\t"+
		"6\u0001\u0000\u0000\u0000\u000b8\u0001\u0000\u0000\u0000\r=\u0001\u0000"+
		"\u0000\u0000\u000fA\u0001\u0000\u0000\u0000\u0011D\u0001\u0000\u0000\u0000"+
		"\u0013V\u0001\u0000\u0000\u0000\u0015g\u0001\u0000\u0000\u0000\u0017o"+
		"\u0001\u0000\u0000\u0000\u0019q\u0001\u0000\u0000\u0000\u001bw\u0001\u0000"+
		"\u0000\u0000\u001d|\u0001\u0000\u0000\u0000\u001f\u0080\u0001\u0000\u0000"+
		"\u0000!\u0084\u0001\u0000\u0000\u0000#\u008d\u0001\u0000\u0000\u0000%"+
		"\u008f\u0001\u0000\u0000\u0000\'\u0091\u0001\u0000\u0000\u0000)*\u0005"+
		"f\u0000\u0000*+\u0005n\u0000\u0000+\u0002\u0001\u0000\u0000\u0000,-\u0005"+
		"(\u0000\u0000-\u0004\u0001\u0000\u0000\u0000./\u0005)\u0000\u0000/\u0006"+
		"\u0001\u0000\u0000\u000001\u0005v\u0000\u000012\u0005e\u0000\u000023\u0005"+
		"c\u0000\u000034\u0005!\u0000\u000045\u0005[\u0000\u00005\b\u0001\u0000"+
		"\u0000\u000067\u0005]\u0000\u00007\n\u0001\u0000\u0000\u000089\u0005i"+
		"\u0000\u00009:\u0005m\u0000\u0000:;\u0005p\u0000\u0000;<\u0005l\u0000"+
		"\u0000<\f\u0001\u0000\u0000\u0000=>\u0005f\u0000\u0000>?\u0005o\u0000"+
		"\u0000?@\u0005r\u0000\u0000@\u000e\u0001\u0000\u0000\u0000AB\u0005i\u0000"+
		"\u0000BC\u0005n\u0000\u0000C\u0010\u0001\u0000\u0000\u0000DE\u0005.\u0000"+
		"\u0000EF\u0005.\u0000\u0000F\u0012\u0001\u0000\u0000\u0000GH\u0005i\u0000"+
		"\u0000HW\u00058\u0000\u0000IJ\u0005i\u0000\u0000JK\u00051\u0000\u0000"+
		"KW\u00056\u0000\u0000LM\u0005i\u0000\u0000MN\u00053\u0000\u0000NW\u0005"+
		"2\u0000\u0000OP\u0005i\u0000\u0000PQ\u00056\u0000\u0000QW\u00054\u0000"+
		"\u0000RS\u0005i\u0000\u0000ST\u00051\u0000\u0000TU\u00052\u0000\u0000"+
		"UW\u00058\u0000\u0000VG\u0001\u0000\u0000\u0000VI\u0001\u0000\u0000\u0000"+
		"VL\u0001\u0000\u0000\u0000VO\u0001\u0000\u0000\u0000VR\u0001\u0000\u0000"+
		"\u0000W\u0014\u0001\u0000\u0000\u0000XY\u0005u\u0000\u0000Yh\u00058\u0000"+
		"\u0000Z[\u0005u\u0000\u0000[\\\u00051\u0000\u0000\\h\u00056\u0000\u0000"+
		"]^\u0005u\u0000\u0000^_\u00053\u0000\u0000_h\u00052\u0000\u0000`a\u0005"+
		"u\u0000\u0000ab\u00056\u0000\u0000bh\u00054\u0000\u0000cd\u0005u\u0000"+
		"\u0000de\u00051\u0000\u0000ef\u00052\u0000\u0000fh\u00058\u0000\u0000"+
		"gX\u0001\u0000\u0000\u0000gZ\u0001\u0000\u0000\u0000g]\u0001\u0000\u0000"+
		"\u0000g`\u0001\u0000\u0000\u0000gc\u0001\u0000\u0000\u0000h\u0016\u0001"+
		"\u0000\u0000\u0000ij\u0005f\u0000\u0000jk\u00053\u0000\u0000kp\u00052"+
		"\u0000\u0000lm\u0005f\u0000\u0000mn\u00056\u0000\u0000np\u00054\u0000"+
		"\u0000oi\u0001\u0000\u0000\u0000ol\u0001\u0000\u0000\u0000p\u0018\u0001"+
		"\u0000\u0000\u0000qr\u0005b\u0000\u0000rs\u0005o\u0000\u0000st\u0005o"+
		"\u0000\u0000tu\u0005l\u0000\u0000u\u001a\u0001\u0000\u0000\u0000vx\u0007"+
		"\u0000\u0000\u0000wv\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000\u0000"+
		"yw\u0001\u0000\u0000\u0000yz\u0001\u0000\u0000\u0000z\u001c\u0001\u0000"+
		"\u0000\u0000{}\u0007\u0001\u0000\u0000|{\u0001\u0000\u0000\u0000}~\u0001"+
		"\u0000\u0000\u0000~|\u0001\u0000\u0000\u0000~\u007f\u0001\u0000\u0000"+
		"\u0000\u007f\u001e\u0001\u0000\u0000\u0000\u0080\u0081\u0007\u0002\u0000"+
		"\u0000\u0081\u0082\u0001\u0000\u0000\u0000\u0082\u0083\u0006\u000f\u0000"+
		"\u0000\u0083 \u0001\u0000\u0000\u0000\u0084\u0088\u0005\"\u0000\u0000"+
		"\u0085\u0087\t\u0000\u0000\u0000\u0086\u0085\u0001\u0000\u0000\u0000\u0087"+
		"\u008a\u0001\u0000\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000\u0088"+
		"\u0086\u0001\u0000\u0000\u0000\u0089\u008b\u0001\u0000\u0000\u0000\u008a"+
		"\u0088\u0001\u0000\u0000\u0000\u008b\u008c\u0005\"\u0000\u0000\u008c\""+
		"\u0001\u0000\u0000\u0000\u008d\u008e\u0005;\u0000\u0000\u008e$\u0001\u0000"+
		"\u0000\u0000\u008f\u0090\u0005{\u0000\u0000\u0090&\u0001\u0000\u0000\u0000"+
		"\u0091\u0092\u0005}\u0000\u0000\u0092(\u0001\u0000\u0000\u0000\u0007\u0000"+
		"Vgoy~\u0088\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}