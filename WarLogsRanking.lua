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
    for raid, bosses in pairs(db["Temple Noir"]["Niisha"]) do
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

GameTooltip:HookScript(
    "OnShow",
    function()
        -- Check if _G["GameTooltipTextLeft1"]:GetText() match with pattern "name-realm"
        local matchPatern = _G["GameTooltipTextLeft1"]:GetText() and string.match(_G["GameTooltipTextLeft1"]:GetText(), "^(%a+)-(%a+)$")
        if (matchPatern) then
            local tt = InitAddon()
            tt:ClearAllPoints()
            tt:SetPoint("TOPLEFT", GameTooltip, "TOPRIGHT", 0, 0)
            tt:Show()
        end
    end
)
