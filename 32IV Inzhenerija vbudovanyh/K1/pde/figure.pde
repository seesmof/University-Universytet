void setup() {
  size(400, 400);
}

void draw() {
  background(255);
  fill(120, 77, 32, 77);
  noStroke();

  // body
  ellipse(200, 200, 70, 80);
  rect(177, 108, 40, 52);

  stroke(120, 77, 32, 77);
  strokeWeight(3);

  // arms & legs
  line(171, 177, 132, 132);
  line(231, 183, 132, 132);
  line(189, 237, 180, 292);
  line(210, 237, 230, 292);

  // treasure
  stroke(253, 200, 63);
  line(120, 112, 120, 147);
  line(110, 123, 130, 123);

  stroke(120, 77, 32, 77);
  fill(255);

  // face
  ellipse(187, 127, 12, 12);
  ellipse(207, 129, 12, 12);
  arc(197, 147, 27, 12, 0, PI);

  fill(0, 0, 0, 73);
  noStroke();

  ellipse(187, 127, 5, 5);
  ellipse(207, 129, 5, 5);
}
