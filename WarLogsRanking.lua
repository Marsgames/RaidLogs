local colors = {
    ["grey"] = "|cff9d9d9d",
    ["gray"] = "|cff9d9d9d",
    ["green"] = "|cff1eff00",
    ["blue"] = "|cff0070dd",
    ["purple"] = "|cffa335ee",
    ["orange"] = "|cffff8000",
    ["pink"] = "|cffeb569c",
    ["herloom"] = "|cffe6cc80",
    ["white"] = "|cffffffff",
    ["yellow"] = "|cffffff00"
}

local extBosses = {
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

local datas = {
    ["Niisha"] = {
        ["Castle Nathria"] = {
            ["Shriekwing"] = {
                ["N"] = 87,
                ["H"] = 83,
                ["M"] = 0
            },
            ["Huntsman Altimor"] = {
                ["N"] = 80,
                ["H"] = 72,
                ["M"] = 0
            },
            ["Hungering Destroyer"] = {
                ["N"] = 91,
                ["H"] = 82,
                ["M"] = 0
            },
            ["Sun King's Salvation"] = {
                ["N"] = 74,
                ["H"] = 80,
                ["M"] = 0
            },
            ["Artificer Xy'Mox"] = {
                ["N"] = 76,
                ["H"] = 82,
                ["M"] = 0
            },
            ["Lady Inerva Darkvein"] = {
                ["N"] = 83,
                ["H"] = 87,
                ["M"] = 0
            },
            ["The Council of Blood"] = {
                ["N"] = 80,
                ["H"] = 77,
                ["M"] = 0
            },
            ["Sludgefist"] = {
                ["N"] = 90,
                ["H"] = 59,
                ["M"] = 0
            },
            ["Stone Legion Generals"] = {
                ["N"] = 79,
                ["H"] = 60,
                ["M"] = 0
            },
            ["Sire Denathrius"] = {
                ["N"] = 82,
                ["H"] = 37,
                ["M"] = 0
            }
        },
        ["Sanctum of Domination"] = {
            ["The Tarragrue"] = {
                ["N"] = 97,
                ["H"] = 82,
                ["M"] = 0
            },
            ["The Eye of the Jailer"] = {
                ["N"] = 97,
                ["H"] = 94,
                ["M"] = 0
            },
            ["The Nine"] = {
                ["N"] = 93,
                ["H"] = 49,
                ["M"] = 0
            },
            ["Remnant of Ner'zhul"] = {
                ["N"] = 60,
                ["H"] = 8,
                ["M"] = 0
            },
            ["Soulrender Dormazain"] = {
                ["N"] = 85,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Painsmith Raznal"] = {
                ["N"] = 48,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Guardian of the First Ones"] = {
                ["N"] = 90,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Fatescribe Roh-Kalo"] = {
                ["N"] = 72,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Kel'Thuzad"] = {
                ["N"] = 91,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Sylvanas Windrunner"] = {
                ["N"] = 82,
                ["H"] = 0,
                ["M"] = 0
            }
        },
        ["Sepulcher of the First Ones"] = {
            ["Vigilant Guardian"] = {
                ["N"] = 93,
                ["H"] = 70,
                ["M"] = 0
            },
            ["Dausegne, the Fallen Oracle"] = {
                ["N"] = 99,
                ["H"] = 100,
                ["M"] = 0
            },
            ["Artificer Xy'Mox"] = {
                ["N"] = 79,
                ["H"] = 67,
                ["M"] = 0
            },
            ["Prototype Pantheon"] = {
                ["N"] = 90,
                ["H"] = 63,
                ["M"] = 0
            },
            ["Skolex, the Insatiable Ravener"] = {
                ["N"] = 99,
                ["H"] = 50,
                ["M"] = 0
            },
            ["Halondrus the Reclaimer"] = {
                ["N"] = 95,
                ["H"] = 100,
                ["M"] = 0
            },
            ["Lihuvim, Principal Architect"] = {
                ["N"] = 98,
                ["H"] = 71,
                ["M"] = 0
            },
            ["Anduin Wrynn"] = {
                ["N"] = 64,
                ["H"] = 57,
                ["M"] = 0
            },
            ["Lords of Dread"] = {
                ["N"] = 87,
                ["H"] = 50,
                ["M"] = 0
            },
            ["Rygelon"] = {
                ["N"] = 88,
                ["H"] = 100,
                ["M"] = 0
            },
            ["The Jailer"] = {
                ["N"] = 89,
                ["H"] = 50,
                ["M"] = 0
            }
        }
    }
}

local function ternary(condition, ifTrue, ifFalse)
    if condition then
        return ifTrue
    else
        return ifFalse
    end
end

local function InitAddon()
    local frame = WarLogsRanking or CreateFrame("GameTooltip", "WarLogsRanking", PVEFrame, "GameTooltipTemplate")
    frame:SetOwner(PVEFrame, "ANCHOR_NONE")

    if (IsAddOnLoaded("RaiderIO")) then
        local ri = RaiderIO_ProfileTooltip
        frame:SetPoint("TOPLEFT", ri, "TOPRIGHT", 0, 0)
    else
        frame:ClearAllPoints()
        frame:SetPoint("TOPLEFT", PVEFrame, "TOPRIGHT", 0, 0)
    end

    frame:AddLine(colors.white .. "Niisha - Temple-Noir")
    frame:AddLine(" ")

    local raidCount = 0
    for raid, bosses in pairs(datas["Niisha"]) do
        raidCount = raidCount + 1
        frame:AddLine(raid)

        for i = 0, #extBosses[raid] do
            local boss = extBosses[raid][i]
            local difficulties = bosses[boss]
            local maxDifficulty = "-"
            local lineLeft = ""
            local lineRight = ""

            for difficulty, rank in pairs(difficulties) do
                local scoreColor = ternary(difficulties[difficulty] < 25, colors["grey"], ternary(difficulties[difficulty] < 50, colors["green"], ternary(difficulties[difficulty] < 75, colors["blue"], ternary(difficulties[difficulty] < 95, colors["purple"], ternary(difficulties[difficulty] < 99, colors["orange"], ternary(difficulties[difficulty] < 100, colors.pink, colors["herloom"]))))))
                if (maxDifficulty == "-" and rank > 0) then
                    maxDifficulty = difficulty
                    local diffColor = ternary(difficulty == "N", colors["green"], ternary(difficulty == "H", colors["blue"], colors["purple"]))
                    lineLeft = diffColor .. difficulty .. " " .. colors["white"] .. boss
                    lineRight = scoreColor .. rank .. "%"
                end
            end
            if lineLeft == "" then
                frame:AddDoubleLine(colors.grey .. "- " .. colors.white .. boss, colors.grey .. "N/A")
            else
                frame:AddDoubleLine(lineLeft, lineRight)
            end
        end

        if raidCount < 3 then
            frame:AddLine(" ")
        end
    end

    return frame
end

PVEFrame:HookScript(
    "OnShow",
    function()
        local tt = InitAddon()
        tt:Show()
    end
)
