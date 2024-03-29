import streamlit as st

robotCode = {"Robot Code Setup":
    '''
#include <NewPing.h>
#define MAX_DISTANCE 200
const int PWMA = 5;
const int PWMB = 5;
const int AIN1 = 4;
const int AIN2 = 6;
const int BIN1 = 3;
const int BIN2 = 2;

const int motorSpeed = 255;
const int motorTurnSpeed = 150;

const int sensor1Trig = 8;
const int sensor1Echo = 9;
const int sensor2Trig = 10;
const int sensor2Echo = 11;

NewPing sonar1(sensor1Trig, sensor1Echo, MAX_DISTANCE);
NewPing sonar2(sensor2Trig, sensor2Echo, MAX_DISTANCE);

void setup() {
  pinMode(PWMA, OUTPUT);
  pinMode(PWMB, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);

  //Serial.begin(9600);
  delay(5000);
}   
    ''',
    "Robot Move Forward":
    '''
void moveForward() {
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);

  analogWrite(PWMA, motorSpeed);
  analogWrite(PWMB, motorSpeed);
}    
    ''',
    "Robot Move Backward":
    '''
void moveBackward() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);

  analogWrite(PWMA, motorSpeed);
  analogWrite(PWMB, motorSpeed);
} 
    ''',
    "Robot Turn Left":
    '''
void leftTurn() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);

  analogWrite(PWMA, motorTurnSpeed);
  analogWrite(PWMB, motorTurnSpeed);
} 
    ''',
    "Robot Turn Right":
    '''
void rightTurn() {
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);

  analogWrite(PWMA, motorTurnSpeed);
  analogWrite(PWMB, motorTurnSpeed);
}
    ''',
    "Robot Stop Motors":
    '''
void stopMotors() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, LOW);

  analogWrite(PWMA, 0);
  analogWrite(PWMB, 0);
}
    ''',
    "Robot Sensor Distance Code Initialization":
    '''
void loop() {
  unsigned int distance1 = sonar1.ping_cm();
  unsigned int distance2 = sonar2.ping_cm();
}
    '''}

IRcode = {"Detect Black or White":
    '''const int outPin1 = 8; 
const int outPin2 = 9; 
void setup() {
  pinMode(outPin1, INPUT);
  pinMode(outPin2, INPUT);
  Serial.begin(9600);
}

void loop() {
  int sensorValue1 = digitalRead(outPin1);
  int sensorValue2 = digitalRead(outPin2);
  
  if(sensorValue1 == 0 && sensorValue1 == 0){
    Serial.print("White\\n");
  }else{
    Serial.print("Black\\n");
  }
  
  delay(1000);
}'''}

prototypes = {"Prototype #1":
  '''
#include <NewPing.h>
#define MAX_DISTANCE 200

const short sensor1Trig = 8;
const short sensor1Echo = 9;
const short sensor2Trig = 10;
const short sensor2Echo = 11;

NewPing sonar1(sensor1Trig, sensor1Echo, MAX_DISTANCE);
NewPing sonar2(sensor2Trig, sensor2Echo, MAX_DISTANCE);

const short outPin1 = 12; 
const short outPin2 = 13; 

void setup() {
  pinMode(outPin1, INPUT);
  pinMode(outPin2, INPUT);
  Serial.begin(9600);
}

void loop() {
  unsigned short distance1 = sonar1.ping_cm();
  unsigned short distance2 = sonar2.ping_cm();

  unsigned short irVal1 = digitalRead(outPin1);
  unsigned short irVal2 = digitalRead(outPin2);

  if(irVal1 == 0 || irVal2 == 0){
    Serial.println("Stopping...");
  }else{
    if(distance1 > 0 && distance1 < 60 || distance2 > 0 && distance2 < 60){
      Serial.println("Moving Forward...");
    }else{
      Serial.println("Rotating...");
    }
  }

  delay(100);
}
  ''',"Prototype #2":
    '''
#include <NewPing.h>
#define MAX_DISTANCE 200
#define LIMIT_DISTANCE 22

const int PWMA = 5;
const int PWMB = 5;
const int AIN1 = 4;
const int AIN2 = 6;
const int BIN1 = 3;
const int BIN2 = 2;

const int motorSpeed = 255;
const int motorTurnSpeed = 100;

const int left_Trig = 8;
const int left_Echo = 9;
const int right_Trig = 10;
const int right_Echo = 11;

const int left_IR = 12; 
const int Right_IR = 13; 
const int back_IR = 7;

NewPing sonar1(left_Trig, left_Echo, MAX_DISTANCE);
NewPing sonar2(right_Trig, right_Echo, MAX_DISTANCE);

void setup() {
  pinMode(PWMA, OUTPUT);
  pinMode(PWMB, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);

  pinMode(left_IR, INPUT);
  pinMode(Right_IR, INPUT);
  pinMode(back_IR, INPUT);

  Serial.begin(9600);
  delay(5000);
}

void moveForward() {
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);

  analogWrite(PWMA, motorSpeed);
  analogWrite(PWMB, motorSpeed);
}

void moveBackward() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);

  analogWrite(PWMA, motorSpeed);
  analogWrite(PWMB, motorSpeed);
}

void stopMotors() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, LOW);

  analogWrite(PWMA, 0);
  analogWrite(PWMB, 0);
}

void rightTurn() {
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);

  analogWrite(PWMA, motorTurnSpeed);
  analogWrite(PWMB, motorTurnSpeed);
}

void loop() {
  unsigned int leftSensor = sonar1.ping_cm();
  unsigned int rightSensor = sonar2.ping_cm();

  // IR == 0 (White)
  // IR == 1 (Black)
  unsigned int leftIR = digitalRead(left_IR);
  unsigned int rightIR = digitalRead(Right_IR);
  unsigned int backIR = digitalRead(back_IR);

  Serial.print("Sensor 1: ");
  Serial.print(leftSensor);
  Serial.print(" : Sensor 2: ");
  Serial.println(rightSensor);
  if (leftSensor <= LIMIT_DISTANCE && leftSensor != 0|| rightSensor <= LIMIT_DISTANCE && rightSensor != 0) {
    moveForward();
  } else {
    stopMotors(); 
    delay(1); 
    rightTurn();  
  }

  delay(100);
}    
    ''',"Prototype #3":'''
void loop() {
  // IR == 0 (White)
  // IR == 1 (Black)
  unsigned int leftIR = digitalRead(left_IR);
  unsigned int rightIR = digitalRead(Right_IR);
  unsigned int backIR = digitalRead(back_IR);

  unsigned long startTime = 0;

  if (leftIR == 1 || rightIR == 1) {
    startTime = millis(); 
    while (millis() - startTime < 600) { 
      moveBackward();
      delay(100); 
    }
  }else if (backIR == 1) {
    moveForward();
  }else {
    moveForward();
  }

  delay(100);
}
    ''',"Prototype #4":
      '''
void loop() {
  unsigned int leftSensor = sonar1.ping_cm();
  unsigned int rightSensor = sonar2.ping_cm();

  // IR == 0 (White)
  // IR == 1 (Black)
  unsigned int leftIR = digitalRead(left_IR);
  unsigned int rightIR = digitalRead(Right_IR);
  unsigned int backIR = digitalRead(back_IR);

  unsigned long startTime = 0;
  if(leftIR == 0 || rightIR == 0 || backIR == 0){
    if (leftSensor <= MAX_DISTANCE && leftSensor != 0 || rightSensor <= MAX_DISTANCE && rightSensor != 0) {
      moveForward();
    } else {
      stopMotors(); 
      rightTurn();  
    }
  }else if(backIR == 1){
    startTime = millis(); 
    while (millis() - startTime < 600) { 
      moveForward();
      delay(100); 
    }
  }else if(leftIR == 0 || rightIR == 0){
    startTime = millis(); 
    while (millis() - startTime < 600) { 
      moveBackward();
      delay(100); 
    }   
  }

  delay(1);
}      
      ''',"Final":
        '''
#include <NewPing.h>
#include <Arduino.h>
#define MAX_DISTANCE 50
// Hulom's Group
const int PWMA = 5;
const int PWMB = 5;
const int AIN1 = 4;
const int AIN2 = 6;
const int BIN1 = 3;
const int BIN2 = 2;

const int moveForwardSpeed = 255;
const int moveBackwardSpeed = 255;
const int motorTurnSpeed = 255;

const int left_Trig = 8;
const int left_Echo = 9;
const int right_Trig = 10;
const int right_Echo = 11;

const int left_IR = 12; 
const int Right_IR = 13; 
const int back_IR = 7;

NewPing sonar1(left_Trig, left_Echo, MAX_DISTANCE);
NewPing sonar2(right_Trig, right_Echo, MAX_DISTANCE);

void setup() {
  pinMode(PWMA, OUTPUT);
  pinMode(PWMB, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);

  pinMode(left_IR, INPUT);
  pinMode(Right_IR, INPUT);
  pinMode(back_IR, INPUT);

  delay(5000);
}

void moveForward() {
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
  analogWrite(PWMA, moveForwardSpeed);
  analogWrite(PWMB, moveForwardSpeed);
}

void moveBackward() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);
  analogWrite(PWMA, moveBackwardSpeed);
  analogWrite(PWMB, moveBackwardSpeed);
}

void stopMotors() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, LOW);
  analogWrite(PWMA, 0);
  analogWrite(PWMB, 0);
}

void leftTurn() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
  analogWrite(PWMA, motorTurnSpeed);
  analogWrite(PWMB, motorTurnSpeed);
}

void rightTurn() {
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);
  analogWrite(PWMA, motorTurnSpeed);
  analogWrite(PWMB, motorTurnSpeed);
}

void loop() {
  unsigned int leftSensor = sonar1.ping_cm();
  unsigned int rightSensor = sonar2.ping_cm();
  unsigned int leftIR = digitalRead(left_IR);
  unsigned int rightIR = digitalRead(Right_IR);
  unsigned int backIR = digitalRead(back_IR);

  if (leftIR == 1 || rightIR == 1 || backIR == 1) {
    if (leftIR == 1 || rightIR == 1) {
      moveBackward();
      delay(1000); 
      stopMotors();
      rightTurn();
    }
    else if (backIR == 1) {
      moveForward();
      delay(1000);
      stopMotors();
      rightTurn();
    }
  } else {
    if (leftSensor <= MAX_DISTANCE && leftSensor != 0|| rightSensor <= MAX_DISTANCE && rightSensor != 0) {
      moveForward();
    } else {
      stopMotors();
      rightTurn();
    }
  }
  delay(1);
}

        '''}
final = {"Final":
        '''
#include <NewPing.h>
#include <Arduino.h>
#define MAX_DISTANCE 50
// Hulom's Group
const int PWMA = 5;
const int PWMB = 5;
const int AIN1 = 4;
const int AIN2 = 6;
const int BIN1 = 3;
const int BIN2 = 2;

const int moveForwardSpeed = 255;
const int moveBackwardSpeed = 255;
const int motorTurnSpeed = 255;

const int left_Trig = 8;
const int left_Echo = 9;
const int right_Trig = 10;
const int right_Echo = 11;

const int left_IR = 12; 
const int Right_IR = 13; 
const int back_IR = 7;

NewPing sonar1(left_Trig, left_Echo, MAX_DISTANCE);
NewPing sonar2(right_Trig, right_Echo, MAX_DISTANCE);

void setup() {
  pinMode(PWMA, OUTPUT);
  pinMode(PWMB, OUTPUT);
  pinMode(AIN1, OUTPUT);
  pinMode(AIN2, OUTPUT);
  pinMode(BIN1, OUTPUT);
  pinMode(BIN2, OUTPUT);

  pinMode(left_IR, INPUT);
  pinMode(Right_IR, INPUT);
  pinMode(back_IR, INPUT);

  delay(5000);
}

void moveForward() {
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
  analogWrite(PWMA, moveForwardSpeed);
  analogWrite(PWMB, moveForwardSpeed);
}

void moveBackward() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);
  analogWrite(PWMA, moveBackwardSpeed);
  analogWrite(PWMB, moveBackwardSpeed);
}

void stopMotors() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, LOW);
  analogWrite(PWMA, 0);
  analogWrite(PWMB, 0);
}

void leftTurn() {
  digitalWrite(AIN1, LOW);
  digitalWrite(AIN2, HIGH);
  digitalWrite(BIN1, HIGH);
  digitalWrite(BIN2, LOW);
  analogWrite(PWMA, motorTurnSpeed);
  analogWrite(PWMB, motorTurnSpeed);
}

void rightTurn() {
  digitalWrite(AIN1, HIGH);
  digitalWrite(AIN2, LOW);
  digitalWrite(BIN1, LOW);
  digitalWrite(BIN2, HIGH);
  analogWrite(PWMA, motorTurnSpeed);
  analogWrite(PWMB, motorTurnSpeed);
}

void loop() {
  unsigned int leftSensor = sonar1.ping_cm();
  unsigned int rightSensor = sonar2.ping_cm();
  unsigned int leftIR = digitalRead(left_IR);
  unsigned int rightIR = digitalRead(Right_IR);
  unsigned int backIR = digitalRead(back_IR);

  if (leftIR == 1 || rightIR == 1 || backIR == 1) {
    if (leftIR == 1 || rightIR == 1) {
      moveBackward();
      delay(1000); 
      stopMotors();
      rightTurn();
    }
    else if (backIR == 1) {
      moveForward();
      delay(1000);
      stopMotors();
      rightTurn();
    }
  } else {
    if (leftSensor <= MAX_DISTANCE && leftSensor != 0|| rightSensor <= MAX_DISTANCE && rightSensor != 0) {
      moveForward();
    } else {
      stopMotors();
      rightTurn();
    }
  }
  delay(1);
}

        '''}
st.set_page_config("Sumo Robot Code", page_icon="🤖",layout='centered', initial_sidebar_state='auto')

def loopingCode(z):
    for k, v in z.items(): 
        st.subheader(k)
        st.code(v, language='c')
        st.markdown("---")  

def main():
    
    #page = st.sidebar.selectbox("Choose a page",["Code Part","Infrared (IR) Sensor","Prototypes"])
    loopingCode(final)
    #if page == "Code Part":
       # loopingCode(robotCode)
    #elif page == "Infrared (IR) Sensor":
       # loopingCode(IRcode)
    #elif page == "Prototypes":
        #loopingCode(prototypes)
    
        
    st.write("Copyright © 2024 Josuan. All rights reserved.")
    
if __name__ == '__main__':
    main()