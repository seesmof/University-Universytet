boolean stopped=false;
int circleSize=50;
int x=0;
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
    if (goingRight && x<width-circleSize/2) {
      x+=speed;
    } else if (goingRight && x>=width-circleSize/2) {
      goingRight=false;
      x-=speed;
    } else if (!goingRight && x>0+circleSize/2) {
      x-=speed;
    } else if (!goingRight && x<=0+circleSize/2) {
      goingRight=true;
      x+=speed;
    }
  }
  ellipse(x, height/2, circleSize, circleSize);
}

void mousePressed() {
  stopped=!stopped;
}
