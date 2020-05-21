// This #include statement was automatically added by the Particle IDE.
#include <HC_SR04.h>

double distance = 0.0;

int triggerPin = D4;
int echoPin = D5;

HC_SR04 rangefinder = HC_SR04(triggerPin, echoPin);

void setup() {
    Spark.variable("distance", &distance, DOUBLE);
    Wire.begin(8);
    Wire.onRequest(requestEvent);

}

void loop() {
   
    distance = rangefinder.getDistanceCM();
    
    if (distance < 15)
    {
        Particle.publish("CLOSE", "close", PRIVATE);
    }
    
    delay(1000);
}


void requestEvent()
{
    if (distance < 10)
    {
        Wire.write("A"); //too close
        
    } else if (distance < 20) {
        Wire.write("B"); //close enough
    } else if (distance < 30 )
    {
        Wire.write("C"); //far enough
    } else 
    {
        Wire.write("D");
    }
}



