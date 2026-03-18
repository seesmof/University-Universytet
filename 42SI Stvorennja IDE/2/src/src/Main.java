import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.CharStreams;
import gen.MainParser;
import gen.MainLexer;

public
class Main {
    public static void main(String[] args) {
        MainLexer lexer = new MainLexer(CharStreams.fromString("5+2+3"));
        MainParser parser = new MainParser(new CommonTokenStream(lexer));

        parser.start();
        System.out.println("executed");
    }
}
