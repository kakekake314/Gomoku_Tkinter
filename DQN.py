#!/usr/bin/env python
# -*- coding: utf8 -*-
import chainer
import chainer.functions as F
import chainer.links as L
import chainerrl
import numpy as np
from Banmen import Banmen
from TestPlayer import TestPlayer
from Player import Player



#Q関数
class QFunction(chainer.Chain,object):
    def __init__(self, obs_size, n_actions, n_hidden_channels=98):
        super(QFunction,self).__init__(
            l0=L.Linear(obs_size, n_hidden_channels),
            l1=L.Linear(n_hidden_channels, n_hidden_channels),
            l2=L.Linear(n_hidden_channels, n_hidden_channels),
            l3=L.Linear(n_hidden_channels, n_actions))
    def __call__(self, x, test=False):

        h = F.leaky_relu(self.l0(x))
        h = F.leaky_relu(self.l1(h))
        h = F.leaky_relu(self.l2(h))
        return chainerrl.action_value.DiscreteActionValue(self.l3(h))



class DQNPlayer(Player,object):

	def __init__(self,name,isSenkou):
		super(DQNPlayer,self).__init__(name,isSenkou)
		self.learning()


	def action(self,banmen):

		action = self.agent.act(self.convertTo1D(banmen))
		col,row = self.getColRow(banmen,action)
		return col,row

	def convertTo1D(self,data):
		oneDData = []
		for row in range(len(data)):
			for col in range(len(data)):
				oneDData.append(data[row][col])
		return np.array(oneDData,dtype=np.float32)

	def getColRow(self,data,action):
		num = 0
		for row in range(len(data)):
			for col in range(len(data)):
				if num == action:
					return col,row
				num += 1

	def learning(self):
		banmen = Banmen()

		player = TestPlayer("学習用プレイヤー",True,banmen)

		obs_size = 49
		n_actions = 49

		q_func = QFunction(obs_size,n_actions)
		optimizer = chainer.optimizers.Adam(eps=1e-2)
		optimizer.setup(q_func)

		gamma = 0.95

		explorer = chainerrl.explorers.LinearDecayEpsilonGreedy(
			start_epsilon=1.0, end_epsilon=0.3, decay_steps=50000, random_action_func=player.randomAction)
		replay_buffer = chainerrl.replay_buffer.ReplayBuffer(capacity=10 ** 6)
		agent_p1 = chainerrl.agents.DoubleDQN(
			q_func, optimizer, replay_buffer, gamma, explorer,
			replay_start_size=500, update_interval=1,
			target_update_interval=100)
		agent_p2 = chainerrl.agents.DoubleDQN(
			q_func, optimizer, replay_buffer, gamma, explorer,
			replay_start_size=500, update_interval=1,
			target_update_interval=100)


		agent_p2.load("result/result6_20000")
		agent_p2.load("result/result6_20000")

		# n_episodes = 20000
		n_episodes = 0

		miss = 0
		win = 0
		draw = 0

		for i in range(1,n_episodes +1):
			banmen.reset()
			reward = 0
			agents = [agent_p1,agent_p2]
			turn = np.random.choice([0,1])
			last_state = None
			boolTurn = True
			if turn == 0:
				boolTurn = True
			else:
				boolTurn = False
			while not banmen.isFinished():
				action = agents[turn].act_and_train(banmen.convertTo1D(),reward)

				banmen.put(action,boolTurn)
				# banmen.printData()



				if banmen.isFinished():
					alignedNum = banmen.getAlignedNumber()
					if (alignedNum == 1 and turn == 0) or (alignedNum == 2 and turn == 1):
						reward = 1
						win += 1
					elif alignedNum == 0:
						draw += 1
					else:
						reward = -1
					if banmen.getMissed():
						miss += 1

					agents[turn].stop_episode_and_train(banmen.convertTo1D(),reward,True)
					if agents[1 if turn == 0 else 0].last_state is not None and not banmen.getMissed():
						agents[1 if turn == 0 else 0].stop_episode_and_train(last_state, reward*-1,True)
				else:
					last_state = banmen.convertTo1D()
					# banmen.change()
					if turn == 0:
						turn = 1
						boolTurn = False
					else:
						turn = 0
						boolTurn = True

			if i % 100 == 0:
				print("episode:", i, " / rnd:", player.getCount(), " / miss:", miss, " / win:", win, " / draw:", draw, " / statistics:", agent_p1.get_statistics(), " / epsilon:", agent_p1.explorer.epsilon)
				miss = 0
				win = 0
				draw = 0
				player.setCount(0)
				# print reward
				# banmen.printData()
			if i % 10000 == 0:
				agent_p1.save("result/result6_"+str(i))

		self.agent = agent_p1



	def action(self,banmen):

		action = self.agent.act(self.convertTo1D(banmen))
		col,row = self.getColRow(banmen,action)
		return col,row

	def convertTo1D(self,data):
		oneDData = []
		for row in range(len(data)):
			for col in range(len(data)):
				oneDData.append(data[row][col])
		return np.array(oneDData,dtype=np.float32)

	def getColRow(self,data,action):
		num = 0
		for row in range(len(data)):
			for col in range(len(data)):
				if num == action:
					return col,row
				num += 1












