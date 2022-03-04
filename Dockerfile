# Pull a base image
FROM python:3.9-slim as base

# Set environment variables
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

FROM base AS python-deps

# Copy requirements to the container
COPY Pipfile Pipfile.lock ./
COPY ./src /src

# Install pipenv and compilation dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    pip install --upgrade pip && \
    pip install pipenv && \
    PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy && \
    useradd --create-home appuser

FROM base AS runtime

COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
WORKDIR /home/appuser
USER appuser

# Install application into container
COPY . .

EXPOSE 8000

# Run the application
# ENTRYPOINT ["python", "-m", "http.server"]
# CMD ["--directory", "directory", "8000"]
