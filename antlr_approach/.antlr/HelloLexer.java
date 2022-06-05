// Generated from e:\python_projects\compilation_theory\antlr_approach\Hello.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class HelloLexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "ID", "WS", "PLUS", "MINUS", "DPLUS", "DMINUS", "MUL", "DIV", 
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


	public HelloLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Hello.g4"; }

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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B\u018d\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2\3\2\3\2\3\2\3\3\6\3\u008b\n\3\r\3"+
		"\16\3\u008c\3\4\6\4\u0090\n\4\r\4\16\4\u0091\3\4\3\4\3\5\3\6\3\6\3\7\3"+
		"\b\3\b\3\b\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\16\3\17\3\20\3\20\3\21"+
		"\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\27\3\27\3\30\3\30"+
		"\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35"+
		"\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3"+
		"\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3&"+
		"\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3+\3+"+
		"\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60"+
		"\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62"+
		"\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\64\3\64\3\64\3\64\3\64\3\64"+
		"\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66"+
		"\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\39\39\39"+
		"\39\39\39\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3<\3<\3<\3<\3<"+
		"\3<\3<\3<\3<\3<\3=\3>\3?\3@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A\3A"+
		"\3A\3A\3A\3A\3A\3A\3A\3A\3A\2\2B\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23"+
		"\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31"+
		"\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60"+
		"_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081B\3\2\4\3\2c"+
		"|\5\2\13\f\17\17\"\"\2\u018e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3"+
		"\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2"+
		"\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37"+
		"\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3"+
		"\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2"+
		"\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C"+
		"\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2"+
		"\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2"+
		"\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i"+
		"\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2"+
		"\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081"+
		"\3\2\2\2\3\u0083\3\2\2\2\5\u008a\3\2\2\2\7\u008f\3\2\2\2\t\u0095\3\2\2"+
		"\2\13\u0096\3\2\2\2\r\u0098\3\2\2\2\17\u0099\3\2\2\2\21\u009c\3\2\2\2"+
		"\23\u009d\3\2\2\2\25\u009f\3\2\2\2\27\u00a1\3\2\2\2\31\u00a3\3\2\2\2\33"+
		"\u00a4\3\2\2\2\35\u00a5\3\2\2\2\37\u00a6\3\2\2\2!\u00a8\3\2\2\2#\u00aa"+
		"\3\2\2\2%\u00ac\3\2\2\2\'\u00ae\3\2\2\2)\u00b0\3\2\2\2+\u00b2\3\2\2\2"+
		"-\u00b3\3\2\2\2/\u00b5\3\2\2\2\61\u00b7\3\2\2\2\63\u00b9\3\2\2\2\65\u00bc"+
		"\3\2\2\2\67\u00bf\3\2\2\29\u00c2\3\2\2\2;\u00c5\3\2\2\2=\u00c8\3\2\2\2"+
		"?\u00cb\3\2\2\2A\u00cf\3\2\2\2C\u00d5\3\2\2\2E\u00d9\3\2\2\2G\u00e0\3"+
		"\2\2\2I\u00e5\3\2\2\2K\u00ea\3\2\2\2M\u00f0\3\2\2\2O\u00f3\3\2\2\2Q\u00f6"+
		"\3\2\2\2S\u00fb\3\2\2\2U\u0100\3\2\2\2W\u0106\3\2\2\2Y\u010a\3\2\2\2["+
		"\u010f\3\2\2\2]\u0114\3\2\2\2_\u011a\3\2\2\2a\u0124\3\2\2\2c\u0128\3\2"+
		"\2\2e\u0130\3\2\2\2g\u0131\3\2\2\2i\u0138\3\2\2\2k\u013e\3\2\2\2m\u0147"+
		"\3\2\2\2o\u014e\3\2\2\2q\u0153\3\2\2\2s\u0159\3\2\2\2u\u0160\3\2\2\2w"+
		"\u0168\3\2\2\2y\u0172\3\2\2\2{\u0173\3\2\2\2}\u0174\3\2\2\2\177\u0175"+
		"\3\2\2\2\u0081\u0176\3\2\2\2\u0083\u0084\7j\2\2\u0084\u0085\7g\2\2\u0085"+
		"\u0086\7n\2\2\u0086\u0087\7n\2\2\u0087\u0088\7q\2\2\u0088\4\3\2\2\2\u0089"+
		"\u008b\t\2\2\2\u008a\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008a\3\2"+
		"\2\2\u008c\u008d\3\2\2\2\u008d\6\3\2\2\2\u008e\u0090\t\3\2\2\u008f\u008e"+
		"\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2\u0092"+
		"\u0093\3\2\2\2\u0093\u0094\b\4\2\2\u0094\b\3\2\2\2\u0095\n\3\2\2\2\u0096"+
		"\u0097\7/\2\2\u0097\f\3\2\2\2\u0098\16\3\2\2\2\u0099\u009a\7/\2\2\u009a"+
		"\u009b\7/\2\2\u009b\20\3\2\2\2\u009c\22\3\2\2\2\u009d\u009e\7\61\2\2\u009e"+
		"\24\3\2\2\2\u009f\u00a0\7\'\2\2\u00a0\26\3\2\2\2\u00a1\u00a2\7^\2\2\u00a2"+
		"\30\3\2\2\2\u00a3\32\3\2\2\2\u00a4\34\3\2\2\2\u00a5\36\3\2\2\2\u00a6\u00a7"+
		"\7_\2\2\u00a7 \3\2\2\2\u00a8\u00a9\7}\2\2\u00a9\"\3\2\2\2\u00aa\u00ab"+
		"\7\177\2\2\u00ab$\3\2\2\2\u00ac\u00ad\7<\2\2\u00ad&\3\2\2\2\u00ae\u00af"+
		"\7=\2\2\u00af(\3\2\2\2\u00b0\u00b1\7.\2\2\u00b1*\3\2\2\2\u00b2,\3\2\2"+
		"\2\u00b3\u00b4\7@\2\2\u00b4.\3\2\2\2\u00b5\u00b6\7>\2\2\u00b6\60\3\2\2"+
		"\2\u00b7\u00b8\7?\2\2\u00b8\62\3\2\2\2\u00b9\u00ba\7?\2\2\u00ba\u00bb"+
		"\7?\2\2\u00bb\64\3\2\2\2\u00bc\u00bd\7@\2\2\u00bd\u00be\7?\2\2\u00be\66"+
		"\3\2\2\2\u00bf\u00c0\7>\2\2\u00c0\u00c1\7?\2\2\u00c18\3\2\2\2\u00c2\u00c3"+
		"\7#\2\2\u00c3\u00c4\7?\2\2\u00c4:\3\2\2\2\u00c5\u00c6\7>\2\2\u00c6\u00c7"+
		"\7>\2\2\u00c7<\3\2\2\2\u00c8\u00c9\7@\2\2\u00c9\u00ca\7@\2\2\u00ca>\3"+
		"\2\2\2\u00cb\u00cc\7k\2\2\u00cc\u00cd\7p\2\2\u00cd\u00ce\7v\2\2\u00ce"+
		"@\3\2\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2\7q\2\2\u00d2"+
		"\u00d3\7c\2\2\u00d3\u00d4\7v\2\2\u00d4B\3\2\2\2\u00d5\u00d6\7e\2\2\u00d6"+
		"\u00d7\7j\2\2\u00d7\u00d8\7c\2\2\u00d8D\3\2\2\2\u00d9\u00da\7u\2\2\u00da"+
		"\u00db\7v\2\2\u00db\u00dc\7t\2\2\u00dc\u00dd\7k\2\2\u00dd\u00de\7p\2\2"+
		"\u00de\u00df\7i\2\2\u00dfF\3\2\2\2\u00e0\u00e1\7d\2\2\u00e1\u00e2\7q\2"+
		"\2\u00e2\u00e3\7q\2\2\u00e3\u00e4\7n\2\2\u00e4H\3\2\2\2\u00e5\u00e6\7"+
		"x\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7f\2\2\u00e9J"+
		"\3\2\2\2\u00ea\u00eb\7y\2\2\u00eb\u00ec\7j\2\2\u00ec\u00ed\7k\2\2\u00ed"+
		"\u00ee\7n\2\2\u00ee\u00ef\7g\2\2\u00efL\3\2\2\2\u00f0\u00f1\7h\2\2\u00f1"+
		"\u00f2\7q\2\2\u00f2N\3\2\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7h\2\2\u00f5"+
		"P\3\2\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9\7u\2\2\u00f9"+
		"\u00fa\7g\2\2\u00faR\3\2\2\2\u00fb\u00fc\7v\2\2\u00fc\u00fd\7t\2\2\u00fd"+
		"\u00fe\7w\2\2\u00fe\u00ff\7g\2\2\u00ffT\3\2\2\2\u0100\u0101\7h\2\2\u0101"+
		"\u0102\7c\2\2\u0102\u0103\7n\2\2\u0103\u0104\7u\2\2\u0104\u0105\7g\2\2"+
		"\u0105V\3\2\2\2\u0106\u0107\7e\2\2\u0107\u0108\7k\2\2\u0108\u0109\7p\2"+
		"\2\u0109X\3\2\2\2\u010a\u010b\7e\2\2\u010b\u010c\7q\2\2\u010c\u010d\7"+
		"w\2\2\u010d\u010e\7v\2\2\u010eZ\3\2\2\2\u010f\u0110\7o\2\2\u0110\u0111"+
		"\7c\2\2\u0111\u0112\7k\2\2\u0112\u0113\7p\2\2\u0113\\\3\2\2\2\u0114\u0115"+
		"\7w\2\2\u0115\u0116\7u\2\2\u0116\u0117\7k\2\2\u0117\u0118\7p\2\2\u0118"+
		"\u0119\7i\2\2\u0119^\3\2\2\2\u011a\u011b\7p\2\2\u011b\u011c\7c\2\2\u011c"+
		"\u011d\7o\2\2\u011d\u011e\7g\2\2\u011e\u011f\7u\2\2\u011f\u0120\7r\2\2"+
		"\u0120\u0121\7c\2\2\u0121\u0122\7e\2\2\u0122\u0123\7g\2\2\u0123`\3\2\2"+
		"\2\u0124\u0125\7u\2\2\u0125\u0126\7v\2\2\u0126\u0127\7f\2\2\u0127b\3\2"+
		"\2\2\u0128\u0129\7k\2\2\u0129\u012a\7p\2\2\u012a\u012b\7e\2\2\u012b\u012c"+
		"\7n\2\2\u012c\u012d\7w\2\2\u012d\u012e\7f\2\2\u012e\u012f\7g\2\2\u012f"+
		"d\3\2\2\2\u0130f\3\2\2\2\u0131\u0132\7t\2\2\u0132\u0133\7g\2\2\u0133\u0134"+
		"\7v\2\2\u0134\u0135\7w\2\2\u0135\u0136\7t\2\2\u0136\u0137\7p\2\2\u0137"+
		"h\3\2\2\2\u0138\u0139\7d\2\2\u0139\u013a\7t\2\2\u013a\u013b\7g\2\2\u013b"+
		"\u013c\7c\2\2\u013c\u013d\7m\2\2\u013dj\3\2\2\2\u013e\u013f\7e\2\2\u013f"+
		"\u0140\7q\2\2\u0140\u0141\7p\2\2\u0141\u0142\7v\2\2\u0142\u0143\7k\2\2"+
		"\u0143\u0144\7p\2\2\u0144\u0145\7w\2\2\u0145\u0146\7g\2\2\u0146l\3\2\2"+
		"\2\u0147\u0148\7f\2\2\u0148\u0149\7g\2\2\u0149\u014a\7n\2\2\u014a\u014b"+
		"\7g\2\2\u014b\u014c\7v\2\2\u014c\u014d\7g\2\2\u014dn\3\2\2\2\u014e\u014f"+
		"\7g\2\2\u014f\u0150\7p\2\2\u0150\u0151\7f\2\2\u0151\u0152\7n\2\2\u0152"+
		"p\3\2\2\2\u0153\u0154\7e\2\2\u0154\u0155\7n\2\2\u0155\u0156\7c\2\2\u0156"+
		"\u0157\7u\2\2\u0157\u0158\7u\2\2\u0158r\3\2\2\2\u0159\u015a\7r\2\2\u015a"+
		"\u015b\7w\2\2\u015b\u015c\7d\2\2\u015c\u015d\7n\2\2\u015d\u015e\7k\2\2"+
		"\u015e\u015f\7e\2\2\u015ft\3\2\2\2\u0160\u0161\7r\2\2\u0161\u0162\7t\2"+
		"\2\u0162\u0163\7k\2\2\u0163\u0164\7x\2\2\u0164\u0165\7c\2\2\u0165\u0166"+
		"\7v\2\2\u0166\u0167\7g\2\2\u0167v\3\2\2\2\u0168\u0169\7r\2\2\u0169\u016a"+
		"\7t\2\2\u016a\u016b\7q\2\2\u016b\u016c\7v\2\2\u016c\u016d\7g\2\2\u016d"+
		"\u016e\7e\2\2\u016e\u016f\7v\2\2\u016f\u0170\7g\2\2\u0170\u0171\7f\2\2"+
		"\u0171x\3\2\2\2\u0172z\3\2\2\2\u0173|\3\2\2\2\u0174~\3\2\2\2\u0175\u0080"+
		"\3\2\2\2\u0176\u0177\7]\2\2\u0177\u0178\7c\2\2\u0178\u0179\7/\2\2\u0179"+
		"\u017a\7|\2\2\u017a\u017b\7C\2\2\u017b\u017c\7/\2\2\u017c\u017d\7\\\2"+
		"\2\u017d\u017e\7a\2\2\u017e\u017f\7_\2\2\u017f\u0180\7]\2\2\u0180\u0181"+
		"\7c\2\2\u0181\u0182\7/\2\2\u0182\u0183\7|\2\2\u0183\u0184\7C\2\2\u0184"+
		"\u0185\7/\2\2\u0185\u0186\7\\\2\2\u0186\u0187\7a\2\2\u0187\u0188\7\62"+
		"\2\2\u0188\u0189\7/\2\2\u0189\u018a\7;\2\2\u018a\u018b\7_\2\2\u018b\u018c"+
		"\7,\2\2\u018c\u0082\3\2\2\2\5\2\u008c\u0091\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}