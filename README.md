# Webots Robot Navigation Project (e-puck)

Wall Following (Right-Hand Rule) + Optional Line Following

This repository contains a **Webots** controller project for **e-puck** that performs:

* ✅ **Right wall following** (maze navigation)
* ✅ **Corner handling** (front obstacle avoidance)
* ✅ **Gap handling** (when the right wall disappears → turn right to search)
* (Optional) ✅ **Line following** using ground sensors (`gs0..gs2`) if your world has a line texture

---

## Project Structure

```
.
├─ controllers/
│  └─ wall_follow_right/
│     └─ wall_follow_right.py
├─ worlds/
│  └─ <your_world>.wbt
├─ README.md
└─ (optional) docs/, images/
```

---

## Requirements

* **Webots R2025a** (recommended)
* Python controller enabled inside Webots
* Robot: **e-puck**

> Note: If you see errors about missing `.proto` templates or `.dll` plugins, make sure your Webots installation is complete and you are using the **official release** folder (not a partial copy).

---

## Quick Start (Run in Webots)

1. Open the world:

   * `File > Open World…`
   * Select: `worlds/<your_world>.wbt`

2. Click the e-puck robot in the scene and check:

   * `controller = "wall_follow_right"`

3. Press **Run** ▶️

---

## Common e-puck Device Names

### Wheels

The default e-puck motor names are usually:

* `left wheel motor`
* `right wheel motor`

If your controller shows:

> `Device "left wheel" was not found`

Then your motor names are different.
To fix it, open the robot in Webots and check the motor device names in the Scene Tree.

---

## Sensors Used (Wall Following)

e-puck IR proximity sensors:

* `ps0` … `ps7`

Typical mapping (may vary by model/world):

* **Front**: `ps7` and `ps0`
* **Right side**: `ps2` and `ps1`

✅ Recommended: run a sensor diagnostic first to confirm mapping.

---

## Sensor Diagnostic (Recommended)

Use this quick script to print sensor values and confirm which sensor is **front** and **right**:

```python
from controller import Robot
robot = Robot()
timestep = int(robot.getBasicTimeStep())

ps=[]
for i in range(8):
    s=robot.getDevice(f"ps{i}")
    s.enable(timestep)
    ps.append(s)

while robot.step(timestep) != -1:
    vals=[round(s.getValue(),1) for s in ps]
    print("ps0..ps7 =", vals)
```

Move the robot close to:

* a wall in front → find which sensor increases
* a wall on right → find which sensor increases

---

## Controller Behavior (Wall Follow Right)

### States

The wall-follow controller uses a simple state machine:

* **FOLLOW**: keep a target distance from the right wall
* **TURN_RIGHT**: if right wall is lost (gap), rotate right to find it
* **AVOID_LEFT**: if obstacle in front, turn left to avoid collision

### Key Parameters (Tuning)

Inside the controller you will find:

* `TARGET` → desired distance to wall (or “raw sensor target”)
* `WALL_LOST` / `WALL_FOUND` → hysteresis thresholds (prevents jitter)
* `FRONT_STOP` → emergency avoidance threshold
* `BASE_SPEED`, `TURN_SPEED`

If the robot:

* **keeps hitting corners** → increase front avoidance sensitivity
* **goes straight in empty space** → lower `WALL_LOST` and improve TURN_RIGHT behavior
* **oscillates near wall** → reduce gain / steering limit

---

## Optional: Line Following (Ground Sensors)

If your world includes a line texture and you want **line following** instead of wall following, e-puck supports ground sensors:

* `gs0`, `gs1`, `gs2`

Line following is typically **more stable** than wall following for simple tasks.

---

## Troubleshooting

### 1) Robot does not move

* Check motor names in code match Webots device names.
* Confirm `setPosition(float('inf'))` and `setVelocity(...)` are called.

### 2) Device not found error

Example:

> `Device "left wheel" was not found`

Fix:

* Replace motor name strings with actual device names in your robot.

### 3) Webots proto/template error

Example:

> `failed to import JavaScript template ... wbgeometry.js`

Fix ideas:

* Reinstall Webots properly (do not run from a broken temp folder).
* Avoid custom PROTO references if not needed.
* If using GitHub raw PROTO links, download the PROTO locally instead.

### 4) Bluetooth DLL error

Example:

> `e-puck_bluetooth.dll remote control library initialisation failed`

Fix:

* You can usually ignore this if you are not using Bluetooth remote control.
* Or disable/remove remote control plugin from robot settings if enabled.

---

## Credits

* Webots: Cyberbotics
* Robot: e-puck (GCtronic)

---

## Group Members

1. Ibrahim Bin Nasrum (2116467)
2. Almasri Suhail Jihad (2128771)
3. Maeyd Abdallah Mahamat Abacar (2117777)
4. Khairuldddin bin Zulkiflei (2210527)
5. Muhammad Raziq Bin Kaharuddin (2120225)

