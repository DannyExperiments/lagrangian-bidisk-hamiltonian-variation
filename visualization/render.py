#!/usr/bin/env python3
"""Render the support derivative over length proportion and relative angle."""
from math import acos, cos, pi, sin, sqrt, tau
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SIZE = (704, 452)
BG, CARD, RULE = "#0b151f", "#142331", "#354957"
WHITE, MUTED, AQUA, GOLD = "#f2fafb", "#b8ced9", "#76ded3", "#ffd082"
WORKED_S, WORKED_ANGLE = 9 / 25, acos(3 / 5)


def font(size, bold=False):
    choices = [
        Path("/System/Library/Fonts/Supplemental") / ("Arial Bold.ttf" if bold else "Arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu") / ("DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"),
    ]
    for path in choices:
        if path.is_file():
            return ImageFont.truetype(str(path), size)
    raise RuntimeError("Provide Arial or DejaVu Sans.")


TITLE, BODY, LABEL, SMALL = font(31, True), font(22), font(20, True), font(17)


def support_rate(s, relative_angle):
    return -(sqrt(s) + sqrt(1 - s)) * cos(relative_angle) ** 2


def plot(draw, camera):
    def projection(s, t, rate):
        x, y = 1.2 * (s - 0.5), t - 0.5
        horizontal = x * cos(camera) + y * sin(camera)
        depth = -x * sin(camera) + y * cos(camera)
        return (230 + 211 * horizontal, 190 + 58 * depth - 64 * rate), depth + rate / 3

    def line(points, color, width=1):
        draw.line([projection(*p)[0] for p in points], fill=color, width=width)

    for k in range(6):
        v = k / 5
        line([(v, 0, 0), (v, 1, 0)], RULE)
        line([(0, v, 0), (1, v, 0)], RULE)

    ns, na = 14, 21
    mesh = []
    for i in range(ns + 1):
        s = 0.02 + 0.96 * i / ns
        mesh.append([(s, j / na, support_rate(s, pi * j / na)) for j in range(na + 1)])
    faces = []
    for i in range(ns):
        for j in range(na):
            vertices = [mesh[i][j], mesh[i + 1][j], mesh[i + 1][j + 1], mesh[i][j + 1]]
            projected = [projection(*v) for v in vertices]
            mean_rate = sum(v[2] for v in vertices) / 4
            q = -mean_rate / sqrt(2)
            fill = (int(32 + 37 * q), int(80 + 78 * q), int(90 + 70 * q))
            faces.append((sum(v[1] for v in projected) / 4, [v[0] for v in projected], fill))
    for _, vertices, fill in sorted(faces, reverse=True):
        draw.polygon(vertices, fill=fill, outline="#397a82")

    line([(0.02, 0.5, 0), (0.98, 0.5, 0)], AQUA, 3)
    t = WORKED_ANGLE / pi
    p = projection(WORKED_S, t, support_rate(WORKED_S, WORKED_ANGLE))[0]
    line([(WORKED_S, t, 0), (WORKED_S, t, support_rate(WORKED_S, WORKED_ANGLE))], GOLD, 2)
    x, y = p
    draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=GOLD, outline=WHITE, width=1)


def vector(draw, angle, color, label):
    center = (510, 244)
    end = (center[0] + 96 * cos(angle), center[1] - 96 * sin(angle))
    draw.line((center, end), width=4, fill=color)
    tips = [(end[0] - 13 * cos(angle + d), end[1] + 13 * sin(angle + d)) for d in (-0.42, 0.42)]
    draw.polygon([end, *tips], fill=color)
    draw.text((end[0] + 17 * cos(angle), end[1] - 17 * sin(angle)), label, font=LABEL, fill=color, anchor="mm")


def frame(camera):
    im = Image.new("RGB", SIZE, BG)
    draw = ImageDraw.Draw(im)
    draw.text((24, 18), "How the bidisk’s support moves", fill=WHITE, font=TITLE)
    draw.text((25, 60), "Initial response to a compactly supported Hamiltonian", fill=MUTED, font=BODY)
    draw.rounded_rectangle((22, 102, 440, 363), 16, fill=CARD, outline=RULE)
    draw.rounded_rectangle((453, 102, 681, 363), 16, fill=CARD, outline=RULE)
    draw.text((231, 116), "Support derivative", fill=WHITE, font=LABEL, anchor="mt")
    draw.text((231, 337), "Length proportion s  ·  relative angle θ", fill=MUTED, font=SMALL, anchor="mt")
    plot(draw, camera)
    draw.text((567, 116), "Worked direction", fill=WHITE, font=LABEL, anchor="mt")
    vector(draw, 0, AQUA, "x")
    vector(draw, WORKED_ANGLE, GOLD, "y")
    draw.arc((472, 206, 548, 282), 360 - WORKED_ANGLE * 180 / pi, 360, fill=GOLD, width=2)
    draw.text((567, 274), "s = 9/25,   x · y = 3/5", fill=MUTED, font=SMALL, anchor="mt")
    draw.text((567, 309), "Support rate −63/125", fill=GOLD, font=LABEL, anchor="mt")
    draw.text((352, 381), "Spherical average of the full width rate is −4/3", fill=WHITE, font=BODY, anchor="mt")
    draw.text((352, 420), "The zero ridge occurs at orthogonal disk directions.", fill=MUTED, font=SMALL, anchor="mt")
    return im


def main():
    count = 42
    frames = [frame(0.52 + i * tau / count) for i in range(count)]
    palette_sheet = Image.new("RGB", (3 * SIZE[0], SIZE[1]))
    for j in range(3):
        palette_sheet.paste(frames[j * count // 3], (j * SIZE[0], 0))
    palette = palette_sheet.quantize(colors=96)
    images = [im.quantize(palette=palette, dither=Image.Dither.NONE) for im in frames]
    out = Path(__file__).with_name("support-variation.gif")
    images[0].save(out, save_all=True, append_images=images[1:], duration=120, loop=0, optimize=True)
    print(f"{out.name}: {count} frames, {out.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
