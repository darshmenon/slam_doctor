#!/usr/bin/env python3
"""Render docs/demo_run.jsonl (real `slam_doctor --json` reports from an ORB-SLAM3 cafe run in Gazebo) into docs/demo.gif."""
import json
import os
import time

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 15)
COL = {'ERROR': (255, 95, 95), 'WARN': (240, 200, 80), 'OK': (110, 220, 130), 'INFO': (205, 205, 205)}
W, H, LH = 1000, 330, 19
BG, FG, DIM = (22, 24, 30), (205, 205, 205), (120, 125, 135)

reports = [json.loads(l) for l in open(os.path.join(HERE, 'demo_run.jsonl')) if l.startswith('{')]
# keep ~14 frames, always including the first and last
step = max(1, len(reports) // 14)
picked = reports[::step][:13] + [reports[-1]]


def frame(i, r):
    img = Image.new('RGB', (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 26], fill=(40, 43, 52))
    d.text((12, 5), 'slam_doctor --hints      (live capture: ORB-SLAM3 exploring the Gazebo cafe)', font=FONT, fill=DIM)
    s = r['summary']
    d.text((14, 36), f'--- {time.strftime("%H:%M:%S", time.localtime(r["time"]))}  score={s["score"]}  corrections={s["corrections"]}  '
                     f'largest={s["largest_correction_m"]}m  resumes={s["tracker_resumes"]}  travel={s["travel_m"]}m ---', font=FONT, fill=FG)
    y = 62
    for f in r['findings'][:8]:
        d.text((14, y), f'{f["level"]:5s} [{f["code"]}] {f["msg"]}'[:112], font=FONT, fill=COL.get(f['level'], FG))
        y += LH
        if f.get('hint') and f['level'] != 'OK':
            d.text((14, y), f'      -> {f["hint"]}'[:112], font=FONT, fill=DIM)
            y += LH
    d.text((14, H - 24), f'report {i + 1}/{len(picked)}', font=FONT, fill=DIM)
    return img


frames = [frame(i, r) for i, r in enumerate(picked)]
dur = [800] * len(frames)
dur[-1] = 2500
frames[0].save(os.path.join(HERE, 'demo.gif'), save_all=True, append_images=frames[1:], duration=dur, loop=0, optimize=True)
print(len(frames), 'frames ->', os.path.join(HERE, 'demo.gif'))
