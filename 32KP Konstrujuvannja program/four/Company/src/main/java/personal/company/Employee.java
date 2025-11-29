/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package personal.company;

/**
 *
 * @author seesm
 */
public class Employee extends Human {
  String departament;
  String position;
  int salary;

  void acceptEmployee(String departament, String position, int salary) {
    this.departament = departament;
    this.position = position;
    this.salary = salary != 0 ? salary : 10;
    System.out.println(super.lastName + " " + super.firstName + " " + super.middleName
        + " is accepted to departament \'" + this.departament + "\' on a position of \'" + this.position
        + "\' for a salary of " + this.salary + ".");
  }

  void fireEmployee() {
    this.departament = "";
    this.position = "";
    System.out.println(super.lastName + " " + super.firstName + " " + super.middleName + " is fired from the job.");
  }
}
