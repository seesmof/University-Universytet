import java.time.LocalDate;

package 4. Company;

public enum Gender {
  M("Male"),
  F("Female")

  private final String name;

  private Gender(String name) {
    this.name=name;
  }

  public String getName() {
    return this.name;
  }
}

public class Human {
  String lastName;
  String firstName;
  String middleName;
  LocalDate birthDate;
  Gender gender;
}
