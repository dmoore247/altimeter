# Databricks notebook source
# MAGIC %sh ls -R /dbfs/tmp/altimeter_single_account

# COMMAND ----------

# MAGIC %pip install kglab rdflib

# COMMAND ----------

from rdflib import Graph

# COMMAND ----------

# MAGIC %sh
# MAGIC cd /tmp/altimeter_single_account/20221027/1666897012/6c2e70a0-d688-4872-908c-21813f883a2f
# MAGIC gunzip master.rdf.gz
# MAGIC ls

# COMMAND ----------

# MAGIC %sh head /tmp/altimeter_single_account/20221027/1666897012/6c2e70a0-d688-4872-908c-21813f883a2f/master.rdf

# COMMAND ----------

g = Graph()

g.parse("/tmp/altimeter_single_account/20221027/1666897012/6c2e70a0-d688-4872-908c-21813f883a2f/master.rdf")

# COMMAND ----------

import pprint
for stmt in g:
    pprint.pprint(stmt)

# COMMAND ----------

len(g)

# COMMAND ----------



# COMMAND ----------


