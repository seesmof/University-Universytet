import java.math.BigDecimal;
import java.math.RoundingMode;
import java.text.DecimalFormat;

public class a {
  static Double getSinus(Double x, Double n) {
    Double angle = Double.valueOf(x / n);
    Double res = Math.sin(angle);
    DecimalFormat formatter = new DecimalFormat("#0.000000000000000");
    System.out.println(formatter.format(res));
    return res;
  }

  public static void main(String[] args) {
    getSinus(1.0, 3.0);
  }
}
