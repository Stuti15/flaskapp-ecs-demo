FROM public.ecr.aws/docker/library/python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
EXPOSE 80
CMD ["python", "app.py"]
