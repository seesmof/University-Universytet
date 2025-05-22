import javax.swing.JOptionPane;
int angle = 0;

void setup() {
  size(512, 512);
}

void draw() {
  background(255);
  noStroke();

  String enteredAngle = JOptionPane.showInputDialog(null, "Enter servo angle", "Enter", JOptionPane.PLAIN_MESSAGE);
  try {
    angle = Integer.parseInt(enteredAngle);
  } catch(NumberFormatException e) {
    JOptionPane.getRootFrame().dispose();
  }

  println(angle);
}