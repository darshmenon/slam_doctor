# Changelog

## Unreleased
- Per-robot baselines: `--learn SECS` records the normal `map->odom` and `odom` message rates, `--baseline` warns with `RATE_DROP` / `RATE_SPIKE` below half or above double that. Plain statistics, no model. Run live against the fake SLAM graph (learn at 20 Hz, quiet at 20 Hz, `RATE_DROP` at 4 Hz).

## 0.1.0
- First release: attach to any running ROS 2 SLAM (slam_toolbox, Cartographer, RTAB-Map, ORB-SLAM3) and report its health.
- Checks: `TRACKING_LOST`, `TRACKING_FLAP`, `JUMP_STORM`, `BIG_JUMP`, `MAP_STALL`, `MAP_NONE`, `NO_MAP_ODOM`, `DRIFT_HIGH`.
- Loop-closure / map-correction timeline (`--events FILE`): when, how far (m, deg).
- Camera quality (`--image TOPIC`): `FEATURE_POOR`, `BLURRED`, `DARK`, `OVEREXPOSED` (OpenCV ORB when installed, NumPy fallback).
- `--json`, `--hints`, `--diagnostics`, `--once N` (exit 1 on ERROR), 0-100 health score.
