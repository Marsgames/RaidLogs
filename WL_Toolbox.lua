WLToolbox = {}
WLToolbox.__index = WLToolbox

local _, ns = ...
local db = ns.db
local convTable = {}

-- Colors used in the addon (principally for the rank percentages)
WLToolbox.colors = {
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

-- Ternary function to reduce the number of lines in the code
-- Maybe who should use something like a quarternary function to reduce the number of lines even more?
-- Maybe we should use a ToolBox namespace for this?
function WLToolbox:Ternary(condition, ifTrue, ifFalse)
    if condition then
        return ifTrue
    else
        return ifFalse
    end
end
-- TODO: Create something that looks like a switch/case statement

function WLToolbox:SplitDatasForPlayer(name, realm)
    if (realm == nil) then
        realm = playerRealm
    end
    if (charData[realm] == nil or charData[realm][name] == nil) then
        return {}
    end

    local playerDatas = charData[realm][name]
    local playerTable = {}

    -- new data format = "encounterType:rankPercent:average:killCount/encounterType2:..."
    local raids = {strsplit("/", playerDatas)}

    for _, boss in pairs(raids) do
        local splitTable = {strsplit(":", boss)}

        local encounterType = tonumber(splitTable[1])
        local rank = tonumber(splitTable[2])
        local killCount = tonumber(splitTable[3])
        local bossId = convTable[encounterType]["encounter"]
        local bossDifficulty = convTable[encounterType]["difficulty"]
        local metric = convTable[encounterType]["metric"]

        if playerTable[bossId] == nil then
            playerTable[bossId] = {}
        end
        playerTable[bossId][bossDifficulty] = {
            ["metric"] = metric,
            ["rank"] = rank,
            ["killCount"] = killCount
        }
    end

    return playerTable
end

function WLToolbox:CalculateAverageForPlayer(name, realm, raid)
    playerDatas = WLToolbox:SplitDatasForPlayer(name, realm)
    local difficulty = ""
    local raidName = db.RaidName[raid]
    local score = 0
    local metric = ""

    local average = 0
    local count = 0

    local difficulties = {5, 4, 3}
    local bossIDs = {}
    for _, bossID in pairs(db.BossId[raid]) do
        table.insert(bossIDs, bossID)
    end
    for _, diff in pairs(difficulties) do
        for _, bossID in pairs(bossIDs) do
            if (playerDatas[bossID] ~= nil and playerDatas[bossID][diff] ~= nil) then
                average = average + playerDatas[bossID][diff]["rank"]
                count = count + 1
            end
        end
        if (count > 0) then
            difficulty = diff
            score = average / count
            if (bossIDs[1] and playerDatas[bossIDs[1]] and playerDatas[bossIDs[1]][diff] and playerDatas[bossIDs[1]][diff]["metric"]) then
                metric = playerDatas[bossIDs[1]][diff]["metric"]
            end
            return difficulty, raidName, score
        end
    end

    return difficulty, raidName, score
end

function WLToolbox:ScoreToColor(score)
    score = tonumber(score)
    return WLToolbox:Ternary(score < 25, WLToolbox.colors["grey"], WLToolbox:Ternary(score < 50, WLToolbox.colors["green"], WLToolbox:Ternary(score < 75, WLToolbox.colors["blue"], WLToolbox:Ternary(score < 95, WLToolbox.colors["purple"], WLToolbox:Ternary(score < 99, WLToolbox.colors.orange, WLToolbox:Ternary(score < 100, WLToolbox.colors.pink, WLToolbox.colors.herloom))))))
end

function WLToolbox:DifficultyToName(difficulty)
    return WLToolbox:Ternary(difficulty == 5, "M", WLToolbox:Ternary(difficulty == 4, "H", "N"))
end

function WLToolbox:DifficultyToColor(difficulty)
    if (type(difficulty) == "string") then
        return WLToolbox:Ternary(difficulty == "M", WLToolbox.colors["purple"], WLToolbox:Ternary(difficulty == "H", WLToolbox.colors["blue"], WLToolbox.colors["green"]))
    end
    return WLToolbox:Ternary(difficulty == 5, WLToolbox.colors["purple"], WLToolbox:Ternary(difficulty == 4, WLToolbox.colors["blue"], WLToolbox.colors["green"]))
end

function WLToolbox:GetMetricFromPlayertable(playertable)
    local dps = 0
    local hps = 0

    for _, boss in pairs(playertable) do
        for _, difficulty in pairs(boss) do
            if (difficulty["metric"] == "dps") then
                dps = dps + 1
            elseif (difficulty["metric"] == "hps") then
                hps = hps + 1
            end
        end
    end

    if (dps > hps) then
        return "dps"
    end
    return "hps"
end

function WLToolbox:MetricToIcon(metric)
    return WLToolbox:Ternary(metric == "dps", "|A:4257:19:19|a", WLToolbox:Ternary(metric == "hps", "|A:4258:19:19|a", "|A:4259:19:19|a"))
end

function WLToolbox:Contains(table, element)
    for _, value in pairs(table) do
        if value == element then
            return true
        end
    end
    return false
end

function WLToolbox:GetLastRaidNumber(raids)
    local lastRaid = nil
    for raid, _ in pairs(raids) do
        lastRaid = raid
    end
    return lastRaid
end

function WLToolbox:GetAllRaidsNumber(extension)
    local raids = {}
    for raidNumber, _ in pairs(extension) do
        table.insert(raids, raidNumber)
    end
    table.sort(raids)
    return raids
end

---------- Events ----------
local addonLoaded = false
local function OnAddonLoaded(_, _, addonName)
    if addonLoaded then
        do return end
    end

    if (addonName == "WarLogs_DB_EU") or (C_AddOns.IsAddOnLoaded("WarLogs_DB_EU")) then
        WarLogsAddCharsToDB(_G["WL_DB_EU"])
        convTable = _G["EU_gnippam"]
        addonLoaded = true
    elseif (addonName == "WarLogs_DB_US") or (C_AddOns.IsAddOnLoaded("WarLogs_DB_US")) then
        WarLogsAddCharsToDB(_G["WL_DB_US"])
        convTable = _G["US_gnippam"]
        addonLoaded = true
    elseif (addonName == "WarLogs_DB_CN") or (C_AddOns.IsAddOnLoaded("WarLogs_DB_CN")) then
        WarLogsAddCharsToDB(_G["WL_DB_CN"])
        convTable = _G["CN_gnippam"]
            addonLoaded = true
    elseif (addonName == "WarLogs_DB_KR") or (C_AddOns.IsAddOnLoaded("WarLogs_DB_KR")) then
        WarLogsAddCharsToDB(_G["WL_DB_KR"])
        convTable = _G["KR_gnippam"]
            addonLoaded = true
    elseif (addonName == "WarLogs_DB_TW") or (C_AddOns.IsAddOnLoaded("WarLogs_DB_TW")) then
        WarLogsAddCharsToDB(_G["WL_DB_TW"])
        convTable = _G["TW_gnippam"]
            addonLoaded = true
    end
end

local f = CreateFrame("Frame")
f:RegisterEvent("ADDON_LOADED")
f:SetScript("OnEvent", OnAddonLoaded)
---------- Events ----------