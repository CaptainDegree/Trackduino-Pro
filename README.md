# Trackduino Pro API

This **API**'s goal is to provide implementation of Robotrack's Trackduino interface on MicroPython 32-bit platform.

This **API** contains:
- Common Arduino-like functions;
- Pin definitions;
- Timer management class;
- Robotrack's executor drivers;
- Robotrack's sensor drivers.

## Notation list

| Notation | Meaning                       |
| :------: | :---------------------------- |
|    IR    | Infrared                      |
|   CdS    | Cadmium sulfide photoresistor |
|    BT    | Bluetooth                     |
|    RC    | Remote control                |

## Robotrack's driver compatibility

| Sensor                                     | Implemented |
| :----------------------------------------- | :---------: |
| Analog mic                                 |     ✔️      |
| Built-in buttons                           |     ✔️      |
| Button                                     |     ✔️      |
| CdS                                        |     ✔️      |
| Combined color sensor                      |     ✔️      |
| Digital mic                                |     ✔️      |
| External motor encoder                     |     ✔️      |
| Flame sensor                               |     ✔️      |
| IR sensor                                  |     ✔️      |
| Magnetic field sensor                      |     ✔️      |
| Temperature sensor                         |     ✔️      |
| Tilt sensor                                |     ✔️      |
| Ultrasonic distance sensor                 |     ✔️      |
| Vibration sensor                           |     ✔️      |
| Accelerometer / Gyroscope                  |      ❌      |
| BT RC                                      |      ❌      |
| IR RC receiver                             |      ❌      |
| Neurotrack connector                       |      ❌      |
| Young Neurophysiologist-engineer connector |      ❌      |

| Executor      | Implemented |
| :------------ | :---------: |
| DC motor      |     ✔️      |
| Servo (Big)   |     ✔️      |
| Servo (Small) |     ✔️      |
| Buzzer        |     ✔️      |
| Built-in LED  |     ✔️      |
| LED           |     ✔️      |
| Display       |      ❌      |
| Audiotrack    |      ❌      |
