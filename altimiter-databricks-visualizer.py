# Databricks notebook source
# MAGIC %pip install pyvis rdflib kglab

# COMMAND ----------

# MAGIC %sh ls -R /dbfs/tmp/altimeter_single_account/20221028/1666966271/cae383f3-dc96-40f4-8b63-99164fc2eae3

# COMMAND ----------

import rdflib

g = 

# COMMAND ----------

    def build_pyvis_graph (
        self,
        *,
        notebook: bool = False,
        style: dict = None,
        ) -> pyvis.network.Network:
        """
Factory pattern to create a [`pyvis.network.Network`](https://pyvis.readthedocs.io/en/latest/documentation.html?highlight=network#pyvis.network.Network) object, populated by transforms in this subgraph.
See <https://pyvis.readthedocs.io/>
    notebook:
flag for whether or not the interactive visualization will be generated within a notebook
    style:
optional style dictionary
    returns:
a `PyVis` network object
        """
        pyvis_graph = pyvis.network.Network(notebook=notebook)

        if not style:
            style = {}

        for s, p, o in self.as_tuples():
            # label the subject
            s_label = self.n3fy(s)
            s_id = self.transform(s_label)
            self.pyvis_style_node(pyvis_graph, s_id, s_label, style=style)

            # label the object
            o_label = str(self.n3fy(o))
            o_id = self.transform(o_label)
            self.pyvis_style_node(pyvis_graph, o_id, o_label, style=style)

            # label the predicate
            p_label = self.n3fy(p)
            pyvis_graph.add_edge(s_id, o_id, label=p_label)

        return pyvis_graph
