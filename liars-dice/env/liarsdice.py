from pettingzoo import AECEnv


class raw_env(AECEnv):
    metadata = {
        "name": "custom_environment_v0",
    }

    def __init__(self):
        self.possible_agents = ["player_" + str(r) for r in range(1)]
        pass

    def reset(self, seed=None, options=None):
        pass

    def step(self, actions):
        pass

    def render(self):
        pass

    def observation_space(self, agent):
        return self.observation_spaces[agent]

    def action_space(self, agent):
        return self.action_spaces[agent]
