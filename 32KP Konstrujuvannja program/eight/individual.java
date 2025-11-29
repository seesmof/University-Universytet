import java.io.PrintStream;
import java.lang.reflect.Field;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Collections;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.concurrent.TimeUnit;

import static java.nio.charset.StandardCharsets.UTF_8;

public class individual {
  public static void main(String[] args) {
    SortedSet<String> set = new TreeSet<>();
    while (true) {
      LocalDateTime dateTime = LocalDateTime.now();
      DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd.MM.yyyy HH:mm:ss:AA");
      System.out.println(dateTime.format(formatter) + " ");
      DateTimeFormatter result = DateTimeFormatter.ofPattern("AA:ss:hh dd.MM.yyyy");
      set.add(dateTime.format(result));
      System.out.println(set);
      try {
        Thread.sleep(1000);
      } catch (InterruptedException exception) {
        exception.printStackTrace();
      }
    }
  }
}
