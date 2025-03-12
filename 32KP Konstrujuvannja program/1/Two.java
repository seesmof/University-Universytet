import java.util.Arrays;
import java.util.Collections;
import java.util.Map;
import java.util.TreeMap;

class Two {
  public static void showMatrix(int[][] matrix) {
    for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix.length; j++) {
        System.out.print(matrix[i][j] + " ");
      }
      System.out.println();
    }
  }

  public static void main(String[] args) {
    int matrixSize = 3;
    int[][] matrix = new int[matrixSize][matrixSize];
    matrix[0][0] = 1;
    matrix[0][1] = 3;
    matrix[0][2] = 1;
    matrix[1][0] = 5;
    matrix[1][1] = 1;
    matrix[1][2] = 1;
    matrix[2][0] = 1;
    matrix[2][1] = 7;
    matrix[2][2] = 1;

    TreeMap<Integer, String> numbers = new TreeMap<Integer, String>(Collections.reverseOrder());

    for (int i = 0; i < matrix.length; i++) {
      for (int j = 0; j < matrix.length; j++) {
        int el = matrix[i][j];
        System.out.print(el + " ");
        String position = i + "," + j;
        numbers.put(el, position);
      }
      System.out.println();
    }

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

      System.out.println();
      showMatrix(matrix);
      System.out.println();
      numbers.put(key, neededPosition);

      matrixSizeCounter += 1;
    }
  }
}