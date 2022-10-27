# Databricks notebook source
# MAGIC %md # Altimeter
# MAGIC ## Turn AWS resources into RDFs
# MAGIC https://github.com/tableau/altimeter
# MAGIC 
# MAGIC Document the setup and running `altimiter` on a Databricks cluster

# COMMAND ----------

# MAGIC %sh pip install -r requirements.txt

# COMMAND ----------

# MAGIC %sh pwd

# COMMAND ----------

# MAGIC %sh cat conf/current_single_account.toml

# COMMAND ----------

# MAGIC %sh
# MAGIC export AWS_DEFAULT_REGION="us-west-2"
# MAGIC export PYTHONPATH=/Workspace/Repos/douglas.moore@databricks.com/altimeter
# MAGIC export PATH=.:$PATH
# MAGIC cd bin
# MAGIC ./altimeter ../conf/current_single_account.toml >log.txt

# COMMAND ----------

# MAGIC %sh tail -1  bin/log.txt

# COMMAND ----------

# MAGIC %sh
# MAGIC zcat /tmp/altimeter_single_account/20221027/1666897012/6c2e70a0-d688-4872-908c-21813f883a2f/master.rdf.gz

# COMMAND ----------

import kglab

# COMMAND ----------


