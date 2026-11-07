"""All site text lives here. Edit this file, then run: python3 _build/build.py"""

SITE = {
    "name": "Natapatr Lorsathian",
    "short": "Nat",
    "base_url": "https://natapatrl.github.io/portfolio/",
    "description": "Natapatr (Nat) Lorsathian - gameplay, level and UX/UI designer. "
                   "Puzzle, platformer and level design work in Unity, Unreal and UEFN.",
    "email_user": "natapatr.lors",
    "email_domain": "gmail.com",
    "linkedin": "https://www.linkedin.com/in/natapatrl",
    "linkedin_label": "Natapatr (Nat) Lorsathian",
    "itch": "https://twonah.itch.io/",
}

HOME = {
    # Home windows read like a game's UI (player profile, loadout), not a code terminal.
    "profile_title": "PLAYER PROFILE",
    "player_label": "PLAYER",
    "player": "NAT",
    "class_label": "CLASS",
    # Shown as the colour-coded discipline chips used on the project tags.
    "classes": ["Gameplay Design", "Level Design", "UX/UI Design"],
    "loadout_label": "LOADOUT",
    "tools": ["Unity", "Unreal", "Figma"],
    "latest_title": "LATEST PROJECT",
    "latest_tag": "NEW",
    "quest_label": "DESIGN QUEST:",
    "quest": "DEFEAT FRUSTRATION",
    "reward": "USER REWARD: +100 DESIGN POINTS",
    # Projects shown under the quest band on the home page (by slug). The Projects page lists all.
    "picks": ["peritoneum", "world-x-recipe", "biotech-lab"],
}

ABOUT = {
    "title": "WHO AM I?",
    # Interactive chat. Nat's messages are the left (lavender) bubbles; the reader's picks are
    # the right (mint) bubbles. Each topic disappears once asked. When none are left, the only
    # option is the final link.
    "intro": [
        "Hi, I'm Natapatr. Nat for short.",
        "I'm a game designer. Level design and UX/UI are my favorites.",
        "Ask me anything!",
    ],
    "topics": [
        {
            "q": "What makes a game great?",
            "a": [
                "It has to feel good to play.",
                "Fun is the foundation, but even a fun game gets frustrating if it isn't user-friendly.",
            ],
        },
        {
            "q": "Your design goal?",
            "a": ["Balancing fun with a smooth user experience."],
        },
        {
            "q": "What tools do you use?",
            "a": ["Unity, Unreal (incl. UEFN) and Figma for UI prototypes."],
        },
        {
            "q": "Working on anything now?",
            "a": [
                "Anonymized! Our Global Game Jam 2026 entry, 1st place at Game Dev Hub Bangkok.",
                "We grew it into a full game. It's out now on Steam.",
            ],
        },
    ],
    "final": "View my projects",
}

CONTACT = {
    "heading": "INTERESTED IN MY RESUME?",
    "lines": [
        "Reach out below. (Or via any convenient platform of your choice)",
        "If I haven't already, I'll send you a version of my Resume tailored specifically for the occasion.",
    ],
}

# Order here = order on the site. The first project is the featured one on the home page.
PROJECTS = [
    {
        "slug": "anonymized",
        "title": "Anonymized",
        "subtitle": "Entry: Global Game Jam 2026",
        "year": "2026",
        "kind": "Team Project",
        "roles": "Gameplay Designer | Level Designer | UX Designer",
        "tags": ["Gameplay Design", "Level Design", "UX/UI Design"],
        "blurb": "Movement-based color-shifting puzzle game; Global Game Jam 2026 submission "
                 "under the theme 'Mask'.",
        "tagline": "Movement-based color-shifting puzzle game.",
        "genre": "Color-shift puzzle",
        # Short HUD badges on the home featured block (kept to a couple of words each).
        "badges": [("award", "1st place / GGJ 2026 Bangkok"), ("status", "Out now")],
        "awards": [
            "1st Place - Game Dev Hub Bangkok (Global Game Jam 2026)",
            "Finalist - BIDC Rising Star Award 2026",
            "Finalist - Rising Tide 4, Platformer, Puzzles & Arcade (Blue Ocean Games)",
        ],
        "stats": [
            ("Team size", "4"),
            ("Engine", "Unity"),
            ("Timeframe", "72 hours (jam)"),
            ("Status", "Out now on Steam"),
        ],
        "links": [
            ("View on Steam", "https://store.steampowered.com/app/4548240/Anonymized/"),
            ("Jam version on itch.io", "https://arkudada.itch.io/anonymized"),
        ],
        "hero_ph": "Anonymized key art or gameplay screenshot",
        "overview": [
            "Anonymized is a puzzle game following the 2026 Global Game Jam's theme, \"Mask\".",
            "You play as a digital rat, hacking your way into an unknown system in search for the "
            "hidden 'cheese'. To progress, you must 'mask' yourself in various hues to bypass the "
            "firewall nodes.",
            "This game also has multiple accessibility features such as color-blindness support and "
            "being playable on almost every input device including, DDR pad.",
        ],
        "history_title": "Work History",
        "history": [
            "Designed the game's core loop and mechanic interactions",
            "Worked on over 12 in-game levels",
            "Oversee the development of the game's UX and UI",
            "Pushed the implementation of various accessibility features",
            "Conducted extensive playtests to polish both UX/UI and levels",
            "Helped with composing various SFX and the BGM",
        ],
        "sections": [],
        "gallery_ph": ["Level layout / puzzle screenshot", "UI or accessibility options screenshot"],
    },
    {
        "slug": "peritoneum",
        "title": "Peritoneum",
        "subtitle": "Entry: [IndieCritical] Summer Jam 2025",
        "year": "2025",
        "kind": "Team Project",
        "roles": "Gameplay Designer | Level Designer",
        "tags": ["Gameplay Design", "Level Design"],
        "genre": "Physics platformer",
        "blurb": "A unique platformer using physics-based movement; an IndieCritical Summer Jam 2025 "
                 "submission under the theme 'Not What It Seems'.",
        "stats": [
            ("Team size", "6"),
            ("Engine", "Unity"),
            ("Timeframe", "10 days"),
            ("Status", "Completed"),
        ],
        "links": [("Play on itch.io", "https://arkudada.itch.io/peritoneum")],
        "hero_ph": "Peritoneum gameplay screenshot",
        "overview": [
            "Peritoneum is an experimental platformer created under the jam's theme, \"Not What It "
            "Seems.\" It subverts the traditional platformer tropes by introducing unexpected mechanics.",
            "Rather than aiming for a convention and polished game, my jam team (formed mostly from "
            "strangers) focused on experimentation and fun. As such, the game's design reflects this "
            "philosophy; the core mechanic uses a gun's blast to propel the character towards a direction.",
            "Designing around that logic, action elements are blended in to create a more satisfying and "
            "complete experience of using a firearm. A controllable directional propulsion pack was also "
            "added to give players greater movement feel and control.",
        ],
        "history_title": "Work History",
        "history": [
            "Curated 5 progressively challenging levels",
            "Implemented a diegetic tutorial that encourages the player to experiment and test things "
            "out on their own",
            "Designed a boss fight encounter using state machines, working closely with the programmer "
            "for its implementation",
            "Worked on the various game mechanics, such as enemy attacks and player abilities",
            "Coordinated workflow between both programmers and artists as the creative lead",
        ],
        "sections": [],
        "gallery_ph": ["Level screenshot", "Boss fight screenshot"],
    },
    {
        "slug": "world-x-recipe",
        "title": "World X Recipe",
        "subtitle": "Entry: Global Game Jam 2025",
        "year": "2025",
        "kind": "Team Project",
        "roles": "Gameplay Designer | UX Designer",
        "tags": ["Gameplay Design", "UX/UI Design"],
        "genre": "Claw-machine arcade",
        "blurb": "Arcade-inspired claw-machine game; Global Game Jam 2025 submission under the theme "
                 "'Bubble'.",
        "stats": [
            ("Team size", "12"),
            ("Engine", "Unity"),
            ("Timeframe", "47 hours"),
            ("Status", "Completed"),
        ],
        "links": [("Play on itch.io", "https://arkudada.itch.io/wxr")],
        "hero_ph": "World X Recipe title screen or gameplay",
        "overview": [
            "World X Recipe is an arcade-inspired game based on Global Game Jam's 2025 theme, \"Bubbles\".",
            "The concept formed quickly after the team, fusing the idea of 'bubbles' and 'abduction'. "
            "Soon came the UFO theme, which was fused with the creative vision of it being an arcade "
            "game. The result is a meta-like claw machine experience, made in the given 47 hours for "
            "the jam.",
        ],
        "history_title": "Work History",
        "history": [
            "Prototyped the game's various UI on Figma",
            "Managed the development of the game's UX",
            "Designed the core mechanics alongside other designers",
            "Tuned the game's feel",
            "Helped with the implementation of various SFX",
        ],
        "sections": [
            ("Why Claw Machine?", [
                "With only 2 days to develop the game, scope was the primary constraint. I aimed to "
                "create something mechanically simple and immediately readable yet engaging and "
                "replayable. Arcade games became the reference point due to their short loops and clear "
                "objectives, which has stood the test of time.",
                "To integrate the jam's theme of \"Bubbles\" into gameplay, I looked at how real bubbles "
                "behave. Their buoyancy and upward motion can be translated into the game loop of claw "
                "machines; grab and lift.",
            ], "Figma UI prototype or claw gameplay"),
        ],
        "gallery_ph": [],
    },
    {
        "slug": "biotech-lab",
        "title": "Biotech Lab",
        "subtitle": "Environmental Storytelling Project",
        "list_title": "Environmental Story",
        "year": "2024",
        "kind": "Solo Project",
        "roles": "Level Designer",
        "tags": ["Level Design"],
        "genre": "Narrative level",
        "blurb": "Practice and showcase on scene composition, level flow and environmental storytelling.",
        "stats": [
            ("Team size", "Solo"),
            ("Engine", "Unreal Fortnite (UEFN)"),
            ("Timeframe", "3 weeks"),
            ("Status", "Completed"),
        ],
        "links": [],
        "hero_ph": "Biotech Lab environment shot",
        "overview": [
            "This project marked my first attempt at environmental storytelling, and initially, I "
            "struggled with conveying the narrative without relying on words.",
            "However, through the process of crafting this experimental level, I learned how to guide "
            "players toward points of interest and use scene composition to subtly reveal details about "
            "the game world.",
        ],
        "history_title": "Work History",
        "history": [
            "Drafted level blueprint",
            "Blocked out the level",
            "Set-dressed the level",
            "Added and tuned the lighting",
            "Implemented sound effects and BGM",
            "Conducted playtests",
        ],
        "sections": [
            ("Scene Composition", [
                "Thanks to my hobby in photography, I had prior knowledge of scene composition. That made "
                "the task of designing various points of interest throughout the level an enjoyable task, "
                "which got me engaged in the workflow and subsequently increased my productivity.",
                "Once I have established the main narrative, everything began to fall into place despite "
                "the initial delay. This allowed me to complete the project in its final remaining days, "
                "even though I had spent too much time on the ideation process.",
            ], "Point-of-interest / composition screenshot"),
        ],
        "gallery_ph": ["Level blueprint or block-out", "Final set-dressed shot"],
    },
    {
        "slug": "frost-fortress",
        "title": "Frost Fortress",
        "subtitle": "Multiplayer Level Design",
        "list_title": "Multiplayer Map",
        "year": "2024",
        "kind": "Solo Project",
        "roles": "Level Designer",
        "tags": ["Level Design"],
        "genre": "Third-person shooter arena",
        "blurb": "Concept level designed for a multiplayer third-person shooter experience. Practice on "
                 "map-based combat balance using layout, sightlines, and map objectives.",
        "stats": [
            ("Team size", "Solo"),
            ("Engine", "Unreal Fortnite (UEFN)"),
            ("Timeframe", "3 weeks"),
            ("Status", "Completed"),
        ],
        "links": [],
        "hero_ph": "Frost Fortress overview shot",
        "overview": [
            "As part of the effort to expand my level design skill set, this project is my attempt at "
            "multiplayer level design, using Fortnite's established combat system within the UEFN level "
            "editor.",
            "With the varied workflow of frequent testing and the rapid development of a small-scale "
            "level, I have developed a newfound enjoyment for level design.",
        ],
        "history_title": "Work History",
        "history": [
            "Drafted the level blueprint",
            "Rapidly developed level block-outs",
            "Tested multiplayer-compatibility",
            "Frequently tested the balance and level flow",
            "Checked and adjusted various sightlines",
            "Decorated and set-dressed the level",
        ],
        "sections": [
            ("Rapid Development", [
                "Since a multiplayer map is not linear like a traditional single player map, more of its "
                "development is dedicated to perfecting a single large play area.",
                "This calls for multiple play-testing for many aspects of the level to ensure its balance, "
                "flow and most importantly, replayability.",
                "This project gave me first-hand experience with the process of rapid development. From "
                "finishing the whole map within a few days to testing it every time the level has been "
                "changed.",
            ], "Top-down map layout with sightlines"),
        ],
        "gallery_ph": ["Block-out vs. final comparison", "In-match screenshot"],
    },
    {
        "slug": "unpuzzled-business",
        "title": "Unpuzzled Business",
        "subtitle": "Escape Room Puzzle Game",
        "year": "2024",
        "kind": "Team Project",
        "roles": "Gameplay Designer | Level Designer",
        "tags": ["Gameplay Design", "Level Design"],
        "genre": "Escape room puzzle",
        "blurb": "Escape room puzzle game; focused on improving player guidance through level flow and "
                 "lighting.",
        "stats": [
            ("Team size", "9"),
            ("Engine", "Unreal 5.2"),
            ("Timeframe", "4 months"),
            ("Status", "Completed"),
        ],
        "links": [],
        "hero_ph": "Unpuzzled Business room screenshot",
        "overview": [
            "Unpuzzled Business is a supernatural-themed escape room puzzle game developed by a team of nine.",
            "I served as both gameplay and level designer, while also leading the project as creative director.",
            "My primary challenge was transforming a vague concept left to the team by a former member "
            "into a cohesive, playable experience.",
        ],
        "history_title": "Contributions",
        "history": [
            "Created puzzle flowcharts to streamline development",
            "Designed and implemented core puzzle mechanics",
            "Conducted user testing to refine player guidance",
            "Implemented lighting and environmental story",
        ],
        "sections": [
            ("Puzzle Flowchart", [
                "The first task I completed for the team was creating the puzzle flowchart, which outlined "
                "each puzzle step alongside detailing its theme, mechanics, related items, and event triggers.",
                "This flowchart significantly improved the team's workflow, enabling all roles to work in "
                "parallel and eliminating many of the bottlenecks that had previously slowed development.",
            ], "Puzzle flowchart"),
            ("Player Guidance", [
                "After the completion of the first playable prototype, a recurring issue emerged around the "
                "clarity of the puzzles and mechanics.",
                "I have identified that this is largely due to the game's immersive and diegetic design "
                "hindering the communication of various game mechanics.",
                "To address this, I conducted user research and playtesting focused on player guidance. "
                "Based on the feedback and analysis, I improved the level's readability by adjusting "
                "lighting, incorporating leading lines, and simplifying certain puzzle elements to enhance "
                "clarity without compromising immersion.",
            ], "Before / after guidance comparison"),
            ("Lighting Problems", [
                "With all the lighting improvements and changes comes more issues. One such issue concerns "
                "the game's performance due to the heavy use of volumetric and moveable lighting, in order "
                "to improve player guidance.",
                "After discussing the issue with programmers, I have created a lighting guideline that "
                "details the limitations of light placement in each room. I also have a hand in editing and "
                "optimizing the lighting in-engine, utilizing my knowledge on lighting in Unreal Engine.",
            ], "Lighting guideline page or lit room"),
        ],
        "gallery_ph": [],
    },
]


# ---------------------------------------------------------------------------------------------
# Design log (project pages): Overview tab + one tab per highlight + Debrief tab.
# Each highlight: (tab title, image label, problem, decision, result[, link]).
#   - Text in [brackets] is a placeholder saying what goes there; fill it in when the project is
#     rewritten with Nat. Unbracketed lines are stand-ins condensed from the old Wix text (the full
#     old text is still in each project's "overview" / "sections" above, no longer shown).
#   - link = (other project's slug, that project's highlight title). The page shows it as
#     "EVOLVED FROM ..." (older project) or "REFINED IN ..." (newer project) and opens that tab.
# Anonymized is where the earlier ideas come together: Peritoneum's diegetic tutorial, World X
# Recipe's diegetic UI, Unpuzzled Business's puzzle flow and player guidance, and Biotech Lab's
# environmental storytelling, all done better.
DESIGN_LOG = {
    "anonymized": {
        "highlights": [
            ("TUTORIAL", "Tutorial level clip",
             "[ what new players had to learn, and why text pop-ups wouldn't fit ]",
             "[ how the levels teach colour-shifting by doing; what changed since Peritoneum ]",
             "[ playtest sign it worked: e.g. players clearing the opening without help ]",
             ("peritoneum", "DIEGETIC TUTORIAL")),
            ("DIEGETIC UI", "In-world UI / HUD screenshot",
             "[ what information players needed while playing ]",
             "[ how it lives in the game world instead of a HUD; what improved over World X Recipe ]",
             "[ effect on readability or immersion ]",
             ("world-x-recipe", "DIEGETIC UI")),
            ("PUZZLE FLOW", "Puzzle flow chart or level sequence",
             "[ how 12+ levels needed to ramp up without spikes ]",
             "[ how puzzles were sequenced and documented; what improved over Unpuzzled Business ]",
             "[ result: smoother difficulty curve, faster level building, etc. ]",
             ("unpuzzled-business", "PUZZLE FLOW")),
            ("PLAYER GUIDANCE", "Before / after guidance comparison",
             "[ where playtesters got lost or misread a puzzle ]",
             "[ what was changed: colour, light, layout, signposting ]",
             "[ what playtests showed afterwards ]",
             ("unpuzzled-business", "PLAYER GUIDANCE")),
            ("ENV. STORY", "Environment / world screenshot",
             "[ what the world needed to say about the rat, the system and the 'cheese' ]",
             "[ how levels and props tell it without dialogue; builds on Biotech Lab ]",
             "[ how players picked the story up ]",
             ("biotech-lab", "SCENE COMPOSITION")),
        ],
    },
    "peritoneum": {
        "highlights": [
            ("DIEGETIC TUTORIAL", "Tutorial area screenshot",
             "[ the gun-blast movement is unusual; what players had to figure out ]",
             "[ how the tutorial lets players experiment instead of reading instructions ]",
             "[ how quickly players got the movement in playtests ]",
             ("anonymized", "TUTORIAL")),
            ("BOSS FIGHT", "Boss fight clip or state diagram",
             "[ what the boss needed to test from everything the player learned ]",
             "[ the state machine design, and working with the programmer to build it ]",
             "[ how the fight played in the end ]"),
            ("LEVEL PROGRESSION", "Level screenshot",
             "[ how to ramp 5 levels in 10 days ]",
             "[ what each level introduces or combines ]",
             "[ result ]"),
        ],
    },
    "world-x-recipe": {
        "highlights": [
            ("WHY CLAW MACHINE", "Claw gameplay",
             "Only 47 hours to build a game around the theme \"Bubbles\".",
             "Chose an arcade claw machine: short loop, clear goal, and bubbles' upward pull maps onto grab and lift.",
             "[ how the idea landed with players / at the jam ]"),
            ("DIEGETIC UI", "Figma prototype or in-game machine UI",
             "[ what players needed to see: time, score, controls ]",
             "[ how it was built into the arcade machine itself, prototyped in Figma ]",
             "[ effect on the arcade feel ]",
             ("anonymized", "DIEGETIC UI")),
            ("GAME FEEL", "Claw handling clip",
             "[ what felt off about the claw at first ]",
             "[ what was tuned: speed, weight, grab timing ]",
             "[ how it felt after tuning ]"),
        ],
    },
    "biotech-lab": {
        "highlights": [
            ("SCENE COMPOSITION", "Point-of-interest / composition screenshot",
             "My first environmental storytelling level; telling the story without words was hard.",
             "Used composition from my photography to place points of interest that guide the player.",
             "Once the narrative was set, the level came together in the final days.",
             ("anonymized", "ENV. STORY")),
        ],
    },
    "frost-fortress": {
        "highlights": [
            ("RAPID ITERATION", "Block-out vs. final comparison",
             "A multiplayer map isn't linear: one large play area has to stay balanced and replayable.",
             "Blocked out fast and playtested after every change.",
             "Finished the whole map within a few days."),
            ("SIGHTLINES", "Top-down map layout with sightlines",
             "[ which sightlines were too long or one-sided ]",
             "[ how cover and layout were adjusted ]",
             "[ effect on fights ]"),
            ("BALANCE AND FLOW", "In-match screenshot",
             "[ where players clustered or avoided ]",
             "[ changes to routes, spawns or objectives ]",
             "[ how matches played afterwards ]"),
        ],
    },
    "unpuzzled-business": {
        "highlights": [
            ("PUZZLE FLOW", "Puzzle flowchart",
             "The team inherited a vague concept from a former member, and every role was waiting on someone else.",
             "Mapped every puzzle step into one flowchart: theme, mechanics, items and event triggers.",
             "Art, programming and design could work in parallel, clearing most bottlenecks.",
             ("anonymized", "PUZZLE FLOW")),
            ("PLAYER GUIDANCE", "Before / after guidance comparison",
             "Playtesters couldn't read the puzzles; the diegetic design was hiding how the mechanics worked.",
             "Ran guidance-focused playtests, then added leading lines, adjusted lighting and simplified some puzzle elements.",
             "Puzzles read clearly without breaking immersion.",
             ("anonymized", "PLAYER GUIDANCE")),
            ("LIGHTING BUDGET", "Lighting guideline page or lit room",
             "Heavy volumetric and movable lights added for guidance started hurting performance.",
             "Wrote a per-room lighting guideline with the programmers and optimized lights in-engine.",
             "[ result: performance or guidance outcome ]"),
        ],
    },
}
DEBRIEF_PLACEHOLDER = "[ 1–2 lines: what I learned / what I'd do next ]"
