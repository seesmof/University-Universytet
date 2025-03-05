import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

class Two {
  public static void main(String[] args) {
    Scanner inputReader = new Scanner(System.in);
    System.out.print("Please enter matrix dimensions: ");
    int matrixSize = inputReader.nextInt();
    List<Integer> allNumbers = new ArrayList<Integer>();

    int[][] givenMatrix = new int[matrixSize][matrixSize];
    for (int i = 0; i < matrixSize; i++) {
      for (int j = 0; j < matrixSize; j++) {
        int readableRow = i + 1;
        int readableColumn = j + 1;
        System.out.print("Enter matrix's element on row " + readableRow + ", column " + readableColumn + ": ");
        int givenNumber = inputReader.nextInt();
        givenMatrix[i][j] = givenNumber;
        allNumbers.add(givenNumber);
      }
    }

    System.err.println("\nEntered matrix:");
    for (int i = 0; i < givenMatrix.length; i++) {
      for (int j = 0; j < givenMatrix.length; j++) {
        System.out.print(givenMatrix[i][j] + " ");
      }
      System.out.println();
    }

    allNumbers.sort(Comparator.reverseOrder());
    int[] largestNumbers = new int[matrixSize];
    for (int i = 0; i < largestNumbers.length; i++) {
      largestNumbers[i] = allNumbers.get(i);
      System.out.println(largestNumbers[i]);
    }

    inputReader.close();
  }
}