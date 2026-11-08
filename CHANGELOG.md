# Changelog

## 0.1.0
- First release: attach to any running ROS 2 SLAM (slam_toolbox, Cartographer, RTAB-Map, ORB-SLAM3) and report its health.
- Checks: `TRACKING_LOST`, `TRACKING_FLAP`, `JUMP_STORM`, `BIG_JUMP`, `MAP_STALL`, `MAP_NONE`, `NO_MAP_ODOM`, `DRIFT_HIGH`.
- Loop-closure / map-correction timeline (`--events FILE`): when, how far (m, deg).
- Camera quality (`--image TOPIC`): `FEATURE_POOR`, `BLURRED`, `DARK`, `OVEREXPOSED` (OpenCV ORB when installed, NumPy fallback).
- `--json`, `--hints`, `--diagnostics`, `--once N` (exit 1 on ERROR), 0-100 health score.
