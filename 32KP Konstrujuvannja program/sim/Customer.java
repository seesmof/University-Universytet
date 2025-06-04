import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Customer {
  public static Comparator<Map<String, String>> mapComparator = new Comparator<Map<String, String>>() {
    public int compare(Map<String, String> one, Map<String, String> two) {
      return one.get("name").compareTo(two.get("name"));
    }
  };

  public static void main(String[] args) {
    ArrayList<Map<String, String>> customers = new ArrayList<>();
    try {
      File studentsData = new File("customer.txt");
      Scanner scanner = new Scanner(studentsData);
      while (scanner.hasNextLine()) {
        String[] values = scanner.nextLine().split(",");
        Map<String, String> data = new HashMap<>();
        data.put("id", values[0]);
        data.put("surname", values[1]);
        data.put("name", values[2]);
        data.put("middleName", values[3]);
        data.put("birthDate", values[4]);
        data.put("address", values[5]);
        data.put("cardNumber", values[6]);
        data.put("accountNumber", values[7]);
        customers.add(data);
      }
    } catch (Exception exception) {
      exception.printStackTrace();
    }

    customers.sort(mapComparator);
    for (Map<String, String> map : customers) {
      System.out.println("- " + map.get("name") + ", " + map.get("cardNumber"));
    }

    System.out.println();
    String min = "2222 0000 0000 0000";
    String max = "7777 0000 0000 0000";
    System.out.println("Customers with cards above " + min + " and below " + max);
    for (Map<String, String> map : customers) {
      if (Integer.parseInt(min.split(" ")[0]) <= Integer.valueOf(map.get("cardNumber").split(" ")[0])
          && Integer.parseInt(max.split(" ")[0]) >= Integer.valueOf(map.get("cardNumber").split(" ")[0]))
        System.out.println("- " + map.get("name") + ", " + map.get("cardNumber"));
    }
  }
}
