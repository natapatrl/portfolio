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
    "intro": "I'M NAT; A GAMEPLAY, LEVEL, UX/UI DESIGNER.",
    "tools": "I WORK IN: UNITY \\\\ UNREAL \\\\ FIGMA",
    "quest_label": "DESIGN QUEST:",
    "quest": "DEFEAT FRUSTRATION",
    "reward": "USER REWARD: +100 DESIGN POINTS",
}

ABOUT = {
    "title": "WHO AM I?",
    # Interactive chat. Nat's messages are the left (lavender) bubbles; the reader's picks are
    # the right (mint) bubbles. Each topic disappears once asked. When none are left, the only
    # option is the final link.
    "intro": [
        "Hello, I'm Natapatr Lorsathian (Nat for short).",
        "I'm a versatile game designer. While proficient with the basics of every design "
        "discipline, I enjoy UI/UX and level design the most.",
        "Ask me anything below!",
    ],
    "topics": [
        {
            "q": "What makes a game great to you?",
            "a": [
                "I firmly believe that a great game must first and foremost feel good to play.",
                "While fun is undoubtedly the foundation of game design, even the most enjoyable "
                "game can quickly become frustrating if it's not user-friendly.",
            ],
        },
        {
            "q": "So what's your design goal?",
            "a": [
                "Striking a balance between fun and user experience is key to creating a truly "
                "great gameplay experience.",
            ],
        },
        {
            "q": "What tools do you work with?",
            "a": [
                "Unity, Unreal (including UEFN, Fortnite's level editor) and Figma, which I use "
                "to prototype UI.",
            ],
        },
        {
            "q": "What are you working on right now?",
            "a": [
                "Anonymized! It started as our Global Game Jam 2026 entry and won 1st place at "
                "Game Dev Hub Bangkok.",
                "Now it's being developed into a full game, and the demo is already on Steam.",
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
        "awards": [
            "1st Place - Game Dev Hub Bangkok (Global Game Jam 2026)",
            "Finalist - BIDC Rising Star Award 2026",
            "Finalist - Rising Tide 4, Platformer, Puzzles & Arcade (Blue Ocean Games)",
        ],
        "stats": [
            ("Team size", "4"),
            ("Engine", "Unity"),
            ("Timeframe", "72 hours (jam)"),
            ("Status", "Jam version completed // Steam release in development"),
        ],
        "links": [
            ("Play the demo on Steam", "https://store.steampowered.com/app/4765400/ANONYMIZED_Demo/"),
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
