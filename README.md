# sendwithus2pdf

_**CAVEAT EMPTOR**: This is not offically supported by Sendwithus_

This script leverages the [Sendwithus API](https://support.sendwithus.com/api/)
to convert templates to PDF files. It assumes that you have
[Docker](https://docs.docker.com/engine/install/) installed.

## Running
First, add your Sendwithus API key into a `.env` file (see `.env.example`).

Next, run the `run.sh` script:

```sh
$ ./run.sh
```

Docker will pull in all the dependicies and start running the Python script.
When it's done you should find your PDFs in the `out/` directory
