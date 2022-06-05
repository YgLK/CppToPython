// Generated from e:\python_projects\compilation_theory\antlr_approach\Hello.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class HelloParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, ID=2, WS=3, PLUS=4, MINUS=5, DPLUS=6, DMINUS=7, MUL=8, DIV=9, 
		MOD=10, ESC=11, RPARENTH=12, LPARENTH=13, LSQUARE=14, RSQUARE=15, LBRACE=16, 
		RBRACE=17, COLON=18, SEMICOLON=19, COMMA=20, DOT=21, GTHAN=22, LTHAN=23, 
		EQUAL=24, DEQUAL=25, GREATER_EQUAL=26, LESS_EQUAL=27, NOEQUAL=28, LBIT=29, 
		RBIT=30, INT=31, FLOAT=32, CHAR=33, STRING=34, BOOL=35, VOID=36, WHILE=37, 
		FOR=38, IF=39, ELSE=40, TRUE=41, FALSE=42, CIN=43, COUT=44, MAIN=45, USING=46, 
		NAMESPACE=47, STD=48, INCLUDE=49, HASH=50, RETURN=51, BREAK=52, CONTINUE=53, 
		DELETE=54, ENDL=55, CLASS=56, PUBLIC=57, PRIVATE=58, PROTECTED=59, STRINGVAR=60, 
		COMMENTVAR=61, FLOATVAR=62, INTVAR=63, VARNAME=64;
	public static final int
		RULE_hi = 0;
	private static String[] makeRuleNames() {
		return new String[] {
			"hi"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'hello'", null, null, "'+'", "'-'", "'++'", "'--'", "'*'", "'/'", 
			"'%'", "'\\'", "')'", "'('", "'['", "']'", "'{'", "'}'", "':'", "';'", 
			"','", "'.'", "'>'", "'<'", "'='", "'=='", "'>='", "'<='", "'!='", "'<<'", 
			"'>>'", "'int'", "'float'", "'cha'", "'string'", "'bool'", "'void'", 
			"'while'", "'fo'", "'if'", "'else'", "'true'", "'false'", "'cin'", "'cout'", 
			"'main'", "'using'", "'namespace'", "'std'", "'include'", "'#'", "'return'", 
			"'break'", "'continue'", "'delete'", "'endl'", "'class'", "'public'", 
			"'private'", "'protected'", "'"([^\\\n]|(\\.))*?"'", "'^//.*'", "'-?d*.{0,1}d+'", 
			"'-?d+'", "'[a-zA-Z_][a-zA-Z_0-9]*'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, "ID", "WS", "PLUS", "MINUS", "DPLUS", "DMINUS", "MUL", "DIV", 
			"MOD", "ESC", "RPARENTH", "LPARENTH", "LSQUARE", "RSQUARE", "LBRACE", 
			"RBRACE", "COLON", "SEMICOLON", "COMMA", "DOT", "GTHAN", "LTHAN", "EQUAL", 
			"DEQUAL", "GREATER_EQUAL", "LESS_EQUAL", "NOEQUAL", "LBIT", "RBIT", "INT", 
			"FLOAT", "CHAR", "STRING", "BOOL", "VOID", "WHILE", "FOR", "IF", "ELSE", 
			"TRUE", "FALSE", "CIN", "COUT", "MAIN", "USING", "NAMESPACE", "STD", 
			"INCLUDE", "HASH", "RETURN", "BREAK", "CONTINUE", "DELETE", "ENDL", "CLASS", 
			"PUBLIC", "PRIVATE", "PROTECTED", "STRINGVAR", "COMMENTVAR", "FLOATVAR", 
			"INTVAR", "VARNAME"
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
	public String getGrammarFileName() { return "Hello.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public HelloParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class HiContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(HelloParser.ID, 0); }
		public HiContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_hi; }
	}

	public final HiContext hi() throws RecognitionException {
		HiContext _localctx = new HiContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_hi);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2);
			match(T__0);
			setState(3);
			match(ID);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B\b\4\2\t\2\3\2\3"+
		"\2\3\2\3\2\2\2\3\2\2\2\2\6\2\4\3\2\2\2\4\5\7\3\2\2\5\6\7\4\2\2\6\3\3\2"+
		"\2\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}