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

  static Integer getSinus(Integer x, Integer n) {
    Double angle = Double.valueOf(x / n);
    Double calculatedAngle = Math.sin(angle);
    DecimalFormat formatter = new DecimalFormat("#0.000000000000000");
    System.out.println(formatter.format(calculatedAngle));
    return calculatedAngle.intValue();
  }

  static Double getTangence(Double x, Double n) {
    Double angle = Double.valueOf(x / n);
    Double res = Math.tan(angle);
    DecimalFormat formatter = new DecimalFormat("#0.000000000000000");
    System.out.println(formatter.format(res));
    return res;
  }

  static Integer getTangence(Integer x, Integer n) {
    Double angle = Double.valueOf(x / n);
    Double calculatedAngle = Math.tan(angle);
    DecimalFormat formatter = new DecimalFormat("#0.000000000000000");
    System.out.println(formatter.format(calculatedAngle));
    return calculatedAngle.intValue();
  }

  static Float getCosinus(Float x, Float n) {
    Float angle = Float.valueOf(x / n);
    Float res = (float) Math.cos(angle);
    DecimalFormat formatter = new DecimalFormat("#0.000000000000000");
    System.out.println(formatter.format(res));
    return res;
  }

  static Long getCosinus(Long x, Long n) {
    Double angle = Double.valueOf(x / n);
    Double calculatedAngle = Math.cos(angle);
    DecimalFormat formatter = new DecimalFormat("#0.000000000000000");
    System.out.println(formatter.format(calculatedAngle));
    return calculatedAngle.longValue();
  }

  static Float getCotangent(Float x, Float n) {
    Float angle = Float.valueOf(x / n);
    Float res = (float) (1 / Math.tan(angle));
    DecimalFormat formatter = new DecimalFormat("#0.000000000000000");
    System.out.println(formatter.format(res));
    return res;
  }

  static Long getCotangent(Long x, Long n) {
    Double angle = Double.valueOf(x / n);
    Double calculatedAngle = 1 / Math.tan(angle);
    DecimalFormat formatter = new DecimalFormat("#0.000000000000000");
    System.out.println(formatter.format(calculatedAngle));
    return calculatedAngle.longValue();
  }

  public static void main(String[] args) {
    System.out.print("Sinus Double: ");
    getSinus(1.0, 3.0);
    System.out.print("Sinus Integer: ");
    getSinus(9, 3);

    System.out.println("");
    System.out.print("Tangent Double: ");
    getTangence(1.0, 3.0);
    System.out.print("Tangent Integer: ");
    getTangence(9, 3);

    System.out.println("");
    System.out.print("Cosinus Float: ");
    getCosinus(1.0f, 3.0f);
    System.out.print("Cosinus Long: ");
    getCosinus(Long.valueOf(9), Long.valueOf(3));

    System.out.println("");
    System.out.print("Cotangent Float: ");
    getCotangent(1.0f, 3.0f);
    System.out.print("Cotangent Long: ");
    getCotangent(Long.valueOf(9), Long.valueOf(3));
  }
}
