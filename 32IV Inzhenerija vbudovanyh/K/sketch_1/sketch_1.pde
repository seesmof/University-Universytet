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

  fill(255);

  // face
  ellipse(120, 120, 20, 20);
  ellipse(187,127,12,12);
  ellipse(207,129,12,12);
  arc(187, 147, 27, 12, 0, PI/4.0);
}
