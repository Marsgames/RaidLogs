local addonName, ns = ...
local db = ns.db

db = {}

db.RaidName = {
    [26] = "Castle Nathria",
    [28] = "Sanctum of Domination",
    [29] = "Sepulcher of the First Ones",
    [31] = "Vault of the Incarnates"
}
db.RaidID = {
    ["Castle Nathria"] = 26,
    ["Sanctum of Domination"] = 28,
    ["Sepulcher of the First Ones"] = 29,
    ["Vault of the Incarnates"] = 31
}

-- To get groups id :
-- https://wow.tools/dbc/?dbc=groupfinderactivity
db.GrpID = {
    [267] = "Castle Nathria",
    [271] = "Sanctum of Domination",
    [282] = "Sepulcher of the First Ones",
    [310] = "Vault of the Incarnates"
}

db.BossName = {
    [26] = {
        [2398] = "Shriekwing",
        [2418] = "Huntsman Altimor",
        [2383] = "Hungering Destroyer",
        [2402] = "Sun King's Salvation",
        [2405] = "Artificer Xy'Mox",
        [2406] = "Lady Inerva Darkvein",
        [2412] = "The Council of Blood",
        [2399] = "Sludgefist",
        [2417] = "Stone Legion Generals",
        [2407] = "Sire Denathrius"
    },
    [28] = {
        [2423] = "The Tarragrue",
        [2433] = "The Eye of the Jailer",
        [2429] = "The Nine",
        [2432] = "Remnant of Ner'zhul",
        [2434] = "Soulrender Dormazain",
        [2430] = "Painsmith Raznal",
        [2436] = "Guardian of the First Ones",
        [2431] = "Fatescribe Roh-Kalo",
        [2422] = "Kel'Thuzad",
        [2435] = "Sylvanas Windrunner"
    },
    [29] = {
        [2512] = "Vigilant Guardian",
        [2540] = "Dausegne, the Fallen Oracle",
        [2553] = "Artificer Xy'Mox",
        [2544] = "Prototype Pantheon",
        [2542] = "Skolex, the Insatiable Ravener",
        [2529] = "Halondrus the Reclaimer",
        [2539] = "Lihuvim, Principal Architect",
        [2546] = "Anduin Wrynn",
        [2543] = "Lords of Dread",
        [2549] = "Rygelon",
        [2537] = "The Jailer"
    },
    [31] = {
        [2587] = "Eranog",
        [2639] = "Terros",
        [2590] = "The Primalist Council",
        [2592] = "Sennarth, The Cold Breath",
        [2635] = "Dathea, Ascended",
        [2605] = "Kurog Grimtotem",
        [2614] = "Broodkeeper Diurna",
        [2607] = "Raszageth the Storm-Eater"
    }
}
db.BossId = {
    [26] = {
        ["Shriekwing"] = 2398,
        ["Huntsman Altimor"] = 2418,
        ["Hungering Destroyer"] = 2383,
        ["Sun King's Salvation"] = 2402,
        ["Artificer Xy'Mox"] = 2405,
        ["Lady Inerva Darkvein"] = 2406,
        ["The Council of Blood"] = 2412,
        ["Sludgefist"] = 2399,
        ["Stone Legion Generals"] = 2417,
        ["Sire Denathrius"] = 2407
    },
    [28] = {
        ["The Tarragrue"] = 2423,
        ["The Eye of the Jailer"] = 2433,
        ["The Nine"] = 2429,
        ["Remnant of Ner'zhul"] = 2432,
        ["Soulrender Dormazain"] = 2434,
        ["Painsmith Raznal"] = 2430,
        ["Guardian of the First Ones"] = 2436,
        ["Fatescribe Roh-Kalo"] = 2431,
        ["Kel'Thuzad"] = 2422,
        ["Sylvanas Windrunner"] = 2435
    },
    [29] = {
        ["Vigilant Guardian"] = 2512,
        ["Dausegne, the Fallen Oracle"] = 2540,
        ["Artificer Xy'Mox"] = 2553,
        ["Prototype Pantheon"] = 2544,
        ["Skolex, the Insatiable Ravener"] = 2542,
        ["Halondrus the Reclaimer"] = 2529,
        ["Lihuvim, Principal Architect"] = 2539,
        ["Anduin Wrynn"] = 2546,
        ["Lords of Dread"] = 2543,
        ["Rygelon"] = 2549,
        ["The Jailer"] = 2537
    },
    [31] = {
        ["Eranog"] = 2587,
        ["Terros"] = 2639,
        ["The Primalist Council"] = 2590,
        ["Sennarth, The Cold Breath"] = 2592,
        ["Dathea, Ascended"] = 2635,
        ["Kurog Grimtotem"] = 2605,
        ["Broodkeeper Diurna"] = 2614,
        ["Raszageth the Storm-Eater"] = 2607
    }
}

db["Extension"] = {
    ["Shadowlands"] = {
        [26] = {
            [0] = "Shriekwing",
            [1] = "Huntsman Altimor",
            [2] = "Hungering Destroyer",
            [3] = "Sun King's Salvation",
            [4] = "Artificer Xy'Mox",
            [5] = "Lady Inerva Darkvein",
            [6] = "The Council of Blood",
            [7] = "Sludgefist",
            [8] = "Stone Legion Generals",
            [9] = "Sire Denathrius"
        },
        [28] = {
            [0] = "The Tarragrue",
            [1] = "The Eye of the Jailer",
            [2] = "The Nine",
            [3] = "Remnant of Ner'zhul",
            [4] = "Soulrender Dormazain",
            [5] = "Painsmith Raznal",
            [6] = "Guardian of the First Ones",
            [7] = "Fatescribe Roh-Kalo",
            [8] = "Kel'Thuzad",
            [9] = "Sylvanas Windrunner"
        },
        [29] = {
            [0] = "Vigilant Guardian",
            [1] = "Dausegne, the Fallen Oracle",
            [2] = "Artificer Xy'Mox",
            [3] = "Prototype Pantheon",
            [4] = "Skolex, the Insatiable Ravener",
            [5] = "Halondrus the Reclaimer",
            [6] = "Lihuvim, Principal Architect",
            [7] = "Anduin Wrynn",
            [8] = "Lords of Dread",
            [9] = "Rygelon",
            [10] = "The Jailer"
        }
    },
    ["Dragonflight"] = {
        [31] = {
            [0] = "Eranog",
            [1] = "Terros",
            [2] = "The Primalist Council",
            [3] = "Sennarth, The Cold Breath",
            [4] = "Dathea, Ascended",
            [5] = "Kurog Grimtotem",
            [6] = "Broodkeeper Diurna",
            [7] = "Raszageth the Storm-Eater"
        }
    }
}

ns.db = db
