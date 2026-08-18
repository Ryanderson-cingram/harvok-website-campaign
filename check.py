#!/usr/bin/env python3
"""Check a Bricks element list against the rules the server does NOT enforce.

    python3 check.py page.json                 # a draft you are about to create
    python3 check.py references/components/*   # the library itself

Accepts either a Bricks paste envelope {"content": [...]} or a bare element array.
Exits non-zero if anything fails. The server checks ids/parents/children/themeStyles;
this covers the four defects that keep reaching review:

    - a root section that paints (the background belongs to the panel inside it)
    - a root section with no side gutter, or with _margin instead of padding
    - themeStyles on a primitive
    - text that fails WCAG contrast against its inherited background
"""
import glob
import json
import sys

PRIMITIVES = {"section", "container", "block", "div", "heading", "text-basic", "button"}
IMAGE = object()   # sentinel: background is a photo, so contrast rides on the scrim


def contrast(fg, bg):
    def lum(h):
        h = h.lstrip("#")
        if len(h) == 3:
            h = "".join(c * 2 for c in h)
        ch = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
        f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
        r, g, b = map(f, ch)
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
    a, b = sorted((lum(fg), lum(bg)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def hexof(node):
    """Colour hex out of a Bricks colour object, or None."""
    if isinstance(node, dict):
        # A colour carrying an rgba()/hsla() with alpha 0 is the palette's transparent
        # token — it paints nothing, so it must not be read as its nominal hex.
        for k in ("rgb", "hsl"):
            v = node.get(k)
            if isinstance(v, str) and v.rstrip(") ").rsplit(",", 1)[-1].strip() == "0":
                return None
        h = node.get("hex") or node.get("raw")
        if isinstance(h, str) and h.startswith("#"):
            return h
    return None


def font_px(settings):
    """Desktop font size, defaulting to body copy when unset."""
    typo = settings.get("_typography") or {}
    try:
        return float(str(typo.get("font-size", 16)).rstrip("px") or 16)
    except ValueError:
        return 16.0


def check(elements, label):
    problems = []
    by_id = {e["id"]: e for e in elements if isinstance(e, dict) and "id" in e}
    roots = [e for e in elements if e.get("parent") in (0, "0")]

    for e in roots:
        s = e.get("settings") or {}
        if not isinstance(s, dict):
            continue
        if any(k == "_margin" or k.startswith("_margin:") for k in s):
            problems.append(f"{e['id']} ({e.get('label') or e['name']}): root uses _margin — "
                            f"vertical rhythm comes from padding only")
        if hexof((s.get("_background") or {}).get("color")) or (s.get("_background") or {}).get("image"):
            problems.append(f"{e['id']}: root section carries a background — on this site the "
                            f"background belongs to the container inside it, so the panel sits "
                            f"inset in the 20px frame instead of bleeding to the edge")
        pad = s.get("_padding") or {}
        for side in ("left", "right"):
            v = pad.get(side)
            if v is None:
                problems.append(f"{e['id']}: root has no {side} padding — the 20px frame is missing "
                                f"and content will sit flush against the viewport edge")
            elif float(str(v) or 0) < 16:
                problems.append(f"{e['id']}: root {side} padding is {v} — the frame is 20 "
                                f"(0 only at mobile_portrait)")
        # mobile_portrait is the one breakpoint where the live site drops the frame to 0.
        for bp in ("tablet_portrait", "mobile_landscape"):
            bpad = s.get(f"_padding:{bp}") or {}
            for side in ("left", "right"):
                if side in bpad and float(str(bpad[side]) or 0) == 0:
                    problems.append(f"{e['id']}: root {side} padding is 0 at {bp} — the frame only "
                                    f"drops to 0 at mobile_portrait")

    # Inherit background down the tree, then contrast-check every piece of text.
    def walk(el, bg):
        s = el.get("settings") or {}
        if isinstance(s, dict):
            back = s.get("_background") or {}
            if back.get("image"):
                bg = IMAGE      # text over a photo: verify the scrim by hand, not by hex
            own = hexof(back.get("color"))
            if own:
                bg = own
            if el["name"] in PRIMITIVES and "themeStyles" in el:
                problems.append(f"{el['id']}: themeStyles on a primitive ({el['name']}) — "
                                f"Bricks renders it unstyled")
            fg = hexof(((s.get("_typography") or {}).get("color")))
            text = s.get("text") or s.get("title")
            if fg and bg and bg is not IMAGE and text:
                px, ratio = font_px(s), contrast(fg, bg)
                weight = str((s.get("_typography") or {}).get("font-weight") or "400")
                large = px >= 24 or (px >= 19 and weight.isdigit() and int(weight) >= 700)
                need = 3.0 if large else 4.5
                if ratio < need:
                    problems.append(f"{el['id']}: {fg} on {bg} is {ratio:.2f}:1 at {px:.0f}px — "
                                    f"needs {need}:1")
        for cid in el.get("children") or []:
            if cid in by_id:
                walk(by_id[cid], bg)

    for r in roots:
        walk(r, None)

    print(f"{'FAIL' if problems else 'ok  '}  {label}  ({len(elements)} elements)")
    for p in problems:
        print(f"        {p}")
    return not problems


def load(path):
    d = json.load(open(path))
    return d["content"] if isinstance(d, dict) and "content" in d else d


def demo():
    """Self-check: the rules must actually fire."""
    # Known-bad: root margin, no frame, background bleeding on the root, red 14px on dark.
    bad = [{"id": "aaaaaa", "name": "section", "parent": 0, "children": ["bbbbbb"],
            "settings": {"_margin": {"top": "40"},
                         "_background": {"color": {"hex": "#212121"}}}},
           {"id": "bbbbbb", "name": "text-basic", "parent": "aaaaaa", "children": [],
            "settings": {"text": "eyebrow",
                         "_typography": {"color": {"hex": "#e60012"}, "font-size": "14"}}}]
    assert not check(bad, "demo/should-fail"), "checker missed a known-bad page"

    # Known-good: section carries only the 20px frame, the panel inside carries the background.
    good = [{"id": "aaaaaa", "name": "section", "parent": 0, "children": ["cccccc"],
             "settings": {"_padding": {"left": "20", "right": "20"}}},
            {"id": "cccccc", "name": "container", "parent": "aaaaaa", "children": ["bbbbbb"],
             "settings": {"_width": "100%", "_padding": {"left": "60", "right": "60"},
                          "_background": {"color": {"hex": "#212121"}}}},
            {"id": "bbbbbb", "name": "text-basic", "parent": "cccccc", "children": [],
             "settings": {"text": "eyebrow",
                          "_typography": {"color": {"hex": "#e0e0e0"}, "font-size": "14"}}}]
    assert check(good, "demo/should-pass"), "checker flagged a clean page"
    assert round(contrast("#e60012", "#212121"), 2) == 3.35
    print("self-check ok")


if __name__ == "__main__":
    args = sys.argv[1:]
    if args == ["--demo"]:
        demo()
        sys.exit(0)
    paths = [p for a in (args or ["references/components/*.json"]) for p in sorted(glob.glob(a))]
    if not paths:
        sys.exit("no files matched")
    sys.exit(0 if all([check(load(p), p) for p in paths]) else 1)
