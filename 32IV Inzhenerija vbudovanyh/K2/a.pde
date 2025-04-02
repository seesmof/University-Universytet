int rectangleWidth=77;
int rectangleHeight=77;
int firstColor=255;
int secondColor=0;

void setup() {
  size(512, 512);
  background(0,255,255);
}

void draw() {
  noStroke();

  fill(firstColor);
  rect(width/2-rectangleWidth, height/2-rectangleHeight, rectangleWidth, rectangleHeight);
  fill(secondColor);
  rect(width/2+rectangleWidth, height/2+rectangleHeight, rectangleWidth, rectangleHeight);
}
