class Node(object):
	"""docstring for Node"""
	def __init__(self, definitions, current, local_value, outgoing, value_added_outgoing, retention, steer_power, num_collectors, total, p_pow, _max, collector_power, pull_power, retain_power, highest_power):
		super(Node, self).__init__()
		self.definitions = definitions
		self.current = current
		self.local_value=local_value
		self.outgoing=outgoing
		self.value_added_outgoing=value_added_outgoing
		self.retention=retention
		self.steer_power=steer_power
		self.num_collectors=num_collectors
		self.total=total
		self.p_pow=p_pow
		self.max=_max
		self.collector_power=collector_power
		self.pull_power=pull_power
		self.retain_power=retain_power
		self.highest_power=highest_power

if __name__ == '__main__':
	africanGreatLakes = Node('african_great_lakes',0,0,0,0,0,0,0,0,0,0,0,0,0,0)
	print(africanGreatLakes.definitions)