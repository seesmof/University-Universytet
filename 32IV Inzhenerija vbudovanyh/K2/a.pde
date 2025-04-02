int x=23;
int h=17;
int y=23;

void setup() {
  size(512, 512);
}

void draw() {
  background(255);

  stroke(177, 187, 57);
  fill(255);
  println(pmouseX,pmouseY);

  for (int i = 0; i < 7; ++i) {
    ellipse(i*22, i*23, i*7, i*12);
  }
}
