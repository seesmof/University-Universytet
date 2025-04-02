int ballHorizontal=0;
int ballVertical=0;
int speed=7;
boolean goingUp=false;

void setup() {
  size(512, 512);
}

void draw() {
  background(255);
  noStroke();
  fill(25, 130, 196);

  ellipse(ballHorizontal, ballVertical, 33, 33);
  if (ballHorizontal<=height && ballVertical<=width) {
    if (goingUp) {
      goingUp=false;
      ballHorizontal+=speed;
      ballVertical+=speed;
    } else {
      ballHorizontal-=speed;
      ballVertical-=speed;
    }
  }
  println(ballHorizontal,ballVertical,width,height);
}
