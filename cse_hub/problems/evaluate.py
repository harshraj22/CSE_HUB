import subprocess
import os
import multiprocessing

import django
django.setup()

from django.conf import settings
from problems.models import Problem, TestCase

def check(ques, sol, file, time, result):
	'''
		Returns verdict of submitted code being ran on given testcase and corresponding solution
	'''
	# Just for refrence, prints the file being checked in terminal
	print('Checking the file ', file, '_'*27)

	file = os.path.join(settings.BASE_DIR, 'problems', str(file))
	command = 'python3'

	# if given file is cpp file, we need to compile before running testcase
	if str(file).endswith('.cpp'):
		command = './a.out'
		p = subprocess.Popen('g++ {file}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		for line in p.stderr.readlines():
			# if we got compilation error, terminate
			if line:
				result['CE'] = 1
				return 'CE'

	# Just for refrence, prints the full command for file being checked to the terminal
	print(f'evaluating using : cat {ques} | {command} {file}')
	p = subprocess.Popen(f'cat {ques} | {command} {file}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	try:
		output, error = p.communicate(timeout=time)
	except subprocess.TimeoutExpired:
		result['TLE'] = 1
		return 'TLE'

	output = str(output, 'utf-8')
	print('output is :- {output}')

	with open(sol) as f:
		exp_output = f.read()

	# Prints output to the terminal
	print('expected output is :- {exp_output}')

	if output == exp_output:
		result['AC'] = 1
		return 'AC'

	result['WA'] = 1
	return 'WA'

def evaluate(file, id):
	'''
		Returns verdict of submitted code file tested over testcases of id
	'''
	cur_problem = Problem.objects.get(id=id)
	testcases = cur_problem.testcase_set.all()

	processes = []
	manager = multiprocessing.Manager()
	result = manager.dict()

	for test in testcases:
		p = multiprocessing.Process(target=check, args=(str(test.testcase.path), str(test.solution.path), file, cur_problem.time, result))
		# cur_verdict = check(str(test.testcase.path), str(test.solution.path), file, cur_problem.time)
		p.start()
		processes.append(p)

	for process in processes:
		process.join()

	if 'CE' in result.keys():
		return 'CE'
	elif 'TLE' in result.keys():
		return 'TLE'
	elif 'WA' in result.keys():
		return 'WA'
	elif 'AC' in result.keys():
		return 'AC'

		# Just for reference

		# print(f'\n\n\nand returned verdict for current testcase is {cur_verdict}\n\n\n')
		# if cur_verdict != 'AC':
		# 	return cur_verdict

	return 'OTHER'
