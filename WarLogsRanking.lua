local addonName, ns = ...

local db = ns.db

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

local extBosses = db["Extension"]["Shadowlands"]
local playerName = GetUnitName("player")
local playerRealm = GetRealmName()

local function ternary(condition, ifTrue, ifFalse)
    if condition then
        return ifTrue
    else
        return ifFalse
    end
end

local function InitAddon(unitName, unitRealm)
    local frame = WarLogsRanking or CreateFrame("GameTooltip", "WarLogsRanking", PVEFrame, "GameTooltipTemplate")
    frame:SetOwner(PVEFrame, "ANCHOR_NONE")

    if (IsAddOnLoaded("RaiderIO")) then
        local ri = RaiderIO_ProfileTooltip
        frame:SetPoint("TOPLEFT", ri, "TOPRIGHT", 0, 0)
    else
        frame:ClearAllPoints()
        frame:SetPoint("TOPLEFT", PVEFrame, "TOPRIGHT", 0, 0)
    end

    frame:AddLine(colors.white .. unitName .. " - " .. unitRealm)
    frame:AddLine(" ")

    local raidCount = 0
    for raid, bosses in pairs(db[string.lower(unitRealm)][unitName]) do
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

local pveFrameIsShown = false
PVEFrame:HookScript(
    "OnShow",
    function()
        local tt = InitAddon(playerName, playerRealm)
        tt:Show()
        pveFrameIsShown = true
    end
)
PVEFrame:HookScript(
    "OnHide",
    function()
        -- local tt = InitAddon(playerName, playerRealm)
        -- tt:Hide()
        pveFrameIsShown = false
    end
)

GameTooltip:HookScript(
    "OnShow",
    function()
        local name, realm = _G["GameTooltipTextLeft1"]:GetText():match("(.+)%-(.+)")
        if (pveFrameIsShown and (name and realm)) then
            local tt = InitAddon("Niisha", "Temple Noir")
            tt:ClearAllPoints()
            tt:SetPoint("TOPLEFT", GameTooltip, "TOPRIGHT", 0, 0)
            tt:Show()
        end
    end
)
GameTooltip:HookScript(
    "OnHide",
    function()
        local tt = InitAddon(playerName, playerRealm)
    end
)
