import pandas as pd

logs = ['log_hadoop', 'log_flink', 'log_spark']

for l in logs:
	file_ = l[4:] + '_top_ten.txt'
	with open(file_, 'w') as f:
		df = pd.read_csv(l + '.txt',
				sep='#',
				header=None,
				names=['timestamp', 'author'])
		print(df.head(5))
		number_of_authors = df.author.nunique()
		number_of_commits = df.timestamp.count()
		print("%s authors commited %s code changes in %s project" % (
			number_of_authors, number_of_commits, l[4:]))
		top_ten = df.author.value_counts().nlargest(10)
		top_ten.to_csv(f, sep='\t')	
