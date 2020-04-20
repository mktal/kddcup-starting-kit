# The Starting Kit for Learning to Dispatch and Reposition Competition

This repository is the official Learning to Dispatch and Reposition (LDR) Competition **submission template and starter kit**! Clone this to make a new submission!

**Note:** we recommend keeping your clone up-to-date with the upstream before your submission to make sure you receive the latest information about the competition. You could also `watch` this repo so that you are notified whenever there are new updates.

![](http://img-hxy021.didistatic.com/static/outreach/KDD_Cup_1000X500_2020-3-30.jpg)

## Table of contents

* [Quickstart](#quickstart)
* [Implement your own dispatch and reposition agent](#implement-your-own-dispatch-and-reposition-agent)
* [Test your agent locally](#test-your-agent-locally)
* [Get ready for submission](#get-ready-for-submission)
* [Development tips](#development-tips)

**Other Resources**:
- [DiDi Official Announcement](https://outreach.didichuxing.com/competition/kddcup2020/) - Background and overview.
- [LDR Competition Page](https://biendata.com/competition/kdd_didi/) - Main registration page & leaderboard
- [GAIA Open Dataset](https://outreach.didichuxing.com/research/opendata/en/) - Download the competition dataset

**Contact**

Please contact the organizers (kddcup2020@didiglobal.com) if you have any problem concerning this challenge.


```
.
├── samples                 # The sample data illustrating the api of your agent required by the simulator.
├── local_test.py           # A demo of how your agent will be used during simulation.
├── run_local.sh            # Run test in the simulation environment.
├── environment.yml         # The simulation environment specified in a conda environment file.
├── Dockerfile              # The simulation environment specified in a Dockerfile.
├── README                  # The readme file.
└── model                   # IMPORTANT: Your submission folder.
    └── agent.py            # IMPORTANT: Your implementation of the dispatch and reposition.
```

## Quickstart

Clone this repo. Create your submission bundle by zipping the whole `model` folder. Make sure **no extra directories are created within the zip**, e.g., `zip -j submission.zip model/*`. And head over to the [competition website](https://biendata.com/competition/kdd_didi/) for your first submission!

## Implement your own dispatch and reposition agent!

A LDR agent is equipped with two performable actions, `dispatch` and `reposition`, which receive `observations` from the environment, computing order-driver assignment and driver repositioning destinations, respectively.

```python
class Agent(object):
  """ Agent for dispatching and reposition """

  def __init__(self):
    """ Load your trained model and initialize the parameters """
    pass

  def dispatch(self, dispatch_observ):
    """ Compute the assignment between drivers and passengers at each time step
    :param dispatch_observ: a list of dict, the key in the dict includes:
        order_id, int
        driver_id, int
        order_driver_distance, estimated distance between the driver and the order, float
        order_start_location, a list as [lng, lat], float
        order_finish_location, a list as [lng, lat], float
        driver_location, a list as [lng, lat], float
        timestamp, current simulation time, int
        order_finish_timestamp, estimated order finish time, int
        day_of_week, Monday=0, Sunday=6, int
        reward_units, reward received after the order is completed, float
        pick_up_eta, estimated time (in seconds) it takes the driver to pick up the order, float

    :return: a list of dict, the key in the dict includes:
        order_id and driver_id, the pair indicating the assignment
    """
    pass

  def reposition(self, repo_observ):
    """ Compute the reposition action for the given drivers
    :param repo_observ: a dict, the key in the dict includes:
        timestamp: int
        driver_info: a list of dict, the key in the dict includes:
            driver_id: id of the idle driver in the treatment group, int
            grid_id: id of the grid the driver is located at, str
        day_of_week: int

    :return: a list of dict, the key in the dict includes:
        driver_id: id of the idle driver in the treatment group, int
        destination: id of the grid the driver is repositioned to, str
    """
    pass
```

Look into the `agent.py` file inside the `model` folder for more details. The `agent.py` implements a default policy and is provided for you to base your submission. The `model` folder must contain all your submitted files including **the `agent.py` and its dependencies**.

## Test your agent locally

During online evaluation the simulator will look for the `agent.py` file inside your submission bundle and import your `Agent` class. A valid submission requires

- An `agent.py` file in the **first directory level** of your submission bundle after unzipped;
- The `Agent` class structure and function signatures kept unchanged as documented above.

We suggest developing your agent inside the `model` folder. To make sure your agent run correctly in the online evaluation environment, you just need to run

```bash
./run_local.sh
```

It will launch a docker environment, import your model and call your agent on a sample dataset provided for you as a quick test before the submission.

In particular, the `local_test.py` gives an example of how your submission will be used in the simulation and the `Dockerfile` describes the environment where your `agent.py` will be executed.

## Get ready for submission

When you are ready to submit, zip the `model` folder while making sure no extra directories are created within the zip, e.g., go inside the `model` folder and run `zip -r ../submission.zip . -x '*.git*' -x '*__pycache__*'` which creates your submission bundle `submission.zip` just outside of the `model` folder.

Finally head over to the [competition website](https://biendata.com/competition/kdd_didi/) to see how your algorithm performs!

## Development tips

#### Test your agent locally first before online submission

Online evaluation puts a limit on number of submissions per day and provides only rudimentary error messages for security reasons. The purpose of this repo is thus to provide you with a local testing environment so that you can eliminate most of errors without the need for online submission. Also in local testing you get access to the full stack trace and much faster feedback. This can save you a lot of time debugging. Please make use of it as much as possible. 

#### Enhance your agent with your offline trained `modelfile`

Suppose your `model` directory looks like this, where `modelfile` resides next to the `agent.py` inside the `model` folder
```
├── model
    └── agent.py
    └── modelfile
```
You can use code like below to load the `modelfile` into your agent
```python
import os
MODEL_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'modelfile')
class Agent(object):
  def __init__(self):
    self._load(MODEL_PATH)
  def _load(self, modelpath):
    """ Implement your model loading routine """
    pass
```

#### Debug using the error messages

We currently do not provide stack trace for security reasons. We do provide error messages with error types defined for each case involving the `Agent`:

- `InitAgentError` when there are exceptions from `Agent.__init__`
- `DispatchAgentError` when there are exceptions from `Agent.dispatch`
- `RepositionAgentError` when there are exceptions from `Agent.reposition`




