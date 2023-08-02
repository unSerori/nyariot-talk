//sample:https://programresource.net/2020/05/17/3295.html
#define USE_WIFI 1
#ifdef USE_WIFI
#include <WiFi.h>
char ssid[] = "YourNetworkName";  //WiFiのSSID
char pass[] = "YourPassword";     //WiFiのパスワード
#endif

//VCC - 3.3V
//GND - GND
//OUT - GPIO35

#define NUM_HISTORY 60         //マイク入力履歴保持数（直近で最大を取るため）
int mic_history[NUM_HISTORY];  //直近のマイク入力値、フィルタリング後
int mic_index = 0;             //保存位置
#define MIC_PIN 35
#define SPKR_PIN 25

void setup() {
  Serial.begin(115200);
  pinMode(SPKR_PIN, OUTPUT);
  delay(5); //マイクの録音がいきなり始まるのを防ぐため。未検証
}

boolean recMode = false;
int recCount = 0;
int delayMicroS = 66;
#define recSize 30000
short recData[30000];

void loop() {
  int micin;
  unsigned long micavg = 0;
  int micinr = analogRead(MIC_PIN);

  mic_history[mic_index++] = micinr;
  if (mic_index == NUM_HISTORY)
    mic_index = 0;

  micin = 0;
  for (int i = 0; i < NUM_HISTORY; i++)  //最近のマイク入力の平均値
    micavg += (unsigned long)mic_history[i];
  micavg = micavg / NUM_HISTORY;

  for (int i = 0; i < NUM_HISTORY; i++)  //最近のマイク入力の最大のふり幅
    micin = max(micin, abs(mic_history[i] - (int)micavg));

  if (micin > 500 && !recMode) {
    Serial.print("録音開始");
    recMode = true;
    recCount = 0;
  }
  if (recMode) {
    recData[recCount++] = std::pow(micinr, 5)/std::pow(1000, 5);
    //recData[recCount++] = micinr;
  }

  if (recMode && recCount >= recSize) {
    Serial.print("録音終了");
    recMode = false;
    for (int i = 0; i < recSize/10; i++) {
      Serial.printf("%d, ", recData[i]);
      if(i%10 == 9) Serial.println();
    }
    delay(2000);
    for(int i=0; i<recSize; i++){
      dacWrite(SPKR_PIN, recData[i]);
      delayMicroseconds(delayMicroS*2.5);
    }
    Serial.println("再生終了");
  }
  dacWrite(SPKR_PIN, 0);

  if(recMode) delayMicroseconds(delayMicroS);
  else delay(10);
}