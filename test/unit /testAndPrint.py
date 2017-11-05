import traceback

def testAndPrint(got, expected, task_name = None):

	try:
		if got != expected:
			if task_name is None:
				print('Got {}, expected {}'.format(got, expected))
			else:
				print('{}:\nGot {}, expected {}'.format(task_name, got, expected))
	except Exception as e:
			traceback.print_exc(e)