# The Starting Kit for Order Dispatch and Reposition Competition

This repository is the main **submission template and starter kit**!

```
.
├── samples                 # The sample data passed to your agent during simulation.
├── local_test.py           # A demo of how your agent will be used during simulation.
├── run_local.sh            # Run test in the simulation environment inside docker.
├── environment.yml         # The simulation environment specified in a conda environment file.
├── Dockerfile              # The simulation environment specified in a Dockerfile.
├── README                  # The readme file.
└── model                   # IMPORTANT: Your submission folder.
    └── agent.py            # IMPORTANT: Your implementation of the dispatch and reposition.
```

The `model` folder contains all your submitted files including your implementations and dependencies. The `agent.py` inside the `model` folder is provided for you to base your submission.

The `local_test.py` gives an example of how your submission will be used in the simulation and the `Dockerfile` describes the environment where your `agent.py` will be executed.

Create your submission bundle by zipping the whole folder. Make sure no extra directories are created within the zip, e.g., `zip -j submission.zip model/*`

