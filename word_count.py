from pyspark import SparkContext

# NOTE: When run in cluster mode, Spark picks up master details from spark-submit.
sc = SparkContext(appName="DistributedWordCount")

# A sample dataset: a list of text lines
text_lines = [
    "Spark is fast",
    "Spark is scalable",
    "Distributed computing with Spark",
    "Python and Spark go well together",
    "Python provides a simple interface to Spark",
    "Other options include Java, Scala, and R, but Python is the most beginner-friendly",
]

# RDD from the text lines above
lines_rdd = sc.parallelize(text_lines)

# flatMap - to split each line into words
words_rdd = lines_rdd.flatMap(lambda line: line.split(" "))

# Map each word to a tuple (word, 1)
word_pairs_rdd = words_rdd.map(lambda word: (word, 1))

# Reduce by key to count occurrences
word_counts_rdd = word_pairs_rdd.reduceByKey(lambda a, b: a + b)

# Collect the results back to the driver
results = word_counts_rdd.collect()

print("Distributed Word Count Results:")
for word, count in results:
    print(f"{word}: {count}")

sc.stop()
