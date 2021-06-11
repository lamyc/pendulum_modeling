/*
  Arduino LSM9DS1 - Accelerometer Application

  This example reads the acceleration values as relative direction and degrees,
  from the LSM9DS1 sensor and prints them to the Serial Monitor or Serial Plotter.

  The circuit:
  - Arduino Nano 33 BLE

  Created by Riccardo Rizzo

  Modified by Jose García
  27 Nov 2020

  This example code is in the public domain.
*/

#include <Arduino_LSM9DS1.h>

float x, y, z;
int degreesX = 0;
int degreesY = 0;
int degreesZ = 0;
unsigned long NewTime, OldTime, exact;

void setup() {
  Serial.begin(9600);
  while (!Serial);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }

  Serial.print("Accelerometer sample rate = ");
  Serial.print(IMU.accelerationSampleRate());
  Serial.println("Hz");
  Serial.println();
  Serial.println("Acceleration in G's");
  Serial.println("Time\tX\tY\tZ");
  OldTime = millis();
}

void loop() {
  NewTime = millis();
  
  if (NewTime - OldTime >= 100) {
    if (IMU.accelerationAvailable()) {
      IMU.readAcceleration(x, y, z); //output x, y, z acceleration in terms of g.
    }
  exact = millis();
  Serial.print(exact);
  Serial.print('\t');
  Serial.print(x,8);
  Serial.print('\t');
  Serial.print(y,8);
  Serial.print('\t');
  Serial.println(z,8);
  OldTime = NewTime;
  }
}
