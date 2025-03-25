void setup() {
  size(512, 512);
}

void draw() {
  background(255);
  stroke(177, 187, 57);
  line(0, 0, width, height);
  println(pmouseX,pmouseY);
}
