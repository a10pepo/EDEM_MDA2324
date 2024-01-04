FROM jupyter/base-notebook

COPY ./scripts /data

WORKDIR /data

CMD ["jupyter", "notebook", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]