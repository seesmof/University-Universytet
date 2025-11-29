import java.util.Collections;
import java.util.Scanner;
import java.util.TreeMap;

class Two {
  public static void showMatrix(int[][] matrix) {
    System.out.println();
    for (int row = 0; row < matrix.length; row++) {
      for (int col = 0; col < matrix.length; col++) {
        if (row == col) {
          System.out.print("\033[0;1m" + matrix[row][col] + "\033[0m ");
        } else {
          System.out.print(matrix[row][col] + " ");
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
    for (int row = 0; row < matrix.length; row++) {
      for (int col = 0; col < matrix.length; col++) {
        int readableRow = row + 1;
        int readableCol = col + 1;
        System.out.print("Please enter element on row " + readableRow + " and col " + readableCol + ": ");

        int givenElement = inputReader.nextInt();
        matrix[row][col] = givenElement;
        String position = row + "," + col;
        numbers.put(givenElement, position);
      }
    }
    showMatrix(matrix);

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
      String neededPosition = neededRow + "," + neededCol;
      System.out.println("Needs to be on row " + neededRow + " and on col " + neededCol);

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