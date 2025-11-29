/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package personal.company;

import java.util.Arrays;
import java.util.Vector;

import personal.company.Departament;
import personal.company.Employee;
import personal.company.Position;

/**
 *
 * @author seesm
 */
public class Company {
    public static void main(String[] args) {
        Employee david = new Employee();
        david.lastName = "Salomon";
        david.firstName = "David";
        david.middleName = "Kristoffersen";

        Employee abraam = new Employee();
        abraam.lastName = "Ionathan";
        abraam.firstName = "Abraam";
        abraam.middleName = "Hansen";

        Employee ananias = new Employee();
        ananias.lastName = "Emil";
        ananias.firstName = "Ananias";
        ananias.middleName = "Simonsen";

        Departament farming = new Departament();
        farming.departamentName = "Farming";
        farming.numberOfWorkers = 3;
        farming.workingHours = 7;
        david.departament = farming.departamentName;
        abraam.departament = farming.departamentName;
        ananias.departament = farming.departamentName;

        Position sower = new Position();
        sower.positionName = "Sower of seeds";
        sower.positionResponsibilities = new Vector<>(Arrays.asList(
                "buy seeds",
                "keep seeds dry",
                "sow seeds"));
        Position harvester = new Position();
        harvester.positionName = "Harvester of produce";
        harvester.positionResponsibilities = new Vector<>(Arrays.asList(
                "keep tools clean",
                "prepare for harvest",
                "harvest the produce"));
        Position plower = new Position();
        plower.positionName = "Plower of ground";
        plower.positionResponsibilities = new Vector<>(Arrays.asList(
                "keep the plow working",
                "plow the ground",
                "keep the plow clean"));

        david.position = sower.positionName;
        sower.positionEmployees.add(david);
        abraam.position = harvester.positionName;
        harvester.positionEmployees.add(abraam);
        ananias.position = plower.positionName;
        plower.positionEmployees.add(ananias);

        sower.callAnEmployee(sower.positionEmployees.elementAt(0));
        harvester.callAnEmployee(harvester.positionEmployees.elementAt(0));
        plower.callAnEmployee(plower.positionEmployees.elementAt(0));

        sower.giveOrder(sower.positionEmployees.elementAt(0), "Buy more seeds");
        harvester.giveOrder(harvester.positionEmployees.elementAt(0), "Fix the tools");
        plower.giveOrder(plower.positionEmployees.elementAt(0), "Maintain the plow");

        System.out.println(ananias.firstName + " works in a departament called '" + ananias.departament + "' and works "
                + farming.workingHours + " hours per day.");
        ananias.fireEmployee();
    }
}
