# Databricks notebook source
# MAGIC %sh pip install git+https://github.com/dmoore247/altimeter.git awscli structlog

# COMMAND ----------

# MAGIC %sh python setup.py bdist

# COMMAND ----------

# MAGIC %sh
# MAGIC export AWS_DEFAULT_REGION="us-west-2"
# MAGIC altimeter current_single_account.toml

# COMMAND ----------

# MAGIC %sh pwd

# COMMAND ----------


