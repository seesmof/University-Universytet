import java.io.File;
import java.io.IOException;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Queue;
import java.util.Random;
import java.util.Scanner;
import java.util.Stack;

public class Product {
  public static void main(String[] args) {
    ArrayList<Map<String, String>> products = new ArrayList<>();
    String fileName = "products.txt";
    try {
      File file = new File(fileName);
      Scanner scanner = new Scanner(file);
      while (scanner.hasNextLine()) {
        String[] values = scanner.nextLine().split(",");
        Map<String, String> product = new LinkedHashMap<String, String>();
        product.put("id", values[0]);
        product.put("name", values[1]);
        product.put("manufacturer", values[2]);
        product.put("price", values[3]);
        product.put("expiresInDays", values[4]);
        product.put("amount", values[5]);
        products.add(product);
      }
    } catch (IOException exception) {
      exception.printStackTrace();
    }

    String name = "Potato";
    System.out.println("Products with " + name + " name:");
    for (Map<String, String> map : products) {
      if (!map.get("name").equals(name))
        continue;
      System.out.println("- " + map.get("name") + " from " + map.get("manufacturer") + " epxires in "
          + map.get("expiresInDays") + " days.");
    }

    name = "Tomato";
    int price = 60;
    System.out.println("\nProducts of name " + name + " with price less than " + price + ":");
    for (Map<String, String> map : products) {
      if (Integer.parseInt(map.get("price")) > price)
        continue;
      System.out.println("- " + map.get("name") + " costs " + map.get("price"));
    }

    int expiryDays = 20;
    System.out.println("\nProducts that expire in less than " + expiryDays + " days:");
    for (Map<String, String> map : products) {
      if (Integer.parseInt(map.get("expiresInDays")) > expiryDays)
        continue;
      System.out.println("- " + map.get("name") + " with " + map.get("amount") + " pieces in a bunch, from "
          + map.get("manufacturer") + " expires in "
          + map.get("expiresInDays") + " days");
    }

    Stack Is = new Stack<>();
    Stack Us = new Stack<>();
    int n = 5;
    Random numberGetter = new Random();
    for (int i = 0; i < n; i++) {
      Is.push(numberGetter.nextInt(n * 10));
      Us.push(numberGetter.nextInt(n * 10));
    }
  }
}