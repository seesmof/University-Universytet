import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;

public class a {
  public static void main(String[] args) {
    String ab = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ";
    ByteBuffer buffer = StandardCharsets.UTF_8.encode(ab);

    String utf8EncodedString = StandardCharsets.UTF_8.decode(buffer).toString();
  }
}
