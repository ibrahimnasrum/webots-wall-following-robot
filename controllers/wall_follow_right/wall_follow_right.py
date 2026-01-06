from controller import Robot
import math

robot = Robot()
timestep = int(robot.getBasicTimeStep())
dt = timestep / 1000.0

def list_devices():
    print("=== DEVICES ON THIS ROBOT ===")
    for i in range(robot.getNumberOfDevices()):
        d = robot.getDeviceByIndex(i)
        print("-", d.getName())
    print("=============================")

def get_any(names, kind):
    for n in names:
        d = robot.getDevice(n)
        if d is not None:
            return d, n
    print(f"[ERROR] {kind} not found. Tried: {names}")
    list_devices()
    raise RuntimeError(f"{kind} device not found")

def clamp(v, lo, hi): return max(lo, min(hi, v))

# -------- MOTORS (e-puck names) --------
lm, lm_name = get_any(["left wheel motor", "left motor", "left wheel"], "Left motor")
rm, rm_name = get_any(["right wheel motor", "right motor", "right wheel"], "Right motor")
lm.setPosition(float("inf"))
rm.setPosition(float("inf"))
MAX_SPEED = min(lm.getMaxVelocity(), rm.getMaxVelocity())

# -------- SENSORS (e-puck ps0..ps7) --------
ps = []
for i in range(8):
    s = robot.getDevice(f"ps{i}")
    if s is None:
        print("[ERROR] Missing ps sensors. This robot may not be standard e-puck.")
        list_devices()
        raise RuntimeError("ps sensors not found")
    s.enable(timestep)
