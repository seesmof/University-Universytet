void setup() {
  size(640, 480);
  background(255);
}

void resetBackground() {
  fill(255);
  // up left
  rect(0,0,width/2,height/2);
  // up right
  rect(width/2,0,width,height/2);
  // down left
  rect(0,height/2,width/2,height/2);
  // down right
  rect(width/2,height/2,width,height);

  fill(0);
  line(width/2, 0, width/2, height);
  line(0, height/2, width, height/2);
}

void draw() {
  println(mouseX,mouseY);
  if (mouseX<width/2 && mouseY<height/2) {
    resetBackground();
    fill(255,255,0);
    rect(0, 0, width/2, height/2);
  } else if (mouseX>=width/2 && mouseY<height/2) {
    resetBackground();
    fill(255,255,0);
    rect(width/2, 0, width, height/2);
  } else if (mouseX<width/2 && mouseY>=height/2) {
    resetBackground();
    fill(255,255,0);
    rect(0, height/2, width/2, height);
  } else if (mouseX>=width/2 && mouseY>=height/2) {
    resetBackground();
    fill(255,255,0);
    rect(width/2, height/2, width, height);
  }
}
