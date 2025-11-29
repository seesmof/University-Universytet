import java.util.Scanner;

class One {
  public static boolean isNumberPalindrome(int number) {
    String stringNumber = "" + number;
    String reversedString = new StringBuilder(stringNumber).reverse().toString();

    if (stringNumber.equals(reversedString))
      return true;
    else
      return false;
  }

  public static void main(String[] args) {
    Scanner inputScanner = new Scanner(System.in);

    System.out.print("Please enter N, number of digits: ");
    int numberOfDigits = inputScanner.nextInt();

    int[] numbersArray = new int[numberOfDigits];
    for (int i = 0; i < numbersArray.length; i++) {
      int readableNumber = i + 1;
      System.out.print("Please enter digit number " + readableNumber + ": ");
      int thisNumber = inputScanner.nextInt();
      numbersArray[i] = thisNumber;
    }
    inputScanner.close();

    System.out.println("\nPalindrome numbers:");
    for (int i = 0; i < numbersArray.length; i++) {
      int thisNumber = numbersArray[i];
      boolean isThisNumberPalindrome = isNumberPalindrome(thisNumber);
      if (isThisNumberPalindrome)
        System.out.println("- " + thisNumber);
    }
  }
}