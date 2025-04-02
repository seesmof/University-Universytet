int horizontal=0;
int vertical=0;
int speed=7;
boolean goingUp=false;

void setup() {
  size(512, 512);
}

void draw() {
  background(255);
  noStroke();
  fill(25, 130, 196);

  ellipse(horizontal, vertical, 33, 33);
  if (!goingUp && horizontal<width && vertical<height) {
    horizontal+=speed;
    vertical+=speed;
  } else if (!goingUp && horizontal>=width && vertical>=height) {
    goingUp=true;
    horizontal-=speed;
    vertical-=speed;
  } else if (goingUp && horizontal>0 && vertical>0) {
    horizontal-=speed;
    vertical-=speed;
  } else if (goingUp && horizontal<=0 && vertical<=0) {
    goingUp=false;
    horizontal+=speed;
    vertical+=speed;
  }
}
