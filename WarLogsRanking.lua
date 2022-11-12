-- WLRVars = {
--     version = GetAddOnMetadata("WarLogsRanking", "Version"),
--     prefixAddon = "WaRLoGsRaNkInG",
--     addonTruncatedVersion = 1
-- }

local isWCLRankLoaded = IsAddOnLoaded("WarLogsRanking")
local isRaiderioLoaded = IsAddOnLoaded("RaiderIO")

print("isWCLRankLoaded: " .. tostring(isWCLRankLoaded))
print("isRaiderioLoaded: " .. tostring(isRaiderioLoaded))

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
                ["N"] = 76,
                ["H"] = 79,
                ["M"] = 0
            },
            ["Huntsman Altimor"] = {
                ["N"] = 81,
                ["H"] = 80,
                ["M"] = 0
            },
            ["Hungering Destroyer"] = {
                ["N"] = 90,
                ["H"] = 82,
                ["M"] = 0
            },
            ["Sun King's Salvation"] = {
                ["N"] = 86,
                ["H"] = 75,
                ["M"] = 0
            },
            ["Artificer Xy'Mox"] = {
                ["N"] = 83,
                ["H"] = 75,
                ["M"] = 0
            },
            ["Lady Inerva Darkvein"] = {
                ["N"] = 86,
                ["H"] = 90,
                ["M"] = 0
            },
            ["The Council of Blood"] = {
                ["N"] = 80,
                ["H"] = 77,
                ["M"] = 0
            },
            ["Sludgefist"] = {
                ["N"] = 82,
                ["H"] = 62,
                ["M"] = 0
            },
            ["Stone Legion Generals"] = {
                ["N"] = 73,
                ["H"] = 59,
                ["M"] = 0
            },
            ["Sire Denathrius"] = {
                ["N"] = 82,
                ["H"] = 27,
                ["M"] = 0
            }
        },
        ["Sanctum of Domination"] = {
            ["The Tarragrue"] = {
                ["N"] = 95,
                ["H"] = 80,
                ["M"] = 0
            },
            ["The Eye of the Jailer"] = {
                ["N"] = 95,
                ["H"] = 85,
                ["M"] = 0
            },
            ["The Nine"] = {
                ["N"] = 88,
                ["H"] = 26,
                ["M"] = 0
            },
            ["Remnant of Ner'zhul"] = {
                ["N"] = 45,
                ["H"] = 4,
                ["M"] = 0
            },
            ["Soulrender Dormazain"] = {
                ["N"] = 68,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Painsmith Raznal"] = {
                ["N"] = 48,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Guardian of the First Ones"] = {
                ["N"] = 84,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Fatescribe Roh-Kalo"] = {
                ["N"] = 64,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Kel'Thuzad"] = {
                ["N"] = 77,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Sylvanas Windrunner"] = {
                ["N"] = 50,
                ["H"] = 0,
                ["M"] = 0
            }
        },
        ["Sepulcher of the First Ones"] = {
            ["Vigilant Guardian"] = {
                ["N"] = 93,
                ["H"] = 45,
                ["M"] = 0
            },
            ["Dausegne, the Fallen Oracle"] = {
                ["N"] = 99,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Artificer Xy'Mox"] = {
                ["N"] = 79,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Prototype Pantheon"] = {
                ["N"] = 90,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Skolex, the Insatiable Ravener"] = {
                ["N"] = 99,
                ["H"] = 58,
                ["M"] = 0
            },
            ["Halondrus the Reclaimer"] = {
                ["N"] = 95,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Lihuvim, Principal Architect"] = {
                ["N"] = 98,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Anduin Wrynn"] = {
                ["N"] = 64,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Lords of Dread"] = {
                ["N"] = 87,
                ["H"] = 0,
                ["M"] = 0
            },
            ["Rygelon"] = {
                ["N"] = 88,
                ["H"] = 0,
                ["M"] = 0
            },
            ["The Jailer"] = {
                ["N"] = 89,
                ["H"] = 0,
                ["M"] = 0
            }
        }
    }
}

-- Create empty frame
local frame = CreateFrame("Frame", "WarLogsRanking", UIParent)
frame:SetFrameStrata("BACKGROUND")
frame:SetWidth(256)

local texture = frame:CreateTexture(nil, "BACKGROUND")
-- texture:SetTexture("Interface\\Glues\\CharacterCreate\\UI-CharacterCreate-Factions.blp")
texture:SetAllPoints(frame)
texture:SetColorTexture(0, 0, 0.1, 0.75)
frame.texture = texture
frame.line = 0

frame:SetPoint("CENTER", 20, 0)
-- frame:Show()

-- Add text to my frame
local function AddLineToFrame(frame, text)
    -- local fontString = frame:CreateFontString(nil, "OVERLAY", "GameFontNormal")
    -- fontString:SetPoint("TOPLEFT", 0, -16 * frame.line)
    -- fontString:SetText(text)
    frame.text = frame:CreateFontString(nil, "OVERLAY", "GameFontNormal")
    -- frame.text:SetFont("Fonts\\FRIZQT__.TTF", 12)
    frame.text:SetPoint("TOPLEFT", 0, -16 * frame.line)
    frame.text:SetText(text)
    frame.line = frame.line + 1
end

local function ternary(condition, ifTrue, ifFalse)
    if condition then
        return ifTrue
    else
        return ifFalse
    end
end

AddLineToFrame(frame, colors["white"] .. "Niisha (Temple-Noir)")
AddLineToFrame(frame, "")

for raid, bosses in pairs(datas["Niisha"]) do
    AddLineToFrame(frame, raid)

    -- for loop from 0 to extBosses[raid] count
    -- for i = 0, #extBosses[raid] do
    --     print(i .. " " .. extBosses[raid][i] .. " : " .. tostring(bosses[extBosses[raid][i]]))
    -- end
    -- for boss, difficulties in pairs(bosses) do
    for i = 0, #extBosses[raid] do
        local boss = extBosses[raid][i]
        local difficulties = bosses[boss]
        local maxDifficulty = "-"
        local line = ""

        for difficulty, rank in pairs(difficulties) do
            local scoreColor = ternary(difficulties[difficulty] < 25, colors["grey"], ternary(difficulties[difficulty] < 50, colors["green"], ternary(difficulties[difficulty] < 75, colors["blue"], ternary(difficulties[difficulty] < 95, colors["purple"], ternary(difficulties[difficulty] < 99, colors["orange"], ternary(difficulties[difficulty] < 100, colors.pink, colors["herloom"]))))))
            if (maxDifficulty == "-" and rank > 0) then
                maxDifficulty = difficulty
                local diffColor = ternary(difficulty == "N", colors["green"], ternary(difficulty == "H", colors["blue"], colors["purple"]))
                line = diffColor .. difficulty .. " " .. colors["white"] .. boss .. " : " .. scoreColor .. rank .. "%"
            end
        end
        if line == "" then
            AddLineToFrame(frame, colors["grey"] .. "- " .. colors.white .. boss .. " : " .. colors["grey"] .. "N/A")
        else
            AddLineToFrame(frame, line)
        end
    end

    -- for boss, difficulties in pairs(bosses) do
    --     local scoreColor = ternary(difficulties["M"] < 25, colors["grey"], ternary(difficulties["M"] < 50, colors["green"], ternary(difficulties["M"] < 75, colors["blue"], ternary(difficulties["M"] < 95, colors["purple"], ternary(difficulties["M"] < 99, colors["orange"], colors["herloom"])))))
    --     lines[count] = colors["purple"] .. "M " .. colors["white"] .. boss .. "  : " .. scoreColor .. difficulties["M"] .. "%"
    --     if difficulties["M"] > 0 then
    --         maxDiff = "M"
    --     end
    --     count = count + 1
    -- end

    -- if maxDiff == "-" then
    --     count = 0
    --     for boss, difficulties in pairs(bosses) do
    --         local scoreColor = ternary(difficulties["H"] < 25, colors["grey"], ternary(difficulties["H"] < 50, colors["green"], ternary(difficulties["H"] < 75, colors["blue"], ternary(difficulties["H"] < 95, colors["purple"], ternary(difficulties["H"] < 99, colors["orange"], colors["herloom"])))))
    --         lines[count] = colors["blue"] .. "H " .. colors["white"] .. boss .. "  : " .. scoreColor .. difficulties["H"] .. "%"
    --         if difficulties["H"] > 0 then
    --             maxDiff = "H"
    --         end
    --         count = count + 1
    --     end
    -- end

    -- if maxDiff == "-" then
    --     count = 0
    --     for boss, difficulties in pairs(bosses) do
    --         local scoreColor = ternary(difficulties["N"] < 25, colors["grey"], ternary(difficulties["N"] < 50, colors["green"], ternary(difficulties["N"] < 75, colors["blue"], ternary(difficulties["N"] < 95, colors["purple"], ternary(difficulties["N"] < 99, colors["orange"], colors["herloom"])))))
    --         lines[count] = colors["blue"] .. "N " .. colors["white"] .. boss .. "  : " .. scoreColor .. difficulties["N"] .. "%"
    --         if difficulties["N"] > 0 then
    --             maxDiff = "N"
    --         end
    --         count = count + 1
    --     end
    -- end

    -- if maxDiff == "-" then
    --     for boss, difficulties in pairs(bosses) do
    --         boss = string.sub(boss, 4)
    --         AddLineToFrame(frame, colors["grey"] .. "- " .. colors["white"] .. boss .. "  : " .. colors["grey"] .. "N/A")
    --     end
    -- else
    --     -- sort lines
    --     table.sort(
    --         lines,
    --         function(a, b)
    --             return a < b
    --         end
    --     )
    --     for i = 0, count - 1 do
    --         -- remove pattern \d\d. from line
    --         print("i = " .. i)
    --         lines[i] = string.gsub(lines[i], "%d%d%.", "")
    --         AddLineToFrame(frame, lines[i])
    --     end
    -- end
    AddLineToFrame(frame, "")
end

--     end

--     for boss, difficulties in pairs(bosses) do
--         AddLineToFrame(frame, colors["white"] .. "  " .. boss)
--         for difficulty, rank in pairs(difficulties) do
--             AddLineToFrame(frame, difficulty)
--         end
--     end
--     AddLineToFrame(frame, "")
-- end

frame:SetHeight(16 * frame.line)
local isAnchored = false
local function SetRaiderIOAnchor()
    if (not isRaiderioLoaded) then
        return
    end

    local ri = RaiderIO_ProfileTooltip
    frame:ClearAllPoints()
    frame:SetPoint("TOPLEFT", ri, "TOPRIGHT", 0, 0)
    frame:SetParent(ri)
    idAnchored = true
end
local function SetLFGAnchor()
    local pveFrame = PVEFrame
    frame:ClearAllPoints()
    frame:SetPoint("TOPLEFT", pveFrame, "TOPRIGHT", 0, 0)
    frame:SetParent(pveFrame)

    pveFrame:HookScript(
        "OnShow",
        function()
            frame:Show()
            if (not isAnchored) then
                SetRaiderIOAnchor()
            end
        end
    )
    pveFrame:HookScript(
        "OnHide",
        function()
            frame:Hide()
        end
    )
end

SetLFGAnchor()

-- if (isRaiderioLoaded) then
--     -- SetRaiderIOAnchor()
--     local ri = RaiderIO_ProfileTooltip
--     frame:ClearAllPoints()
--     frame:SetPoint("TOPLEFT", ri, "TOPRIGHT", 0, 0)
--     frame:SetParent(ri)
-- else
--     local function SetAddonAnchor(self, event, arg1, ...)
--         if event == "ADDON_LOADED" and arg1 == "RaiderIO" then
--         -- SetRaiderIOAnchor()
--         end
--     end
--     local addonLoadFrame = CreateFrame("Frame")
--     addonLoadFrame:RegisterEvent("ADDON_LOADED")
--     addonLoadFrame:SetScript("OnEvent", SetAddonAnchor)
-- end

-- SetLFGAnchor()

-- for raid, bosses in pairs(datas["Niisha"]) do
--     AddLineToFrame(frame, raid)
--     local difficultyMax = ""
--     for boss, difficulties in pairs(bosses) do
--         for difficulty, rank in pairs(difficulties) do
--             if difficultyMax == "M" then
--                 break
--             end
--             if difficultyMax ~= "M" and difficulty == "M" and rank > 0 then
--                 difficultyMax = colors["purple"] .. "M"
--                 print("diff set to M")
--             elseif difficultyMax ~= "M" and difficulty == "H" and rank > 0 then
--                 difficultyMax = colors["blue"] .. "H"
--                 print("diff set to H")
--             elseif difficultyMax ~= "M" and difficultyMax ~= "H" and difficulty == "N" and rank > 0 then
--                 difficultyMax = colors["green"] .. "N"
--                 print("diff set to N")
--             end
--         end
--     end
--     for boss, difficulties in pairs(bosses) do
--         print("difficulties", difficulties)
--         DevTools_Dump(difficulties)
--         print("difficultyMax", difficultyMax)
--         print("difficulties[difficultyMax]", boss[difficultyMax])
--         do
--             return
--         end
--         local scoreColor = ternary(difficulties[difficultyMax] < 25, colors["grey"], ternary(difficulties[difficultyMax] < 50, colors["green"], ternary(difficulties[difficultyMax] < 75, colors["blue"], ternary(difficulties[difficultyMax] < 95, colors["purple"], ternary(difficulties[difficultyMax] < 99, colors["orange"], colors["herloom"])))))
--         AddLineToFrame(frame, difficultyMax .. " " .. boss .. " : " .. scoreColor .. difficulties[difficultyMax])
--     end
-- end
