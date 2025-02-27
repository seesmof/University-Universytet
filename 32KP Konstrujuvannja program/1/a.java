import java.util.Map;

class a {
  public static void main(String[] args) {
    Map<Integer, Integer> testCases = Map.of(1, 1, 2, 4, 7, 3);
    testCases.forEach((k, v) -> {
      System.err.println(k + " and " + v);
    });
  }

  public static int testTarget(int value, int target) {
    int result = 0;
    if (value > target)
      result = +1;
    else if (value < target)
      result = -1;
    else
      result = 0;
    return result;
  }
}