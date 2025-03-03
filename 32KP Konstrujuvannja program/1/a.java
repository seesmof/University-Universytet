class a {
  public static void main(String[] args) {
    int[][] grid = new int[3][3];
    int counter = 0;
    for (int i = 0; i < grid.length; i++) {
      for (int j = 0; j < grid.length; j++) {
        grid[i][j] = counter;
        counter += 1;
      }
    }

    System.err.println("Grid:");
    for (int i = 0; i < grid.length; i++) {
      for (int j = 0; j < grid.length; j++) {
        System.err.print(grid[i][j] + " ");
      }
      System.err.println();
    }
  }
}