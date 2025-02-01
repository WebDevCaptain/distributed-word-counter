FROM bitnami/spark:3.5.4

WORKDIR /opt



COPY word_count.py /opt/word_count.py

# ENTRYPOINT ["python", "/opt/word_count.py"]

EXPOSE 8080

CMD ["bash"]