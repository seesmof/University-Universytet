/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package personal.company;

import personal.company.Employee;

/**
 *
 * @author seesm
 */
public class Company {
    public static void main(String[] args) {
        Employee employee = new Employee();
        employee.firstName = "Oleh";
        employee.lastName = "Onyshchenko";
        employee.middleName = "Antonovych";
        employee.birthDate = "2005-09-21";
        employee.acceptEmployee("Farming", "Plow driver", 10);
    }
}
