import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Student {
  public static void main(String[] args) {
    ArrayList<Map<String, String>> students = new ArrayList<>();
    ArrayList<String> faculties = new ArrayList<>();
    ArrayList<String> groups = new ArrayList<>();

    File studentsData = new File("students.txt");
    try {
      Scanner scanner = new Scanner(studentsData);
      while (scanner.hasNextLine()) {
        String[] values = scanner.nextLine().split(",");
        Map<String, String> data = new HashMap<>();
        data.put("id", values[0]);
        data.put("surname", values[1]);
        data.put("name", values[2]);
        data.put("middleName", values[3]);
        data.put("birthDate", values[4]);
        data.put("address", values[5]);
        data.put("phone", values[6]);
        data.put("faculty", values[7]);
        data.put("course", values[8]);
        data.put("group", values[9]);
        students.add(data);
        faculties.add(data.get("faculty"));
        groups.add(data.get("group"));
      }
    } catch (Exception exception) {
      exception.printStackTrace();
    }

    String faculty = "KNT";
    System.out.println("Students for " + faculty + " faculty:");
    for (Map<String, String> map : students) {
      if (!map.get("faculty").equals(faculty))
        continue;
      System.out.println("- " + map.get("surname") + " " + map.get("name") + ", " + map.get("faculty"));
    }

    String previousFaculty = "";
    System.out.println();
    for (String facultyString : faculties) {
      if (facultyString.equals(previousFaculty))
        continue;
      System.out.println("Students of " + facultyString + " faculty:");
      for (Map<String, String> map : students) {
        if (map.get("faculty").equals(facultyString))
          System.out.println("- " + map.get("surname") + " " + map.get("name") + ", " + map.get("group"));
      }
      previousFaculty = facultyString;
    }

    System.out.println();
    Integer year = 2005;
    System.out.println("Students born after year " + year + ":");
    for (Map<String, String> map : students) {
      if (Integer.valueOf(map.get("birthDate").split("-")[2]) < year)
        continue;
      System.out.println("- " + map.get("surname") + " " + map.get("name") + " " + map.get("group"));
    }

    System.out.println();
    String group = "KNT-122";
    System.out.println("Students from " + group + " group:");
    for (Map<String, String> map : students) {
      if (!map.get("group").equals(group))
        continue;
      System.out.println("- " + map.get("surname") + " " + map.get("name") + " " + map.get("middleName"));
    }

    ArrayList<Map<String, String>> reversedStudents = new ArrayList<>();
    for (int i = students.size() - 1; i >= 0; i--) {
      reversedStudents.add(students.get(i));
    }
    ArrayList<String> lines = new ArrayList<>();
    for (Map<String, String> map : reversedStudents) {
      String line = "";
      line += map.get("id") + ",";
      line += map.get("surname") + ",";
      line += map.get("name") + ",";
      line += map.get("middleName") + ",";
      line += map.get("birthDate") + ",";
      line += map.get("address") + ",";
      line += map.get("phone") + ",";
      line += map.get("faculty") + ",";
      line += map.get("course") + ",";
      line += map.get("group");
      lines.add(line);
    }

    Writer writer = null;
    try {
      writer = new BufferedWriter(new OutputStreamWriter(new FileOutputStream("students.txt"), "utf-8"));
      for (String line : lines) {
        writer.write(line + "\n");
      }
    } catch (IOException e) {
      e.printStackTrace();
    } finally {
      try {
        writer.close();
      } catch (Exception exception) {
        exception.printStackTrace();
      }
    }
  }
}
