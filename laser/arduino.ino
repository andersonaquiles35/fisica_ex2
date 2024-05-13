int resist;
int time2;
int time;

void setup(){
  Serial.begin(115200);
}

void loop(){
  resist = analogRead(A3);
  while(resist<120){
    resist = analogRead(A3);
  }
  time=millis();

  delay(350);
  resist = analogRead(A3);
  while(resist<120){
    resist = analogRead(A3);
  }
  time2=millis();

  Serial.println(time2-time);
  delay(1000);
}
