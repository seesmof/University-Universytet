int circleHorizontal=0;
int speed=7;
boolean goingRight=true;
int circleHeight=33;

void setup() {
  size(512, 512);
}

void draw() {
  background(255);
  noStroke();
  fill(137, 203, 37);

  ellipse(circleHorizontal, height/2, circleHeight, circleHeight);
  if (goingRight && circleHorizontal-circleHeight/2<width-circleHeight) {
    circleHorizontal+=speed;
  } else if (goingRight && circleHorizontal>=width-circleHeight*2) {
    goingRight=false;
    circleHorizontal-=speed;
    println(circleHorizontal);
    println(width-circleHeight*2);
  } else if (!goingRight && circleHorizontal-circleHeight/2>0) {
    circleHorizontal-=speed;
  } else if (!goingRight && circleHorizontal-circleHeight/2<=0) {
    circleHorizontal+=speed;
    goingRight=true;
  }
}
