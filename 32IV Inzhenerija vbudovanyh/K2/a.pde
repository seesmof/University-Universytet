void setup() {
  size(512, 512);
  background(255);
}

void draw() {
  stroke(255, 202, 58);
  strokeWeight(7);

  line(pmouseX,pmouseY,mouseX,mouseY);
}
