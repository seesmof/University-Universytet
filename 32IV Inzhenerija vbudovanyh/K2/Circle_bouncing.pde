int x=0;
int speed=7;
boolean goingRight = true;

void setup() {
  size(512, 512);
}

void draw() {
  background(255);
  noStroke();
  fill(137, 203, 37);

  ellipse(x, height/2, 33, 33);
  if (goingRight && x<width) {
    x+=speed;
  } else if (x>=width && goingRight) {
    goingRight=false;
    x-=speed;
  } else if (!goingRight && x>0) {
    x-=speed;
  } else if (!goingRight && x<=0) {
    x+=speed;
    goingRight=true;
  }
  println(x,width);
}
