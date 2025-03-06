import java.util.Collections;
import java.util.TreeMap;

class a {
  public static void main(String[] args) {
    TreeMap<Integer, String> t = new TreeMap<Integer, String>(Collections.reverseOrder());
    t.put(8, "1,2");
    t.put(7, "1,1");
    System.out.println(t);
  }
}