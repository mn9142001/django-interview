# Do not modify the base image
FROM python:3.8-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /code

# Install dependencies
COPY ./requirements.txt /srv/requirements.txt
RUN pip install -r /srv/requirements.txt

# Copy the Django application code into the container
COPY . /code/

# Run Django migrations (assuming manage.py is present in the root directory of your project)
RUN python manage.py migrate

# Expose the port on which Django will run
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
