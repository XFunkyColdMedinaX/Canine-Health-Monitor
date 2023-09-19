#include <Adafruit_MLX90614.h>

Adafruit_MLX90614 mlx = Adafruit_MLX90614();

long instance1=0, timer;

double hrv =0, hr = 72, interval = 0;

int value = 0, count = 0;  

bool flag = 0;

#define shutdown_pin 10 

#define threshold 100 // to identify R peak

#define timer_value 10000 // 10 seconds timer to calculate hr

/////////////////////////////OXy//////////////

#include <Wire.h>
#include "MAX30105.h"
#include "spo2_algorithm.h"

MAX30105 particleSensor;

#define MAX_BRIGHTNESS 255

#if defined(__AVR_ATmega328P__) || defined(__AVR_ATmega168__)
//Arduino Uno doesn't have enough SRAM to store 100 samples of IR led data and red led data in 32-bit format
//To solve this problem, 16-bit MSB of the sampled data will be truncated. Samples become 16-bit data.
uint16_t irBuffer[100]; //infrared LED sensor data
uint16_t redBuffer[100];  //red LED sensor data
#else
uint32_t irBuffer[100]; //infrared LED sensor data
uint32_t redBuffer[100];  //red LED sensor data
#endif

int32_t bufferLength; //data length
int32_t spo2; //SPO2 value
int8_t validSPO2; //indicator to show if the SPO2 calculation is valid
int32_t heartRate; //heart rate value
int8_t validHeartRate; //indicator to show if the heart rate calculation is valid

byte pulseLED = 12; //Must be on PWM pin
byte readLED = 13; //Blinks with each data read



void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("Adafruit MLX90614 test");

  if (!mlx.begin()) {
    Serial.println("Error connecting to MLX sensor. Check wiring.");
    while (1);
  };

  Serial.print("Emissivity = "); Serial.println(mlx.readEmissivity());
  Serial.println("================================================");

  pinMode(10, INPUT); // Configuración para la detección LO +
  pinMode(11, INPUT); // Configuración para la detección LO -

  //OxySetup();  
}


void loop() {
 

  Temp();
  ECG();


}

void Temp() {  
  Serial.print(mlx.readObjectTempC()); Serial.print("*C,");
  Serial.print(mlx.readObjectTempF()); Serial.print("*F,");
  }

void ECG() { 

  if((digitalRead(10) == 1)||(digitalRead(11) == 1)){

    Serial.println("leads off!");

    digitalWrite(shutdown_pin, LOW); //standby mode

    instance1 = micros();

    timer = millis();

  }

  else {

    digitalWrite(shutdown_pin, HIGH); //normal mode

    value = analogRead(A0);

    value = map(value, 250, 400, 0, 100); //to flatten the ecg values a bit

    if((value > threshold) && (!flag)) {

      count++;  

      Serial.println("in");

      flag = 1;

      interval = micros() - instance1; //RR interval

      instance1 = micros(); 

    }

    else if((value < threshold)) {

      flag = 0;

    }

    if ((millis() - timer) > 10000) {

      hr = count*6;

      timer = millis();

      count = 0; 

    }

    hrv = hr/60 - interval/1000000;

    Serial.print(hr);

    Serial.print(",");

    Serial.print(hrv);

    Serial.print(",");

    Serial.println(value);

    delay(100);

  }

}

void OxySetup() {
  pinMode(pulseLED, OUTPUT);
  pinMode(readLED, OUTPUT);

  // Initialize sensor
  if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) //Use default I2C port, 400kHz speed
  {
    Serial.println(F("MAX30105 was not found. Please check wiring/power."));
    while (1);
  }

  //Serial.println(F("Attach sensor to finger with rubber band. Press any key to start conversion"));
  //while (Serial.available() == 0) ; //wait until user presses a key
  Serial.read();

  byte ledBrightness = 60; //Options: 0=Off to 255=50mA
  byte sampleAverage = 4; //Options: 1, 2, 4, 8, 16, 32
  byte ledMode = 2; //Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
  byte sampleRate = 100; //Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
  int pulseWidth = 411; //Options: 69, 118, 215, 411
  int adcRange = 4096; //Options: 2048, 4096, 8192, 16384

  particleSensor.setup(ledBrightness, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange); //Configure sensor with these settings
}
