import java.io.PrintStream;
import java.lang.reflect.Field;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import static java.nio.charset.StandardCharsets.UTF_8;

public class a {
  public static void main(String[] args) {
    String ab = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ";
    PrintStream out = new PrintStream(System.out, true, UTF_8);
    out.println(ab);
  }
}
