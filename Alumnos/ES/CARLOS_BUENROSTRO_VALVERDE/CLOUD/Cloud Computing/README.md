# CLOUD COMPUTING - END2END

A continuación expongo el proceso llevado a cabo para la realización de este Postwork.

En primer lugar, iniciamos la sesion a través de la terminal de nuestro ordenador y ejecutamos los diferentes comandos de gcloud SDK para activar las APIs necesarias para el trabajo. ![Running APIs](./Postwork/Running_APIs.png) Seguidamente, creamos la Virtual Machine en la plataforma [Google Cloud Platform](https://cloud.google.com). A través de Virtual Machines Instances.
![VM_Creation](./Postwork/VM_Creation.png)

Una vez la máquina virtual se encuentra levantada, debemos crear el bucket en el cual almacenaremos los archivos necesarios para la creación de tablas en SQL. ![Bucket Creation](./Postwork/Bucket_Creation.png)

En nuestra cuenta principal deberemos garantizar los diferentes accesos para poder trabajar. En este caso activamos el rol de Administrador de almacenamiento.![Storage Permission](./Postwork/Storage_Permission.png)

El siguiente paso a realizar será la creación de la Base de Datos en PostgreSQL. Para ello, se deberá acceder en la barra de búsqueda a SQL y comenzar a configurar la BBDD deseada. ![PostgreSQL Instance](./Postwork/PostgreSQL_Instance.png)

Cuando se haya generado la instancia de SQL, tendremos que subir al bucket creado el archivo de creación de tablas; y este tiene que ser importado por la instancia SQL. ![Data Import to Bucket](./Postwork/Data_Import_Bucket.png) ![Data Import to Instance SQL](./Postwork/Data_Import_PostgreSQL.png)

El siguiente paso a seguir es la conexión con la instancia para poder visualizar las tablas por consola. A continuación se puede observar ambas: 
![Postgres Connection](./Postwork/PostgreSQL_Connection.png) ![Table Visualization Console](./Postwork/Table_Visualization.png)

Cuando sean visibles estas tablas, se pasará a realizar la conexión con DBeaver para la visualización de la BBDD. 

**En este caso, como daba muchos problemas el Proxy, he conectado a través de la IP Pública de la instancia SQL de GCP**

**Queda pendiente cerrar una reunión con Miguel para poder solucionar esta parte y de esta forma poder realizar la conexión a través de Proxy**

![Table Visualization DBeaver](./Postwork/Tables_Visualization_DBeaver.png)

A continuación, se crearán los secrets a través del Secret Manager de GCP que serán necesarios para la creación de la Cloud Function. ![Secrets Creation](./Postwork/Secrets_Creation.png)

Más tarde, se accede a la consola de Cloud Function para poder crear la funcion. Tras la creación de la misma, se debe acceder a Cloud Run service para hacer la conexión con la instancia de SQL que se ha creado.
![Cloud Function Creation](./Postwork/Cloud_Function_Creation.png)
![Cloud Function Revision](./Postwork/Cloud_Function_Revision.png)

A través de la Cloud Shell, se ha creado la imagen docker que permitirá ejecutar Grafana para la realización y visualización de los datos procesados. Esta debe de ser enviada al repositorio creado en Artifact Registry
![Building Docker Image](./Postwork/Building_Docker_Image.png)
![Image Pushed to Repo](./Postwork/Image_Pushed_to_Repo.png)

Se configura seguidamente el Cloud Run Service. ![Cloud Run Service Creation](./Postwork/Cloud_Run_Service_Creation.png)

En uno de los últimos pasos a seguir en la configuración del entorno será ejecutado el generador de datos. Para comprobar que los datos han seguido el flujo correcto, desde DBeaver se pueden realizar las diferentes queries necesarias para corroborar que los datos procesados están llegando.
![Running Script](./Postwork/Running_Script.png)
![Data Ingestion DBeaver](./Postwork/Data_Ingestion_DBeaver.png)

Por último, se accederá a Grafana. En este paso se deberán configurar las conexiones a la BBDD. Una vez se tenga la configuración realizada, se podrá comenzar con la creación del dashboard para plasmar los mejores datos y métricas del proyecto.

![Grafana Dashboard](./Postwork/Grafana_Dashboard.png)

