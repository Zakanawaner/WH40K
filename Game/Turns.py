from statemachine import StateMachine, State


class PlayerTurn(StateMachine):
    CommandPhase = State('Command Phase', initial=True)
    MovementPhase = State('Movement Phase')
    PsychicPhase = State('Psychic Phase')
    ShootingPhase = State('Shooting Phase')
    ChargePhase = State('Charge Phase')
    FightPhase = State('Fights Phase')
    MoralePhase = State('Morale Phase')
    EndOfTurn = State('End of Turn')

    endOfCommand = CommandPhase.to(MovementPhase)
    endOfMovement = MovementPhase.to(PsychicPhase)
    endOfPsychic = PsychicPhase.to(ShootingPhase)
    endOfShooting = ShootingPhase.to(ChargePhase)
    endOfCharge = ChargePhase.to(FightPhase)
    endOfFight = FightPhase.to(MoralePhase)
    endOfMorale = MoralePhase.to(EndOfTurn)
    endOfTurn = EndOfTurn.to(CommandPhase)
