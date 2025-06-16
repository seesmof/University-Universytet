import java.io.PrintStream;
import java.lang.reflect.Field;
import java.nio.ByteBuffer;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import static java.nio.charset.StandardCharsets.UTF_8;

public class a {
  public static void main(String[] args) {
    List<String> someList = new ArrayList<>();
    someList.add("Help");
    someList.add("please");
    System.out.println(someList);

    List<String> otherList = Collections.unmodifiableList(someList);
    otherList.add("Begging");
    System.out.println(someList);
  }
}

// java.util.Collections$UnmodifiableCollection.add(Collections.java:1075) at
// Main.main(Main.java:21)