import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintStream;
import java.lang.reflect.Field;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.concurrent.TimeUnit;

import static java.nio.charset.StandardCharsets.UTF_8;

public class two {
  public static void main(String[] args) {
    FileWriter writer;
    while (true) {
      LocalDateTime dateTime = LocalDateTime.now();
      DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd.MM.yyyy HH:mm:ss:AA");
      String formattedTime = dateTime.format(formatter);
      System.out.println(formattedTime);
      try {
        writer = new FileWriter("times.txt", true);
        writer.write(formattedTime + "\n");
        writer.close();
      } catch (IOException exception) {
        exception.printStackTrace();
      }

      try {
        Thread.sleep(1000);
      } catch (InterruptedException exception) {
        exception.printStackTrace();
      }
    }
  }
}
