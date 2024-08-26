# Use the official Python image
FROM python:3.9-slim

# Copy the Python script from the B directory in the build context
COPY Hello-world.py .

# Run the Python script
CMD ["python", "Hello-world.py"]
