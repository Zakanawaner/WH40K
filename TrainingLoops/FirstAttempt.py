import numpy
import matplotlib.pyplot as plt


def vanilla_loop(RedAgents, GreenAgents, Env, NumEpisodes=2000, Movements=100, PlotEnable=False):
    num_episodes = NumEpisodes
    Episode = 0
    red_scores, red_eps_history, red_avg_score = [], [], []
    green_scores, green_eps_history, green_avg_score = [], [], []
    while Episode < num_episodes:
        s_0 = Env.start(RedAgents, GreenAgents)
        Done = False
        RedTurn = True
        movements = 0
        red_score, green_score = 0, 0
        while not Done:
            movements += 1
            if PlotEnable:
                Env.plot(RedAgents, GreenAgents)
            if RedTurn:
                for i, Unit in enumerate(RedAgents.Units):
                    action = Unit.choose(s_0)
                    s_1, r, Done = Env.step(action, i, RedAgents, RedTurn)
                    if movements > Movements:
                        Done = True
                        r = -Env.WinningReward
                    red_score += r
                    RedAgents.Units[i].store_transition(s_0, action, r, s_1, Done)
                    RedAgents.Units[i].learn()
                    RedAgents.Units[i].epsilon_decay()
                    s_0 = s_1
                    if Done:
                        red_scores.append(red_score)
                        red_eps_history.append(Unit.Epsilon)
                        red_avg_score.append(numpy.mean(red_scores[-100:]))
                        print('Episode ', Episode,
                              'score %.2f' % red_score,
                              'average score %.2f' % numpy.mean(red_scores[-100:]),
                              'epsilon %.2f' % Unit.Epsilon,
                              'RedAgents win' if Env.redArmyWins else '')
                        break
                RedTurn = False
            else:
                for i, Unit in enumerate(GreenAgents.Units):
                    action = Unit.choose(s_0)
                    s_1, r, Done = Env.step(action, i, GreenAgents, RedTurn)
                    if movements > Movements:
                        Done = True
                        r = -Env.WinningReward
                    green_score += r
                    GreenAgents.Units[i].store_transition(s_0, action, r, s_1, Done)
                    GreenAgents.Units[i].learn()
                    GreenAgents.Units[i].epsilon_decay()
                    s_0 = s_1
                    if Done:
                        green_scores.append(green_score)
                        green_eps_history.append(Unit.Epsilon)
                        green_avg_score.append(numpy.mean(green_scores[-100:]))
                        print('Episode ', Episode,
                              'score %.2f' % green_score,
                              'average score %.2f' % numpy.mean(green_scores[-100:]),
                              'epsilon %.2f' % Unit.Epsilon,
                              'GreenAgents win' if Env.greenArmyWins else '')
                        break
                RedTurn = True
        Episode += 1
    x = [i + 1 for i in range(len(red_avg_score))]
    plt.plot(x, red_avg_score)
    plt.savefig('./Images/FirstApproach/vanilla_red.png')
    plt.close()
    x = [i + 1 for i in range(len(green_avg_score))]
    plt.plot(x, green_avg_score)
    plt.savefig('./Images/FirstApproach/vanilla_green.png')


def pineapple_loop(RedAgents, GreenAgents, Env, NumEpisodes=2000, Movements=300, PlotEnable=False, Verbose=1):
    num_episodes = NumEpisodes
    Episode = 0
    red_scores, red_eps_history, red_avg_score = [], [], []
    green_scores, green_eps_history, green_avg_score = [], [], []
    while Episode < num_episodes:
        s_0 = Env.start(RedAgents, GreenAgents)
        Done = False
        RedTurn = True
        movements = 0
        red_score, green_score = 0, 0
        while not Done:
            movements += 1
            if PlotEnable:
                Env.plot(RedAgents, GreenAgents)
            for i, Unit in enumerate(RedAgents.Units):
                action = Unit.choose(s_0)
                s_1, r, Done = Env.step(action, i, RedAgents, RedTurn)
                if movements > Movements or Env.greenArmyWins:
                    Done = True
                    Env.redArmyWins = False
                    r = -Env.WinningReward
                red_score += r
                RedAgents.Units[i].store_transition(s_0, action, r, s_1, Done)
                s_0 = s_1
            RedTurn = False
            for i, Unit in enumerate(GreenAgents.Units):
                action = Unit.choose(s_0)
                s_1, r, Done = Env.step(action, i, GreenAgents, RedTurn)
                if movements > Movements or Env.redArmyWins:
                    Done = True
                    Env.greenArmyWins = False
                    r = -Env.WinningReward
                green_score += r

                if Env.greenArmyWins:
                    red_score = -1

                GreenAgents.Units[i].store_transition(s_0, action, r, s_1, Done)
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
            green_eps_history.append(Unit.Epsilon)
            green_avg_score.append(numpy.mean(green_scores[-1000:]))
            GreenAgents.Units[i].RewardMemory[-len(rewards):] = rewards
            GreenAgents.Units[i].learn()
            if Env.greenArmyWins:
                GreenAgents.Units[i].epsilon_decrease()
            elif Env.redArmyWins:
                GreenAgents.Units[i].epsilon_increase()
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
            elif Env.greenArmyWins:
                RedAgents.Units[i].epsilon_increase()
        if (Verbose == 1 and (Env.redArmyWins or Env.greenArmyWins)) or (Verbose == 2):
            print('Episode', Episode,
                  'RED score %.2f' % float(red_avg_score[Episode]/len(RedAgents.Units)),
                  'GREEN score %.2f' % float(green_avg_score[Episode]/len(GreenAgents.Units)),
                  'red epsilon %.5f' % RedAgents.Units[0].Epsilon,
                  'green epsilon %.5f' % GreenAgents.Units[0].Epsilon,
                  'RedAgents   win in {} movements'.format(movements) if Env.redArmyWins else ''
                  'GreenAgents win in {} movements'.format(movements) if Env.greenArmyWins else '')
        Episode += 1
    x = [i + 1 for i in range(len(red_avg_score))]
    plt.plot(x, red_avg_score, 'r')
    plt.plot(x, green_avg_score, 'g')
    plt.savefig('./Images/FirstApproach/Pineapple.png')
    plt.close()
