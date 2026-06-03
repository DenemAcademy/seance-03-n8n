from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "support-technique-seance-03.html"
INDEX_OUT = ROOT / "index.html"


DOCS = {
    "n8n_docs": "https://docs.n8n.io/",
    "n8n_workflows": "https://docs.n8n.io/workflows/",
    "n8n_workflow_components": "https://docs.n8n.io/workflows/components/",
    "n8n_node_types": "https://docs.n8n.io/integrations/builtin/node-types/",
    "n8n_http_request": "https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/",
    "n8n_api": "https://docs.n8n.io/api/",
    "n8n_api_auth": "https://docs.n8n.io/api/authentication/",
    "n8n_api_reference": "https://docs.n8n.io/api/api-reference/",
    "n8n_mcp_instance": "https://docs.n8n.io/advanced-ai/mcp/accessing-n8n-mcp-server/",
    "n8n_mcp_trigger": "https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/",
    "n8n_mcp_client": "https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp/",
    "n8n_ai_agent": "https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/",
    "codex_mcp": "https://developers.openai.com/codex/mcp",
    "codex_cli": "https://developers.openai.com/codex/cli",
    "claude_mcp": "https://code.claude.com/docs/en/mcp",
}


def item(
    title: str,
    why: str,
    do: str,
    verify: str,
    question: str,
    image: str,
    *,
    link: str = "n8n_docs",
    code: list[str] | None = None,
    tip: str = "",
) -> dict[str, object]:
    return {
        "title": title,
        "why": why,
        "do": do,
        "verify": verify,
        "question": question,
        "image": image,
        "link": link,
        "code": code or [],
        "tip": tip
        or "Gardez une preuve avant de continuer : capture, execution, lien, JSON, message d’erreur ou commande copiée proprement.",
    }


CHAPTERS = [
    (
        "Acte 1 - Comprendre n8n",
        "On pose les mots simples avant de toucher au canvas. Le fil rouge est une demande client qui arrive et qui doit être traitée sans perdre d’information.",
        "Comprendre",
        "blue",
        [
            item(
                "n8n en phrase simple",
                "n8n est un outil d’automatisation visuelle. Il relie des services entre eux : formulaire, email, Slack, Notion, CRM, API, IA. Une action arrive, n8n la reçoit, applique une logique, puis déclenche la suite. L’idée n’est pas de remplacer votre jugement. L’idée est d’éviter de refaire chaque jour les mêmes gestes manuels.",
                "Retenez une phrase courte : `n8n fait circuler une donnée entre plusieurs outils, avec des règles visibles.` Cette phrase suffit pour commencer. Si la définition devient trop technique, la pratique devient floue.",
                "Vous savez expliquer la différence entre une discussion avec une IA et un workflow qui se déclenche tout seul.",
                "Quelle tâche revient souvent dans votre journée et mérite une règle claire ?",
                "interface-s3/hero-n8n-map.png",
                link="n8n_docs",
                code=["n8n = trigger + nodes + données + executions", "Objectif = automatiser une suite d’actions vérifiables"],
                tip="Ne commencez pas par chercher le node parfait. Commencez par écrire le geste manuel que vous voulez supprimer.",
            ),
            item(
                "Automatiser sans se perdre",
                "Automatiser ne veut pas dire tout rendre automatique. Une bonne automatisation enlève une action répétitive, pas une décision importante. Si une réponse doit être validée par une personne, n8n peut préparer le message et demander une validation. Ce point est important pour garder un usage sérieux.",
                "Séparez les tâches en trois groupes : ce qui peut se faire seul, ce qui doit être préparé par n8n, et ce qui doit rester validé à la main. Cette séparation évite les workflows trop dangereux.",
                "Chaque étape du futur workflow a un niveau de risque : faible, moyen ou sensible.",
                "Est-ce que cette action peut partir sans relecture, ou doit-elle attendre votre accord ?",
                "interface-s3/security-checklist.png",
                link="n8n_workflow_components",
                code=["Automatique : ajouter une ligne dans une table", "Semi-auto : préparer un email", "Manuel : envoyer une offre commerciale sensible"],
            ),
            item(
                "Le fil rouge business",
                "Toute la séance suit le même exemple. Le Comptoir Bleu reçoit une demande depuis un formulaire : nom, email, date, nombre de personnes et message libre. n8n doit nettoyer la donnée, vérifier les champs importants, préparer une réponse, notifier l’équipe et garder une trace.",
                "Écrivez le scénario en une ligne : `Quand une demande arrive, n8n la vérifie, prépare une réponse, alerte l’équipe et l’enregistre.` Cette phrase devient la boussole de la séance.",
                "Le scénario tient en une seule phrase et il produit un résultat concret.",
                "Si le workflow réussit, quelle trace doit rester visible dans votre outil de suivi ?",
                "interface-s3/workflow-first-build.png",
                link="n8n_workflows",
                code=["Déclencheur : formulaire ou webhook", "Traitement : nettoyer et vérifier", "Sortie : notification + trace + réponse préparée"],
                tip="Un bon fil rouge doit parler d’un vrai usage quotidien, pas d’une démo abstraite.",
            ),
            item(
                "Workflow, node, trigger",
                "Un workflow est le scénario complet. Un node est une étape du scénario. Un trigger est le node qui démarre tout. Si ces trois mots sont clairs, l’interface devient beaucoup plus facile à lire.",
                "Dans le fil rouge, le workflow s’appelle `Lead - réception et réponse`. Le trigger reçoit la demande. Les nodes suivants nettoient, vérifient, appellent l’IA, notifient et enregistrent.",
                "Vous pouvez pointer chaque étape et dire si c’est un trigger, un node de logique, un node d’action ou un node IA.",
                "Où commence le workflow, et quelle est la première donnée reçue ?",
                "interface-s3/node-anatomy.png",
                link="n8n_workflow_components",
                code=["Workflow = histoire complète", "Trigger = départ", "Node = étape", "Execution = preuve du passage"],
            ),
            item(
                "La donnée circule en JSON",
                "n8n transporte des données sous forme d’objets. Ce n’est pas juste du texte sur un écran. Un node reçoit des champs, les modifie, puis transmet une sortie. Comprendre ça évite de chercher une erreur au mauvais endroit.",
                "Quand un node se termine, ouvrez sa sortie et repérez les noms exacts des champs : `name`, `email`, `message`, `date`. Le node suivant doit utiliser ces noms exacts.",
                "Vous savez retrouver un champ dans la sortie d’un node au lieu de l’inventer.",
                "Quel champ précis le node suivant doit-il lire ?",
                "interface-s3/data-flow-json.png",
                link="n8n_workflow_components",
                code=['{{ $json.email }}', '{{ $json.message }}', "{{ $json.date }}"],
                tip="Si un champ est vide, ne corrigez pas le node final. Remontez au premier node où le champ disparaît.",
            ),
            item(
                "Cloud ou self-hosted",
                "n8n peut être utilisé en cloud ou hébergé soi-même. Le cloud simplifie le démarrage, les mises à jour et l’accès public aux webhooks. Le self-hosted donne plus de contrôle, mais demande plus de responsabilité technique : serveur, variables, sauvegardes, sécurité et mise à jour.",
                "Pour une première séance, partez sur l’idée simple : n8n Cloud pour apprendre vite, self-hosted quand l’équipe sait gérer l’infrastructure. Le choix technique ne doit pas bloquer la compréhension du workflow.",
                "Vous savez pourquoi un webhook cloud est plus simple à tester qu’un n8n local non exposé à Internet.",
                "Est-ce que vous voulez apprendre l’outil ou gérer un serveur dès maintenant ?",
                "n8n-overview.png",
                link="n8n_docs",
                code=["Cloud = plus simple pour démarrer", "Self-hosted = plus de contrôle, plus d’entretien"],
            ),
            item(
                "Ce que n8n ne décide pas",
                "n8n applique des règles. Il ne connaît pas votre vraie priorité business si vous ne l’écrivez pas. Il ne sait pas non plus si une donnée est sensible, si un client doit être appelé avant un email, ou si un message doit attendre une validation.",
                "Avant de construire, écrivez les limites : pas d’envoi automatique au client au début, pas de suppression de données, pas d’activation sans test, pas de clé API dans le JSON.",
                "Les limites sont visibles dans le workflow ou dans une note de documentation.",
                "Quelle action pourrait créer un problème si elle partait trop vite ?",
                "interface-s3/security-checklist.png",
                link="n8n_workflows",
                code=["Limite 1 : ne pas envoyer au client sans validation", "Limite 2 : ne pas activer avant test complet", "Limite 3 : ne jamais exposer les secrets"],
            ),
            item(
                "API, node et MCP",
                "Trois mots reviennent souvent. Un node est une brique n8n prête à configurer. Une API est une porte HTTP pour parler à un service. MCP est un protocole qui permet à un agent comme Claude Code ou Codex d’utiliser des outils de manière structurée.",
                "Gardez cette règle : node quand l’intégration existe, HTTP Request quand il faut appeler une API, MCP quand un agent doit découvrir et utiliser des outils.",
                "Vous savez choisir entre node prêt à l’emploi, HTTP Request et MCP sans mélanger les rôles.",
                "Est-ce que je connecte deux applications, ou est-ce que je donne un outil à un agent ?",
                "interface-s3/mcp-two-directions.png",
                link="n8n_mcp_instance",
                code=["Node = brique n8n", "API = appel HTTP", "MCP = outil exposé à un agent"],
            ),
            item(
                "La place de Claude Code et Codex",
                "Claude Code et Codex ne sont pas des nodes n8n classiques. On ne les met pas dans le canvas comme un simple bouton. Ils peuvent aider de deux façons : écrire ou relire un workflow JSON via l’API n8n, ou appeler des outils n8n exposés en MCP.",
                "Retenez la phrase : `Claude Code et Codex ne tournent pas dans n8n, ils travaillent autour de n8n.` Ils peuvent créer, modifier, relire ou déclencher des workflows si les accès sont bien cadrés.",
                "Vous savez expliquer pourquoi `connecter Codex à n8n` peut vouloir dire API ou MCP selon le besoin.",
                "Est-ce que l’agent doit créer le workflow, ou seulement utiliser un workflow déjà prêt ?",
                "interface-s3/mcp-two-directions.png",
                link="codex_mcp",
                code=["Créer un workflow = API n8n ou import JSON", "Utiliser un workflow = MCP n8n exposé comme outil"],
            ),
            item(
                "La carte de la séance",
                "La suite avance dans un ordre volontaire : comprendre, lire l’interface, construire un workflow, apprendre les nodes, ajouter l’IA, connecter MCP, connecter l’API, puis passer en routine de production. Cet ordre évite de commencer par les options les plus abstraites.",
                "Gardez la carte sous les yeux. Quand une notion devient floue, revenez au fil rouge : une demande arrive, n8n la transforme, l’équipe reçoit une alerte et la trace reste consultable.",
                "Vous savez pourquoi chaque partie arrive avant la suivante.",
                "Quelle est la prochaine action visible, pas seulement la prochaine idée ?",
                "interface-s3/final-checklist.png",
                link="n8n_docs",
                code=["1. Comprendre", "2. Construire", "3. Connecter", "4. Tester", "5. Activer"],
            ),
        ],
    ),
    (
        "Acte 2 - Lire l’interface n8n",
        "On apprend à se repérer avant de construire. Le but est de savoir où cliquer, où vérifier et où revenir quand quelque chose casse.",
        "Interface",
        "violet",
        [
            item("Le tableau de bord", "Le tableau de bord liste les workflows, leurs noms, leur état et parfois leur dossier ou projet. C’est là que l’on revient pour rouvrir, dupliquer ou contrôler une automatisation.", "Repérez le workflow de test et donnez-lui un nom lisible. Évitez `test 1`, `nouveau workflow`, `copie finale vraie finale`.", "Le nom explique le déclencheur et le résultat.", "Quel nom serait compris par quelqu’un qui ouvre n8n demain ?", "n8n-overview.png", link="n8n_workflows", code=["Lead - réception formulaire - notification interne"]),
            item("L’éditeur visuel", "L’éditeur est le canvas. Les nodes se placent à gauche, à droite, ou en branches. Les lignes montrent comment les données circulent. Une page propre rend le debug beaucoup plus simple.", "Placez les nodes dans le sens de lecture : arrivée, nettoyage, condition, IA, notification, trace. Ajoutez de l’espace entre les grandes étapes.", "Le parcours se lit sans zoomer ni deviner.", "Est-ce qu’une personne peut suivre le flux avec les yeux ?", "n8n-editor.png", link="n8n_workflow_components"),
            item("Le panneau des nodes", "Le panneau des nodes sert à chercher une brique. Il contient des triggers, des actions, des nodes core, des nodes IA et parfois des intégrations installées. Il ne faut pas choisir le premier résultat sans lire son rôle.", "Cherchez `Webhook`, `Edit Fields`, `IF`, `HTTP Request`, `AI Agent`. Pour chaque node, notez s’il démarre, transforme, décide ou agit.", "Vous savez ranger un node dans une famille simple.", "Est-ce que ce node déclenche, transforme, décide ou envoie ?", "n8n-nodes.png", link="n8n_node_types", code=["Trigger", "Core", "App", "AI", "Tool"]),
            item("La fenêtre d’un node", "Quand un node est ouvert, n8n montre ses paramètres. C’est souvent ici que l’erreur se cache : mauvaise méthode HTTP, mauvais champ, mauvais credential, mauvais format de sortie.", "Ouvrez un node et lisez les paramètres avant de les modifier. Notez la méthode, l’URL, le credential, les champs d’entrée et la sortie attendue.", "Vous pouvez expliquer ce que le node doit recevoir et produire.", "Quel est le contrat de ce node : entrée, action, sortie ?", "interface-s3/node-anatomy.png", link="n8n_workflow_components"),
            item("Les credentials", "Les credentials gardent les accès aux services : API key, OAuth, token, compte Gmail, Slack, Notion. Un workflow sérieux ne colle pas les secrets dans un champ texte visible.", "Créez les credentials dans n8n, puis sélectionnez-les dans le node. Pour un support public ou un dépôt Git, ne montrez jamais la valeur d’une clé.", "La clé n’apparaît ni dans le HTML, ni dans le JSON partagé, ni dans une capture.", "Si cette capture part sur GitHub, est-ce qu’un secret fuit ?", "interface-s3/credentials-safe.png", link="n8n_api_auth"),
            item("Les executions", "Une execution est la preuve qu’un workflow a tourné. Elle montre chaque node, les données d’entrée, les sorties et les erreurs. Pour apprendre n8n, c’est plus important que le canvas joli.", "Après chaque test, ouvrez l’execution. Repérez le premier node rouge, pas le dernier effet visible. L’erreur se corrige là où elle apparaît d’abord.", "Vous savez retrouver la cause d’un échec en partant de l’execution.", "Quel node a cassé en premier ?", "n8n-executions.png", link="n8n_workflows", code=["Erreur 401 = souvent credential/header", "Erreur 404 = souvent URL", "Erreur champ vide = souvent mapping"]),
            item("Activer un workflow", "Un workflow actif peut tourner sans vous. C’est pratique, mais cela demande plus de contrôle. Une automatisation non testée peut envoyer des messages, créer des lignes ou appeler des APIs avec de mauvaises données.", "Gardez le workflow inactif pendant la construction. Activez seulement quand un test complet passe avec une donnée réaliste.", "L’activation arrive après une execution réussie, pas avant.", "Est-ce que je serais à l’aise si ce workflow tournait demain matin sans moi ?", "n8n-trigger.png", link="n8n_workflows"),
            item("Manual Trigger pour apprendre", "Le Manual Trigger est idéal pour apprendre. Il permet de lancer un workflow à la demande, sans attendre un vrai formulaire ou un vrai événement. Cela évite de mélanger apprentissage et production.", "Ajoutez un Manual Trigger dans les workflows de test. Injectez une donnée simple dans un Set/Edit Fields pour simuler une demande client.", "Le workflow peut se tester sans vraie donnée externe.", "Est-ce que je peux reproduire le test en deux clics ?", "interface-s3/trigger-map.png", link="n8n_node_types", code=["Manual Trigger", "Edit Fields", "Test workflow"]),
            item("Notes et organisation", "Les notes sur le canvas ne sont pas décoratives. Elles expliquent pourquoi une branche existe, ce qui est volontairement bloqué, et ce qu’il faut vérifier avant activation. Une bonne note évite une confusion plus tard.", "Ajoutez une note courte au début du workflow : objectif, source, sortie, limites. Une phrase suffit.", "Le workflow raconte son but sans ouvrir la vidéo ou la conversation.", "Quelle information sera oubliée dans une semaine si elle n’est pas écrite ?", "interface-s3/production-routine.png", link="n8n_workflows"),
            item("Premier tour d’interface", "Avant de construire le vrai flux, faites un tour simple : dashboard, canvas, panneau nodes, credentials, execution, activation. Ce tour crée des repères. Sans repère, chaque erreur ressemble à un gros problème.", "Ouvrez chaque zone une fois. Le but n’est pas de tout paramétrer. Le but est de savoir où revenir quand le workflow se bloque.", "Vous savez où créer, tester, lire l’erreur, gérer les secrets et activer.", "Si un node échoue, où allez-vous regarder en premier ?", "n8n-ai-agent-config.png", link="n8n_workflow_components"),
        ],
    ),
    (
        "Acte 3 - Construire le premier workflow",
        "On construit le fil rouge étape par étape. Chaque section ajoute une brique utile, sans sauter directement vers l’IA ou MCP.",
        "Workflow",
        "cyan",
        [
            item("Le formulaire de départ", "Le workflow commence avec une demande client. Le plus simple est d’imaginer un formulaire : nom, email, date, nombre de personnes, message. Cette donnée représente le vrai travail à automatiser.", "Créez une donnée de test avec ces champs. Si vous utilisez un vrai formulaire, commencez avec une version test.", "La donnée contient assez d’informations pour traiter le besoin.", "Quelles informations sont obligatoires pour répondre correctement ?", "interface-s3/workflow-first-build.png", link="n8n_workflows", code=['{"name":"Camille","email":"camille@example.com","date":"vendredi","people":6}']),
            item("Webhook pour recevoir", "Le Webhook permet à un service externe d’envoyer une donnée à n8n. Il est utile pour formulaires, landing pages, CRM, outils no-code ou scripts. Le webhook est une porte d’entrée.", "Ajoutez un Webhook Trigger et copiez son URL de test. Envoyez une donnée simple avant de brancher un vrai outil.", "L’execution montre que n8n reçoit bien le payload.", "Est-ce que la donnée arrive vraiment, ou est-ce que je regarde seulement l’URL ?", "n8n-trigger.png", link="n8n_workflow_components", code=["POST https://votre-n8n/webhook-test/lead-comptoir-bleu"]),
            item("Nettoyer avec Edit Fields", "Une demande brute contient souvent trop de champs. Edit Fields permet de garder seulement ce qui sert. C’est une étape simple mais très importante : un workflow propre commence avec une donnée propre.", "Gardez `name`, `email`, `date`, `people`, `message`, `source`. Renommez les champs si les noms sont trop techniques.", "La sortie du node est plus courte et lisible.", "Quels champs sont vraiment utiles pour la suite ?", "interface-s3/data-flow-json.png", link="n8n_workflow_components", code=["name", "email", "date", "people", "message", "source"]),
            item("Vérifier les informations avec IF", "Le node IF sépare les cas. Exemple : si l’email est présent, on prépare une réponse. Si l’email manque, on alerte l’équipe pour compléter. Cette logique évite d’envoyer une mauvaise réponse.", "Ajoutez une condition : email existe et date existe. Branche vraie : suite normale. Branche fausse : notification interne.", "Une donnée complète prend la bonne branche, une donnée incomplète prend l’autre.", "Quelle information bloque vraiment la suite ?", "interface-s3/if-switch-logic.png", link="n8n_node_types"),
            item("Préparer une réponse simple", "Avant d’envoyer quoi que ce soit, préparez un message. L’IA peut aider, mais elle doit recevoir un contexte clair : style simple, pas de promesse inventée, demande de confirmation, message court.", "Ajoutez un node IA ou un bloc de texte qui génère un brouillon. Au début, gardez l’envoi manuel ou interne.", "Le message préparé est lisible et ne promet rien qui n’existe pas.", "Est-ce que ce message peut être relu par une personne avant envoi ?", "n8n-ai-agent.jpg", link="n8n_ai_agent", code=["Rédige une réponse courte.", "Ne confirme pas la réservation.", "Demande les informations manquantes si besoin."]),
            item("Notifier l’équipe", "Une notification sert à ne pas perdre la demande. Slack, email ou Notion peuvent faire l’affaire. Le choix dépend de l’outil que l’équipe ouvre vraiment. Une notification dans un outil jamais consulté ne sert à rien.", "Choisissez un seul canal pour le test. Envoyez nom, besoin, date, lien vers l’execution et brouillon de réponse.", "La notification donne assez d’informations pour agir sans rouvrir tout n8n.", "Où l’équipe regarde-t-elle vraiment ses demandes ?", "interface-s3/workflow-first-build.png", link="n8n_node_types"),
            item("Garder une trace", "La trace évite de perdre l’historique. Elle peut aller dans Notion, Google Sheets, Airtable, CRM ou une base n8n. La trace sert aussi à vérifier que le workflow a bien fait son travail.", "Ajoutez une étape qui enregistre une ligne : date de réception, nom, email, besoin, statut, lien execution.", "Chaque demande test crée une trace unique.", "Si le client rappelle demain, où retrouverez-vous la demande ?", "interface-s3/production-routine.png", link="n8n_workflows", code=["status = nouveau", "source = formulaire", "execution_url = ..."]),
            item("Tester avec deux cas", "Un seul test ne suffit pas. Il faut tester au moins deux cas : demande complète et demande incomplète. Sinon, vous ne savez pas si la branche IF fonctionne.", "Lancez un test complet avec email et date, puis un test sans email. Notez la branche prise par chaque execution.", "Les deux branches passent exactement comme prévu.", "Est-ce que le workflow sait gérer le cas imparfait ?", "interface-s3/executions-debug.png", link="n8n_workflows"),
            item("Faire une première version lisible", "La première version ne doit pas être parfaite. Elle doit être lisible, testable et facile à corriger. Une automatisation trop ambitieuse dès le départ devient dure à débugger.", "Limitez la version 1 à cinq étapes : recevoir, nettoyer, vérifier, notifier, tracer. L’IA peut rester en brouillon au début.", "La version 1 fonctionne sans action risquée.", "Est-ce que ce workflow tient encore dans votre tête ?", "interface-s3/workflow-first-build.png", link="n8n_workflows"),
            item("Résumé du workflow 1", "À ce stade, le fil rouge existe. Il ne fait pas encore tout, mais il montre la logique : un événement arrive, la donnée est propre, une règle décide, une notification part et une trace reste.", "Écrivez un résumé en cinq lignes dans une note du workflow. Ce résumé devient votre documentation de départ.", "Quelqu’un peut comprendre le workflow sans vous demander une explication orale.", "Quelle phrase résume le résultat obtenu ?", "interface-s3/final-checklist.png", link="n8n_workflows"),
        ],
    ),
    (
        "Acte 4 - Comprendre les nodes essentiels",
        "On garde le même fil rouge, mais on élargit la boîte à outils. Le but est de savoir quel node choisir selon le problème.",
        "Nodes",
        "green",
        [
            item("Trigger nodes", "Les triggers démarrent un workflow. Sans trigger, rien ne part. Manual, Webhook, Schedule, Form et App Trigger ne répondent pas au même besoin.", "Choisissez le trigger selon l’événement réel : clic manuel, donnée entrante, heure fixe, formulaire ou événement d’une app.", "Le trigger correspond au moment réel où le workflow doit démarrer.", "Quand ce workflow doit-il commencer exactement ?", "interface-s3/trigger-map.png", link="n8n_node_types"),
            item("Action nodes", "Les action nodes font quelque chose dans un outil : envoyer un email, créer une page, poster sur Slack, ajouter une ligne, mettre à jour un CRM. C’est souvent la partie visible du workflow.", "Ajoutez une action seulement quand la donnée est propre. Une action trop tôt propage les erreurs.", "L’action produit un résultat visible dans l’outil cible.", "Quel résultat externe doit exister après ce node ?", "n8n-nodes.png", link="n8n_node_types"),
            item("Core nodes", "Les core nodes manipulent la logique interne : IF, Switch, Merge, Code, Set/Edit Fields, Wait, Split, Loop. Ils rendent le workflow fiable avant les actions externes.", "Utilisez un core node pour préparer la donnée avant d’appeler un outil. Cela rend l’erreur plus facile à lire.", "La donnée sort du core node dans le format attendu.", "Est-ce que la donnée est prête avant de sortir de n8n ?", "interface-s3/node-anatomy.png", link="n8n_node_types"),
            item("HTTP Request", "HTTP Request est le node universel pour appeler une API. Il est utile quand n8n n’a pas de node dédié ou quand l’intégration officielle ne couvre pas votre cas.", "Paramétrez méthode, URL, headers, body et authentication. Testez la réponse avec peu de données.", "Le status code, le body et les erreurs sont compris.", "Est-ce que je connais la méthode, l’URL et le header attendu ?", "interface-s3/http-request-api.png", link="n8n_http_request", code=["GET = lire", "POST = créer", "PUT/PATCH = modifier", "DELETE = supprimer avec prudence"]),
            item("Code node", "Le Code node permet d’écrire du JavaScript quand les nodes visuels ne suffisent pas. Il est utile, mais il peut rendre le workflow plus difficile à maintenir si on l’utilise trop vite.", "Utilisez Code pour une transformation précise : nettoyer un texte, convertir une date, créer un champ calculé. Évitez de cacher toute la logique dans du code.", "Le code est court et son résultat est visible dans la sortie.", "Est-ce que cette logique mérite du code, ou un node visuel suffit ?", "interface-s3/data-flow-json.png", link="n8n_node_types", code=["return items.map(item => ({ json: { ...item.json, source: 'formulaire' } }));"]),
            item("IF et Switch", "IF décide entre deux branches. Switch choisit entre plusieurs routes. Ils sont utiles pour séparer les demandes urgentes, incomplètes, commerciales ou techniques.", "Dans le fil rouge, ajoutez un Switch sur le type de demande si le message contient réservation, événement, recrutement ou autre.", "Chaque route reçoit seulement les demandes qui la concernent.", "Combien de chemins réels existe-t-il dans ce processus ?", "interface-s3/if-switch-logic.png", link="n8n_node_types"),
            item("Merge", "Merge sert à réunir deux branches ou deux sources de données. Par exemple : demande du formulaire + fiche client du CRM. Sans Merge, les informations restent séparées.", "Utilisez Merge quand deux chemins doivent redevenir un seul flux. Nommez clairement ce que chaque branche apporte.", "La sortie contient les informations des deux côtés.", "Quelles deux sources doivent se rejoindre ?", "interface-s3/merge-wait-loop.png", link="n8n_node_types"),
            item("Wait et Loop", "Wait permet d’attendre. Loop traite une liste étape par étape. Ces nodes sont utiles pour relances, lots, listes de clients ou temporisations. Ils doivent être contrôlés pour éviter les boucles trop longues.", "Ajoutez Wait pour une relance test ou Loop pour traiter plusieurs lignes. Fixez une limite claire.", "Le workflow ne boucle pas sans fin et ne spamme pas les outils externes.", "Quelle limite protège ce workflow ?", "interface-s3/merge-wait-loop.png", link="n8n_node_types"),
            item("Error Trigger", "Un workflow peut échouer. Error Trigger démarre un flux de gestion d’erreur. C’est une vraie pratique de production : l’erreur devient visible au lieu de rester cachée.", "Créez un workflow d’erreur qui notifie le nom du workflow, le node fautif, le message et le lien d’execution.", "Une erreur volontaire déclenche une alerte utile.", "Qui doit être prévenu quand le workflow casse ?", "interface-s3/error-workflow.png", link="n8n_workflows"),
            item("Sous-workflows", "Un sous-workflow évite de répéter la même logique partout. Par exemple, formater une notification ou vérifier une adresse email peut devenir une brique réutilisable.", "Attendez d’avoir répété une logique deux ou trois fois avant de la sortir en sous-workflow. Ne créez pas une abstraction trop tôt.", "Le sous-workflow a une entrée claire et une sortie claire.", "Est-ce une vraie répétition ou juste une idée de rangement ?", "interface-s3/production-routine.png", link="n8n_workflows"),
        ],
    ),
    (
        "Acte 5 - Ajouter l’IA dans n8n",
        "L’IA arrive après les bases. Elle sert à préparer, classer, résumer ou décider un chemin, mais elle doit rester cadrée.",
        "IA",
        "violet",
        [
            item("OpenAI et Anthropic dans n8n", "n8n peut appeler des modèles via des nodes IA ou HTTP Request. C’est différent de Codex ou Claude Code. Ici, n8n parle à une API de modèle pour produire un texte, classer une demande ou extraire une information.", "Utilisez un credential dédié pour OpenAI ou Anthropic. Le prompt doit être court, précis, et relié aux champs du workflow.", "La réponse du modèle est utilisée comme une donnée, pas comme une vérité automatique.", "Est-ce que l’IA produit une aide ou une action finale ?", "n8n-ai-agent-config.png", link="n8n_ai_agent"),
            item("AI Agent node", "L’AI Agent node peut raisonner et utiliser des outils. Il ne sert pas seulement à générer du texte. Il peut choisir un outil, appeler une API, récupérer une information et produire une sortie.", "Ajoutez un AI Agent seulement si une simple génération de texte ne suffit pas. Donnez-lui un objectif et des outils limités.", "L’agent sait quels outils il peut utiliser et pourquoi.", "Est-ce qu’un agent est nécessaire, ou un simple node de modèle suffit ?", "interface-s3/ai-agent-tools.png", link="n8n_ai_agent"),
            item("Tools d’un agent", "Un agent sans outil parle. Un agent avec outils agit. Dans n8n, les tools peuvent être des requêtes, des workflows, des services ou un MCP Client Tool. Plus les outils sont larges, plus le risque monte.", "Donnez à l’agent un petit nombre d’outils. Chaque outil doit avoir un nom clair et une description simple.", "L’agent n’a pas accès à des actions hors sujet.", "Quel outil exact l’agent doit-il avoir pour faire son travail ?", "interface-s3/ai-agent-tools.png", link="n8n_ai_agent"),
            item("Prompt court et utile", "Un prompt n8n doit guider une tâche précise. Un prompt trop long peut mélanger les priorités. Un prompt trop vague produit une réponse difficile à vérifier.", "Dans le fil rouge, demandez : `Classe la demande en réservation, événement, question ou autre. Réponds seulement avec un JSON.`", "La sortie est courte et facile à utiliser par le node suivant.", "Est-ce que la sortie peut être lue par un workflow, pas seulement par une personne ?", "n8n-ai-agent.jpg", link="n8n_ai_agent", code=['{"type":"reservation","priority":"normal","missing":["phone"]}']),
            item("Sortie structurée", "La sortie structurée évite les textes imprévisibles. Un JSON propre permet à IF, Switch ou HTTP Request d’utiliser la réponse. C’est souvent la différence entre une démo jolie et un workflow fiable.", "Demandez un format JSON simple avec trois champs maximum au début. Validez que le JSON se parse correctement.", "Le node suivant peut lire la réponse sans interprétation humaine.", "Quels champs exacts doivent sortir de l’IA ?", "interface-s3/workflow-json-structure.png", link="n8n_ai_agent"),
            item("Validation humaine", "Une IA peut préparer une réponse sans l’envoyer. Cette étape respecte le niveau débutant et le niveau production. On garde le contrôle tant que le workflow n’a pas fait ses preuves.", "Envoyez le brouillon en interne avec un lien d’execution. Le message final part seulement après validation humaine.", "Aucun client ne reçoit un texte non relu pendant les premiers tests.", "À quel moment une personne doit-elle reprendre la main ?", "interface-s3/security-checklist.png", link="n8n_workflows"),
            item("Permissions des tools", "Un outil donné à un agent doit être limité. Si l’agent peut lire, écrire, supprimer et activer partout, l’automatisation devient trop risquée. Le bon design donne juste l’outil nécessaire.", "Créez des outils séparés : `lire_lead`, `créer_note`, `préparer_email`. Évitez un outil vague appelé `faire_action`.", "Chaque outil dit clairement ce qu’il peut faire.", "Est-ce que ce nom d’outil cache une action trop large ?", "interface-s3/ai-agent-tools.png", link="n8n_mcp_client"),
            item("L’IA vérifie la donnée", "L’IA peut aider à repérer un message incomplet ou une intention. Mais la règle finale doit rester testable. Par exemple, vérifier qu’un email existe ne demande pas d’IA. Comprendre un message libre peut demander l’IA.", "Utilisez des règles simples avant l’IA, puis l’IA seulement pour le texte libre.", "Les vérifications simples ne coûtent pas d’appel modèle inutile.", "Est-ce une règle mécanique ou une compréhension de texte ?", "interface-s3/if-switch-logic.png", link="n8n_ai_agent"),
            item("Éviter l’invention", "Une IA peut inventer un horaire, un prix ou une promesse si le prompt la laisse faire. Dans un workflow business, cette erreur peut devenir visible par un client.", "Ajoutez une consigne : ne pas inventer, demander les informations manquantes, utiliser uniquement les champs fournis.", "Le brouillon ne contient pas de donnée absente du formulaire.", "Quelle information l’IA n’a pas le droit d’inventer ?", "n8n-ai-agent-config.png", link="n8n_ai_agent", code=["N’invente pas de disponibilité.", "Ne confirme pas une réservation.", "Demande une validation interne."]),
            item("IA prête pour MCP/API", "Une fois que l’IA est cadrée dans n8n, on peut parler de MCP et d’API. Sinon, connecter Codex ou Claude Code à un workflow mal compris ne fait qu’accélérer la confusion.", "Gardez le workflow simple et testé avant d’ajouter des agents externes. Le MCP ou l’API doit servir un besoin clair.", "Le workflow de base tourne sans MCP ni API complexe.", "Est-ce que j’ajoute une connexion parce qu’elle sert, ou parce qu’elle paraît avancée ?", "interface-s3/mcp-two-directions.png", link="n8n_mcp_instance"),
        ],
    ),
    (
        "Acte 6 - Connecter n8n en MCP",
        "MCP sert à donner des outils aux agents. On distingue clairement n8n serveur MCP et n8n client MCP.",
        "MCP",
        "blue",
        [
            item("MCP en mots simples", "MCP signifie Model Context Protocol. Dans cette séance, retenez simplement : un agent peut découvrir des outils, lire leur description et les appeler proprement. C’est plus cadré que coller une clé API dans une conversation.", "Écrivez la définition : `MCP donne des outils contrôlés à un agent.` Puis notez quel outil n8n doit exposer ou consommer.", "Vous savez dire ce que MCP apporte par rapport à une simple clé API.", "Quel outil voulez-vous donner à l’agent, et avec quelle limite ?", "interface-s3/mcp-two-directions.png", link="n8n_mcp_instance"),
            item("n8n serveur MCP instance", "La documentation n8n explique que l’instance peut exposer des workflows à des clients MCP quand la fonctionnalité est activée. Cela permet à un client comme Claude Code ou Codex d’interagir avec les workflows disponibles.", "Activez seulement ce qui est nécessaire. Côté n8n, rendez les workflows disponibles en MCP avec une description claire.", "Le client MCP voit uniquement des outils utiles et compréhensibles.", "Si le client liste les outils, les noms sont-ils assez clairs ?", "web-captures/n8n-mcp-instance-docs.png", link="n8n_mcp_instance"),
            item("MCP Server Trigger", "Le MCP Server Trigger expose un workflow comme serveur MCP. C’est utile quand vous voulez transformer un workflow n8n en outil appelable par un agent. Le workflow démarre quand l’outil MCP est appelé.", "Créez un workflow dédié, ajoutez MCP Server Trigger, décrivez l’outil, choisissez l’authentification et testez l’URL de test avant la production.", "L’outil apparaît côté client et déclenche une execution côté n8n.", "Qu’est-ce que cet outil a le droit de faire exactement ?", "web-captures/n8n-mcp-trigger-docs.png", link="n8n_mcp_trigger"),
            item("MCP Client Tool", "Le MCP Client Tool fait l’inverse : n8n devient client d’un serveur MCP externe. Un AI Agent dans n8n peut utiliser des outils publiés par ce serveur.", "Dans un AI Agent, ajoutez MCP Client Tool, configurez l’endpoint SSE ou HTTP, l’authentification, puis limitez les outils inclus.", "L’agent appelle un outil externe et la réponse revient dans n8n.", "Est-ce que n8n doit exposer un outil, ou consommer un outil externe ?", "web-captures/n8n-mcp-client-tool-docs.png", link="n8n_mcp_client"),
            item("Claude Code comme client MCP", "Claude Code peut se connecter à des serveurs MCP. Cela permet de lui donner un outil n8n contrôlé au lieu de lui demander d’improviser un accès. Dans cette séance, Claude Code devient client, n8n devient serveur.", "Ajoutez le serveur MCP n8n avec la commande Claude Code adaptée à l’URL et à l’authentification. Vérifiez ensuite la liste des serveurs.", "Claude Code voit le serveur n8n dans `/mcp` ou dans la liste MCP.", "Est-ce que Claude Code appelle un outil limité, ou a-t-il trop de pouvoir ?", "interface-s3/claude-code-mcp-setup.png", link="claude_mcp", code=["claude mcp add --transport http n8n-mcp https://votre-n8n/mcp-server/http", "claude mcp list", "/mcp"]),
            item("Claude Code avec token", "Si l’endpoint n8n demande un token, le token doit être stocké proprement. Évitez de le mettre dans un support, un README public ou une capture. Une commande peut utiliser un header, mais le secret ne doit pas finir dans Git.", "Utilisez une variable d’environnement quand c’est possible. Ne partagez jamais la valeur réelle.", "La commande documentée montre `<TOKEN>` ou une variable, jamais la clé réelle.", "Si ce dépôt devient public, est-ce que le token fuit ?", "web-captures/claude-code-mcp-docs.png", link="claude_mcp", code=['claude mcp add --transport http n8n-mcp https://votre-n8n/mcp-server/http --header "Authorization: Bearer <TOKEN>"']),
            item("Codex comme client MCP", "Codex peut aussi utiliser MCP. La documentation OpenAI indique que Codex peut être configuré avec des serveurs MCP, notamment via la configuration ou la commande Codex MCP. Le principe reste le même : donner un outil précis à l’agent.", "Ajoutez n8n comme serveur MCP dans Codex avec une URL HTTP, ou dans le fichier de configuration. Gardez les secrets hors du dépôt.", "Codex liste le serveur et peut appeler l’outil n8n prévu.", "Quel outil Codex doit-il vraiment appeler ?", "interface-s3/codex-mcp-setup.png", link="codex_mcp", code=["codex mcp add n8n-mcp --url https://votre-n8n/mcp-server/http", "codex mcp list", "/mcp"]),
            item("Codex et config TOML", "La config Codex peut déclarer un serveur MCP. C’est pratique pour garder un réglage stable. Mais un fichier de config partagé ne doit pas contenir de secret réel.", "Déclarez l’URL et utilisez un token via variable ou header sécurisé selon votre cas. Si vous mettez un exemple dans Git, remplacez la valeur par un placeholder.", "Le fichier est lisible et ne contient pas de secret.", "Est-ce un exemple public ou une vraie configuration privée ?", "web-captures/codex-mcp-docs.png", link="codex_mcp", code=["[mcp_servers.n8n-mcp]", 'url = "https://votre-n8n/mcp-server/http"', 'http_headers = { "authorization" = "Bearer <TOKEN>" }']),
            item("Description des outils MCP", "Un outil MCP doit avoir un nom et une description compréhensibles. Si l’agent ne comprend pas l’outil, il peut l’utiliser au mauvais moment. Une bonne description explique l’entrée attendue, l’action et la sortie.", "Décrivez l’outil comme une mini-fiche : `crée une demande interne`, `entrée : nom, email, message`, `sortie : id de la ligne créée`.", "Claude Code ou Codex peut choisir le bon outil sans deviner.", "Le nom de l’outil dit-il ce qu’il fait vraiment ?", "interface-s3/n8n-as-mcp-server.png", link="n8n_mcp_trigger"),
            item("Dépanner MCP", "Les problèmes MCP viennent souvent d’une URL, d’une auth, d’un transport ou d’un outil non exposé. Il faut diagnostiquer dans l’ordre, pas tout changer d’un coup.", "Vérifiez l’URL, le transport, le token, la liste d’outils côté client et les executions côté n8n. Corrigez un élément à la fois.", "Vous savez où le lien casse : client, auth, endpoint ou workflow.", "Est-ce que le client atteint n8n, ou est-ce que n8n refuse l’appel ?", "interface-s3/executions-debug.png", link="n8n_mcp_instance", code=["1. URL", "2. Auth", "3. Transport", "4. Outil exposé", "5. Execution n8n"]),
        ],
    ),
    (
        "Acte 7 - Connecter n8n en API avec Claude Code et Codex",
        "L’API sert quand un agent doit créer, lire ou mettre à jour des workflows n8n de manière contrôlée.",
        "API",
        "orange",
        [
            item("API n8n en mots simples", "L’API n8n permet à un programme de parler à n8n avec des requêtes HTTP. Elle peut lister, créer, mettre à jour ou activer des workflows selon les endpoints. C’est puissant, donc il faut commencer en lecture avant d’écrire.", "Commencez par `GET /api/v1/workflows`. Ne demandez pas tout de suite à un agent de créer ou activer un workflow.", "La réponse API liste les workflows sans rien modifier.", "Est-ce que je suis encore en lecture, ou déjà en écriture ?", "web-captures/n8n-api-reference-docs.png", link="n8n_api_reference", code=["GET /api/v1/workflows", "Header: X-N8N-API-KEY"]),
            item("Créer une clé API", "La clé API donne l’accès à n8n. Elle doit rester dans un gestionnaire de secrets, une variable d’environnement ou un credential. Elle ne doit jamais être collée dans une conversation publique ou un dépôt.", "Dans n8n, créez une clé API, copiez-la une seule fois, puis stockez-la proprement. Pour les exemples, utilisez `<N8N_API_KEY>`.", "Aucune clé réelle n’apparaît dans le support ou dans Git.", "Qui peut utiliser cette clé, et pour quoi faire ?", "web-captures/n8n-api-auth-docs.png", link="n8n_api_auth", code=["export N8N_API_KEY='***'", "export N8N_BASE_URL='https://votre-n8n.app.n8n.cloud'"]),
            item("Lister les workflows", "Lister les workflows est le test le plus sûr. Il vérifie l’URL, la clé et le header sans modifier l’instance. C’est la première commande à faire avant de brancher un agent.", "Lancez une commande `curl` de lecture. Si elle échoue, corrigez l’URL ou la clé avant toute création.", "La commande retourne une liste ou une erreur claire.", "L’agent sait-il lire avant d’écrire ?", "interface-s3/api-create-workflow.png", link="n8n_api_reference", code=["curl -s \"$N8N_BASE_URL/api/v1/workflows\" \\", "  -H \"X-N8N-API-KEY: $N8N_API_KEY\""]),
            item("Créer un workflow", "Créer via API demande un JSON valide. Un agent peut aider à produire ce JSON, mais vous devez le relire. Le JSON doit contenir un nom, des nodes, des connections et des settings cohérents.", "Demandez à Claude Code ou Codex de générer un workflow JSON minimal. Importez-le ou envoyez-le en API seulement après lecture.", "Le workflow créé reste inactif au départ si possible, ou au minimum non connecté à une action sensible.", "Est-ce que ce JSON peut créer un workflow sans envoyer de message réel ?", "interface-s3/workflow-json-structure.png", link="n8n_api_reference", code=["POST /api/v1/workflows", "Body: workflow JSON", "Relire avant envoi"]),
            item("Mettre à jour sans casser", "Mettre à jour un workflow existant est plus risqué que créer une copie. Une bonne méthode consiste à dupliquer, tester, puis remplacer. Cela évite de casser une automatisation active.", "Avant un `PUT`, exportez le workflow actuel ou créez une copie de test. Demandez à l’agent de modifier seulement la copie.", "Le workflow actif n’est pas modifié sans sauvegarde.", "Est-ce que je peux revenir à la version précédente ?", "interface-s3/security-checklist.png", link="n8n_api_reference"),
            item("Activer et désactiver", "L’activation est l’étape qui transforme un test en automatisation réelle. Elle ne doit pas être confiée à un agent sans garde-fou. Une bonne pratique : création et modification par API, activation manuelle après test.", "Gardez l’activation comme étape humaine au début. Quand l’équipe maîtrise, ajoutez une commande d’activation avec validation explicite.", "Une activation a toujours une execution de test juste avant.", "Qu’est-ce qui se passe si ce workflow se déclenche maintenant ?", "interface-s3/api-create-workflow.png", link="n8n_api_reference", code=["POST /api/v1/workflows/{id}/activate", "POST /api/v1/workflows/{id}/deactivate"]),
            item("Claude Code génère le JSON", "Claude Code est utile pour écrire un workflow JSON, créer un script `deploy_n8n_workflow.sh`, relire la structure et vérifier les champs. Il ne doit pas recevoir une clé API en clair dans le prompt.", "Donnez-lui un fichier exemple sans secret et demandez une version minimale du workflow. Le script doit lire `N8N_API_KEY` depuis l’environnement.", "Le résultat contient un JSON lisible et un script qui ne contient aucun secret.", "Est-ce que Claude Code peut travailler avec un exemple sans voir la vraie clé ?", "interface-s3/claude-code-mcp-setup.png", link="claude_mcp", code=["Lis workflow.example.json.", "Génère workflow.lead.json.", "Le script doit utiliser $N8N_API_KEY."]),
            item("Codex génère le JSON", "Codex peut aussi créer ou relire le JSON, écrire un script de déploiement, proposer une checklist et comparer le workflow à la documentation officielle. Le rôle reste le même : produire une base contrôlable.", "Demandez à Codex une version en deux fichiers : `workflow.lead.json` et `README-deploiement.md`. La clé reste une variable.", "Le README explique comment tester sans activer.", "Est-ce que Codex produit une livraison vérifiable, pas seulement du texte ?", "interface-s3/codex-mcp-setup.png", link="codex_cli", code=["codex", "Crée un workflow JSON n8n minimal.", "Ne mets aucun secret dans les fichiers."]),
            item("API ou MCP pour les agents", "API et MCP ne répondent pas au même besoin. API : l’agent crée ou modifie n8n directement via HTTP. MCP : l’agent utilise des outils exposés par n8n. Pour créer des workflows, l’API est souvent directe. Pour utiliser un workflow prêt, MCP est plus propre.", "Choisissez le chemin avant de configurer : création/maintenance = API, appel d’outil = MCP. Si les deux sont nécessaires, gardez deux accès séparés.", "Le choix API/MCP est justifié par le besoin, pas par l’effet de nouveauté.", "L’agent doit-il construire n8n ou appeler n8n ?", "interface-s3/mcp-two-directions.png", link="n8n_mcp_instance"),
            item("Test et rollback", "Un agent peut aller vite. La sécurité vient du rollback. Export JSON, copie de workflow, désactivation facile, test manuel, trace d’execution. Sans ça, une automatisation peut casser silencieusement.", "Avant chaque changement API, exportez ou copiez. Après changement, lancez un test manuel. Si le résultat est mauvais, revenez à la copie.", "Vous pouvez annuler le changement en moins d’une minute.", "Quelle est ma sortie de secours si l’agent se trompe ?", "interface-s3/final-checklist.png", link="n8n_api_reference", code=["1. Exporter", "2. Modifier copie", "3. Tester", "4. Activer", "5. Surveiller"]),
        ],
    ),
    (
        "Acte 8 - Passer en routine de production",
        "La dernière partie transforme la démo en méthode quotidienne. n8n doit rester lisible, testable et maintenable.",
        "Production",
        "green",
        [
            item("Nommage des workflows", "Un bon nom fait gagner du temps. Il doit dire le déclencheur, l’objet et le résultat. Le nom n’est pas un détail : c’est ce que l’équipe verra dans la liste, les erreurs et les exports.", "Utilisez un format simple : `Lead - source - action`. Exemple : `Lead - formulaire site - Slack + CRM`.", "Le nom se comprend sans ouvrir le canvas.", "Quel nom donnera envie de cliquer au bon endroit ?", "interface-s3/production-routine.png", link="n8n_workflows"),
            item("Description et notes", "La description raconte le but, les limites et les contacts. Elle évite de dépendre d’une seule personne. Une note courte dans le workflow peut expliquer une branche spéciale.", "Ajoutez trois lignes : objectif, entrée, sortie. Ajoutez une ligne de limite si une action reste manuelle.", "Le workflow peut être repris sans relire toute la séance.", "Quelle information doit rester dans n8n, pas seulement dans votre tête ?", "interface-s3/production-routine.png", link="n8n_workflows"),
            item("Gestion des secrets", "Les secrets sont souvent la partie la plus fragile : tokens, API keys, OAuth, webhooks privés. Une fuite peut donner accès à des outils réels. Le support et GitHub ne doivent jamais contenir ces valeurs.", "Stockez les secrets dans credentials, variables d’environnement ou gestionnaire de secrets. Remplacez toute valeur dans les exemples par `<TOKEN>`.", "Un `rg` sur les fichiers ne trouve aucune clé réelle.", "Si le repo devient public, qu’est-ce qui fuit ?", "interface-s3/credentials-safe.png", link="n8n_api_auth", code=["rg -n \"sk-|api_key|Bearer|N8N_API_KEY\" ."]),
            item("Workflow d’erreur", "Une erreur non vue peut coûter plus cher que l’absence d’automatisation. Un workflow d’erreur informe rapidement la bonne personne, avec le bon contexte.", "Créez une notification d’erreur avec workflow, node, message, execution URL et priorité. N’envoyez pas un roman.", "Une erreur test déclenche une alerte compréhensible.", "Qui doit savoir que le workflow a cassé ?", "interface-s3/error-workflow.png", link="n8n_workflows"),
            item("Surveiller les executions", "Les executions montrent si le workflow tient dans le temps. Au début, regardez-les souvent. Ensuite, gardez une routine : erreurs, durée, volume, données manquantes.", "Pendant les premiers jours, vérifiez les executions chaque matin. Notez les erreurs répétées et corrigez la cause, pas seulement le symptôme.", "Les erreurs répétées diminuent au fil des corrections.", "Quelle erreur revient assez souvent pour mériter une règle ?", "n8n-executions.png", link="n8n_workflows"),
            item("Limiter le bruit", "Une automatisation qui envoie trop d’alertes sera ignorée. La qualité d’une notification vient de sa précision. Mieux vaut une alerte utile qu’une avalanche de messages.", "Définissez les cas qui méritent une notification : nouvelle demande, erreur, action sensible, résumé quotidien. Le reste peut rester dans les logs.", "Chaque notification appelle une action claire.", "Si cette alerte arrive dix fois par jour, sera-t-elle encore lue ?", "interface-s3/if-switch-logic.png", link="n8n_workflows"),
            item("Exporter et versionner", "Exporter un workflow en JSON permet de garder une sauvegarde. Git peut ensuite suivre les versions. C’est pratique avant une grosse modification par Codex ou Claude Code.", "Exportez le workflow avant une modification importante. Ajoutez-le dans un dossier `workflows/` si le projet est suivi dans Git.", "La version précédente est récupérable.", "Pouvez-vous revenir à la version d’hier ?", "interface-s3/workflow-json-structure.png", link="n8n_api_reference"),
            item("Documenter le passage de relais", "Un bon passage de relais explique comment tester, quoi surveiller, où sont les credentials, et quoi ne pas toucher. C’est court, mais cela rend le workflow utilisable par une autre personne.", "Créez un README de workflow : but, déclencheur, données attendues, outils touchés, test, rollback.", "La documentation tient sur une page et répond aux questions pratiques.", "Que doit savoir la prochaine personne avant de cliquer sur Activer ?", "interface-s3/final-checklist.png", link="n8n_workflows"),
            item("Routine quotidienne", "La routine évite de transformer n8n en usine à gaz. Une tâche répétée devient un workflow seulement si elle est claire, stable, vérifiable et utile. Sinon, elle reste manuelle ou semi-automatique.", "Pour chaque nouvelle idée, posez cinq questions : déclencheur, donnée, décision, action, preuve. Si une réponse manque, ne construisez pas encore.", "Vous savez refuser une automatisation trop floue.", "Quel est le déclencheur, quelle donnée arrive, quelle preuve reste ?", "interface-s3/production-routine.png", link="n8n_workflows", code=["Déclencheur ?", "Donnée ?", "Décision ?", "Action ?", "Preuve ?"]),
            item("Récapitulatif final", "La séance tient en une méthode : comprendre le processus, construire petit, tester chaque node, ajouter l’IA seulement quand elle aide, choisir API ou MCP selon le besoin, puis documenter. Ce parcours suffit pour démarrer proprement avec n8n.", "Reprenez le fil rouge et dites ce que fait chaque étape. Si une étape ne se justifie pas, elle doit être simplifiée ou retirée.", "Vous pouvez créer un premier workflow utile sans partir dans tous les sens.", "Quelle automatisation simple allez-vous tester en premier ?", "interface-s3/final-checklist.png", link="n8n_docs"),
        ],
    ),
]


def e(text: object) -> str:
    return escape(str(text), quote=True)


def flat_sections() -> list[dict[str, object]]:
    sections: list[dict[str, object]] = []
    for chapter_i, (chapter, intro, tag, color, items) in enumerate(CHAPTERS, start=1):
        for item_i, section in enumerate(items, start=1):
            merged = dict(section)
            merged["chapter"] = chapter
            merged["chapter_intro"] = intro
            merged["tag"] = tag
            merged["color"] = color
            merged["chapter_i"] = chapter_i
            merged["item_i"] = item_i
            sections.append(merged)
    return sections


def badge(text: str, color: str) -> str:
    colors = {
        "blue": "bg-blue-600 text-white",
        "violet": "bg-violet-600 text-white",
        "cyan": "bg-cyan-100 text-slate-950",
        "green": "bg-emerald-100 text-slate-950",
        "orange": "bg-orange-100 text-slate-950",
    }
    return f'<span class="{colors[color]} border-2 border-slate-950 px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] shadow-neo-sm">{e(text)}</span>'


def image_src(name: str) -> str:
    if name.startswith("web-captures/"):
        return f"img/{name}"
    if name.startswith("interface-s3/"):
        return f"img/{name}"
    return f"img/{name}"


def code_block(lines: list[str], label: str = "Bloc pratique") -> str:
    if not lines:
        return ""
    return f"""
      <div class="code-panel max-w-full overflow-hidden border-2 border-slate-950 bg-slate-950 text-white shadow-neo">
        <div class="flex items-center justify-between border-b-2 border-white/20 bg-slate-900 px-4 py-2">
          <span class="font-mono text-[11px] font-black uppercase tracking-[.16em] text-cyan-200">{e(label)}</span>
          <button type="button" class="copy-btn border-2 border-white bg-white px-3 py-1 text-xs font-black text-slate-950 transition hover:-translate-y-0.5">Copier</button>
        </div>
        <pre class="max-w-full whitespace-pre-wrap break-words p-5 text-sm leading-7"><code>{e(chr(10).join(lines))}</code></pre>
      </div>
    """


def image_card(section: dict[str, object], index: int) -> str:
    src = image_src(str(section["image"]))
    return f"""
      <figure class="group min-w-0 overflow-hidden border-2 border-slate-950 bg-white shadow-neo">
        <img class="aspect-[16/10] w-full bg-white object-contain transition duration-300 group-hover:scale-[1.015]" src="{src}" alt="{e(section['title'])}" loading="lazy">
        <figcaption class="border-t-2 border-slate-950 bg-white px-4 py-3 text-sm font-semibold leading-6 text-slate-700">
          Visuel {index:02d} · {e(section['tag'])} · {e(section['title'])}
        </figcaption>
      </figure>
    """


def table(section: dict[str, object]) -> str:
    rows = [
        ("Pourquoi", section["why"]),
        ("Action", section["do"]),
        ("Vérification", section["verify"]),
        ("Question", section["question"]),
    ]
    body = ""
    for label, value in rows:
        body += f"""
          <tr>
            <th class="w-[170px] border-2 border-slate-950 bg-blue-50 px-4 py-3 text-left font-mono text-[11px] font-black uppercase tracking-[.14em] text-slate-700">{e(label)}</th>
            <td class="border-2 border-slate-950 bg-white px-4 py-3 text-sm leading-7 text-slate-700">{e(value)}</td>
          </tr>
        """
    return f'<table class="mt-6 w-full border-collapse text-left">{body}</table>'


def section_html(section: dict[str, object], number: int) -> str:
    variant = number % 5
    link = DOCS[str(section["link"])]
    intro = f"""
      <div class="flex flex-wrap items-center gap-3">
        {badge(str(section['tag']), str(section['color']))}
        <span class="border-2 border-slate-950 bg-white px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] shadow-neo-sm">{number:02d}</span>
        <a href="{link}" target="_blank" rel="noreferrer" class="border-2 border-slate-950 bg-white px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] text-blue-700 shadow-neo-sm transition hover:-translate-y-0.5">Source</a>
      </div>
      <h2 class="mt-6 max-w-3xl text-4xl font-black leading-[1.02] tracking-normal text-slate-950 md:text-6xl">{e(section['title'])}</h2>
      <p class="mt-5 text-lg leading-8 text-slate-700">{e(section['why'])}</p>
    """
    action_card = f"""
      <div class="border-2 border-slate-950 bg-violet-50 p-5 shadow-neo">
        <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-violet-700">Ce que vous faites</p>
        <p class="mt-3 leading-8 text-slate-800">{e(section['do'])}</p>
      </div>
    """
    verify_card = f"""
      <div class="border-2 border-slate-950 bg-cyan-50 p-5 shadow-neo-sm">
        <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-cyan-700">Comment vérifier</p>
        <p class="mt-3 leading-8 text-slate-800">{e(section['verify'])}</p>
      </div>
    """
    question_card = f"""
      <div class="border-2 border-slate-950 bg-white p-5 shadow-neo-sm">
        <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-slate-500">Question à se poser</p>
        <p class="mt-3 text-lg font-bold leading-8 text-slate-950">{e(section['question'])}</p>
      </div>
    """
    tip = f"""
      <div class="mt-6 border-2 border-slate-950 bg-blue-600 p-5 text-white shadow-neo">
        <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-blue-100">Tip terrain</p>
        <p class="mt-3 leading-8">{e(section['tip'])}</p>
      </div>
    """
    code = code_block(section["code"], "À copier / adapter")  # type: ignore[arg-type]
    img = image_card(section, number)
    if variant == 1:
        body = f"""
          <div class="grid gap-8 lg:grid-cols-[.95fr_1.05fr] lg:items-start">
            <div>{intro}{action_card}{tip}</div>
            <div>{img}{verify_card}{code}</div>
          </div>
        """
    elif variant == 2:
        body = f"""
          <div class="grid gap-8 lg:grid-cols-[1.05fr_.95fr] lg:items-start">
            <div>{intro}{verify_card}{question_card}{code}</div>
            <div>{img}{tip}</div>
          </div>
        """
    elif variant == 3:
        body = f"""
          <div>{intro}{img}
            <div class="mt-8 grid gap-5 md:grid-cols-3">{action_card}{verify_card}{question_card}</div>
            {tip}{code}
          </div>
        """
    elif variant == 4:
        body = f"""
          <div class="grid gap-8 lg:grid-cols-2 lg:items-start">
            <div>{img}</div>
            <div>{intro}{table(section)}{code}</div>
          </div>
        """
    else:
        body = f"""
          <div>{intro}
            <div class="mt-8 grid gap-6 lg:grid-cols-[.9fr_1.1fr] lg:items-start">
              <div>{action_card}{verify_card}{question_card}</div>
              <div>{img}{code}{tip}</div>
            </div>
          </div>
        """
    return f"""
    <section id="section-{number:02d}" class="section-block reveal mx-auto max-w-7xl bg-white px-4 py-14 sm:px-6 lg:px-8">
      {body}
    </section>
    """


def chapter_nav(sections: list[dict[str, object]]) -> str:
    cards = ""
    for i, (chapter, intro, tag, color, _) in enumerate(CHAPTERS, start=1):
        start = (i - 1) * 10 + 1
        end = i * 10
        cards += f"""
          <a href="#section-{start:02d}" class="group border-2 border-slate-950 bg-white p-5 shadow-neo transition hover:-translate-y-1 hover:bg-blue-50">
            <div class="flex items-center justify-between gap-4">
              {badge(tag, color)}
              <span class="font-mono text-xs font-black text-slate-500">{start:02d}-{end:02d}</span>
            </div>
            <h3 class="mt-5 text-2xl font-black leading-tight text-slate-950">{e(chapter.replace(' - ', ' · '))}</h3>
            <p class="mt-3 text-sm leading-7 text-slate-600">{e(intro)}</p>
          </a>
        """
    return f"""
      <section class="mx-auto max-w-7xl bg-white px-4 py-12 sm:px-6 lg:px-8">
        <div class="grid gap-5 md:grid-cols-2 xl:grid-cols-4">{cards}</div>
      </section>
    """


def sources_table() -> str:
    rows = [
        ("n8n Docs", DOCS["n8n_docs"], "Base officielle pour workflows, nodes et interface."),
        ("Workflow components", DOCS["n8n_workflow_components"], "Définitions workflow, nodes, triggers et executions."),
        ("Node types", DOCS["n8n_node_types"], "Familles de nodes n8n."),
        ("HTTP Request", DOCS["n8n_http_request"], "Appels API depuis un workflow."),
        ("n8n API", DOCS["n8n_api_reference"], "Endpoints pour workflows et automatisation externe."),
        ("API authentication", DOCS["n8n_api_auth"], "Clés API et accès."),
        ("n8n MCP", DOCS["n8n_mcp_instance"], "Accès MCP côté instance."),
        ("MCP Server Trigger", DOCS["n8n_mcp_trigger"], "Exposer un workflow comme serveur MCP."),
        ("MCP Client Tool", DOCS["n8n_mcp_client"], "Utiliser un serveur MCP depuis n8n."),
        ("AI Agent", DOCS["n8n_ai_agent"], "Agent IA et outils dans n8n."),
        ("Codex MCP", DOCS["codex_mcp"], "Configuration MCP côté Codex."),
        ("Claude Code MCP", DOCS["claude_mcp"], "Configuration MCP côté Claude Code."),
    ]
    body = ""
    for name, url, desc in rows:
        body += f"""
          <tr>
            <td class="border-2 border-slate-950 bg-white px-4 py-3 font-bold">{e(name)}</td>
            <td class="border-2 border-slate-950 bg-white px-4 py-3"><a class="font-semibold text-blue-700 underline decoration-2 underline-offset-4" href="{url}" target="_blank" rel="noreferrer">{e(url)}</a></td>
            <td class="border-2 border-slate-950 bg-white px-4 py-3 text-slate-700">{e(desc)}</td>
          </tr>
        """
    return f"""
      <section class="mx-auto max-w-7xl bg-white px-4 py-16 sm:px-6 lg:px-8">
        <div class="border-2 border-slate-950 bg-white p-6 shadow-neo">
          <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-violet-700">Sources vérifiées le 3 juin 2026</p>
          <h2 class="mt-4 text-4xl font-black text-slate-950">Liens officiels à garder</h2>
          <div class="mt-6 overflow-x-auto">
            <table class="min-w-[850px] border-collapse text-sm">{body}</table>
          </div>
        </div>
      </section>
    """


def render() -> str:
    sections = flat_sections()
    section_markup = "\n".join(section_html(section, i) for i, section in enumerate(sections, start=1))
    nav = chapter_nav(sections)
    return f"""<!doctype html>
<html lang="fr" class="scroll-smooth">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Denem Academy · Séance 3 · n8n</title>
    <meta name="description" content="Support technique séance 3 : n8n, workflows, nodes, automatisations, API, MCP, Claude Code et Codex.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@600;700;800&display=swap" rel="stylesheet">
    <link rel="icon" href="logo-denem.jpeg">
    <link rel="stylesheet" href="assets/tailwind-s3.css">
    <style>
      :root {{ color-scheme: light; }}
      * {{ box-sizing: border-box; }}
      body {{ margin: 0; background: #fff; color: #0f172a; font-family: Inter, system-ui, sans-serif; letter-spacing: 0; }}
      .reveal {{ opacity: 0; transform: translateY(20px); transition: opacity .6s ease, transform .6s ease; }}
      .reveal.in-view {{ opacity: 1; transform: translateY(0); }}
      .shadow-neo {{ box-shadow: 8px 8px 0 #0f172a; }}
      .shadow-neo-sm {{ box-shadow: 4px 4px 0 #0f172a; }}
      .progress {{ transform-origin: left; transform: scaleX(0); }}
      .code-panel pre {{ overflow-x: auto; }}
      .section-block:nth-child(odd) {{ background-image: linear-gradient(90deg, rgba(37,99,235,.045) 0 1px, transparent 1px), linear-gradient(rgba(124,58,237,.035) 0 1px, transparent 1px); background-size: 34px 34px; }}
      .section-block img {{ max-width: 100%; }}
      @media (prefers-reduced-motion: reduce) {{ .reveal {{ opacity: 1; transform: none; transition: none; }} * {{ scroll-behavior: auto !important; }} }}
    </style>
  </head>
  <body class="bg-white">
    <div class="progress fixed left-0 top-0 z-[70] h-1 w-full bg-gradient-to-r from-blue-600 via-violet-600 to-cyan-500" id="progress"></div>
    <nav class="sticky top-0 z-50 border-b-2 border-slate-950 bg-white/95 backdrop-blur">
      <div class="mx-auto flex max-w-7xl items-center justify-between gap-4 px-4 py-3 sm:px-6 lg:px-8">
        <a href="#" class="flex items-center gap-3">
          <img src="logo-denem.jpeg" alt="DENEM Academy" class="h-9 w-9 border-2 border-slate-950 object-cover shadow-neo-sm">
          <span class="text-sm font-black uppercase tracking-[.18em] text-slate-950">DENEM Academy</span>
        </a>
        <div class="hidden items-center gap-2 md:flex">
          <a class="border-2 border-slate-950 bg-blue-600 px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] text-white shadow-neo-sm" href="#section-01">Départ</a>
          <a class="border-2 border-slate-950 bg-white px-3 py-1 font-mono text-xs font-black uppercase tracking-[.14em] text-slate-950 shadow-neo-sm" href="#sources">Sources</a>
        </div>
      </div>
    </nav>

    <header class="relative overflow-hidden border-b-2 border-slate-950 bg-white">
      <div class="mx-auto grid min-h-[82vh] max-w-7xl gap-10 px-4 py-16 sm:px-6 lg:grid-cols-[1fr_.9fr] lg:items-center lg:px-8">
        <div>
          <div class="flex flex-wrap gap-3">
            {badge('Séance 03', 'blue')}
            {badge('n8n', 'violet')}
            {badge('MCP + API', 'cyan')}
          </div>
          <h1 class="mt-8 text-5xl font-black leading-[.95] tracking-normal text-slate-950 md:text-7xl">
            n8n, workflows, nodes, API et MCP
          </h1>
          <p class="mt-6 max-w-2xl text-xl leading-9 text-slate-700">
            Dans cette séance, on part de zéro : ce qu’est n8n, comment lire son interface, comment construire une automatisation utile, puis comment connecter Claude Code et Codex avec MCP ou avec l’API n8n.
          </p>
          <div class="mt-8 border-2 border-slate-950 bg-violet-50 p-5 shadow-neo">
            <p class="font-mono text-xs font-black uppercase tracking-[.16em] text-violet-700">Fil rouge</p>
            <p class="mt-3 leading-8 text-slate-800">Une demande client arrive depuis un formulaire. n8n la vérifie, prépare une réponse, alerte l’équipe, enregistre une trace, puis laisse une execution lisible pour vérifier.</p>
          </div>
        </div>
        <figure class="border-2 border-slate-950 bg-white p-3 shadow-neo">
          <img src="img/interface-s3/hero-n8n-map.png" alt="Carte n8n workflow API MCP" class="aspect-[16/10] w-full object-contain">
          <figcaption class="border-t-2 border-slate-950 px-3 py-3 text-sm font-semibold text-slate-700">Carte de la séance · trigger, nodes, IA, API, MCP et traces</figcaption>
        </figure>
      </div>
    </header>

    {nav}

    <main>
      {section_markup}
      <div id="sources">{sources_table()}</div>
    </main>

    <footer class="border-t-2 border-slate-950 bg-slate-950 px-4 py-10 text-white sm:px-6 lg:px-8">
      <div class="mx-auto flex max-w-7xl flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <p class="font-black">DENEM Academy · Séance 3 · n8n</p>
        <p class="text-sm text-slate-300">80 sections · captures n8n · API · MCP · Claude Code · Codex</p>
      </div>
    </footer>

    <script>
      const progress = document.getElementById('progress');
      const reveals = Array.from(document.querySelectorAll('.reveal'));
      const io = new IntersectionObserver((entries) => {{
        entries.forEach((entry) => {{
          if (entry.isIntersecting) entry.target.classList.add('in-view');
        }});
      }}, {{ threshold: 0.08 }});
      reveals.forEach((el) => io.observe(el));
      window.addEventListener('scroll', () => {{
        const max = document.documentElement.scrollHeight - innerHeight;
        const value = max > 0 ? scrollY / max : 0;
        progress.style.transform = `scaleX(${{value}})`;
      }}, {{ passive: true }});
      document.querySelectorAll('.copy-btn').forEach((button) => {{
        button.addEventListener('click', async () => {{
          const code = button.closest('.code-panel')?.querySelector('code')?.innerText || '';
          await navigator.clipboard.writeText(code);
          const old = button.textContent;
          button.textContent = 'Copié';
          setTimeout(() => button.textContent = old, 900);
        }});
      }});
      let taps = 0;
      document.querySelector('img[alt="DENEM Academy"]')?.addEventListener('click', () => {{
        taps += 1;
        if (taps === 5) {{
          document.body.classList.toggle('bg-blue-50');
          taps = 0;
        }}
      }});
    </script>
  </body>
</html>
"""


def main() -> None:
    html = render()
    OUT.write_text(html, encoding="utf-8")
    INDEX_OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT.name} and index.html with {len(flat_sections())} sections")


if __name__ == "__main__":
    main()
