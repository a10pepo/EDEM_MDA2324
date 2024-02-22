FROM bde2020/spark-master:latest

# Install system packages
RUN apk --no-cache add \
    python3-dev \
    build-base \
    postgresql-dev \
    krb5-dev

# Set the working directory
WORKDIR /

# Copy the application code
COPY . /opt/project

# Copy the entrypoint file and make it executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy and install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Download and add PostgreSQL JDBC Driver during the build
RUN mkdir -p /opt/spark/jars \
    && wget -O /opt/spark/jars/postgresql-42.7.1.jar https://jdbc.postgresql.org/download/postgresql-42.7.1.jar

RUN ls -l /opt/spark/jars/

ENTRYPOINT [ "/entrypoint.sh" ]

