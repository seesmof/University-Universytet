void setup() {
  size(480, 120);
}

void draw() {
  background(94, 141, 223);
  println(mouseX,mouseY);
  noStroke();

  if (!mousePressed) fill(255);
  else fill(0);
  ellipse(mouseX, mouseY, 50, 50);
}
