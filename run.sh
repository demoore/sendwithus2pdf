#!/usr/bin/env sh
# Build the container
echo "Building the container..."
docker build -t sendwithus2pdf .

# Run it
echo "Generating PDFs..."
docker run -v $(pwd):/app --env-file=.env -it sendwithus2pdf

echo "Complete!"
