from rpy2 import rpy2
from rpy2 import robjects

from rpy2.robjects.packages import importr
# import R's "rnrfa" package
rnrfa = importr('rnrfa')