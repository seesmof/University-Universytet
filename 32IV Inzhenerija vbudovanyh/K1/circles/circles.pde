void setup() {
  size(412, 412);
}

void draw() {
  background(255);

  int opacity = 255;
  fill(255, 89, 94, opacity);
  int border = 0;
  strokeWeight(border);
  stroke(255, 89, 94, 37);
  ellipse(100, 100, 70, 70);

  opacity -= 75;
  fill(138, 201, 38, opacity);
  border += 10;
  strokeWeight(border);
  stroke(138, 201, 38, 37);
  ellipse(200, 200, 70, 70);

  opacity -= 75;
  fill(25, 130, 196, opacity);
  border += 10;
  strokeWeight(border);
  stroke(25, 130, 196, 37);
  ellipse(300, 300, 70, 70);
}
