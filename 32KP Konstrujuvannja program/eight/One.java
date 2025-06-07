import java.io.BufferedOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Random;

public class One {
  public static void main(String[] args) {
    int size = 10;
    int[] array = new int[size];
    Random generator = new Random();
    for (int i = 0; i < size; i++) {
      array[i] = generator.nextInt(size * 10);
    }

    System.out.print("Generated array: ");
    for (int i : array) {
      System.out.print(i + " ");
    }
    System.out.println();

    int[] modified = Arrays.copyOf(array, size);
    int position = size / 2;
    int value = generator.nextInt(size);
    Arrays.fill(modified, position, size, value);
    System.out.print("Filled array: ");
    for (int i : modified) {
      System.out.print(i + " ");
    }

    String fileName = "results.txt";
    try {
      FileWriter writer = new FileWriter(fileName);
      writer.write(Arrays.toString(array));
      writer.write("\n");
      writer.write(Arrays.toString(modified));
      writer.close();
    } catch (IOException exception) {
      exception.printStackTrace();
    }
  }
}