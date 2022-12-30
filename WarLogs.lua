local addonName, ns = ...

local db = ns.db
charData = {}

-- Create public function to populate the db (called from db/WarLogs_DB_XX.lua, but as these files are
--      enabled with "another addon" they do not have the same namespace as this file)
function WarLogsAddCharsToDB(charsTable)
    -- append charsTable to db.char
    for k, v in pairs(charsTable) do
        charData[k] = v
    end
end

-- Load bosses data for current expansion + get player name and realm
local extBosses = db["Extension"]["Dragonflight"]
local playerName = GetUnitName("player")
local playerRealm = GetRealmName()

-- Given a data set, return a tooltip double line formatted string
local function ProcessLines(lineLeft, lineRight, maxDifficulty, datas, difficulty, bossName)
    -- Get color for the rank percentage and difficulty "name"
    local scoreColor = WLToolbox:ScoreToColor(datas["rank"])
    local diffName = WLToolbox:DifficultyToName(difficulty)

    -- If there is a rank for this difficulty, and the difficulty is higher than the previous tested ones, add a line to the tooltip
    if (difficulty > maxDifficulty and datas["rank"] > 0) then
        maxDifficulty = difficulty
        local diffColor = WLToolbox:Ternary(diffName == "N", WLToolbox.colors["green"], WLToolbox:Ternary(diffName == "H", WLToolbox.colors["blue"], WLToolbox.colors["purple"]))
        lineLeft = diffColor .. diffName .. " " .. WLToolbox.colors["white"] .. bossName
        lineRight = scoreColor .. datas["rank"] .. "%"
    end
    return lineLeft, lineRight, maxDifficulty
end

-- If there is no data for a raid, we show every boss greyed out
local function ProcessEmptyRaid(raid, frame, addLineBefore)
    local raidName = db.RaidName[raid]
    if (addLineBefore) then
        frame:AddLine(" ")
    end
    frame:AddDoubleLine(raidName, WLToolbox.colors.grey .. "No data")
    for i = 0, #extBosses[raid] do
        local bossName = extBosses[raid][i]
        frame:AddDoubleLine(WLToolbox.colors.grey .. "-  " .. bossName, "")
    end
end

local function ProcessRaid(raid, frame, unitRealm, unitName, addLineBefore)
    local raidName = db.RaidName[raid]
    if (not charData[unitRealm]) or (not charData[unitRealm][unitName]) then
        ProcessEmptyRaid(raid, frame, addLineBefore)
        return
    end
    -- local playerDatas = charData[unitRealm][unitName]
    local playerTable = WLToolbox:SplitDatasForPlayer(unitName, unitRealm)
    local metric = WLToolbox:GetMetricFromPlayertable(playerTable)

    if (addLineBefore) then
        frame:AddLine(" ")
    end

    --local TankIcon = "|A:4259:19:19|a" -- Should not appear
    frame:AddDoubleLine(raidName, WLToolbox:MetricToIcon(metric))

    if (not extBosses[raid]) then
        return
    end
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
            frame:AddDoubleLine(WLToolbox.colors.grey .. "-  " .. bossName, "")
        else
            frame:AddDoubleLine(lineLeft, lineRight)
        end
    end
end

-- This function shows the tooltip for a player when the PVEFrame is opened.
-- Whether it is for the player datas or an applier
local function ProcessPVEFrameTooltip(unitName, unitRealm)
    local frame = WarLogsFrame or CreateFrame("GameTooltip", "WarLogsFrame", PVEFrame, "GameTooltipTemplate")
    frame:SetOwner(PVEFrame, "ANCHOR_NONE")

    if (IsAddOnLoaded("RaiderIO")) then
        local ri = RaiderIO_ProfileTooltip
        frame:SetPoint("TOPLEFT", ri, "TOPRIGHT", 0, 0)
    else
        local xOffset = 0
        -- TODO: Tester ce code quand une première instance sort en LFR (il faudra surement tweaker l'offset)
        -- if (IsAddOnLoaded("GearHelper")) then
        --     local buttons = lfrCheckButton_GlobalName
        --     if (buttons) then
        --         xOffset = 20
        --     end
        -- end
        -- TODO: Remove offset when hidding the LFR button
        frame:ClearAllPoints()
        frame:SetPoint("TOPLEFT", PVEFrame, "TOPRIGHT", xOffset, 0)
    end

    if (unitName == "Niisha" and unitRealm == "Temple noir") or (unitName == "Tempaxe" and unitRealm == "Temple noir") or (unitName == "Mío" and unitRealm == "Hyjal") then
        frame:AddLine(WLToolbox.colors.green .. unitName .. WLToolbox.colors.white .. " - " .. WLToolbox.colors.blue .. unitRealm .. WLToolbox.colors.white .. " | " .. WLToolbox.colors.purple .. "Author")
    else
        frame:AddLine(WLToolbox.colors.white .. unitName .. " - " .. unitRealm)
    end
    frame:AddLine(" ")

    if (not charData[unitRealm] or not charData[unitRealm][unitName]) then
        ProcessEmptyRaid(31, frame, false)
        return frame
    end

    if not (C_LFGList.GetActiveEntryInfo() == nil) and not (unitName == playerName and unitRealm == playerRealm) then
        local infos = C_LFGList.GetActiveEntryInfo()
        local it = C_LFGList.GetActivityInfoTable(infos.activityID)
        local grpID = it.groupFinderActivityGroupID

        local englishName = db.GrpID[grpID]
        local raidID = db.RaidID[englishName]

        if (not IsAltKeyDown()) and not (englishName == nil) then
            ProcessRaid(raidID, frame, unitRealm, unitName, false)
        else
            ProcessRaid(31, frame, unitRealm, unitName)
        end
    else
        ProcessRaid(31, frame, unitRealm, unitName)
    end

    return frame
end

-- This function shows average ranking for each raid on player tooltip
--[[
        Niisha - Temple noir

        WarLogs Average Ranking
        H Vault of the Incarnates   hps 69%
        M Tomb of Sargeras          dps 99%
    ]]
local function ProcessOveringTooltip(name, realm)
    local tooltipFirstLine = _G["GameTooltipTextLeft1"]:GetText()
    if (tooltipFirstLine == nil) then
        return
    end
    GameTooltip:AddLine(" ")
    GameTooltip:AddLine("WarLogs Average Ranking")

    local raidIDs = {31}
    local playerDatas = WLToolbox:SplitDatasForPlayer(name, realm)
    for i = 1, #raidIDs do
        local raidID = raidIDs[i]
        local difficulty, raidName, score, metric = WLToolbox:CalculateAverageForPlayer(name, realm, raidID)
        metric = WLToolbox:GetMetricFromPlayertable(playerDatas)

        if (score > 0) then
            local difficulty = (WLToolbox:DifficultyToColor(difficulty) .. WLToolbox:DifficultyToName(difficulty))
            local raidName = (WLToolbox.colors.white .. raidName)
            score = string.sub(score, 1, 4)
            local score = (WLToolbox:ScoreToColor(score) .. score .. "%")
            local metricIcon = WLToolbox:MetricToIcon(metric)
            GameTooltip:AddDoubleLine(difficulty .. " " .. raidName, metricIcon .. " " .. score)
        else
            GameTooltip:AddDoubleLine(WLToolbox.colors.grey .. "- " .. raidName, WLToolbox.colors.grey .. "No data")
        end
    end
end

local pveFrameIsShown = false -- Check weather the PVEFrame is shown or not
-- When opening the PVEFrame, show the tooltip for the player
PVEFrame:HookScript(
    "OnShow",
    function()
        local tt = ProcessPVEFrameTooltip(playerName, playerRealm)
        tt:Show()
        pveFrameIsShown = true
    end
)
-- We should hide the tooltip when the PVEFrame is closed
PVEFrame:HookScript(
    "OnHide",
    function()
        local tt = ProcessPVEFrameTooltip(playerName, playerRealm)
        tt:Hide()
        pveFrameIsShown = false
    end
)

-- Everytime a GameTooltip is shown, we check if it's a player tooltip
-- If it's a player tooltip, we extract player name and realm
-- Then, we check if the player is in a LFG group (that would mean that this tooltip is for a player applying to a group)
-- If he is, we check try to show the tooltip for the applying member
local lastPlayerUpdated = ""
GameTooltip:HookScript(
    "OnShow",
    function()
        -- local mouseoverName, source, guid = GameTooltip:GetUnit()
        -- if (mouseoverName ~= nil and guid:find("Player")) then
        --     ProcessOveringTooltip(mouseoverName)
        -- else
        -- TODO: Issue if the realm is the same as the current player
        local name, realm = _G["GameTooltipTextLeft1"]:GetText():match("(.+)%-(.+)")
        if (pveFrameIsShown and (C_LFGList.GetActiveEntryInfo() ~= nil) and (name and realm)) then
            local containsSpace = name:find(" ")
            if (not containsSpace) then
                local id = C_LFGList.GetActiveEntryInfo().activityID
                local difficulty = string.sub(C_LFGList.GetActivityInfoTable(id).shortName, 1, 1)
                local tt = ProcessPVEFrameTooltip(name, realm)
                if (name and realm) then
                    tt:Show()
                else
                    tt:Hide()
                end
            end
        end
        -- end
    end
)
GameTooltip:HookScript(
    "OnHide",
    function()
        local tt = ProcessPVEFrameTooltip(playerName, playerRealm)
        if (pveFrameIsShown) then
            tt:Show()
        else
            tt:Hide()
        end
        lastPlayerUpdated = ""
    end
)

--- When the player is overing a unit, add average ranking to the tooltip
local function OnTooltipSetUnit(tooltip, data)
    if (data.guid:find("Player") == nil) then
        return
    end
    local name = tooltip:GetUnit()
    local firstLine = data.lines[1].leftText
    -- if there is no "-" in the first line, we add it
    if (firstLine:find("-") == nil) then
        firstLine = firstLine .. "-" .. playerRealm
    end
    local _, realm = firstLine:match("(.+)%-(.+)")

    ProcessOveringTooltip(name, realm)
end
TooltipDataProcessor.AddTooltipPostCall(Enum.TooltipDataType.Unit, OnTooltipSetUnit)
---

--- Show different datas ong LFGList for raid or for other activities
local function OnLFGListTooltip(gametooltip, resultID)
    local entry = C_LFGList.GetSearchResultInfo(resultID)
    if (not entry) or (not entry.leaderName) then
        return
    end
    local name, realm = entry.leaderName:match("(.+)%-(.+)")
    -- if (name == nil) then
    --     name = playerName
    -- end
    if (realm == nil) then
        realm = playerRealm
    end

    local grpID = C_LFGList.GetActivityInfoTable(entry.activityID).groupFinderActivityGroupID

    if (db.GrpID[grpID]) then
        ProcessRaid(db.GrpID[grpID].RaidID, gametooltip, name, realm, true)
    else
        ProcessOveringTooltip(name, realm)
    end
end
hooksecurefunc("LFGListUtil_SetSearchEntryTooltip", OnLFGListTooltip)
---

-- Update the tooltip if the player use LALT modifier
-- It's a big fat ugly copy/paste of the GameTooltip:HookScript("OnShow", function() ... end)
-- Maybe we should factorize this a bit
local function OnModifierStateChange(self, event, key, status)
    if (key == "LALT") then
        -- TODO: Issue if the realm is the same as the current player
        if (_G["GameTooltipTextLeft1"]) then
            local text = _G["GameTooltipTextLeft1"]:GetText()
            if (text) then
                local name, realm = text:match("(.+)%-(.+)")
                if (pveFrameIsShown and (C_LFGList.GetActiveEntryInfo() ~= nil) and (name and realm)) then
                    local containsSpace = name:find(" ")
                    if (not containsSpace) then
                        local id = C_LFGList.GetActiveEntryInfo().activityID
                        local difficulty = string.sub(C_LFGList.GetActivityInfoTable(id).shortName, 1, 1)
                        local tt = ProcessPVEFrameTooltip(name, realm)
                        if (name and realm) then
                            tt:Show()
                        else
                            tt:Hide()
                        end
                    end
                else
                    local tt = ProcessPVEFrameTooltip(playerName, playerRealm)
                    tt:Hide()
                end
            end
        end
    end
end

-- Register event to check if the player use LALT modifier
local f = CreateFrame("Frame")
f:RegisterEvent("MODIFIER_STATE_CHANGED")
f:SetScript("OnEvent", OnModifierStateChange)

-- THIS IS somehow HOW RAIDER.IO IS DOING "only applyant" TOOLTIP PROCESSING
--[[
local ScrollBoxUtil do

   ScrollBoxUtil = {}

   ---@class CallbackRegistryMixin
   ---@field public RegisterCallback fun(event: string, callback: fun())

   ---@class ScrollBoxBaseMixin : CallbackRegistryMixin
   ---@field public GetFrames fun(): Frame[]
   ---@field public Update fun()

   ---@param scrollBox ScrollBoxBaseMixin
   ---@param callback fun(frames: Button[], scrollBox: ScrollBoxBaseMixin)
   function ScrollBoxUtil:OnViewFramesChanged(scrollBox, callback)
      if not scrollBox then
         return
      end
      if scrollBox.buttons then -- TODO: legacy 9.X support
         callback(scrollBox.buttons, scrollBox)
         return 1
      end
      if scrollBox.RegisterCallback then
         local frames = scrollBox:GetFrames()
         if frames and frames[1] then
            callback(frames, scrollBox)
         end
         scrollBox:RegisterCallback(ScrollBoxListMixin.Event.OnUpdate, function()
               frames = scrollBox:GetFrames()
               callback(frames, scrollBox)
         end)
         return true
      end
      return false
   end

   ---@param scrollBox ScrollBoxBaseMixin
   ---@param callback fun(self: ScrollBoxBaseMixin)
   function ScrollBoxUtil:OnViewScrollChanged(scrollBox, callback)
      if not scrollBox then
         return
      end
      local function wrappedCallback()
         callback(scrollBox)
      end
      if scrollBox.update then -- TODO: legacy 9.X support
         hooksecurefunc(scrollBox, "update", wrappedCallback)
         return 1
      end
      if scrollBox.RegisterCallback then
         scrollBox:RegisterCallback(ScrollBoxListMixin.Event.OnScroll, wrappedCallback)
         return true
      end
      return false
   end

end

local HookUtil do

   HookUtil = {}

   local hooked = {}

   ---@param frame Frame
   ---@param callback fun(self: Frame, ...)
   ---@param ... string
   function HookUtil:On(frame, callback, ...)
      local hook = hooked[frame]
      if not hook then
         hook = {}
         hooked[frame] = hook
      end
      for _, key in ipairs({...}) do
         local keyHook = hook[key]
         if not keyHook then
            keyHook = {}
            hook[key] = keyHook
         end
         if not keyHook[callback] then
            keyHook[callback] = true
            frame:HookScript(key, callback)
         end
      end
   end

   ---@param frames Frame[]
   ---@param callback fun(self: Frame, ...)
   ---@param ... string
   function HookUtil:OnAll(frames, callback, ...)
      for _, frame in ipairs(frames) do
         HookUtil:On(frame, callback, ...)
      end
   end

   ---@param object Frame[]|Frame
   ---@param map table<string, fun()>
   function HookUtil:MapOn(object, map)
      if type(object) ~= "table" then
         return
      end
      if type(object.GetObjectType) == "function" then
         for key, callback in pairs(map) do
            HookUtil:On(object, callback, key)
         end
         return 1
      end
      for key, callback in pairs(map) do
         HookUtil:OnAll(object, callback, key)
      end
      return true
   end

end

local function OnScroll()
   --print("Call when opening frame or when someone queues")
end
local function OnEnter(self)
   local applicantID = self.applicantID
   local infos = C_LFGList.GetApplicantMemberInfo(applicantID, 1)

   print(infos)
end
local function OnLeave()
end

local hookMap = { OnEnter = OnEnter, OnLeave = OnLeave }

ScrollBoxUtil:OnViewFramesChanged(LFGListFrame.ApplicationViewer.ScrollBox, function(buttons) HookUtil:MapOn(buttons, hookMap) end)
--ScrollBoxUtil:OnViewScrollChanged(LFGListFrame.ApplicationViewer.ScrollBox, OnScroll)
]] --
