import java.util.Scanner;

class Two {
  public static void main(String[] args) {
    Scanner inputReader = new Scanner(System.in);
    System.out.print("Please enter matrix dimensions: ");
    int matrixSize = inputReader.nextInt();

    int[][] givenMatrix = new int[matrixSize][matrixSize];
    for (int i = 0; i < matrixSize; i++) {
      for (int j = 0; j < matrixSize; j++) {
        int readableRow = i + 1;
        int readableColumn = j + 1;
        System.out.print("Enter matrix's element on row " + readableRow + ", column " + readableColumn + ": ");
        int givenNumber = inputReader.nextInt();
        givenMatrix[i][j] = givenNumber;
      }
    }

    for (int i = 0; i < givenMatrix.length; i++) {
      for (int j = 0; j < givenMatrix.length; j++) {
        System.out.print(givenMatrix[i][j] + " ");
      }
      System.out.println();
    }

    int[] largestNumbers = new int[matrixSize];
  }
}