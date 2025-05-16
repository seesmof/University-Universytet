boolean stopped=false;
int lastX=0;
int lastY=0;

void setup() {
  size(480, 120);
}

void draw() {
  background(94, 141, 223);
  noStroke();
  fill(255);

  if (!stopped) {
    lastX=mouseX;
    lastY=mouseY;
  }
  ellipse(lastX, lastY, 50, 50);
}

void mousePressed() {
  stopped=!stopped;
}
