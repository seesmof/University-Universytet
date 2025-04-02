int circleHorizontal=0;
int speed=7;
boolean goingRight=true;

void setup() {
  size(512, 512);
}

void draw() {
  background(255);
  noStroke();
  fill(137, 203, 37);

  ellipse(circleHorizontal, height/2, 33, 33);
  if (goingRight && circleHorizontal<width) {
    circleHorizontal+=speed;
  } else if (circleHorizontal>=width && goingRight) {
    goingRight=false;
    circleHorizontal-=speed;
  } else if (!goingRight && circleHorizontal>0) {
    circleHorizontal-=speed;
  } else if (!goingRight && circleHorizontal<=0) {
    circleHorizontal+=speed;
    goingRight=true;
  }
}
