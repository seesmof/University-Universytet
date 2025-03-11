import java.util.Arrays;
import java.util.Collections;
import java.util.TreeMap;

class Two {
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
        System.out.print(el);
        String position = i + "," + j;
        numbers.put(el, position);
      }
      System.out.println();
    }

    for (int i = 0; i < matrixSize; i++) {

    }
  }
}