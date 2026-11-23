#!/usr/bin/env python3
"""Generate tokens.css from tokens.json (standard library only).

Usage:
  python3 design/build_tokens.py          # write design/tokens.css
  python3 design/build_tokens.py --check  # exit 1 if tokens.css is out of date
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "tokens.json"
OUT = HERE / "tokens.css"

THEMED = ("color", "shadow")  # groups split into light / dark
GENERIC_FAMILIES = {
    "serif", "sans-serif", "monospace", "cursive", "fantasy", "system-ui",
    "ui-serif", "ui-sans-serif", "ui-monospace", "ui-rounded",
}
ALIAS = re.compile(r"^\{([^}]+)\}$")
VAR_REF = re.compile(r"var\((--[a-z0-9-]+)\)")


def var(path):
    return "--" + "-".join(path)


def ref(value):
    """'{a.b}' -> 'var(--a-b)'. Other values are returned unchanged."""
    if isinstance(value, str):
        m = ALIAS.match(value)
        if m:
            return f"var({var(m.group(1).split('.'))})"
    return value


def family(names):
    return ", ".join(n if n in GENERIC_FAMILIES else f'"{n}"' for n in names)


def shadow(layers):
    return ", ".join(
        f"{l['offsetX']} {l['offsetY']} {l['blur']} {l['spread']} {l['color']}" for l in layers
    )


def declarations(path, token):
    kind, value = token.get("$type"), token["$value"]
    if kind == "fontFamily":
        return [(var(path), family(value))]
    if kind == "shadow":
        return [(var(path), shadow(value))]
    if kind == "typography":
        size, weight = ref(value["fontSize"]), ref(value["fontWeight"])
        line, fam = value["lineHeight"], ref(value["fontFamily"])
        return [
            (var(path + ["size"]), size),
            (var(path + ["weight"]), weight),
            (var(path + ["line-height"]), line),
            (var(path + ["letter-spacing"]), value["letterSpacing"]),
            (var(path), f"{weight} {size}/{line} {fam}"),  # use as `font: var(--text-h1)`
        ]
    return [(var(path), ref(value))]


def walk(node, path):
    for key, child in node.items():
        if key.startswith("$"):
            continue
        if "$value" in child:
            yield path + [key], child
        else:
            yield from walk(child, path + [key])


def block(selector, decls, indent=""):
    body = "".join(f"{indent}  {name}: {value};\n" for name, value in decls)
    return f"{indent}{selector} {{\n{body}{indent}}}\n"


def build(tokens):
    base, dark = [("color-scheme", "light")], [("color-scheme", "dark")]
    for group, node in tokens.items():
        if group.startswith("$"):
            continue
        if group in THEMED:
            light_keys = {tuple(p) for p, _ in walk(node["light"], [])}
            dark_keys = {tuple(p) for p, _ in walk(node["dark"], [])}
            if light_keys != dark_keys:
                raise SystemExit(f"{group}: light and dark keys differ: {sorted(light_keys ^ dark_keys)}")
            for mode, target in (("light", base), ("dark", dark)):
                for path, token in walk(node[mode], [group]):
                    target.extend(declarations(path, token))
        else:
            for path, token in walk(node, [group]):
                base.extend(declarations(path, token))

    defined = {name for name, _ in base}
    for name, value in base + dark:
        for target in VAR_REF.findall(str(value)):
            if target not in defined:
                raise SystemExit(f"{name}: unknown reference {target}")

    stylesheet = tokens["font"]["$extensions"]["giri.stylesheet"]
    return (
        "/* Generated from tokens.json by build_tokens.py. Do not edit by hand. */\n"
        f'/* Fonts: <link rel="stylesheet" href="{stylesheet}"> */\n'
        + block(":root", base)
        + "@media (prefers-color-scheme: dark) {\n"
        + block(':root:not([data-theme="light"])', dark, indent="  ")
        + "}\n"
        + block(':root[data-theme="dark"]', dark)
    )


def main():
    css = build(json.loads(SRC.read_text(encoding="utf-8")))
    if "--check" in sys.argv[1:]:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != css:
            print("tokens.css is out of date. Run: python3 design/build_tokens.py", file=sys.stderr)
            return 1
        print("tokens.css is up to date")
        return 0
    OUT.write_text(css, encoding="utf-8")
    print(f"wrote {OUT.relative_to(HERE.parent)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
