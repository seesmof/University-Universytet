import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Stack;

public class Phone {
  public static void main(String[] args) {
    ArrayList<Map<String, String>> phones = new ArrayList<Map<String, String>>();
    try {
      File file = new File("phones.txt");
      Scanner scanner = new Scanner(file);
      while (scanner.hasNextLine()) {
        String[] values = scanner.nextLine().split(",");
        Map<String, String> phone = new LinkedHashMap<>();
        phone.put("id", values[0]);
        phone.put("surname", values[1]);
        phone.put("name", values[2]);
        phone.put("middleName", values[3]);
        phone.put("address", values[4]);
        phone.put("cardNumber", values[5]);
        phone.put("debit", values[6]);
        phone.put("credit", values[7]);
        phone.put("cityTime", values[8]);
        phone.put("interTime", values[9]);
        phones.add(phone);
      }
    } catch (IOException e) {
      e.printStackTrace();
    }

    Integer cityTime = 50;
    System.out.println("\nCustomers with inner city time of more than " + cityTime + ": ");
    for (Map<String, String> map : phones) {
      if (Integer.parseInt(map.get("cityTime")) <= cityTime)
        continue;
      System.out.println("- " + map.get("name") + " from " + map.get("address") + " with credit card number of "
          + map.get("cardNumber") + " has inner city limit of " + map.get("cityTime"));
    }

    System.out.println("\nCustomers who used intercity time:");
    for (Map<String, String> map : phones) {
      if (Integer.parseInt(map.get("interTime")) <= 0)
        continue;
      System.out.println(
          "- " + map.get("surname") + " " + map.get("name") + " used " + map.get("interTime") + " intercity minutes");
    }

    System.out.println("\nAlphabetical customers:");
    for (char c = 'A'; c <= 'Z'; c++) {
      System.out.print(c + " ");
      for (Map<String, String> map : phones) {
        if (!map.get("name").startsWith(String.valueOf(c)))
          continue;
        System.out.print(map.get("name"));
      }
      System.out.println();
    }

    // Stacks
    System.out.println("\nStacks");

    Stack<Integer> one = new Stack<>();
    Stack<Integer> two = new Stack<>();
    for (int i = 0; i < 5; i++) {
      one.push(i);
    }
    for (int j = 4; j >= 0; j--) {
      two.push(j);
    }
    System.out.println("One: " + one);
    System.out.println("Two: " + two);
    Stack<Integer> oneNew = new Stack<>();
    Stack<Integer> twoNew = new Stack<>();
    for (int i = 0; i < 5; i++) {
      int fromOne = (int) one.pop();
      int fromTwo = (int) two.pop();
      oneNew.push(fromOne);
      twoNew.push(fromTwo);
    }
    System.out.println("One: " + oneNew);
    System.out.println("Two: " + twoNew);
  }
}