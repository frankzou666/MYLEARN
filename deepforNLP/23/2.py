
import pydot_ng as pydot

import os

os.environ['PATH'] += 'C:/programfile/Graphviz/bin/'

try:
  # pydot-ng is a fork of pydot that is better maintained.
  import pydot_ng as pydot
except ImportError:
  # pydotplus is an improved version of pydot
  try:
    import pydotplus as pydot
  except ImportError:
    # Fall back on pydot if necessary.
    try:
      import pydot
    except ImportError:
      print('error')
      pydot = None


def check_pydot():
  """Returns True if PyDot and Graphviz are available."""
  pydot.Dot.create(pydot.Dot())
  if pydot is None:
    return False
  try:
    # Attempt to create an image of a blank graph
    # to check the pydot/graphviz installation.
    pydot.Dot.create(pydot.Dot())
    return True
  except (OSError, pydot.InvocationException):
    return False


print(check_pydot())