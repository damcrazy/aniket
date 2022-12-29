from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


def euclidean(a,b,ax=1):
  return np.linalg.norm(a-b,axis=ax)