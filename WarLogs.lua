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

local function ProcessRaid(raid, frame, unitRealm, unitName, addLineBefore)
    local raidName = db.RaidName[raid]
    local bosses = db.char[unitRealm][unitName][raid]
    if (bosses) then
        if (addLineBefore) then
            frame:AddLine(" ")
        end
        local role = bosses[db.BossId[raid][extBosses[raid][0]]][3]["metric"]
        local TankIcon = "|A:4259:19:19|a" -- Should not appear
        local HealerIcon = "|A:4258:19:19|a"
        local DPSIcon = "|A:4257:19:19|a"
        frame:AddDoubleLine(raidName, ternary(role == "dps", DPSIcon, ternary(role == "hps", HealerIcon, TankIcon)))

        for i = 0, #extBosses[raid] do
            local bossName = extBosses[raid][i]
            local bossID = db.BossId[raid][bossName]
            local difficulties = bosses[bossID]
            local maxDifficulty = 0
            local lineLeft = ""
            local lineRight = ""

            -- If there is an error with line 55, expecting table got nil, uncomment bellow lines
            -- print("---------- " .. bossName .. " ----------")
            -- DevTools_Dump(difficulties)

            if (difficulties) then
                for difficulty, datas in pairs(difficulties) do
                    local scoreColor = ternary(datas["best"] < 25, colors["grey"], ternary(datas["best"] < 50, colors["green"], ternary(datas["best"] < 75, colors["blue"], ternary(datas["best"] < 95, colors["purple"], ternary(datas["best"] < 99, colors["orange"], ternary(datas["best"] < 100, colors.pink, colors["herloom"]))))))
                    local diffName = ternary(difficulty == 5, "M", ternary(difficulty == 4, "H", "N"))
                    if (difficulty > maxDifficulty and datas["best"] > 0) then
                        maxDifficulty = difficulty
                        local diffColor = ternary(diffName == "N", colors["green"], ternary(diffName == "H", colors["blue"], colors["purple"]))
                        lineLeft = diffColor .. diffName .. " " .. colors["white"] .. bossName
                        lineRight = scoreColor .. datas["best"] .. "%"
                    end
                end
            end
            if lineLeft == "" then
                frame:AddDoubleLine(colors.grey .. "-  " .. bossName, "")
            else
                frame:AddDoubleLine(lineLeft, lineRight)
            end
        end
    end
end

local function InitAddon(unitName, unitRealm)
    local frame = WarLogs or CreateFrame("GameTooltip", "WarLogs", PVEFrame, "GameTooltipTemplate")
    frame:SetOwner(PVEFrame, "ANCHOR_NONE")

    if (not db.char[unitRealm] or not db.char[unitRealm][unitName]) then
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
        -- TODO: Issue if the realm is the same as the current player
        local name, realm = _G["GameTooltipTextLeft1"]:GetText():match("(.+)%-(.+)")
        -- Name contains space
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
        end
    end
)

local function OnModifierStateChange(self, event, key, status)
    if (key == "LALT") then
        local tt = InitAddon(playerName, playerRealm)
        if (pveFrameIsShown) then
            tt:Show()
        else
            tt:Hide()
        end
    end
end
local f = CreateFrame("Frame")
f:RegisterEvent("MODIFIER_STATE_CHANGED")
f:SetScript("OnEvent", OnModifierStateChange)

-- local hooked = {}

-- local function OnEnterHook(self)
--     print("On a quelque chose, c'est déjà ça")
--     if not self.tooltip then
--         -- The original OnEnter script doesn't show a tooltip in this case,
--         -- so we should exit here, instead of adding text to a tooltip that
--         -- isn't shown or, worse, is currently shown by something else.
--         return
--     end

--     print("hop hop add line tooltip")
--     GameTooltip:AddLine("hello world")
--     GameTooltip:Show()
-- end

-- hooksecurefunc(
--     "LFGListApplicationViewer_UpdateResults",
--     function(self)
--         for k, v in pairs(self) do
--             print(k, v)
--         end
--         -- DevTools_Dump(self.scrollBox)
--         -- local buttons = self.ScrollFrame.buttons
--         -- for i = 1, #buttons do
--         --     local button = buttons[i]
--         --     if not hooked[button] then
--         --         button:HookScript("OnEnter", OnEnterHook)
--         --         hooked[button] = true
--         --     end
--         -- end
--     end
-- )
