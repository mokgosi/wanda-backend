# Pull a base image
FROM python:3.9-slim as base

# Set environment variables
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Copy requirements to the container
COPY Pipfile .
COPY Pipfile.lock .

# Install the requirements to the container
RUN PIPENV_VENV_IN_PROJECT=1 
RUN . pipenv shell pipenv install --system
# RUN cd /src && pipenv install --system

FROM base AS runtime

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Copy the project files into the working directory
COPY . .
# Open a port on the container
EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]