## Define your use case

# Acerca del conjunto de datos:

El conjunto de datos consta de 1,75 millones de transacciones realizadas considerando usuarios simulados a través de varios terminales durante todo el período comprendido entre enero de 2023 y junio de 2023. Sin embargo, los datos están muy desequilibrados, con solo un pequeño porcentaje (0,1345%) de las transacciones clasificadas como fraudulentas.

Debido a la distribución desigual de las clases en el conjunto de datos, es más apropiado evaluar el rendimiento del modelo utilizando AUPRC en lugar de la precisión de la matriz de confusión. La precisión de la matriz de confusión puede ser engañosa en casos de desequilibrio de clase.

## Deliverables
You will have to provide the following:

Basic explanation of:
1. Use case
   
2. Dataset selected 
   
3. Final architecture implemented 
   
4. Json examples of your data json model 
   
5. **Evidence** of the Application has run end to end providing the expected results. With screenshots of the different step: 
   1) the ingestion
   2) the processing with a Consumer
   3) the processing with KSQL, the final printing on screen on the expected outcome.