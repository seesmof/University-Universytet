import java.util.HashMap;
import java.util.Map;

class a {
  public static void main(String[] args) {
    Map<Integer, Integer> testCases = new HashMap<Integer, Integer>();
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