void setup() {
  size(512, 512);
}

void draw() {
  background(255);

  stroke(177, 187, 57);
  fill(255);

  ellipse(mouseX, mouseY, height, 100);
  println(pmouseX,pmouseY);
}
