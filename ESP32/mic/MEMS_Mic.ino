//sample:https://programresource.net/2020/05/17/3295.html
#define USE_WIFI 1
#ifdef USE_WIFI
#include <WiFi.h>
char ssid[] = "YourNetworkName"; //WiFiのSSID
char pass[] = "YourPassword"; //WiFiのパスワード
#endif
 
//VCC - 3.3V
//GND - GND
//OUT - GPIO35
 
#define NUM_HISTORY 60 //マイク入力履歴保持数（直近で最大を取るため）
int mic_history[NUM_HISTORY]; //直近のマイク入力値、フィルタリング後
int mic_index = 0; //保存位置
#define MIC_PIN 35
 
void setup() {
    Serial.begin(115200);
 
#ifdef USE_WIFI
    WiFi.mode(WIFI_STA);
    if (String(WiFi.SSID()) != String(ssid)) {
        WiFi.begin(ssid, pass);
    }
#endif
 
}
 
void loop() {
    int micin;
    unsigned long micavg = 0;
    int micinr = analogRead(MIC_PIN);
 
    mic_history[mic_index++] = micinr;
    if (mic_index == NUM_HISTORY)
        mic_index = 0;
 
    micin = 0;
    for (int i = 0; i < NUM_HISTORY; i++) //最近のマイク入力の平均値
        micavg += (unsigned long)mic_history[i];
    micavg = micavg / NUM_HISTORY;
 
    for (int i = 0; i < NUM_HISTORY; i++) //最近のマイク入力の最大のふり幅
        micin = max(micin, abs(mic_history[i] - (int)micavg));
 
    Serial.printf("2500,%d,%d,0\n", micinr, micin);
    delay(10);
}