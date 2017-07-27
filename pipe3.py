#------------------------- pipe3.py -------------------------
'''This is a partial implementation of Pipelines in Python. It supports a subset of Pipelines features.
 It uses a variety of somewhat advanced Python techniques.

 A pipeline starts with a user-written "specification". Example:
 readfile file1.txt | locate /apple/ | writefile file2.txt
 Interpretaton:
   "|" is the stage separator character. A specification is of the form:
     stage | stage | ...
    each stage is of the form:
      stage name stage specification where stage name is the first word
  So the above user-written "specification" means:
  
   stage         stage               stage             more stage
   name          function            spectification    function 
   ----       --------------------  --------------   --------------------------------
   readfile   read a record from      file1.txt      pass record to the locate stage
   locate     if record contains      apple          pass record to the > stage
   writefile  write the record to     file2.txt
   
   repeat above till file1.txt reaches EOF.
   Close files.
Note < file1.txt | locate /apple/ | > file2.txt also works, as < and > are defined as aliases
for readfile and writefile.

Note:
  Each stage starts with a stage name (e.g. <). A stage name is one word (i.e. contains no blanks)
  Following the stage name and one blank, up to the "|" or end of line is the stage specification.
  This is any additional information the stage needs to do ite job.

One way to run a pipeline is to enter at the command prompt:
$ pipe3.py "< file1.txt | locate /apple/ | > file2.txt"
pipe3.py "scans" the specification:
  splits it it into stages at the "|"
  splits each stage at the firsst blank into stage name and stage specs
  creates a instance of each stage's class
  passes the stage specification to stage.setup() which, as needed,  parses it, reports errors, saves relevant values
  connects stages in a chain such that each can call the next
 If all goes well a pipeLine instance is ready to run. It can be run many times.
 The pipeLine run method calls the run method of the first stage.
 Each calls the run methid of the next, passing one record each time.
 When the last stage is reached it (usually) sends the record to some destination, then terminates.
   This returns control, stage by stage, to the first stage.
 if first stage run method is in a loop, repeats above until out of input.

Classes:
class Stage is the superclass of all stage classes.
classes Readfile,Locate and Writefile are the classes for the stages in the tests.
class Messages: is a mix-in class for classd Stage and class Pipeline, managing Informative, Warning and Error messages.

An instance of class PipeLine is a collection of instances of various stage classes. It:
  scans the specification
  creates stage instances
  connects them
  runs the pipeline
class PipeLineSet is a container for PipeLine instances. More advanced pipe programs implement muitiple pipelines,
each of which is a PipeLine instance.'''

class Messages():
  # messages follow the format of the IBM Mainframe version
  def message(self, msgNo, *args):
    messages = {}
    messages[60] = "E", "FPLPAT060E Delimiter missing after string %s"
    messages[112] = "E", 'FPLPAT112E Excessive options "%s"'
    
    appendix = """FPLSCA003I ... Issued from stage %s of pipeline %s
FPLSCA001I ... Running %s"""

    sev, msg = messages[msgNo]
    line1 = msg % args
    line2 = appendix % (self.stageNo, self.pipeLine.pipeLineNo, self.fullSpec)
    print(line1)
    print(line2)

class Stage(Messages):
  """superclass of all stage classes"""
  alias = None # override as needed
  RC = 0 

  def __init__(self, stageNo, pipeLine, fullSpec):
     self.stageNo = stageNo
     self.pipeLine = pipeLine
     self.fullSpec = fullSpec
     self.RC = 0 

  def output(self, record): raise NotImplementedError
    # must be replaced by the next stage's run method

  def run(self): raise NotImplementedError
    # must be overridden in subclasses of Stage

# Stage classes follow. Each is preceded by @addToDict decorator
'''A decorator is a function:
     - Its name, preceeded by @, appears on the line before a def or class statement;
     - The last step in the def / class statement is a call to the decorator
       function with the function / class object passed as the only parameter;
     - The decorator can do anything; whatever it returns is assigned to the
       name of the function / class being defined. Example:
       
       @dec
       def foo():
         function body

      is equivalent to

       def foo():
         function body
      foo = dec(foo)'''

def addToDict(cls=None, d={}):
  '''- Adds each class.name: class to dictionary d.
     - If there are alias(es) adds each cls.alias : class.
     - returns dictionary when called with no argument'''
  # Note that d={} defines an optional agrument with a default value.
  # The default is created when the def statement is executed.
  # Each call to the function addds a key-value pair to the dictionary.
  # FO: handle abbreviations
  if cls:
    for name in cls.names + cls.aliases:
      d[name] = cls
    return cls
  else:
    return d
  
@addToDict
class Readfile(Stage):
  names = ['READFILE']
  aliases = ['<']
  typ = 'dataSource' # can't use "type" as it is a built-in name.
  def setup(self, specs):
    self.fileName = specs
    return self.RC

  def run(self):
    with open(self.fileName) as f:
      for record in f:
        record = record.strip('\n')
        self.output(record)
      self.output() # detected in writefile - to close the file

@addToDict
class Locate(Stage):
  names = ['LOCATE']
  aliases = []
  typ = 'in_out'
  def setup(self, specs):
    # the stage specification (specs) is a "delimitedString"
    # a delimitedString starts and ends with a delimiter and has no other occurrence
    # of the delimiter.
    # the delimiter is any non-blank character.
    # the rest of the delimitedString is its value.
    # in our example /apple/ is the delimitedString; apple is its value.

    # parse specs to ensure it is a delimitedString and get its value
    self.specs = specs.strip() # ignore any leading or trailing blanks
    if len(self.specs) == 0: # matches no records
      return
    delimiter = self.specs[0] # get the delimiter
    # NOTES regarding messsages:
    #  these are copied from the IBM Pipelines program documentation
      # found at http://vm.marist.edu/~pipeline/authelp.html
    #  in subseaquent versions of this progam messaeges are stored in a sqlite table.
    x = self.specs.find(delimiter, 1) # 2nd occurrence of delimiter?
    if x == -1: # missing
      self.message(60, specs)
      self.RC = 1
    elif x < len(self.specs)-1: # embedded
      self.message(112, specs[x+1:])
      self.RC = 1
    else:
      self.locateString = specs[1:-1]
    return self.RC

  def run(self, record=None):
    if record is None or record.find(self.locateString) >= 0:
      self.output(record)

@addToDict
class Writefile(Stage):
  names = ['WRITEFILE']
  aliases = ['>']
  typ = 'dataSink'

  def setup(self, destFileName ):
    self.destFile = open(destFileName, "w")
    return self.RC

  def run(self, record=None):
    if record is None:
      self.destFile.close()
    else:
      self.destFile .write(record + '\n')

# create dictionary {stageName:stageClass, ...} so we can lookup a stage name from the spec and get the class object
stageDict = addToDict() # retrieve dictionary of stage name : stage class from the decorator

class PipeLineSet(list): # instance is a list of PipeLines
  
  def __init__(self, specs):
    self.startQueue = [] # collection of data source stages.
    # FUTURE: with '?' as the pipeLineSeparator split the spec into pipeLine specs
    # for now:
    self.append(PipeLine(self, specs))

  def run(self):
    for stage in self.startQueue:
      stage.run()# start each data source stage
      # when we add multiple streams each data source stage will run in a thread.
  
class PipeLine(list): # instance is a list of stage instances
  separator = '|'
  pipeLineNo = 1
  RC = 0
  def __init__(self, pipeLineSet, specs):
    self.pipeLineSet = pipeLineSet
    # with '|' as the stage separator split the spec 
    specList = specs.split(self.separator) # e.g. "readfile c:/pipefiles/file1.txt ", "locate /apple/ ", "writefile c:/pipefiles/file2.txt"]
    for stageNo, stage in enumerate(specList, 1):
      # separate the stage name from its specification
      stageName, stageSpecs = stage.split(None, 1) # "e.g. ["readfile", "c:/pipefiles/file1.txt "]
      StageClass = stageDict[stageName.upper()]
      stageInstance = StageClass(stageNo, self, specs)
      self.RC = stageInstance.setup(stageSpecs)
      if self.RC == 0:
        self.append(stageInstance)
        if stageInstance.typ == 'dataSource':
          self.pipeLineSet.startQueue.append(stageInstance)
        if len(self) > 1: # connect to prior stage
          priorStage.output = stageInstance.run
        else:
          priorStage = stageInstance
      else:
        break
    self.pipeLineSet.RC = self.RC

def test():
  # run 1 command line entry or 3 predefined test cases
  import sys
  if len(sys.argv) > 1: # called from command line with a pipe spec passed as the first argument.
    specs = [sys.argv[1]]
  else:
    # 3 test cases
    specs = ["readfile c:/pipefiles/file1.txt | locate /apple/ | writefile c:/pipefiles/file2.txt",  # good spec
             "readfile c:/pipefiles/file1.txt | locate /apple | writefile c:/pipefiles/file2.txt",   # error
             "< c:/pipefiles/file1.txt | locate /apple/e | > c:/pipefiles/file2.txt",                 # error
             "readfile c:/pipefiles/file1.txt | locate /appl/ | writefile c:/pipefiles/file2.txt",] # good spec
  for caseNo, spec in enumerate(specs, 1):
    print('Test case %s -------------------' % (caseNo, ))
    pipeLineSet = PipeLineSet(spec)
    if pipeLineSet.RC == 0:
      pipeLineSet.run()

if __name__ == '__main__':
  test()
#------------------------- end pipe3.py -------------------------