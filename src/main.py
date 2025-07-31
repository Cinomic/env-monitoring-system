import time
import microcontroller
import board
import analogio
import wifi
import adafruit_requests as requests
import adafruit_ahtx0
import neopixel
from rainbowio import colorwheel
import adafruit_bmp3xx

# Setup I2C and sensors
i2c = board.I2C()
sensor = adafruit_ahtx0.AHTx0(i2c)
photoresistor = analogio.AnalogIn(board.A0)
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

# WiFi credentials
WIFI_CREDENTIALS = [
    ("bucknell_iot", ""),
    ("Rehema", "qazWSX11!!"),
    ("bucknell_guests", "")
]

WRITE_API_KEY = "PZA3S7KM86GZB7ON"
DATA_POST_URL = "https://api.thingspeak.com/update?api_key={}&field1={{}}&field2={{}}&field3={{}}&field4={{}}&field5={{}}".format(WRITE_API_KEY)

def connect_wifi():
    for ssid, password in WIFI_CREDENTIALS:
        for attempt in range(5):
            try:
                wifi.radio.connect(ssid, password)
                print(f"Connected to {ssid}")
                return True
            except Exception as e:
                print(f"Connection failed to {ssid}: {e}")
                time.sleep(5)
    microcontroller.reset()

def get_voltage(pin):
    return pin.value * 3.3 / 65535

def convert_to_mV(voltage):
    return voltage * 1000

# Setup NeoPixel
pixels = neopixel.NeoPixel(board.NEOPIXEL, 8, brightness=0.3, auto_write=False)

def light_up_neopixel():
    for i in range(8):
        pixels[i] = (255, 255, 255)
    pixels.show()
    time.sleep(1)

light_up_neopixel()

# Main loop
while True:
    temp_c = sensor.temperature
    temp_f = temp_c * 9 / 5 + 32
    humidity = sensor.relative_humidity
    light_mV = convert_to_mV(get_voltage(photoresistor))
    pressure = bmp.pressure

    if None in (light_mV, temp_f, humidity, pressure):
        print("Sensor reading failed.")
    else:
        url = DATA_POST_URL.format(light_mV, 0.0, temp_f, humidity, pressure)
        try:
            response = requests.get(url)
            print("ThingSpeak response:", response.text)
        except Exception as e:
            print("Error:", e)
            connect_wifi()

    time.sleep(300)

