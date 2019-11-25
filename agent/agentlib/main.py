#!/usr/bin/python

"""simple script to get info from 'top' linux command."""


from subprocess import Popen, PIPE


class Agent:

  def __init__(self):
    self.output_file = '/tmp/agent_output'
    self.splitter = 'PID USER'

  def shell_command(self, cmd):
    """method to execute linux command in the shell""
    try:
      cmd_run = Popen(cmd, stderr=PIPE, stdout=PIPE, shell=True)
      out, err = cmd_run.communicate()
      if err:
        print(f'error during execution:\n{err})
        return False
      return True
    except Exception as e:
      print(f'Exception have happened:\n{e}')

  def parse_output(self, cmd_out):
    """method to parse output of the shell command."""
    result = []
    with open(self.output_file) as f:
      for index, line in enumerate(f):
        if self.splitter in line:
          break
      result = f.readlines[index+1:]
    return result

  def run_top_command(self):
    """actual test#1"""
    cmd = f"top -b 1 -n 1 -c > {self.agent_output}"
    cmd_out = self.shell_command(cmd)
    if cmd_out:
      result = self.parse_output()




def main():
    print("hello world")


