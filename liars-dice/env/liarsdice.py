from pettingzoo import AECEnv


class raw_env(AECEnv):
    metadata = {
        "name": "custom_environment_v0",
    }

    def __init__(
    self,
    agent_dice: int = 6, # starting die count
    dice_face_count: int = 6, # default of 6 sided die
    ):
        self.possible_agents = ["player_" + str(r) for r in range(1)] # 2 agents
        self.total_dice = self.agent_dice * len(possible_agents) # = to starting dice count time number of players

        self.action_space = spaces.Tuple(
            spaces.Discrete(self.total_dice + 1), # Starting from 0, highest dice bid possible is the max number of dice on the table 
            spaces.Discrete(elf.dice_face_count + 1), # Max face value is highest on die 
            spaces.Discrete(1) # Binary representing if agent is calling previous bid
            )

        self.observation_space = spaces.Tuple(
            spaces.Discrete(), #Current agent rolled dice
            spaces.Discrete(self.total_dice), # Total table dice
            spaces.Discrete() # tuple of previous call
            )

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
