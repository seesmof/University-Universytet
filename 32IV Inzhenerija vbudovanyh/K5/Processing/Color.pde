int padding=10;
boolean redOver=false;
boolean greenOver=false;
boolean blueOver=false;
color redColor = color(255, 0, 0);
color greenColor = color(0, 255, 0);
color blueColor = color(0, 0, 255);
color redHighlightColor = color(255, 100, 100);
color greenHighlightColor = color(100, 255, 100);
color blueHighlightColor = color(100, 100, 255);

void setup() {
  size(300*3, 100*3);
}

void draw() {
  update(mouseX,mouseY);
  background(255);
  noStroke();
  int size=width/3;

  if (redOver) fill(redHighlightColor);
  else fill(redColor);
  rect(padding, padding, width/3-padding*2, height-padding*2);

  if (greenOver) fill(greenHighlightColor);
  else fill(greenColor);
  rect(padding+size, padding, width/3-padding*2, height-padding*2);

  if (blueOver) fill(blueHighlightColor);
  else fill(blueColor);
  rect(padding+size*2, padding, width/3-padding*2, height-padding*2);
}

void mousePressed() {
  if (redOver) println("Red");
  if (greenOver) println("Green");
  if (blueOver) println("Blue");
}

void update(int x,int y) {
  if (overRed()) {
    redOver=true;
    greenOver=false;
    blueOver=false;
  }
  else if (overGreen()) {
    redOver=false;
    greenOver=true;
    blueOver=false;
  }
  else if (overBlue()) {
    redOver=false;
    greenOver=false;
    blueOver=true;
  }
  else redOver=greenOver=blueOver=false;
}

boolean overRed() { 
  int size=width/3;
  if (mouseX>=padding && mouseX<=size-padding && mouseY>=padding && mouseY<=size-padding) {
    return true;
  } else {
    return false;
  }
}
boolean overGreen() { 
  int size=width/3;
  if (mouseX>=padding+size && mouseX<=size*2-padding && mouseY>=padding && mouseY<=size-padding) {
    return true;
  } else {
    return false;
  }
}
boolean overBlue() { 
  int size=width/3;
  if (mouseX>=padding+size*2 && mouseX<=size*3-padding && mouseY>=padding && mouseY<=size-padding) {
    return true;
  } else {
    return false;
  }
}