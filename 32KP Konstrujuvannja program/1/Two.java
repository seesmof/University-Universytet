import java.util.Collections;
import java.util.Scanner;
import java.util.TreeMap;

class Two {
  public static void showMatrix(int[][] matrix) {
    System.out.println();
    for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix.length; j++) {
        if (i == j) {
          System.out.print("\033[0;1m" + matrix[i][j] + "\033[0m ");
        } else {
          System.out.print(matrix[i][j] + " ");
        }
      }
      System.out.println();
    }
    System.out.println();
  }

  public static void main(String[] args) {
    Scanner inputReader = new Scanner(System.in);

    // Отримання розміру матриці
    int matrixSize;
    System.out.print("Please enter matrix size: ");
    matrixSize = inputReader.nextInt();

    // Заповнення
    int[][] matrix = new int[matrixSize][matrixSize];
    TreeMap<Integer, String> numbers = new TreeMap<Integer, String>(Collections.reverseOrder());
    for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix.length; j++) {
        int readableRow = i + 1;
        int readableCol = j + 1;
        System.out.print("Please enter element on row " + readableRow + " and col " + readableCol + ": ");

        int givenElement = inputReader.nextInt();
        matrix[i][j] = givenElement;
        String position = i + "," + j;
        numbers.put(givenElement, position);
      }
    }
    System.out.println();

    int matrixSizeCounter = 0;
    for (Integer key : numbers.keySet()) {
      if (matrixSizeCounter >= matrixSize) {
        break;
      }

      String value = numbers.get(key);
      String[] positionParts = value.split(",");
      int positionRow = Integer.parseInt(positionParts[0]);
      int positionCol = Integer.parseInt(positionParts[1]);

      System.out.println(key + ": row " + positionRow + " and col " + positionCol);

      int neededRow = matrixSizeCounter;
      int neededCol = matrixSizeCounter;
      System.out.println("Needs to be on row " + neededRow + " and on col " + neededCol);
      String neededPosition = neededRow + "," + neededCol;

      int swappedElement = matrix[neededRow][neededCol];
      int currentElement = matrix[positionRow][positionCol];
      matrix[neededRow][neededCol] = currentElement;
      matrix[positionRow][positionCol] = swappedElement;

      showMatrix(matrix);
      numbers.put(key, neededPosition);

      matrixSizeCounter += 1;
    }

    inputReader.close();
  }
}