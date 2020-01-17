import sys
import numpy
import os


class ReplicationRatesPlugin:
   def input(self, filename):
      filestuff = open(filename, 'r')
      self.params = dict()
      for line in filestuff:
         contents = line.split('\t')
         self.params[contents[0]] = contents[1].strip()     

   def run(self):
      package = self.params['package']
      self.command = package + " -f " + self.params['fasta']
      if (package == "iRep") or (package == "bPTR"):
         self.command += " -s " + self.params['sam']
      if (package == "bPTR"):
         if ('plots' in self.params):
            self.command += " -plot " + self.params['plots']
         if ('coverage' in self.params and self.params['coverage'] == "yes"):
            self.command += " -m coverage"

   def output(self, filename):
      if (filename != "none"):
         self.command += " -o " + filename
      self.command += " -ff"
      os.system(self.command)

