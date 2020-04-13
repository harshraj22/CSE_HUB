import subprocess
import os
from django.conf import settings
from problems.models import Problem, TestCase

def check(ques, sol, file, time):
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
				return 'CE'

	# Just for refrence, prints the full command for file being checked to the terminal
	print(f'evaluating using : cat {ques} | {command} {file}')
	p = subprocess.Popen(f'cat {ques} | {command} {file}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	try:
		output, error = p.communicate(timeout=time)
	except subprocess.TimeoutExpired:
		return 'TLE'

	output = str(output, 'utf-8')
	print('output is :- {output}')

	with open(sol) as f:
		exp_output = f.read()

	# Prints output to the terminal
	print('expected output is :- {exp_output}')

	if output == exp_output:
		return 'AC'

	return 'WA'

def evaluate(file, id):
	'''
		Returns verdict of submitted code file tested over testcases of id
	'''
	cur_problem = Problem.objects.get(id=id)
	testcases = cur_problem.testcase_set.all()

	for test in testcases:
		cur_verdict = check(str(test.testcase.path), str(test.solution.path), file, cur_problem.time)

		# Just for reference
		print('\n\n\nand returned verdict for current testcase is {cur_verdict}\n\n\n')
		if cur_verdict != 'AC':
			return cur_verdict

	return 'AC'
