FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the application files into the container
COPY app.py /app/

# Install required dependencies
RUN pip install flask

# Expose the application port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
