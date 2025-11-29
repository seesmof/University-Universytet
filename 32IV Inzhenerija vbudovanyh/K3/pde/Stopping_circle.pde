boolean stopped=false;
int circleSize=50;
int circleHorizontal=0;
int speed=3;
boolean goingRight=true;

void setup() {
  size(480, 320);
}

void draw() {
  background(141, 255, 64);
  noStroke();
  fill(255);

  if (!stopped) {
    if (goingRight && circleHorizontal<width-circleSize/2) {
      circleHorizontal+=speed;
    } else if (goingRight && circleHorizontal>=width-circleSize/2) {
      goingRight=false;
      circleHorizontal-=speed;
    } else if (!goingRight && circleHorizontal>0+circleSize/2) {
      circleHorizontal-=speed;
    } else if (!goingRight && circleHorizontal<=0+circleSize/2) {
      goingRight=true;
      circleHorizontal+=speed;
    }
  }
  ellipse(circleHorizontal, height/2, circleSize, circleSize);
}

void mousePressed() {
  stopped=!stopped;
}
