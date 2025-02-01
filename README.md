# Distributed Word Counter with Apache Spark

## Introduction

This is a simple example of distributed word counter using Apache Spark.
It uses a sample dataset of text lines to count the occurrences of individual words.

---

## Setup

This setup is focussed on local development using Docker Compose. It uses 3 Spark containers: a spark master and 2 spark workers nodes.

[Word counter python script](./word_count.py) is mounted into the master node and we connect to the master to execute the script. `PySpark` is used to create an RDD from the text lines and perform distributed word count.

---

## Usage

1. Start the Spark containers using Docker Compose:

   ```bash
   docker-compose up -d
   ```

2. Run the distributed word count example:
   ```bash
   bash submit.sh
   ```

---

## Sample Input

```python
text_lines = [
    "Spark is fast",
    "Spark is scalable",
    "Distributed computing with Spark",
    "Python and Spark go well together",
    "Python provides a simple interface to Spark",
    "Other options include Java, Scala, and R, but Python is the most beginner-friendly",
]
```

## Sample Output

```bash
Distributed Word Count Results:
computing: 1
and: 2
well: 1
include: 1
Scala,: 1
most: 1
is: 3
Other: 1
Java,: 1
the: 1
options: 1
beginner-friendly: 1
together: 1
provides: 1
a: 1
simple: 1
fast: 1
interface: 1
to: 1
go: 1
R,: 1
Distributed: 1
with: 1
Python: 3
but: 1
Spark: 5
scalable: 1
```

---

## License Information

This project is released under the [MIT License](LICENSE).
