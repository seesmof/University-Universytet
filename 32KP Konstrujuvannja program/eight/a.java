import java.io.PrintStream;
import java.lang.reflect.Field;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.concurrent.TimeUnit;

import static java.nio.charset.StandardCharsets.UTF_8;

public class a {
  public static void main(String[] args) {
    while (true) {
      LocalDateTime dateTime = LocalDateTime.now();
      DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd.MM.yyyy HH:mm:ss:AA");
      System.out.println(dateTime.format(formatter));
      try {
        Thread.sleep(1000);
      } catch (InterruptedException exception) {
        exception.printStackTrace();
      }
    }
  }
}
