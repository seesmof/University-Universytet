int rectangleWidth=77;
int rectangleHeight=77;
int firstColor=255;
boolean firstGoingUp=false;
int secondColor=0;
boolean secondGoingDown=false;
int speed=1;

void setup() {
  size(512, 512);
  background(0,255,255);
}

void draw() {
  noStroke();

  fill(firstColor);
  rect(width/2-rectangleWidth*2, height/2-rectangleHeight, rectangleWidth, rectangleHeight);
  if (!firstGoingUp && firstColor>=0) {
    firstColor-=speed;
  } else if (!firstGoingUp && firstColor<=0) {
    firstColor+=speed;
    firstGoingUp=true;
  } else if (firstGoingUp && firstColor<=255) {
    firstColor+=speed;
  } else if (firstGoingUp && firstColor>=255) {
    firstColor-=speed;
    firstGoingUp=false;
  }

  fill(secondColor);
  rect(width/2+rectangleWidth, height/2-rectangleHeight, rectangleWidth, rectangleHeight);
  if (!secondGoingDown && secondColor>=0) {
    secondColor-=speed;
  } else if (!secondGoingDown && secondColor<=0) {
    secondColor+=speed;
    secondGoingDown=true;
  } else if (secondGoingDown && secondColor<=255) {
    secondColor+=speed;
  } else if (secondGoingDown && secondColor>=255) {
    secondColor-=speed;
    secondGoingDown=false;
  }
}
