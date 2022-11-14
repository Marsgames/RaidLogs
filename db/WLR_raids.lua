local addonName, ns = ...
local db = ns.db

db = {}

db["Extension"] = {
    ["Shadowlands"] = {
        ["Castle Nathria"] = {
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
        ["Sanctum of Domination"] = {
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
        ["Sepulcher of the First Ones"] = {
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
    }
}

ns.db = db
