#!/usr/bin/python

"""simple script to get info from 'top' linux command."""


import json
import time
from subprocess import Popen, PIPE


class Agent:

  def __init__(self, conf_path):
    self.output_file = '/tmp/agent_output'
    self.splitter = 'PID USER'
    self.configurator = self.get_config(conf_path)

  def get_config(self, conf_path):
    result = {}
    with open(conf_path) as f:
      try:
        result = json.loads(f.read())
      except:
        print('BAD FORMAT')
    return result

  def shell_command(self, cmd):
    """method to execute linux command in the shell"""
    try:
      cmd_run = Popen(cmd, stderr=PIPE, stdout=PIPE, shell=True)
      out, err = cmd_run.communicate()
      if err:
        print(f'error during execution:\n{err}')
        return False
      return True
    except Exception as e:
      print(f'Exception have happened:\n{e}')

  def parse_output(self):
    """method to parse output of the shell command."""
    result = []
    with open(self.output_file) as f:
      for index, line in enumerate(f):
        if self.splitter in line:
          break
      result = f.readlines()[index+1:]
    return result

  def run_top_command(self):
    """actual test#1"""
    cmd = f"top -b 1 -n 1 -c > {self.output_file}"
    cmd_out = self.shell_command(cmd)
    if cmd_out:
      result = self.parse_output()

  def runner(self):
    """actual entry point."""
    try:
      time_cycle = self.configurator['config']['time_interval']
    except:
      raise(f'BAD CONFIG:\n{self.configurator}')
    while True:
      self.run_top_command()
      time.sleep(time_cycle)

def main():
  conf_path = '/tmp/agent_config.json'
  a = Agent(conf_path)
  a.runner()
