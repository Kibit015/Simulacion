int ledPin = 13; // Pin del LED 
bool parpadeando = false;

void setup() { 
  Serial.begin(9600); // Inicializa la comunicación serial 
  pinMode(ledPin, OUTPUT); // Configura el pin del LED como salida 
} 

void loop() { 
  if (Serial.available() > 0) { 
    char data = Serial.read(); // Lee el dato recibido por Bluetooth 
    
    if (data == '1') { 
      digitalWrite(ledPin, HIGH); // Enciende el LED 
      Serial.println("LED ENCENDIDO"); 
      parpadeando = false;
    } else if (data == '0') { 
      digitalWrite(ledPin, LOW); // Apaga el LED 
      Serial.println("LED APAGADO"); 
      parpadeando = false;
    } else if (data == 'A') { 
      Serial.println("LED PARPADEANDO INFINITAMENTE"); 
      parpadeando = true;
    } 
  } 
  
  if (parpadeando) {
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
  }
}