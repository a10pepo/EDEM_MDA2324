#!/bin/bash
bash /spark/bin/spark-submit --master local --jars /opt/spark/jars/postgresql-42.7.1.jar /opt/project/src/python/spark_jumepe.py
