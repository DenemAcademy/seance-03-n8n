from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "img" / "user-n8n"
OUT.mkdir(parents=True, exist_ok=True)

INK = "#2b2d31"
MUTED = "#7b7d82"
BORDER = "#dedfe3"
ACCENT = "#ff6d5a"
PURPLE = "#6354d9"
GREEN = "#4cae67"
BG = "#ffffff"
SOFT = "#f7f7f8"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    names = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Helvetica Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Helvetica.ttf",
    ]
    for name in names:
        path = Path(name)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


F10 = font(10)
F12 = font(12)
F14 = font(14)
F16 = font(16)
F18 = font(18)
F20 = font(20)
F22 = font(22)
F24 = font(24)
F26 = font(26)
F30 = font(30)
F36 = font(36)
F44 = font(44)
F16B = font(16, True)
F18B = font(18, True)
F20B = font(20, True)
F22B = font(22, True)
F24B = font(24, True)
F26B = font(26, True)
F30B = font(30, True)
F36B = font(36, True)


def text(d: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, fnt=F18, fill=INK) -> None:
    d.text(xy, value, font=fnt, fill=fill)


def rounded(d: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill=BG, outline=BORDER, width=2, radius=10) -> None:
    d.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def line(d: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill=BORDER, width=2) -> None:
    d.line(xy, fill=fill, width=width)


def browser(img: Image.Image, title: str = "n8n.magetrans.fr/home/workflows") -> ImageDraw.ImageDraw:
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, img.width, img.height), fill=BG)
    d.rectangle((0, 0, img.width, 56), fill="#fbfbfc", outline=BORDER)
    text(d, (20, 16), "‹", F30, "#555")
    text(d, (55, 15), "›", F30, "#aaa")
    text(d, (92, 14), "⟳", F22, "#666")
    rounded(d, (300, 8, min(img.width - 300, 1060), 48), fill="#f1f1f4", outline="#f1f1f4", radius=12)
    text(d, (330, 17), title, F16, "#333")
    return d


def sidebar(d: ImageDraw.ImageDraw, h: int, selected: str = "Overview", settings: bool = False) -> None:
    d.rectangle((0, 56, 235, h), fill="#fbfbfc", outline=BORDER)
    text(d, (22, 84), "⌘ n8n", F20B, INK)
    items = ["Overview", "Personal", "Shared with you", "Chat  beta"]
    y = 130
    for item in items:
        fill = "#f2f2f4" if item.startswith(selected) else "#fbfbfc"
        rounded(d, (12, y - 8, 220, y + 34), fill=fill, outline=PURPLE if item.startswith(selected) else fill, width=2, radius=6)
        text(d, (28, y), item, F18, INK)
        y += 48
    if settings:
        y = h - 230
        for item in ["Templates", "Help", "Settings"]:
            text(d, (28, y), item, F18, INK)
            y += 46


def tabs(d: ImageDraw.ImageDraw, x: int, y: int, active: str, labels: list[str]) -> None:
    cx = x
    for label in labels:
        color = ACCENT if label == active else "#707276"
        text(d, (cx, y), label, F18B, color)
        if label == active:
            line(d, (cx, y + 32, cx + len(label) * 11, y + 32), ACCENT, 3)
        cx += max(120, len(label) * 14)


def workflow_row(d: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, meta: str) -> None:
    rounded(d, xy, fill=BG, outline=BORDER, radius=10)
    text(d, (xy[0] + 24, xy[1] + 24), title, F18B, INK)
    text(d, (xy[0] + 24, xy[1] + 52), meta, F14, "#96989c")
    rounded(d, (xy[2] - 180, xy[1] + 26, xy[2] - 80, xy[1] + 58), fill=BG, outline=BORDER, radius=6)
    text(d, (xy[2] - 155, xy[1] + 33), "Personal", F14, MUTED)
    d.ellipse((xy[2] - 56, xy[1] + 32, xy[2] - 38, xy[1] + 50), fill="#e8f7ee", outline=GREEN, width=2)
    text(d, (xy[2] - 29, xy[1] + 30), "⋮", F22, "#444")


def overview() -> Image.Image:
    img = Image.new("RGB", (1600, 900), BG)
    d = browser(img)
    sidebar(d, img.height, "Overview")
    text(d, (290, 92), "Overview", F26B, INK)
    text(d, (290, 126), "All the workflows, credentials and data tables you have access to", F18, "#9a9a9c")
    tabs(d, 305, 200, "Workflows", ["Workflows", "Credentials", "Executions", "Variables", "Data tables"])
    rounded(d, (1080, 96, 1250, 142), fill=ACCENT, outline=ACCENT, radius=8)
    text(d, (1110, 109), "Create workflow", F18B, BG)
    rounded(d, (1080, 250, 1310, 294), fill=BG, outline=BORDER, radius=6)
    text(d, (1125, 262), "Search", F18, "#aaa")
    rounded(d, (1320, 250, 1530, 294), fill=BG, outline=BORDER, radius=6)
    text(d, (1335, 262), "Sort by last updated", F16, "#555")
    workflow_row(d, (290, 335, 1530, 430), "Suivi Teliway V13", "Last updated 1 week ago | Created 26 March")
    workflow_row(d, (290, 450, 1530, 545), "CHATBOT_RH_SECURE_V2", "Last updated 1 week ago | Created 20 May")
    workflow_row(d, (290, 565, 1530, 660), "TMP_XLSX_INSPECT_1779301607226", "Last updated 1 week ago | Created 20 May")
    text(d, (1260, 720), "Total 3", F16, INK)
    rounded(d, (1360, 700, 1398, 738), fill=BG, outline=ACCENT, radius=6)
    text(d, (1374, 708), "1", F16, ACCENT)
    rounded(d, (1450, 700, 1570, 738), fill=BG, outline=BORDER, radius=6)
    text(d, (1470, 708), "50/page", F16, "#555")
    return img


def workflow_canvas(executions: bool = False) -> Image.Image:
    img = Image.new("RGB", (1600, 900), BG)
    d = browser(img, "n8n.magetrans.fr/workflow/suivi-teliway-v13")
    sidebar(d, img.height, selected="", settings=False)
    text(d, (270, 92), "Personal  /  Suivi Teliway V13", F18, "#666")
    rounded(d, (1150, 80, 1220, 118), fill=BG, outline=BORDER, radius=6)
    text(d, (1168, 88), "Publish", F14, "#aaa")
    text(d, (1260, 88), "Saved", F16, "#888")
    rounded(d, (1320, 74, 1560, 126), fill="#f5f8fb", outline=BORDER, radius=6)
    text(d, (1345, 90), "GitHub  Star   190,939", F18B, INK)
    rounded(d, (810, 78, 1080, 126), fill="#dedede", outline="#dedede", radius=8)
    for i, label in enumerate(["Editor", "Executions", "Evaluations"]):
        x = 820 + i * 90
        if (executions and label == "Executions") or (not executions and label == "Editor"):
            rounded(d, (x, 86, x + 78, 120), fill=BG, outline=BG, radius=6)
        text(d, (x + 14, 94), label, F15 if "F15" in globals() else F14, INK if (executions and label == "Executions") or (not executions and label == "Editor") else "#777")
    d.rectangle((235, 126, img.width, img.height), fill="#fcfcfd")
    if executions:
        d.rectangle((235, 126, 420, img.height), fill=BG, outline=BORDER)
        text(d, (260, 175), "Executions", F26, INK)
        text(d, (280, 235), "✓ Auto refresh", F18, MUTED)
        for y, label in [(300, "Jun 1, 09:35:41\nSucceeded in 11.843s"), (405, "May 27, 10:00:40\nSucceeded in 19.913s"), (510, "May 27, 08:16:40\nSucceeded in 10.458s")]:
            d.rectangle((260, y, 390, y + 82), fill="#eeeeef" if y == 300 else BG)
            for j, part in enumerate(label.split("\n")):
                text(d, (280, y + 14 + j * 24), part, F18B if j == 0 else F16, INK if j == 0 else "#777")
        text(d, (450, 165), "Jun 1, 09:35:41", F26B, INK)
        text(d, (450, 205), "Succeeded in 11.843s | ID#117247", F20, GREEN)
        d.rectangle((420, 260, img.width, 690), fill="#fbfbfb")
        draw_nodes(d, 520, 420, small=True)
        d.rectangle((420, 690, img.width, img.height), fill=BG, outline=BORDER)
        text(d, (450, 720), "Logs", F20B, INK)
        text(d, (675, 720), "{}  Next Email   Success in 13ms", F20B, INK)
        rounded(d, (1240, 710, 1305, 748), fill=BG, outline=BORDER, radius=6)
        text(d, (1260, 718), "Input", F16B, INK)
        rounded(d, (1320, 710, 1390, 748), fill="#e8e8e8", outline=BORDER, radius=6)
        text(d, (1340, 718), "Output", F16B, INK)
    else:
        draw_nodes(d, 360, 390, small=True)
        rounded(d, (835, 680, 1060, 740), fill=ACCENT, outline=ACCENT, radius=6)
        text(d, (880, 696), "Execute workflow", F20B, BG)
        for x, label in [(260, "⛶"), (330, "⊕"), (400, "⊖"), (470, "↶"), (540, "🧹")]:
            rounded(d, (x, 680, x + 50, 730), fill=BG, outline=BORDER, radius=6)
            text(d, (x + 14, 692), label, F20, "#555")
    return img


def draw_nodes(d: ImageDraw.ImageDraw, x: int, y: int, small: bool = False) -> None:
    labels = ["Gmail", "Split", "Normalize", "Chat", "Classify", "IF", "Log", "OpenAI", "Filter", "Next", "Gmail", "Postgres", "Mark"]
    step = 72 if small else 105
    box = 28 if small else 42
    for i, label in enumerate(labels):
        bx = x + i * step
        rounded(d, (bx, y, bx + box, y + box), fill=BG, outline="#cfd8d3", radius=4)
        text(d, (bx + 6, y + 7), "{}", F10, ACCENT)
        if i < len(labels) - 1:
            line(d, (bx + box, y + box // 2, bx + step, y + box // 2), "#c8c8c8", 2)
    line(d, (x + step * 6, y + box, x + step * 8, y + 90), "#c8c8c8", 2)
    line(d, (x + step * 8, y + 90, x + step * 10, y + box), "#c8c8c8", 2)


def node_output() -> Image.Image:
    img = Image.new("RGB", (1500, 430), BG)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 300, img.height), fill="#fbfbfb", outline=BORDER)
    text(d, (20, 22), "Logs", F22, INK)
    text(d, (20, 78), "Success in 11.843s", F20, "#777")
    for i, label in enumerate(["Log Run", "Mark Traite", "Mark Lu"]):
        text(d, (45, 150 + i * 55), label, F20, INK)
    text(d, (330, 24), "{}  Next Email   Success in 13ms", F22B, INK)
    rounded(d, (1220, 15, 1298, 54), fill=BG, outline="#aaa", radius=6)
    text(d, (1243, 23), "Input", F18B, INK)
    rounded(d, (1310, 15, 1398, 54), fill="#e8e8e8", outline="#aaa", radius=6)
    text(d, (1330, 23), "Output", F18B, INK)
    text(d, (330, 86), "O U T P U T", F20B, "#999")
    text(d, (1430, 86), "1 item", F18, "#999")
    d.rectangle((330, 130, 1480, 230), fill=BG, outline=BORDER)
    for x in [620, 920]:
        line(d, (x, 130, x, 230), BORDER, 2)
    text(d, (345, 145), "id", F18B, INK)
    text(d, (635, 145), "threadId", F18B, INK)
    text(d, (935, 145), "labelIds", F18B, INK)
    line(d, (330, 175, 1480, 175), BORDER, 2)
    text(d, (345, 190), "19e821c041baf408", F18, "#777")
    text(d, (635, 190), "19e821c041baf408", F18, "#777")
    text(d, (935, 190), "0 : Label_2243004221676319157", F18, "#777")
    return img


def credential_modal() -> Image.Image:
    img = Image.new("RGB", (1600, 950), "#353535")
    d = ImageDraw.Draw(img)
    rounded(d, (40, 35, 1560, 915), fill=BG, outline=BORDER, radius=14)
    text(d, (95, 85), "◌", F44, INK)
    text(d, (140, 80), "OpenAi account 2", F30, INK)
    text(d, (140, 118), "OpenAi", F18, "#999")
    rounded(d, (1420, 82, 1510, 132), fill=ACCENT, outline=ACCENT, radius=7)
    text(d, (1442, 96), "Save", F22B, BG)
    line(d, (40, 175, 1560, 175), BORDER, 2)
    text(d, (70, 235), "Connection", F22, INK)
    text(d, (365, 305), "Need help filling out these fields?  Open docs", F20, ACCENT)
    text(d, (365, 405), "API Key *", F22B, "#777")
    rounded(d, (365, 450, 1510, 520), fill=BG, outline=BORDER, radius=6)
    text(d, (365, 590), "Organization ID (optional)", F22B, "#777")
    rounded(d, (365, 635, 1510, 705), fill=BG, outline=BORDER, radius=6)
    text(d, (365, 735), "Only required if you belong to multiple organisations", F18, "#777")
    text(d, (365, 800), "Base URL", F22B, "#777")
    rounded(d, (365, 845, 1510, 915), fill=BG, outline=BORDER, radius=6)
    text(d, (385, 862), "https://api.openai.com/v1", F22, INK)
    return img


def logs_list() -> Image.Image:
    img = Image.new("RGB", (620, 760), "#f4f4f5")
    d = ImageDraw.Draw(img)
    labels = ["Aucun Match", "Generation Reponse IA", "Loop Candidats", "IF Encore Candidats", "Log Position", "Préparer Candidats", "IF Match Trouvé", "Unified Parser V10", "Log Classification", "Évaluer Match", "Parser Classification"]
    y = 30
    for label in labels:
        text(d, (32, y + 12), "›", F26, "#888")
        rounded(d, (78, y, 120, y + 42), fill=BG, outline=BORDER, radius=7)
        text(d, (90, y + 8), "{}" if "IF" not in label and "Loop" not in label and "Generation" not in label else "↳", F16B, ACCENT if "{}" in "{}" else GREEN)
        text(d, (145, y + 10), label, F20, INK)
        if label != "Aucun Match":
            text(d, (535, y + 10), "1 item", F18, "#999")
        y += 66
    return img


def node_categories(search: str | None = None) -> Image.Image:
    img = Image.new("RGB", (760, 1150), BG)
    d = ImageDraw.Draw(img)
    text(d, (30, 36), "What happens next?", F30B, INK)
    line(d, (0, 100, 760, 100), BORDER, 2)
    rounded(d, (32, 135, 728, 205), fill=BG, outline=PURPLE, radius=8)
    text(d, (75, 152), search or "Search nodes...", F24, "#999" if not search else INK)
    if not search:
        rows = [
            ("AI", "Build autonomous agents, summarize or search documents, etc."),
            ("Action in an app", "Do something in an app or service like Google Sheets, Telegram or Notion"),
            ("Data transformation", "Manipulate, filter or convert data"),
            ("Flow", "Branch, merge or loop the flow, etc."),
            ("Core", "Run code, make HTTP requests, set webhooks, etc."),
            ("Human in the loop", "Wait for approval or human input before continuing"),
            ("Add another trigger", "Triggers start your workflow. Workflows can have multiple triggers."),
        ]
    elif search == "gma":
        rows = [
            ("Gmail", ""),
            ("Gamma", "Create AI-powered presentations, documents, and websites with Gamma"),
            ("GPTMaker", "Consume GPTMaker API"),
            ("gotoHuman", "Request human reviews with gotoHuman"),
            ("GREEN-API for MAX", "Starts the workflow on a Green-Api webhook"),
            ("AgentMail", "Triggers when an email event occurs"),
            ("Figma (Beta)", ""),
            ("Gumroad Trigger", ""),
            ("Enginemailer", ""),
        ]
    else:
        rows = [
            ("TriggerCMD", "Run a command on a computer."),
            ("Chat Trigger", ""),
            ("SSE Trigger", "Triggers the workflow when Server-Sent Events occur"),
            ("Toggl Trigger", ""),
            ("MQTT Trigger", ""),
            ("AMQP Trigger", ""),
            ("Error Trigger", "Triggers the workflow when another workflow has an error"),
            ("Manual Trigger", ""),
            ("Tally Trigger", "Starts the workflow on a Tally form submission"),
        ]
    y = 300 if not search else 290
    for title, body in rows:
        text(d, (115, y), title, F24 if not search else F22, INK)
        if body:
            for i, line_text in enumerate(wrap(body, 42)):
                text(d, (115, y + 36 + i * 26), line_text, F18, "#777")
        text(d, (690, y + 10), "→", F24, "#999")
        y += 120 if body else 82
    return img


def gmail_actions() -> Image.Image:
    img = Image.new("RGB", (760, 1200), BG)
    d = ImageDraw.Draw(img)
    text(d, (35, 42), "‹", F36, "#777")
    text(d, (95, 45), "M", F30B, "#db4437")
    text(d, (150, 42), "Gmail", F30B, INK)
    line(d, (0, 120, 760, 120), BORDER, 2)
    rounded(d, (30, 150, 730, 220), fill=BG, outline=PURPLE, radius=8)
    text(d, (80, 168), "Search Gmail Actions...", F22, "#999")
    text(d, (30, 260), "Actions (26)", F24B, INK)
    text(d, (30, 375), "M E S S A G E  A C T I O N S", F18B, "#777")
    actions = ["Add label to message", "Delete a message", "Get a message", "Get many messages", "Mark a message as read", "Mark a message as unread", "Remove label from message", "Reply to a message", "Send a message", "Send message and wait for response"]
    y = 430
    for action in actions:
        text(d, (32, y), "M", F22B, "#db4437")
        text(d, (96, y), action, F22, INK)
        y += 70
    return img


def settings_menu() -> Image.Image:
    img = overview()
    d = ImageDraw.Draw(img)
    rounded(d, (225, 700, 545, 892), fill=BG, outline=BORDER, radius=8)
    for i, label in enumerate(["Usage and plan", "Personal", "n8n API", "Instance-level MCP", "Sign out"]):
        text(d, (265, 730 + i * 40), label, F18, INK)
    return img


def api_settings() -> Image.Image:
    img = Image.new("RGB", (1600, 900), BG)
    d = browser(img, "n8n.magetrans.fr/settings/api")
    d.rectangle((0, 56, 235, img.height), fill="#fbfbfc", outline=BORDER)
    items = ["‹ Settings", "Usage and plan", "Personal", "n8n API", "Instance-level MCP", "Version 2.2.5"]
    y = 90
    for item in items:
        fill = "#f3f3f4" if item == "n8n API" else "#fbfbfc"
        d.rectangle((10, y - 10, 220, y + 28), fill=fill)
        text(d, (28, y), item, F18, ACCENT if item.startswith("Version") else INK)
        y += 48
    text(d, (300, 160), "API", F36, INK)
    text(d, (370, 175), "(beta)", F18, "#999")
    text(d, (300, 245), "Use your API Key to control n8n programmatically using the n8n API. But if you only want to trigger workflows, consider using the webhook node instead.", F18, "#888")
    workflow_row(d, (300, 330, 1530, 430), "TEST", "Expires on Sat, Jun 6 2026                                      ******T-PI")
    workflow_row(d, (300, 450, 1530, 550), "Baptiste fort", "This API key has expired                                      ******zueQ")
    rounded(d, (1380, 625, 1530, 680), fill=ACCENT, outline=ACCENT, radius=6)
    text(d, (1400, 642), "Create an API Key", F20B, BG)
    return img


def create_api_key() -> Image.Image:
    img = Image.new("RGB", (1300, 900), "#333333")
    d = ImageDraw.Draw(img)
    rounded(d, (80, 90, 1220, 815), fill=BG, outline=BORDER, radius=12)
    text(d, (130, 145), "Create API Key", F36, INK)
    text(d, (1120, 145), "×", F30, "#999")
    text(d, (130, 230), "Label", F24B, INK)
    rounded(d, (130, 275, 1170, 345), fill=BG, outline=PURPLE, radius=7)
    text(d, (148, 292), "e.g Internal Project", F22, "#999")
    text(d, (130, 405), "Expiration", F24B, INK)
    rounded(d, (130, 445, 510, 515), fill=BG, outline=BORDER, radius=7)
    text(d, (150, 463), "30 days", F22, INK)
    text(d, (540, 467), "The API key will expire on Fri, Jul 3 2026", F20, "#777")
    text(d, (130, 570), "Scopes", F24B, INK)
    rounded(d, (130, 615, 1170, 740), fill=BG, outline=BORDER, radius=7)
    scopes = ["tag:create", "tag:list", "tag:read", "workflow:create", "workflow:read", "workflowTags:list", "+ 13"]
    x, y = 150, 630
    for s in scopes:
        w = 18 + len(s) * 11
        rounded(d, (x, y, x + w, y + 35), fill="#e5e5e6", outline="#e5e5e6", radius=18)
        text(d, (x + 10, y + 6), s, F18, INK)
        x += w + 10
        if x > 1000:
            x = 150
            y += 45
    text(d, (170, 765), "Upgrade to unlock the ability to modify API key scopes", F18, ACCENT)
    rounded(d, (1065, 760, 1170, 815), fill="#ffc5bf", outline="#ffc5bf", radius=7)
    text(d, (1090, 775), "Save", F20B, BG)
    return img


def instance_mcp(dialog: bool = False) -> Image.Image:
    img = api_settings()
    d = ImageDraw.Draw(img)
    d.rectangle((235, 56, img.width, img.height), fill=BG)
    text(d, (300, 155), "Instance-level MCP", F36, INK)
    text(d, (300, 210), "Let MCP clients like Claude, Lovable, and other AI tools discover and execute your n8n workflows. Learn more", F16, "#999")
    text(d, (1270, 150), "Enabled", F16B, GREEN)
    rounded(d, (1390, 140, 1540, 178), fill=BG, outline=BORDER, radius=6)
    text(d, (1410, 148), "Connection details", F16, INK)
    tabs(d, 320, 275, "Workflows", ["Workflows", "Connected clients"])
    rounded(d, (300, 330, 1530, 690), fill=BG, outline=BORDER, radius=10)
    text(d, (860, 465), "No workflows enabled", F22, "#888")
    text(d, (720, 510), "Add compatible workflows so MCP clients can discover and execute them", F16, "#888")
    rounded(d, (865, 555, 1030, 605), fill=ACCENT, outline=ACCENT, radius=6)
    text(d, (885, 570), "Enable workflows", F18B, BG)
    if dialog:
        d.rectangle((0, 0, img.width, img.height), fill=(50, 50, 50))
        rounded(d, (300, 120, 1180, 580), fill=BG, outline=BORDER, radius=12)
        text(d, (350, 175), "Enable workflow MCP access", F36, INK)
        text(d, (1080, 175), "×", F30, "#999")
        rounded(d, (350, 255, 1120, 330), fill="#f5f5f6", outline=BORDER, radius=4)
        text(d, (375, 275), "Workflows that are published and have one of webhook, form, schedule or chat trigger", F20, "#777")
        text(d, (375, 304), "nodes can be enabled for MCP access. Read more", F20, "#777")
        rounded(d, (350, 365, 1120, 435), fill=BG, outline=BORDER, radius=7)
        text(d, (400, 385), "Search workflows to connect", F22, "#999")
        rounded(d, (950, 485, 1050, 535), fill=BG, outline="#aaa", radius=7)
        text(d, (977, 500), "Cancel", F20, INK)
        rounded(d, (1070, 485, 1170, 535), fill="#ffc5bf", outline="#ffc5bf", radius=7)
        text(d, (1095, 500), "Enable", F20B, BG)
    return img


def main() -> None:
    images = [
        ("01-overview-workflows.png", overview()),
        ("02-workflow-editor.png", workflow_canvas(False)),
        ("03-execution-success.png", workflow_canvas(True)),
        ("04-node-output.png", node_output()),
        ("05-openai-credential.png", credential_modal()),
        ("06-node-logs-list.png", logs_list()),
        ("07-add-node-categories.png", node_categories()),
        ("08-search-gmail.png", node_categories("gma")),
        ("09-search-trigger.png", node_categories("trigger")),
        ("10-gmail-actions.png", gmail_actions()),
        ("11-settings-menu.png", settings_menu()),
        ("12-api-settings.png", api_settings()),
        ("13-create-api-key.png", create_api_key()),
        ("14-instance-mcp.png", instance_mcp(False)),
        ("15-enable-mcp-access.png", instance_mcp(True)),
    ]
    for name, image in images:
        image.save(OUT / name, quality=94)
    print(f"Wrote {len(images)} requested n8n screens to {OUT}")


if __name__ == "__main__":
    main()
