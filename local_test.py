# -*- coding: utf-8 -*-
# @File: local_test.py
# @Author: Xiaocheng Tang
# @Date:   2020-03-17 17:15:49
import os
import sys
import json
from pprint import pformat


# The folder contains your submission
SUBMISSION_DIR = os.path.abspath('model')
# Sample data is provided to illustrate the input data type
# from the simulator to your agent
SAMPLE_DIR = os.path.abspath('samples')


def main(*args, **kwargs):
  # unused arguments
  del args, kwargs

  # Add user submission to the import path
  sys.path.append(SUBMISSION_DIR)
  from agent import Agent

  # Initialize the user-defined agent
  agent = Agent()

  # Read sample observation data and pass it to the agent for computing actions
  # data schema is the same as the one passed to the agent during simulations
  with open(os.path.join(SAMPLE_DIR, 'dispatch_observ'), 'r') as f:
    dispatch_observ = json.load(f)
  with open(os.path.join(SAMPLE_DIR, 'repo_observ'), 'r') as f:
    repo_observ = json.load(f)

  print("Dispatch observation:\n{}".format(pformat(dispatch_observ)))
  # Implement your own dispatch procedures
  dispatch_action = agent.dispatch(dispatch_observ)
  print("Agent dispatch action:\n{}".format(pformat(dispatch_action)))
  print("============================================================")
  print("============================================================")
  print("Reposition observation:\n{}".format(pformat(repo_observ)))
  # Implement your own reposition procedures
  reposition_action = agent.reposition(repo_observ)
  print("Agent reposition action:\n{}".format(pformat(reposition_action)))


if __name__ == '__main__':
  main()
