#include <Servo.h>

Servo myservo;　//Servoオブジェクトの宣言

void setup() {
  Serial.begin(9600);
  myservo.attach(9);//9番ピンでサーボモータを動かす
  pinMode(2, INPUT_PULLUP); // Inputモードでプルアップ抵抗を有効に
  pinMode(LED_BUILTIN, OUTPUT);
  myservo.write(100); // angle
  digitalWrite(LED_BUILTIN, HIGH);
}
 
void loop(){
  static int flag=0;
  if(digitalRead(2)==LOW){
    flag=1;
  }
  else{
    if(flag==1){
      flag=0;
      Serial.write('1');
      delay(500);
    }
  }
  if(Serial.available()>0){
    char a = Serial.read();
    if(a=='o'){
      myservo.write(100); // angle
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if(a=='c'){
      myservo.write(10);  // angle
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
}
