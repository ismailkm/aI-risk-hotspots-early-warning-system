# Use an official lightweight Python image as a parent image
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container at /app
COPY . .

# Expose the port that Streamlit runs on
EXPOSE 8501

# Run the Streamlit app when the container launches
CMD ["streamlit", "run", "dashboard.py"]