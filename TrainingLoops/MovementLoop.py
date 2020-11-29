import numpy
import matplotlib.pyplot as plt


# NN  -> MoveNetwork
# Env -> GetToTheTargetIndividually
def vanilla_loop(RedAgents, GreenAgents, Env, Beginning=True, Train=True, NumEpisodes=2000, Movements=100, PlotEnable=False, Verbose=1):
    # Load the model if not the fist time working wth the model
    if not Beginning:
        RedAgents.Units[0].load_model('MoveNetwork')
    num_episodes = NumEpisodes
    Episode = 0
    red_scores, red_eps_history, red_avg_score, red_avg_movements, red_movement_array = [], [], [], [], []
    RedTurn = True
    while Episode < num_episodes:
        s_0 = Env.start(RedAgents, GreenAgents)
        Done = False
        movements = 0
        red_score = 0
        while not Done:
            movements += 1
            for i, Unit in enumerate(RedAgents.Units):
                action = Unit.choose('Move', s_0)
                s_1, r, Done = Env.step(action, i, RedAgents, RedTurn)
                if movements > Movements:
                    Done = True
                    Env.redArmyWins = False
                    r = -Env.WinningReward
                red_score += r
                RedAgents.Units[i].store_transition('Move', s_0, action, r, s_1, Done)
                s_0 = s_1
            if PlotEnable and movements <= Movements:
                Env.plot(RedAgents, GreenAgents, Episode, movements)
        if not Env.redArmyWins:
            rewards = numpy.full(movements, -Env.WinningReward, dtype=numpy.float32)
        else:
            rewards = numpy.full(movements, Env.WinningReward, dtype=numpy.float32)
        for i, Unit in enumerate(RedAgents.Units):
            red_scores.append(red_score)
            red_eps_history.append(Unit.MoveEpsilon)
            red_avg_score.append(numpy.mean(red_scores[-1000:]))
            RedAgents.Units[i].MoveRewardMemory[-len(rewards):] = rewards
            RedAgents.Units[i].learn('Move')
            if Env.redArmyWins:
                RedAgents.Units[i].epsilon_decrease('Move')
        red_movement_array.append(movements)
        red_avg_movements.append(numpy.mean(red_movement_array[-1000:]))
        if (Verbose == 1 and (Env.redArmyWins or Env.greenArmyWins)) or (Verbose == 2):
            print('Episode', Episode,
                  'RED score %.2f' % float(red_avg_score[Episode] / len(RedAgents.Units)),
                  'red epsilon %.5f' % RedAgents.Units[0].MoveEpsilon,
                  'green epsilon %.5f' % GreenAgents.Units[0].MoveEpsilon,
                  'RedAgents win in %.2f movements' % float(red_avg_movements[Episode] / len(RedAgents.Units)) if Env.redArmyWins else '')
        Episode += 1
    if not Train:
        RedAgents.Units[0].save_model('MoveNetwork')
    if not PlotEnable:
        x = [i + 1 for i in range(len(red_avg_score))]
        plt.plot(x, red_avg_score, 'r')
        plt.plot(x, red_avg_movements, 'b')
        plt.savefig('./Images/FirstApproach/Graphs/Vanilla.png')
        plt.close()


# NN  -> MoveNetworkCNN
# Env -> GetToTheTargetCNN
def cnn_loop(RedAgents, GreenAgents, Env, Beginning=True, Train=True, NumEpisodes=2000, Movements=100, PlotEnable=False, Verbose=1):
    # Load the model if not the fist time working wth the model
    if not Beginning:
        RedAgents.Units[0].load_model('MoveNetworkCNN')
    num_episodes = NumEpisodes
    Episode = 0
    red_scores, red_eps_history, red_avg_score, red_avg_movements, red_movement_array = [], [], [], [], []
    green_scores, green_eps_history, green_avg_score, green_avg_movements, green_movement_array = [], [], [], [], []
    while Episode < num_episodes:
        s_0 = Env.start(RedAgents, GreenAgents)
        Done = False
        RedTurn = True
        movements = 0
        red_score, green_score = 0, 0
        while not Done:
            movements += 1
            if PlotEnable:
                Env.plot(RedAgents, GreenAgents, Episode, movements)
            for i, Unit in enumerate(RedAgents.Units):
                action, direction, distance = Unit.choose('CNN', s_0)
                s_1, r, Done = Env.step(ActionDirection=direction,
                                        soldier=i,
                                        Army=RedAgents,
                                        redTurn=RedTurn,
                                        ActionDistance=distance)
                if movements > Movements or Env.greenArmyWins:
                    Done = True
                    Env.redArmyWins = False
                    r = -Env.WinningReward
                red_score += r
                RedAgents.Units[i].store_transition('CNN', s_0, action, r, s_1, Done)
                s_0 = s_1
            RedTurn = False
            for i, Unit in enumerate(GreenAgents.Units):
                action, direction, distance = Unit.choose('CNN', s_0)
                s_1, r, Done = Env.step(ActionDirection=direction,
                                        soldier=i,
                                        Army=GreenAgents,
                                        redTurn=RedTurn,
                                        ActionDistance=distance)
                if movements > Movements or Env.redArmyWins:
                    Done = True
                    Env.greenArmyWins = False
                    r = -Env.WinningReward
                red_score += r
                GreenAgents.Units[i].store_transition('CNN', s_0, action, r, s_1, Done)
                s_0 = s_1
            RedTurn = True
        if Env.redArmyWins:
            Env.greenArmyWins = False
        if not Env.greenArmyWins:
            rewards = numpy.full(movements, -Env.WinningReward, dtype=numpy.float32)
        else:
            rewards = numpy.full(movements, Env.WinningReward, dtype=numpy.float32)
        for i, Unit in enumerate(GreenAgents.Units):
            green_scores.append(green_score)
            green_eps_history.append(Unit.CNNEpsilon)
            green_avg_score.append(numpy.mean(green_scores[-1000:]))
            GreenAgents.Units[i].CNNRewardMemory[-len(rewards):] = rewards
            GreenAgents.Units[i].learn('CNN')
            if Env.greenArmyWins:
                GreenAgents.Units[i].epsilon_decrease('CNN')
            # elif Env.redArmyWins:
            #     GreenAgents.Units[i].epsilon_increase('CNN')
        if not Env.redArmyWins:
            rewards = numpy.full(movements, -Env.WinningReward, dtype=numpy.float32)
        else:
            rewards = numpy.full(movements, Env.WinningReward, dtype=numpy.float32)
        for i, Unit in enumerate(RedAgents.Units):
            red_scores.append(red_score)
            red_eps_history.append(Unit.CNNEpsilon)
            red_avg_score.append(numpy.mean(red_scores[-1000:]))
            RedAgents.Units[i].CNNRewardMemory[-len(rewards):] = rewards
            RedAgents.Units[i].learn('CNN')
            if Env.redArmyWins:
                RedAgents.Units[i].epsilon_decrease('CNN')
            # elif Env.greenArmyWins:
            #     RedAgents.Units[i].epsilon_increase('CNN')
        red_movement_array.append(movements)
        red_avg_movements.append(numpy.mean(red_movement_array[-1000:]))
        if (Verbose == 1 and (Env.redArmyWins or Env.greenArmyWins)) or (Verbose == 2):
            print('Episode', Episode,
                  'RED score %.2f' % float(red_avg_score[Episode]/len(RedAgents.Units)),
                  'GREEN score %.2f' % float(green_avg_score[Episode]/len(GreenAgents.Units)),
                  'red epsilon %.5f' % RedAgents.Units[0].CNNEpsilon,
                  'green epsilon %.5f' % GreenAgents.Units[0].CNNEpsilon,
                  'RedAgents   win in {} movements'.format(movements) if Env.redArmyWins else ''
                  'GreenAgents win in {} movements'.format(movements) if Env.greenArmyWins else '')
        Episode += 1
    x = [i + 1 for i in range(len(red_avg_score))]
    plt.plot(x, red_avg_score, 'r')
    plt.plot(x, green_avg_score, 'g')
    plt.plot(x, red_avg_movements, 'b')
    plt.savefig('./Images/FirstApproach/Graphs/Pineapple.png')
    plt.close()


# NN  -> CoherencyNetwork
# Env -> StayTogether
def unit_coherency(RedAgents, Env, Beginning=True, Train=True, NumEpisodes=10, Movements=100, PlotEnable=False, Verbose=1):
    # Load the model if not the fist time working wth the model
    if not Beginning:
        RedAgents.Units[0].load_model('UnitCoherency')
    num_episodes = NumEpisodes
    Episode = 0
    red_scores, red_eps_history, red_avg_score, red_avg_movements, red_movement_array = [], [], [], [], []
    while Episode < num_episodes:
        s_0 = Env.start(RedAgents)
        # Env.plot(RedAgents)
        Done = False
        movements = 0
        red_score = 0
        while not Done:
            movements += 1
            for i, Unit in enumerate(RedAgents.Units):
                if i > 0:
                    ok = False
                    while not ok:
                        coordinates = Unit.choose('Coherency', s_0[i])
                        s_1, r = Env.step(coordinates, i, RedAgents)
                        ok = True if r > 0 else False
                        RedAgents.Units[i].store_transition('Coherency', s_0[i], coordinates, r, s_1, Done)
                        RedAgents.Units[i].learn('Coherency')
                    RedAgents.Units[i].learn('Coherency')
                    s_0[i] = s_1
            if movements > Movements:
                Done = True
            red_score += r
            if PlotEnable and movements <= Movements:
                Env.plot(RedAgents, Episode, movements)
        if not Env.redArmyWins:
            rewards = numpy.full(movements, -Env.WinningReward, dtype=numpy.float32)
        else:
            rewards = numpy.full(movements, Env.WinningReward, dtype=numpy.float32)
        for i, Unit in enumerate(RedAgents.Units):
            red_scores.append(red_score)
            red_eps_history.append(Unit.Epsilon)
            red_avg_score.append(numpy.mean(red_scores[-1000:]))
            RedAgents.Units[i].RewardMemory[-len(rewards):] = rewards
            RedAgents.Units[i].learn()
            if Env.redArmyWins:
                RedAgents.Units[i].epsilon_decrease()
        red_movement_array.append(movements)
        red_avg_movements.append(numpy.mean(red_movement_array[-1000:]))
        if (Verbose == 1 and (Env.redArmyWins or Env.greenArmyWins)) or (Verbose == 2):
            print('Episode', Episode,
                  'RED score %.2f' % float(red_avg_score[Episode] / len(RedAgents.Units)),
                  'red epsilon %.5f' % RedAgents.Units[0].Epsilon,
                  'RedAgents win in %.2f movements' % float(red_avg_movements[Episode] / len(RedAgents.Units)) if Env.redArmyWins else '')
        Episode += 1
    if not Train:
        RedAgents.Units[0].save_model('UnitCoherency')
    if not PlotEnable:
        x = [i + 1 for i in range(len(red_avg_score))]
        plt.plot(x, red_avg_score, 'r')
        plt.plot(x, red_avg_movements, 'b')
        plt.savefig('./Images/FirstApproach/Graphs/Coherency.png')
        plt.close()
