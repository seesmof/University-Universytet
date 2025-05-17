/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package personal.company;

import java.util.Vector;

import personal.company.Departament;
import personal.company.Employee;

/**
 *
 * @author seesm
 */
public class Position extends Departament {
  String positionName;
  Vector<String> positionResponsibilities;
  Vector<Employee> positionEmployees;

  void giveOrder(Employee employee, String order) {
    System.out.println(employee.firstName + " is given an order to " + order.toLowerCase() + ".");
  }

  void callAnEmployee(Employee employee) {
    System.out.println(employee.firstName + " is being called.");
  }
}
