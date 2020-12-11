from statemachine import StateMachine, State


class MissionTurns(StateMachine):
    MusterArmies = State('Muster Armies', initial=True)
    MissionBriefing = State('Mission Briefing')
    CreateBattlefield = State('Create Battlefield')
    DeployForces = State('Deploy Forces')
    DetermineFirstTurn = State('Determine First Turn')
    ResolvePreBattleRules = State('Resolve Pre-Battle Rules')
    Battle = State('Battle')
    EndOfBattle = State('End of Battle')
    DetermineVictor = State('Determine Victor')
    EndOfMission = State('End of Mission')

    endOfMusterArmies = MusterArmies.to(MissionBriefing)
    endOfMissionBriefing = MissionBriefing.to(CreateBattlefield)
    endOfCreateBattlefield = CreateBattlefield.to(DeployForces)
    endOfDeployForces = DeployForces.to(DetermineFirstTurn)
    endOfDetermineFirstTurn = DetermineFirstTurn.to(ResolvePreBattleRules)
    endOfResolvePreBattleRules = ResolvePreBattleRules.to(Battle)
    endOfBattlePhase = Battle.to(EndOfBattle)
    endOfEndOfBattle = EndOfBattle.to(DetermineVictor)
    endOfDetermineVictor = DetermineVictor.to(EndOfMission)


class Mission:
    def __init__(self):
        self.Turn = MissionTurns()
        # Muster armies conditions
        self.DefinedPlayers = False
        self.DefinedBattleSize = False
        self.DefinedArmies = False
        self.DefinedWarlord = False
        # Mission briefing conditions
        self.DefinedMissionObjectives = False
        # Create battlefield conditions
        self.DefinedBoardSize = False
        self.DefineBoardTerrain = False
        self.DefinedObjectives = False
        # Deploy forces conditions
        self.ForcesDeployed = False
        # Determine first turn conditions
        self.DeterminedFirstTurn = False
        # Resolve pre-battle rules
        self.PreBattleRulesResolved = False
        # Battle conditions
        self.Player1Destroyed = False
        self.Player2Destroyed = False
        self.Turn5Finished = False
        # End of battle conditions
        # Determine victor conditions
        self.CountedForWinner = False
        # End of mission conditions

    def check(self):
        if self.Turn.is_MusterArmies:
            if self.DefinedPlayers and self.DefinedBattleSize and self.DefinedArmies and self.DefinedWarlord:
                self.Turn.endOfMusterArmies()
        if self.Turn.is_MissionBriefing:
            if self.DefinedMissionObjectives:
                self.Turn.endOfMissionBriefing()
        if self.Turn.is_CreateBattlefield:
            if self.DefinedBoardSize and self.DefineBoardTerrain and self.DefinedObjectives:
                self.Turn.endOfCreateBattlefield()
        if self.Turn.is_DeployForces:
            if self.ForcesDeployed:
                self.Turn.endOfDeployForces()
        if self.Turn.is_DetermineFirstTurn:
            if self.DeterminedFirstTurn:
                self.Turn.endOfDetermineFirstTurn()
        if self.Turn.is_ResolvePreBattleRules:
            if self.PreBattleRulesResolved:
                self.Turn.endOfResolvePreBattleRules()
        if self.Turn.is_Battle:
            if self.Player1Destroyed or self.Player2Destroyed or self.Turn5Finished:
                self.Turn.endOfBattlePhase()
                self.Turn.endOfEndOfBattle()
        if self.Turn.is_DetermineVictor:
            if self.CountedForWinner:
                self.Turn.endOfDetermineVictor()

    def players_defined(self):
        self.DefinedPlayers = True

    def battle_size_defined(self):
        self.DefinedBattleSize = True

    def armies_defined(self):
        self.DefinedArmies = False

    def warlord_defined(self):
        self.DefinedWarlord = False

    def mission_objectives_defined(self):
        self.DefinedMissionObjectives = False

    def board_size_defined(self):
        self.DefinedBoardSize = False

    def terrain_defined(self):
        self.DefineBoardTerrain = False

    def objectives_defined(self):
        self.DefinedObjectives = False

    def forces_deployed(self):
        self.ForcesDeployed = False

    def first_turn_determined(self):
        self.DeterminedFirstTurn = False

    def battle_rules_resolved(self):
        self.PreBattleRulesResolved = False

    def player_1_destroyed(self):
        self.Player1Destroyed = False

    def player_2_destroyed(self):
        self.Player2Destroyed = False

    def turn_5_finished(self):
        self.Turn5Finished = False

    def counted_for_winner(self):
        self.CountedForWinner = False


class OnlyWar(Mission):
    def __init__(self):
        super().__init__()
        self.BattleSize = ''
        self.Battlefield = (0, 0)

    def set_combat_patrol(self):
        self.BattleSize = 'CombatPatrol'
        self.battle_size_defined()
        self.Battlefield = (44, 30)
        self.board_size_defined()

    def set_incursion(self):
        self.BattleSize = 'Incursion'
        self.battle_size_defined()
        self.Battlefield = (44, 30)
        self.board_size_defined()

    def set_strike_force(self):
        self.BattleSize = 'StrikeForce'
        self.battle_size_defined()
        self.Battlefield = (44, 60)
        self.board_size_defined()

    def set_onslaught(self):
        self.BattleSize = 'Onslaught'
        self.battle_size_defined()
        self.Battlefield = (44, 90)
        self.board_size_defined()
