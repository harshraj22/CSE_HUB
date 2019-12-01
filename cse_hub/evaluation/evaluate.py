import subprocess
import os 
from django.conf import settings
from problems.models import problem, testCase

def check(ques, sol, file):
	'''
		Returns verdict of submitted code being ran on given testcase and corresponding solution
	'''
	# Just for refrence, prints the file being checked
	print('Checking the file ', file, '_'*27)
	
	file = os.path.join(settings.BASE_DIR, 'problems', str(file))
	command = 'python3'

	# if given file is cpp file, we need to compile before running testcase
	if str(file).endswith('.cpp'):
		command = './a.out'
		p = subprocess.Popen(f'g++ {file}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		for line in p.stderr.readlines():
			# if we got compilation error, terminate 
			if line:
				return 'CE'

	# Just for refrence, prints the full command for file being checked
	print(f'evaluating using : cat {ques} | {command} {file}')
	p = subprocess.Popen(f'cat {ques} | {command} {file}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, error = p.communicate()

	output = str(output, 'utf-8')
	print(f'output is :- {output}')

	with open(sol) as f:
		exp_output = f.read()

	print(f'expected output is :- {exp_output}')

	if output == exp_output:
		return 'AC'

	return 'WA'

def evaluate(file, problem_id):
	'''
		Returns verdict of submitted code file tested over testcases of problem_id
	'''
	cur_problem = problem.objects.get(id=problem_id)
	testcases = cur_problem.testcase_set.all()

	for test in testcases:
		cur_verdict = check(str(test.testcase.path), str(test.solution.path), file)
		if cur_verdict != 'AC':
			return cur_verdict

	return 'AC'