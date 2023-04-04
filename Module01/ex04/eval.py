class Evaluator:
	@staticmethod
	def zip_evaluate(words, coefs):
		if len(words) != len(coefs):
			return -1
		return sum(len(elem[0]) * elem[1] for elem in zip(words, coefs))

	@staticmethod
	def enumerate_eval(words, coefs):
		if len(words) != len(coefs):
			return -1
		return sum(len(word) * coefs[i] for i, word in enumerate(words))

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

print("result with zip: ", Evaluator.zip_evaluate(words, coefs))
print("result with enumerate: ", Evaluator.enumerate_eval(words, coefs))