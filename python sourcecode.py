# encoding:utf8
import sys
import re
import os
import psutil # if this makes an error, you need to install the psutil package on your system
import time

maxmem = 0
def showMemTime(when='Resources'):
  global maxmem
  # memory and time measurement
  process = psutil.Process(os.getpid())
  mem = process.get_memory_info()[0] / float(2 ** 20)
  maxmem = max(maxmem, mem)
  ts = process.get_cpu_times()
  sys.stderr.write("{when:<20}: {mb:4.0f} MB (max {maxmb:4.0f} MB), {user:4.1f} s user, {system:4.1f} s system\n".format(
    when=when, mb=mem, maxmb=maxmem, user=ts.user, system=ts.system))

class BigramCounter:
  def __init__(self):
    # initialize storage dictionary (datatype of {} is 'dict')
    self.bigrams = {}

  def count(self, word):
    # make bigram (datatype of (,) is 'tuple')
    for idx in range(1,len(word)):
      self.registerBigram(word[idx-1:idx+1])

  def registerBigram(self, bigram):
    # increase count for this sequence by one
    if bigram not in self.bigrams:
      # if it was not yet in the dictionary
      self.bigrams[bigram] = 1
    else:
      # if it was already in the dictionary
      self.bigrams[bigram] += 1

  def display(self):
    showMemTime('begin display')

    # build list of all frequencies and bigrams
    bigram_freq = list(self.bigrams.items())
    showMemTime('after items')

    # sort that list by frequencies (i.e., second field), descending
    print("sorting ...")
    bigram_freq.sort(key = lambda x:x[1], reverse = True)
    showMemTime('after sorting')

    # iterate over the first five (or less) elements
    print("creating output ...")
    for bigram, occurred in bigram_freq[0:5]:
      try:
        # python 2
        bigram = unicode.encode(bigram, 'utf8')
      except:
        pass
      print("bigram '%s' occured %d times" % (bigram, occurred))

class TrigramCounter:
  def __init__(self):
    # initialize storage dictionary (datatype of {} is 'dict')
    self.trigrams = {}

  def count(self, word):
    # make bigram (datatype of (,) is 'tuple')
    for idx in range(2,len(word)):
      self.registerTrigram(word[idx-2:idx+1])

  def registerTrigram(self, trigram):
    # increase count for this sequence by one
    if trigram not in self.trigrams:
      # if it was not yet in the dictionary
      self.trigrams[trigram] = 1
    else:
      # if it was already in the dictionary
      self.trigrams[trigram] += 1

  def display(self):
    showMemTime('begin display')

    # build list of all frequencies and trigrams
    trigram_freq = list(self.trigrams.items())
    showMemTime('after items')

    # sort that list by frequencies (i.e., second field), descending
    print("sorting ...")
    trigram_freq.sort(key = lambda x:x[1], reverse = True)
    showMemTime('after sorting')

    # iterate over the first five (or less) elements
    print("creating output ...")
    for trigram, occurred in trigram_freq[0:5]:
      try:
        # python 2
        trigram = unicode.encode(trigram, 'utf8')
      except:
        pass
      print("trigram '{}' occured {:>5} times".format(trigram, occurred))

# this is our main function
def main():
  # make sure the user gave us a file to read
  if len(sys.argv) != 2:
    print("need one argument! (file to read from)")
    sys.exit(-1)
  filename = sys.argv[1]

  showMemTime('begin') # let's observe where we use our memory and time

  # read input file
  print("reading from file "+filename)
  inputdata = open(filename,'r').read()
  try:
    # python 2: manual unicode
    inputdata = unicode(inputdata, encoding='utf8')
  except:
    # python 3: unicode per default
    pass
  showMemTime('after reading')

  # split on all newlines and spaces
  print("splitting")
  inputwords = re.split(r' |\n',inputdata)
  showMemTime('after splitting')

  # remove empty strings
  inputwords = list(filter(lambda x: x != '', inputwords))
  showMemTime('after filtering')

  # initialize bigram counter
  bc = BigramCounter()
  tc = TrigramCounter()

  # go through all words
  print("going over words")
  for idx, token in enumerate(inputwords):
    # let's show resources after all 50 K words
    if idx % 50000 == 49999:
      showMemTime('counting {} of {}'.format(idx+1, len(inputwords)))

    bc.count(token)
    tc.count(token)

  showMemTime('after counting')
  print("bigrams:")
  bc.display()
  print("trigrams:")
  tc.display()

main()
showMemTime('at the end')