# Databricks notebook source
# MAGIC %md # Visualize the AWS graph generated by Altimeter

# COMMAND ----------

# MAGIC %pip install kglab rdflib pyvis

# COMMAND ----------

# MAGIC %sh ls -R /dbfs/tmp/altimeter_single_account

# COMMAND ----------

from rdflib import Graph
import kglab

# COMMAND ----------

g = Graph()
base_path = "/dbfs/tmp/altimeter_single_account/20221028/1666966271/cae383f3-dc96-40f4-8b63-99164fc2eae3/"
g.parse(F"{base_path}/master.rdf")
len(g)

# COMMAND ----------

kg = kglab.KnowledgeGraph(import_graph=g)

# COMMAND ----------



# COMMAND ----------

import pandas as pd
pd.options.display.max_colwidth = 200
pd.options.display.max_rows = 200

# COMMAND ----------

# MAGIC %sql set spark.sql.execution.arrow.pyspark.enabled = false 

# COMMAND ----------

import pyvis
notebook = False

# COMMAND ----------

sparql = """
SELECT  ?s ?p ?o
WHERE {
    ?s ?p ?o.
    FILTER (?o = <arn:aws::::account/997819012307>).
}
LIMIT 10
"""
display(kg.query_as_df(sparql=sparql))

# COMMAND ----------

sparql = """
SELECT  DISTINCT ?s ?p ?o ?level
WHERE {
  BIND (<arn:aws:ec2:us-west-2:997819012307:vpc/vpc-0b2c00371b939ad85> AS ?vpc)
  {
    BIND(1 as ?level)
    ?s ?p ?vpc .
  }
  UNION
  {
    BIND(1 as ?level)
    ?vpc ?p ?o
  } 
  UNION 
  {
      BIND(2 as ?level)
      ?ss ?pp ?vpc .
      ?s ?p ?ss
  }
}
LIMIT 100
"""
display(kg.query_as_df(sparql=sparql))

# COMMAND ----------

import pyvis
res = g.query(sparql)
notebook = False

pyvis_graph = pyvis.network.Network(notebook=notebook)

node_vector = []
def transform(node:str):
  if not node in node_vector:
    node_vector.append(node)

  return node_vector.index(node)


for s, p, o in res:
    # label the subject
    s_label = str(s)
    s_id = transform(s_label)
    pyvis_graph.add_node(
              s_id,
              label=s_label,
              title=s_label,
          )

    # label the object
    o_label = str(o)
    o_id = transform(o_label)
    pyvis_graph.add_node(
              o_id,
              label=o_label,
              title=o_label,
          )

    # label the predicate
    p_label = str(p)
    print(s_id, s_label, p_label, o_id, o_label)
    pyvis_graph.add_edge(s_id, o_id, label=p_label)



# COMMAND ----------

displayHTML(pyvis_graph.generate_html())

# COMMAND ----------


