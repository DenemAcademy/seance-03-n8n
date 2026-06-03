from __future__ import annotations

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "img" / "interface-s3"
OUT.mkdir(parents=True, exist_ok=True)

INK = "#0f172a"
BLUE = "#2563eb"
VIOLET = "#7c3aed"
CYAN = "#cffafe"
GREEN = "#dcfce7"
YELLOW = "#fef3c7"
ROSE = "#ffe4e6"
WHITE = "#ffffff"
SOFT = "#f8fafc"
TERMINAL = "#090d1f"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Supplemental/Courier New Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Courier New.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


F_HERO = font(58, True)
F_TITLE = font(38, True)
F_BODY = font(25)
F_BODY_BOLD = font(25, True)
F_MONO = font(21)
F_MONO_BOLD = font(21, True)
F_SMALL = font(18)
F_SMALL_BOLD = font(18, True)


def text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, fnt: ImageFont.ImageFont, fill: str = INK) -> None:
    draw.text(xy, value, font=fnt, fill=fill)


def wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    value: str,
    width: int,
    fnt: ImageFont.ImageFont,
    fill: str = INK,
    gap: int = 8,
) -> int:
    x, y = xy
    avg = max(9, int(getattr(fnt, "size", 20) * 0.52))
    chars = max(18, width // avg)
    for line in wrap(value, chars):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += getattr(fnt, "size", 20) + gap
    return y


def shadow(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], fill: str, outline: str = INK, size: int = 10) -> None:
    x1, y1, x2, y2 = xy
    draw.rectangle((x1 + size, y1 + size, x2 + size, y2 + size), fill=INK)
    draw.rectangle(xy, fill=fill, outline=outline, width=3)


def header(draw: ImageDraw.ImageDraw, title: str, subtitle: str, badge: str) -> None:
    shadow(draw, (54, 50, 310, 104), BLUE, size=7)
    text(draw, (76, 67), badge.upper(), F_SMALL_BOLD, WHITE)
    text(draw, (54, 128), title, F_HERO, INK)
    wrapped(draw, (58, 202), subtitle, 880, F_BODY, "#334155", 9)


def terminal(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, rows: list[tuple[str, str]]) -> None:
    x1, y1, x2, y2 = xy
    shadow(draw, xy, TERMINAL, size=12)
    draw.rectangle((x1, y1, x2, y1 + 58), fill="#111827")
    for i, color in enumerate(["#fb7185", "#facc15", "#34d399"]):
        draw.ellipse((x1 + 24 + i * 30, y1 + 20, x1 + 42 + i * 30, y1 + 38), fill=color)
    text(draw, (x1 + 128, y1 + 17), title, F_SMALL_BOLD, "#f8fafc")
    y = y1 + 90
    for prompt, body in rows:
        color = "#67e8f9" if prompt in {"$", "n8n", "codex", "claude"} else "#c4b5fd"
        text(draw, (x1 + 30, y), prompt, F_MONO_BOLD, color)
        y = wrapped(draw, (x1 + 120, y), body, x2 - x1 - 160, F_MONO, "#f8fafc", 7)
        y += 8


def card(draw: ImageDraw.ImageDraw, xy: tuple[int, int, int, int], title: str, body: str, fill: str = WHITE) -> None:
    shadow(draw, xy, fill, size=7)
    x1, y1, x2, _ = xy
    text(draw, (x1 + 22, y1 + 22), title, F_BODY_BOLD, INK)
    wrapped(draw, (x1 + 22, y1 + 68), body, x2 - x1 - 44, F_SMALL, "#334155", 7)


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: str = INK) -> None:
    draw.line((start, end), fill=color, width=5)
    ex, ey = end
    sx, sy = start
    if ex >= sx:
        draw.polygon([(ex, ey), (ex - 18, ey - 10), (ex - 18, ey + 10)], fill=color)
    else:
        draw.polygon([(ex, ey), (ex + 18, ey - 10), (ex + 18, ey + 10)], fill=color)


def flow(draw: ImageDraw.ImageDraw, boxes: list[tuple[str, str, str]]) -> None:
    y = 360
    w = 230
    for i, (title, body, tone) in enumerate(boxes):
        x = 60 + i * 275
        card(draw, (x, y, x + w, y + 230), title, body, tone)
        if i < len(boxes) - 1:
            arrow(draw, (x + w + 20, y + 115), (x + 265, y + 115), VIOLET if i % 2 else BLUE)


def grid(draw: ImageDraw.ImageDraw, items: list[tuple[str, str, str]]) -> None:
    for i, (title, body, tone) in enumerate(items):
        col = i % 3
        row = i // 3
        x = 60 + col * 460
        y = 330 + row * 245
        card(draw, (x, y, x + 390, y + 200), title, body, tone)


def save(name: str, title: str, subtitle: str, badge: str, draw_fn) -> None:
    image = Image.new("RGB", (1440, 900), WHITE)
    draw = ImageDraw.Draw(image)
    header(draw, title, subtitle, badge)
    draw_fn(draw)
    image.save(OUT / name, quality=94)


SCENES = [
    (
        "hero-n8n-map.png",
        "n8n en une carte",
        "Un événement arrive, n8n le transforme, appelle les bons outils, puis garde une trace vérifiable.",
        "séance 3",
        lambda d: flow(d, [
            ("Déclencheur", "Formulaire, webhook, horaire ou email entrant.", "#dbeafe"),
            ("Logique", "IF, Switch, Merge, Wait et données propres.", "#ede9fe"),
            ("IA", "OpenAI, Anthropic, AI Agent ou outil MCP.", CYAN),
            ("Action", "Email, Slack, Notion, CRM, API ou fichier.", GREEN),
            ("Trace", "Execution, logs, erreurs et historique.", YELLOW),
        ]),
    ),
    (
        "node-anatomy.png",
        "Anatomie d’un node",
        "Un node a une entrée, des paramètres, des credentials, une sortie et un résultat à vérifier.",
        "node",
        lambda d: grid(d, [
            ("Entrée", "Les données reçues du node précédent.", "#dbeafe"),
            ("Paramètres", "Méthode, URL, champs, filtre ou prompt.", "#ede9fe"),
            ("Credentials", "Le secret stocké dans n8n, pas dans le texte.", CYAN),
            ("Sortie", "Le JSON produit pour l’étape suivante.", GREEN),
            ("Erreur", "Le message à lire si le node bloque.", ROSE),
            ("Preuve", "L’execution qui montre ce qui s’est passé.", YELLOW),
        ]),
    ),
    (
        "workflow-first-build.png",
        "Premier workflow",
        "Le fil rouge : une demande client est triée, enrichie, envoyée et enregistrée.",
        "workflow",
        lambda d: flow(d, [
            ("Webhook", "Reçoit la demande depuis un formulaire.", "#dbeafe"),
            ("Edit Fields", "Garde nom, email, besoin et source.", "#ede9fe"),
            ("IF", "Sépare demande complète et demande incomplète.", CYAN),
            ("IA", "Prépare une réponse claire.", GREEN),
            ("Notifier", "Envoie Slack, Gmail ou Notion.", YELLOW),
        ]),
    ),
    (
        "trigger-map.png",
        "Choisir le bon trigger",
        "Le trigger répond à une question simple : quand le workflow doit-il démarrer ?",
        "trigger",
        lambda d: grid(d, [
            ("Manual", "Pour tester sans toucher au réel.", "#dbeafe"),
            ("Webhook", "Pour recevoir une donnée dès qu’elle arrive.", "#ede9fe"),
            ("Schedule", "Pour lancer une routine chaque jour ou semaine.", CYAN),
            ("Form", "Pour créer une entrée simple côté n8n.", GREEN),
            ("Email", "Pour réagir à une boîte mail.", YELLOW),
            ("App Trigger", "Pour écouter un outil connecté.", ROSE),
        ]),
    ),
    (
        "data-flow-json.png",
        "La donnée circule en JSON",
        "n8n passe des objets d’un node à l’autre. Lire le JSON évite de deviner.",
        "donnée",
        lambda d: terminal(d, (54, 345, 1380, 830), "Sortie d’un node", [
            ("n8n", '{"name": "Camille", "email": "camille@example.com"}'),
            ("n8n", '{"besoin": "réservation groupe", "date": "vendredi"}'),
            ("?", "Quel champ doit servir au node suivant ?"),
            ("→", "Si le champ n’existe pas, le workflow se casse ici."),
        ]),
    ),
    (
        "credentials-safe.png",
        "Credentials propres",
        "Les clés restent dans les credentials ou les variables. Jamais dans une capture publique.",
        "sécurité",
        lambda d: grid(d, [
            ("Bon réflexe", "Créer un credential n8n dédié.", GREEN),
            ("À éviter", "Coller une clé API dans un prompt.", ROSE),
            ("Minimum", "Lire avant de créer, créer avant d’activer.", "#dbeafe"),
            ("Rotation", "Changer la clé si elle fuit.", YELLOW),
            ("Scope", "Limiter les droits quand le plan le permet.", "#ede9fe"),
            ("Trace", "Noter qui utilise quoi.", CYAN),
        ]),
    ),
    (
        "executions-debug.png",
        "Lire une execution",
        "Le debug part du node qui a cassé, pas d’une supposition générale.",
        "debug",
        lambda d: terminal(d, (54, 345, 1380, 830), "Execution", [
            ("1", "Webhook : reçu"),
            ("2", "Edit Fields : ok"),
            ("3", "HTTP Request : erreur 401"),
            ("?", "Credential absent ou mauvais header ?"),
            ("→", "Corriger ce node, puis relancer seulement le test."),
        ]),
    ),
    (
        "if-switch-logic.png",
        "IF et Switch",
        "Ces nodes évitent de traiter toutes les demandes de la même manière.",
        "logique",
        lambda d: flow(d, [
            ("Demande", "Un client envoie son besoin.", "#dbeafe"),
            ("IF", "Email présent ?", "#ede9fe"),
            ("Branche A", "Réponse + CRM.", GREEN),
            ("Branche B", "Demande d’information.", YELLOW),
            ("Trace", "La raison est visible.", CYAN),
        ]),
    ),
    (
        "merge-wait-loop.png",
        "Merge, Wait, Loop",
        "Les workflows sérieux doivent parfois rassembler, attendre ou répéter avec limite.",
        "flux",
        lambda d: grid(d, [
            ("Merge", "Réunit deux sources avant la suite.", "#dbeafe"),
            ("Wait", "Attend une date ou une réponse.", "#ede9fe"),
            ("Loop", "Traite une liste sans tout casser.", CYAN),
            ("Limite", "Évite les boucles sans fin.", ROSE),
            ("Preuve", "Chaque passage est visible.", GREEN),
            ("Usage", "Relances, listes, lots et validations.", YELLOW),
        ]),
    ),
    (
        "http-request-api.png",
        "HTTP Request",
        "Le node HTTP Request appelle une API quand il n’existe pas de node prêt à l’emploi.",
        "api",
        lambda d: terminal(d, (54, 345, 1380, 830), "HTTP Request", [
            ("GET", "https://api.exemple.com/customers"),
            ("POST", "https://api.exemple.com/orders"),
            ("HEAD", "Authorization: Bearer *****"),
            ("BODY", '{"email": "client@example.com", "tag": "lead"}'),
            ("→", "Tester la réponse avant d’utiliser la donnée."),
        ]),
    ),
    (
        "ai-agent-tools.png",
        "AI Agent et outils",
        "Un AI Agent doit avoir un modèle et au moins un outil clair. Sinon il parle, mais il n’agit pas.",
        "agent",
        lambda d: flow(d, [
            ("Chat Model", "OpenAI ou Anthropic.", "#dbeafe"),
            ("AI Agent", "Décide quel outil appeler.", "#ede9fe"),
            ("Tools", "Gmail, HTTP, MCP, workflow.", CYAN),
            ("Output", "Réponse ou action vérifiable.", GREEN),
            ("Limite", "Max iterations et format attendu.", YELLOW),
        ]),
    ),
    (
        "mcp-two-directions.png",
        "MCP dans deux sens",
        "n8n peut consommer des outils MCP, ou exposer ses workflows à des clients MCP.",
        "mcp",
        lambda d: grid(d, [
            ("n8n client MCP", "AI Agent + MCP Client Tool appelle un serveur externe.", "#dbeafe"),
            ("n8n serveur MCP", "MCP Server Trigger ou accès instance expose des workflows.", "#ede9fe"),
            ("Claude Code", "Se connecte en client MCP.", CYAN),
            ("Codex CLI", "Se connecte via config MCP.", GREEN),
            ("Risque", "Tous les clients voient ce qui est exposé.", ROSE),
            ("Méthode", "Exposer peu, tester, documenter.", YELLOW),
        ]),
    ),
    (
        "n8n-as-mcp-server.png",
        "n8n comme serveur MCP",
        "Claude Code ou Codex peuvent appeler les workflows que vous rendez disponibles.",
        "serveur",
        lambda d: flow(d, [
            ("Workflow", "Décrit clairement ce qu’il fait.", "#dbeafe"),
            ("Available in MCP", "Activation contrôlée.", "#ede9fe"),
            ("Client", "Claude Code ou Codex.", CYAN),
            ("Tool call", "Exécution ou création de workflow.", GREEN),
            ("Logs", "Contrôle dans n8n.", YELLOW),
        ]),
    ),
    (
        "n8n-as-mcp-client.png",
        "n8n comme client MCP",
        "Un agent n8n peut appeler des outils externes fournis par un serveur MCP.",
        "client",
        lambda d: flow(d, [
            ("AI Agent", "Reçoit la consigne.", "#dbeafe"),
            ("MCP Client Tool", "Pointe vers un SSE endpoint.", "#ede9fe"),
            ("Serveur MCP", "Expose des outils.", CYAN),
            ("Réponse", "Le résultat revient dans le workflow.", GREEN),
            ("Suite", "n8n notifie ou enregistre.", YELLOW),
        ]),
    ),
    (
        "claude-code-mcp-setup.png",
        "Claude Code vers n8n",
        "La commande ajoute n8n comme serveur MCP HTTP dans Claude Code.",
        "claude",
        lambda d: terminal(d, (54, 345, 1380, 830), "Claude Code MCP", [
            ("$", "claude mcp add --transport http n8n-mcp https://votre-n8n/mcp-server/http"),
            ("$", 'claude mcp add --transport http n8n-mcp https://votre-n8n/mcp-server/http --header "Authorization: Bearer <TOKEN>"'),
            ("$", "claude mcp list"),
            ("/", "/mcp pour vérifier les outils disponibles"),
        ]),
    ),
    (
        "codex-mcp-setup.png",
        "Codex CLI vers n8n",
        "Codex lit le serveur MCP dans sa configuration ou via la commande codex mcp.",
        "codex",
        lambda d: terminal(d, (54, 345, 1380, 830), "Codex MCP", [
            ("$", "codex mcp add n8n-mcp --url https://votre-n8n/mcp-server/http"),
            ("TOML", "[mcp_servers.n8n-mcp]"),
            ("TOML", 'url = "https://votre-n8n/mcp-server/http"'),
            ("TOML", 'http_headers = { "authorization" = "Bearer <TOKEN>" }'),
        ]),
    ),
    (
        "api-create-workflow.png",
        "Créer via API",
        "L’API permet à un agent de créer, lister, mettre à jour ou activer un workflow.",
        "api",
        lambda d: terminal(d, (54, 345, 1380, 830), "n8n API", [
            ("GET", "/api/v1/workflows"),
            ("POST", "/api/v1/workflows"),
            ("PUT", "/api/v1/workflows/{id}"),
            ("POST", "/api/v1/workflows/{id}/activate"),
            ("HEAD", "X-N8N-API-KEY: *****"),
        ]),
    ),
    (
        "workflow-json-structure.png",
        "Structure JSON",
        "Un workflow généré par un agent doit contenir nodes, connections, settings et nom lisible.",
        "json",
        lambda d: terminal(d, (54, 345, 1380, 830), "workflow.json", [
            ("{", '"name": "Lead - réception et réponse",'),
            (" ", '"nodes": [ ... ],'),
            (" ", '"connections": { ... },'),
            (" ", '"settings": { "executionOrder": "v1" }'),
            ("}", "Importer, tester, puis activer seulement après contrôle."),
        ]),
    ),
    (
        "security-checklist.png",
        "Sécurité terrain",
        "Une automatisation utile devient dangereuse si les droits sont trop larges.",
        "sécurité",
        lambda d: grid(d, [
            ("Pas de secret", "Aucune clé dans Git ou dans le support.", ROSE),
            ("Test d’abord", "Manual Trigger avant production.", "#dbeafe"),
            ("Droits bas", "Scopes et credentials limités.", "#ede9fe"),
            ("Logs lus", "Executions vérifiées.", CYAN),
            ("Activation manuelle", "Pas d’activation aveugle.", YELLOW),
            ("Rollback", "Export JSON gardé.", GREEN),
        ]),
    ),
    (
        "error-workflow.png",
        "Workflow d’erreur",
        "Une erreur doit alerter quelqu’un au lieu de rester cachée.",
        "erreur",
        lambda d: flow(d, [
            ("Error Trigger", "Démarre sur erreur.", ROSE),
            ("Lire contexte", "Workflow, node, execution.", "#ede9fe"),
            ("Notifier", "Slack ou email interne.", CYAN),
            ("Prioriser", "Bloquant ou simple alerte.", YELLOW),
            ("Corriger", "Retour au node fautif.", GREEN),
        ]),
    ),
    (
        "production-routine.png",
        "Routine production",
        "Un workflow publié a besoin de noms, tests, traces et règles simples.",
        "prod",
        lambda d: grid(d, [
            ("Nom clair", "Verbe + objet + canal.", "#dbeafe"),
            ("Dossier", "Projet ou client visible.", "#ede9fe"),
            ("Description", "But et limite du workflow.", CYAN),
            ("Tags", "Support, lead, CRM, test.", GREEN),
            ("Historique", "Export avant gros changement.", YELLOW),
            ("Surveillance", "Executions et erreurs.", ROSE),
        ]),
    ),
    (
        "final-checklist.png",
        "Checklist finale",
        "Le support finit sur une méthode que vous pouvez refaire sans vous perdre.",
        "final",
        lambda d: grid(d, [
            ("Comprendre", "Ce que n8n automatise.", "#dbeafe"),
            ("Construire", "Un workflow simple.", "#ede9fe"),
            ("Brancher", "API ou MCP selon le besoin.", CYAN),
            ("Tester", "Manual, test URL, executions.", GREEN),
            ("Activer", "Seulement après preuve.", YELLOW),
            ("Documenter", "Résumé et liens officiels.", ROSE),
        ]),
    ),
]


def main() -> None:
    for scene in SCENES:
        save(*scene)
    print(f"Wrote {len(SCENES)} images to {OUT}")


if __name__ == "__main__":
    main()

