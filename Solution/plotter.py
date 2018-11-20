import matplotlib.pyplot as plt
import pandas as pd

def plot_data(iter1, data1, iter2, data2, iter3, data3,ylabel, filename):
	fig, ax = plt.subplots(figsize = (8,5))
	plt.plot(iter1, data1, color = 'navy', linestyle='-', label='qInit = 1.0')
	plt.plot(iter2, data2, color = 'firebrick', linestyle='-', label='qInit = 50.0')
	plt.plot(iter3, data3, color = 'olivedrab', linestyle='-', label='qInit = 200.0')

	plt.legend(loc = 'best')
	plt.xlabel('Iteration')
	plt.ylabel(ylabel)
	plt.grid()
	plt.savefig(filename+'.png')

'''
vi_file = './Easy Value.csv'
pi_file = './Easy Policy.csv'
ql_file = './Easy Q-Learning L0.5 q50.0 E0.5.csv'

value_iteration = pd.read_csv(vi_file, sep=',')
policy_iteration =pd.read_csv(pi_file, sep=',')
q_learning = pd.read_csv(ql_file, sep=',')

vi_iter = value_iteration['iter'].copy().values
vi_rewards = value_iteration['reward'].copy().values
vi_convergence = value_iteration['convergence'].copy().values
vi_time = value_iteration['time'].copy().values
vi_step = value_iteration['steps'].copy().values

pi_iter = policy_iteration['iter'].copy().values
pi_rewards = policy_iteration['reward'].copy().values
pi_convergence = policy_iteration['convergence'].copy().values
pi_time = policy_iteration['time'].copy().values
pi_step = policy_iteration['steps'].copy().values

ql_iter = q_learning['iter'].copy().values
ql_rewards = q_learning['reward'].copy().values
ql_convergence = q_learning['convergence'].copy().values
ql_time = q_learning['time'].copy().values
ql_step = q_learning['steps'].copy().values

plot_data(vi_iter, vi_rewards, pi_iter, pi_rewards, ql_iter, ql_rewards, 'Rewards','rewardFig')
plot_data(vi_iter, vi_convergence, pi_iter, pi_convergence, ql_iter, ql_convergence, 'Convergence','convergenceFig')
plot_data(vi_iter, vi_time, pi_iter, pi_time, ql_iter, ql_time, 'Time', 'timeFig')
plot_data(vi_iter, vi_step, pi_iter, pi_step, ql_iter, ql_step, 'Steps', 'StepFig')
'''
'''
vi_sizefile = './size Value.csv'
pi_sizefile = './size Policy.csv'
ql_sizefile = './size Q-Learning L0.1 E0.5.csv'

value_size = pd.read_csv(vi_sizefile, sep=',')
policy_size =pd.read_csv(pi_sizefile, sep=',')
q_learning_size = pd.read_csv(ql_sizefile, sep=',')

vi_index = value_size['shape'].copy().values
vi_iteration = value_size['iter'].copy().values
vi_rewards = value_size['reward'].copy().values
vi_time = value_size['time'].copy().values

pi_index = policy_size['shape'].copy().values
pi_iteration = policy_size['iter'].copy().values
pi_rewards = policy_size['reward'].copy().values
pi_time = policy_size['time'].copy().values

ql_index = q_learning_size['shape'].copy().values
ql_iteration = q_learning_size['iter'].copy().values
ql_rewards = q_learning_size['reward'].copy().values
ql_time = q_learning_size['time'].copy().values

plot_data(vi_index, vi_iteration, pi_index, pi_iteration, ql_index, ql_iteration, 'Iterations','IterationFig')
plot_data(vi_index, vi_rewards, pi_index, pi_rewards, ql_index, ql_rewards, 'Rewards','SizeRewardsFig')
plot_data(vi_index, vi_time, pi_index, pi_time, ql_index, ql_time, 'Time','SizeTimeFig')
'''

ql03_file = './Hard Q-Learning L0.5 q1.0 E0.5.csv'
ql05_file = './Hard Q-Learning L0.5 q50.0 E0.5.csv'
ql07_file = './Hard Q-Learning L0.5 q250.0 E0.5.csv'

ql03 = pd.read_csv(ql03_file, sep = ',')
ql05 = pd.read_csv(ql05_file, sep = ',')
ql07 = pd.read_csv(ql07_file, sep = ',')

ql03_iter = ql03['iter'].copy().values
ql03_time = ql03['time'].copy().values
ql03_converge = ql03['convergence'].copy().values

ql05_iter = ql05['iter'].copy().values
ql05_time = ql05['time'].copy().values
ql05_converge = ql05['convergence'].copy().values

ql07_iter = ql07['iter'].copy().values
ql07_time = ql07['time'].copy().values
ql07_converge = ql07['convergence'].copy().values

plot_data(ql03_iter, ql03_time, ql05_iter, ql05_time, ql07_iter, ql07_time, 'Time','QL_TimeFig')
plot_data(ql03_iter, ql03_converge, ql05_iter, ql05_converge, ql07_iter, ql07_converge,  'Convergence','QL_CovergenceFig')
