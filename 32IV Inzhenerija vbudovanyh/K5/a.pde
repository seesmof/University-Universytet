int padding=10;
boolean zeroOver=false;
boolean fourtyOver=false;
boolean ninetyOver=false;
color highlightColor = color(245, 245, 245);
int fontSize=50;

void setup() {
  size(300*3, 100*3);
}

void draw() {
  update(mouseX,mouseY);
  background(255);
  stroke(50);
  textSize(fontSize);
  int size=width/3;

  if (zeroOver) fill(highlightColor);
  else fill(255);
  rect(padding, padding, width/3-padding*2, height-padding*2);
  fill(0);
  text("0", (padding+width/3)/2-(fontSize/2), (height)/2);

  if (fourtyOver) fill(highlightColor);
  else fill(255);
  rect(padding+size, padding, width/3-padding*2, height-padding*2);
  fill(0);
  text("45", size*2-size/2-fontSize/2, (height)/2);

  if (ninetyOver) fill(highlightColor);
  else fill(255);
  rect(padding+size*2, padding, width/3-padding*2, height-padding*2);
  fill(0);
  text("90", size*3-size/2-fontSize/2, (height)/2);
}

void mousePressed() {
  if (zeroOver) println("0");
  if (fourtyOver) println("45");
  if (ninetyOver) println("90");
}

void update(int x,int y) {
  if (overZero()) {
    zeroOver=true;
    fourtyOver=false;
    ninetyOver=false;
  }
  else if (overyFourty()) {
    zeroOver=false;
    fourtyOver=true;
    ninetyOver=false;
  }
  else if (overNinety()) {
    zeroOver=false;
    fourtyOver=false;
    ninetyOver=true;
  }
  else zeroOver=fourtyOver=ninetyOver=false;
}

boolean overZero() { 
  int size=width/3;
  if (mouseX>=padding && mouseX<=size-padding && mouseY>=padding && mouseY<=size-padding) {
    return true;
  } else {
    return false;
  }
}
boolean overyFourty() { 
  int size=width/3;
  if (mouseX>=padding+size && mouseX<=size*2-padding && mouseY>=padding && mouseY<=size-padding) {
    return true;
  } else {
    return false;
  }
}
boolean overNinety() { 
  int size=width/3;
  if (mouseX>=padding+size*2 && mouseX<=size*3-padding && mouseY>=padding && mouseY<=size-padding) {
    return true;
  } else {
    return false;
  }
}