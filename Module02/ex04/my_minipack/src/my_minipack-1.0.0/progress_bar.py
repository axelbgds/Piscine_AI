import time

def getBar(barSize, now, total):
	if now == total - 1:
		return "=" * barSize
	done = int(now / total * barSize)
	return "=" * done + ">" + " " * (barSize - done - 1)

def progress_bar(lst):
	start = time.time()
	timepassed = 0
	for x in lst:
		if x == 0:
			oneLoop = time.time()
		if x == 1:
			timepassed = time.time() - oneLoop
		print("ETA: {:.1f}s [{}%][{}] {}/{} | elapsed time {:.1f}s     ".format(timepassed * (len(lst) - x), int((x + 1)/ len(lst) * 100), getBar(30, x, len(lst)), x + 1, len(lst), time.time() - start), end='\r')
		yield x