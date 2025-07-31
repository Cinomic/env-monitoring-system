# Environmental Monitoring System (ECEG 100 - Project 1)

This project is a compact, Wi-Fi-enabled environmental monitoring system developed by **Josh Le Quang** and **Bobby Lorinkov**. It records environmental data in real-time and uploads it to ThingSpeak for remote access and analysis.

## 📊 Monitored Parameters
- 🌡️ Temperature (AHT20)
- 💧 Humidity (AHT20)
- 💡 Light Intensity (Photoresistor)
- 🌬️ Atmospheric Pressure (BMP388)

## 🔧 Features
- ✅ Real-time data acquisition
- ✅ WiFi auto-reconnect with fallback
- ✅ NeoPixel LED status feedback
- ✅ Compact 3D-printed custom enclosure
- ✅ Sensor calibration for accuracy

## 🔁 System Architecture
```
Sensors → ESP32-S3 Feather → WiFi → ThingSpeak Dashboard
```

## 📅 Development Timeline
- **Week 1:** Planning and AHT20 Integration
- **Week 2:** Light Sensor Integration + Enclosure Prototyping
- **Week 3:** NeoPixel, Pressure Sensor, Calibration, WiFi Logic

## 👥 Team Members
- Josh Le Quang
- Bobby Lorinkov

## 📁 File Structure
```
src/                # Main Python code
images/             # Product and diagram images
schematic/          # Schematic design of the system
```

## 📜 License
MIT License
