import java.util.Scanner;
import java.util.TreeMap;

class Three {
  public static void showMatrix(int[][] matrix) {
    System.out.println();
    for (int row = 0; row < matrix.length; row++) {
      for (int col = 0; col < matrix.length; col++) {
        System.out.print(matrix[row][col] + " ");
      }
      System.out.println();
    }
    System.out.println();
  }

  public static void main(String[] args) {
    Scanner inputReader = new Scanner(System.in);
    int matrixSize;
    System.out.print("Please enter matrix size: ");
    matrixSize = inputReader.nextInt();

    int[][] matrix = new int[matrixSize][matrixSize];
    for (int row = 0; row < matrix.length; row++) {
      for (int col = 0; col < matrix.length; col++) {
        int readableRow = row + 1;
        int readableCol = col + 1;
        System.out.print("Please enter element on row " + readableRow + " and col " +
            readableCol + ": ");

        int givenElement = inputReader.nextInt();
        matrix[row][col] = givenElement;
      }
    }
    showMatrix(matrix);

    TreeMap<String, Integer> mins = new TreeMap<String, Integer>();
    for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix.length; j++) {
        int thisElement = matrix[i][j];
        int minIndex = 0;
        int maxIndex = matrixSize - 1;

        int topLeft = Integer.MAX_VALUE;
        int top = Integer.MAX_VALUE;
        int topRight = Integer.MAX_VALUE;
        int right = Integer.MAX_VALUE;
        int bottomRight = Integer.MAX_VALUE;
        int bottom = Integer.MAX_VALUE;
        int bottomLeft = Integer.MAX_VALUE;
        int left = Integer.MAX_VALUE;

        if (i != minIndex && j != minIndex) {
          topLeft = matrix[i - 1][j - 1];
        }
        if (i != minIndex) {
          top = matrix[i - 1][j];
        }
        if (i != minIndex && j != maxIndex) {
          topRight = matrix[i - 1][j + 1];
        }
        if (j != maxIndex) {
          right = matrix[i][j + 1];
        }
        if (j != maxIndex && i != maxIndex) {
          bottomRight = matrix[i + 1][j + 1];
        }
        if (i != maxIndex) {
          bottom = matrix[i + 1][j];
        }
        if (i != maxIndex && j != minIndex) {
          bottomLeft = matrix[i + 1][j - 1];
        }
        if (j != minIndex) {
          left = matrix[i][j - 1];
        }

        if (thisElement < topLeft && thisElement < top && thisElement < topRight && thisElement < right
            && thisElement < bottom && thisElement < bottomRight && thisElement < bottomLeft && thisElement < left) {
          String position = i + "," + j;
          mins.put(position, thisElement);
        }
      }
    }

    System.out.println("Local minimums:");
    for (String key : mins.keySet()) {
      Integer value = mins.get(key);
      String[] valueParts = key.split(",");
      int row = Integer.parseInt(valueParts[0]) + 1;
      int col = Integer.parseInt(valueParts[1]) + 1;

      System.out.println("- Element " + value + " on row " + row + " and col " + col);
    }

    inputReader.close();
  }
}