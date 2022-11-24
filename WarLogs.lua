local addonName, ns = ...

local db = ns.db
local charData = {}

-- Create public function to populate the db (called from db/WarLogs_DB_XX.lua, but as these files are
--      enabled with "another addon" they do not have the same namespace as this file)
function WarLogsAddCharsToDB(charsTable)
    -- append charsTable to db.char
    for k, v in pairs(charsTable) do
        charData[k] = v
    end
end

-- Colors used in the addon (principally for the rank percentages)
-- Maybe we should use a ToolBox namespace for this?
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

-- Load bosses data for current expansion + get player name and realm
local extBosses = db["Extension"]["Shadowlands"]
local playerName = GetUnitName("player")
local playerRealm = GetRealmName()

-- Ternary function to reduce the number of lines in the code
-- Maybe who should use something like a quarternary function to reduce the number of lines even more?
-- Maybe we should use a ToolBox namespace for this?
local function ternary(condition, ifTrue, ifFalse)
    if condition then
        return ifTrue
    else
        return ifFalse
    end
end
-- TODO: Create something that looks like a switch/case statement

-- Givent a data set, return a tooltip double line formatted string
local function ProcessLines(lineLeft, lineRight, maxDifficulty, datas, difficulty, bossName)
    -- Get color for the rank percentage and difficulty "name"
    local scoreColor = ternary(datas["best"] < 25, colors["grey"], ternary(datas["best"] < 50, colors["green"], ternary(datas["best"] < 75, colors["blue"], ternary(datas["best"] < 95, colors["purple"], ternary(datas["best"] < 99, colors["orange"], ternary(datas["best"] < 100, colors.pink, colors["herloom"]))))))
    local diffName = ternary(difficulty == 5, "M", ternary(difficulty == 4, "H", "N"))

    -- If there is a rank for this difficulty, and the difficulty is higher than the previous tested ones, add a line to the tooltip
    if (difficulty > maxDifficulty and datas["best"] > 0) then
        maxDifficulty = difficulty
        local diffColor = ternary(diffName == "N", colors["green"], ternary(diffName == "H", colors["blue"], colors["purple"]))
        lineLeft = diffColor .. diffName .. " " .. colors["white"] .. bossName
        lineRight = scoreColor .. datas["best"] .. "%"
    end
    return lineLeft, lineRight, maxDifficulty
end

local function ProcessRaid(raid, frame, unitRealm, unitName, addLineBefore)
    local raidName = db.RaidName[raid]
    local playerDatas = charData[playerRealm][playerName]
    local playerTable = {}
    local metric = ""
    -- data format = "bossId:bossDifficulty:metric:best:average:killCount/boss2ID:..."

    -- new data format = "encDatas:best:average:killCount/enc2Datas:..."

    local raids = { strsplit("/", playerDatas) }

    for _, boss in pairs(raids) do
        local splitTable = {strsplit(":", boss)}

        local bossId = tonumber(splitTable[1])
        local bossDifficulty = tonumber(splitTable[2])
        metric = splitTable[3]
        local best = tonumber(splitTable[4])
        local average = tonumber(splitTable[5])
        local killCount = tonumber(splitTable[6])

        -- local encounterType = tonumber(splitTable[1])
        -- local best = tonumber(splitTable[2])
        -- local average = tonumber(splitTable[3])
        -- local killCount = tonumber(splitTable[4])
        -- local bossId = 
        -- local bossDifficulty = 
        -- local metric =

        if playerTable[bossId] == nil then
            playerTable[bossId] = {}
        end
        playerTable[bossId][bossDifficulty] = {
            ["metric"] = metric,
            ["best"] = best,
            ["average"] = average,
            ["killCount"] = killCount
        }
    end

    if (addLineBefore) then
        frame:AddLine(" ")
    end

    --local TankIcon = "|A:4259:19:19|a" -- Should not appear
    local HealerIcon = "|A:4258:19:19|a"
    local DPSIcon = "|A:4257:19:19|a"
    frame:AddDoubleLine(raidName, ternary(metric == "dps", DPSIcon, HealerIcon)-- ternary(metric == "hps", HealerIcon, TankIcon)))

    for i = 0, #extBosses[raid] do
        local bossName = extBosses[raid][i]
        local bossID = db.BossId[raid][bossName]
        local difficulties = playerTable[bossID]
        local maxDifficulty = 0
        local lineLeft = ""
        local lineRight = ""

        -- If there is an error with line 55, expecting table got nil, uncomment bellow lines
        -- print("---------- " .. bossName .. " ----------")
        -- DevTools_Dump(difficulties)

        if (difficulties) then
            local datas = difficulties[3]
            if (datas) then
                lineLeft, lineRight, maxDifficulty = ProcessLines(lineLeft, lineRight, maxDifficulty, datas, 3, bossName)
            end
            datas = difficulties[4]
            if (datas) then
            lineLeft, lineRight, maxDifficulty = ProcessLines(lineLeft, lineRight, maxDifficulty, datas, 4, bossName)
            end
            datas = difficulties[5]
            if (datas) then
            lineLeft, lineRight, maxDifficulty = ProcessLines(lineLeft, lineRight, maxDifficulty, datas, 5, bossName)
            end
        end
        if lineLeft == "" then
            frame:AddDoubleLine(colors.grey .. "-  " .. bossName, "")
        else
            frame:AddDoubleLine(lineLeft, lineRight)
        end
    end
end

local function InitAddon(unitName, unitRealm)
    local frame = WarLogsFrame or CreateFrame("GameTooltip", "WarLogsFrame", PVEFrame, "GameTooltipTemplate")
    frame:SetOwner(PVEFrame, "ANCHOR_NONE")

    if (not charData[unitRealm] or not charData[unitRealm][unitName]) then
        return frame
    end

    if (IsAddOnLoaded("RaiderIO")) then
        local ri = RaiderIO_ProfileTooltip
        frame:SetPoint("TOPLEFT", ri, "TOPRIGHT", 0, 0)
    else
        frame:ClearAllPoints()
        frame:SetPoint("TOPLEFT", PVEFrame, "TOPRIGHT", 0, 0)
    end

    if (unitName == "Niisha" and unitRealm == "Temple noir") or (unitName == "Tempaxe" and unitRealm == "Temple noir") or (unitName == "Mío" and unitRealm == "Hyjal") then
        frame:AddLine(colors.green .. unitName .. colors.white .. " - " .. colors.blue .. unitRealm .. colors.white .. " | " .. colors.purple .. "Author")
    else
        frame:AddLine(colors.white .. unitName .. " - " .. unitRealm)
    end
    frame:AddLine(" ")

    if not (C_LFGList.GetActiveEntryInfo() == nil) and not (unitName == playerName and unitRealm == playerRealm) then
        local infos = C_LFGList.GetActiveEntryInfo()
        local it = C_LFGList.GetActivityInfoTable(infos.activityID)
        local grpID = it.groupFinderActivityGroupID

        local englishName = db.GrpID[grpID]
        local raidID = db.RaidID[englishName]

        if (not IsAltKeyDown()) and not (englishName == nil) then
            ProcessRaid(raidID, frame, unitRealm, unitName, false)
        else
            ProcessRaid(29, frame, unitRealm, unitName)
            ProcessRaid(28, frame, unitRealm, unitName, true)
            ProcessRaid(26, frame, unitRealm, unitName, true)
        end
    else
        ProcessRaid(29, frame, unitRealm, unitName)
        ProcessRaid(28, frame, unitRealm, unitName, true)
        ProcessRaid(26, frame, unitRealm, unitName, true)
    end

    return frame
end

local pveFrameIsShown = false -- Check weather the PVEFrame is shown or not
-- When opening the PVEFrame, show the tooltip for the player
PVEFrame:HookScript(
    "OnShow",
    function()
        local tt = InitAddon(playerName, playerRealm)
        tt:Show()
        pveFrameIsShown = true
    end
)
-- We should hide the tooltip when the PVEFrame is closed
PVEFrame:HookScript(
    "OnHide",
    function()
        local tt = InitAddon(playerName, playerRealm)
        tt:Hide()
        pveFrameIsShown = false
    end
)

-- Everytime a GameTooltip is shown, we check if it's a player tooltip
-- If it's a player tooltip, we extract player name and realm
-- Then, we check if the player is in a LFG group (that would mean that this tooltip is for a player applying to a group)
-- If he is, we check try to show the tooltip for the applying member
GameTooltip:HookScript(
    "OnShow",
    function()
        -- TODO: Issue if the realm is the same as the current player
        local name, realm = _G["GameTooltipTextLeft1"]:GetText():match("(.+)%-(.+)")
        if (pveFrameIsShown and (C_LFGList.GetActiveEntryInfo() ~= nil) and (name and realm)) then
            local containsSpace = name:find(" ")
            if (not containsSpace) then
                local id = C_LFGList.GetActiveEntryInfo().activityID
                local difficulty = string.sub(C_LFGList.GetActivityInfoTable(id).shortName, 1, 1)
                local tt = InitAddon(name, realm)
                if (not IsAddOnLoaded("RaiderIO")) then
                    tt:ClearAllPoints()
                    tt:SetPoint("TOPLEFT", GameTooltip, "TOPRIGHT", 0, 0)
                end
                if (name and realm) then
                    tt:Show()
                else
                    tt:Hide()
                end
            end
        end
    end
)
GameTooltip:HookScript(
    "OnHide",
    function()
        local tt = InitAddon(playerName, playerRealm)
        if (pveFrameIsShown) then
            tt:Show()
        else
            tt:Hide()
        end
    end
)

-- Update the tooltip if the player use LALT modifier
-- It's a big fat ugly copy/paste of the GameTooltip:HookScript("OnShow", function() ... end)
-- Maybe we should factorize this a bit
local function OnModifierStateChange(self, event, key, status)
    if (key == "LALT") then
        -- TODO: Issue if the realm is the same as the current player
        local name, realm = _G["GameTooltipTextLeft1"]:GetText():match("(.+)%-(.+)")
        if (pveFrameIsShown and (C_LFGList.GetActiveEntryInfo() ~= nil) and (name and realm)) then
            local containsSpace = name:find(" ")
            if (not containsSpace) then
                local id = C_LFGList.GetActiveEntryInfo().activityID
                local difficulty = string.sub(C_LFGList.GetActivityInfoTable(id).shortName, 1, 1)
                local tt = InitAddon(name, realm)
                if (not IsAddOnLoaded("RaiderIO")) then
                    tt:ClearAllPoints()
                    tt:SetPoint("TOPLEFT", GameTooltip, "TOPRIGHT", 0, 0)
                end
                if (name and realm) then
                    tt:Show()
                else
                    tt:Hide()
                end
            end
        else
            local tt = InitAddon(playerName, playerRealm)
            tt:Hide()
        end
    end
end

-- Register event to check if the player use LALT modifier
local f = CreateFrame("Frame")
f:RegisterEvent("MODIFIER_STATE_CHANGED")
f:SetScript("OnEvent", OnModifierStateChange)
