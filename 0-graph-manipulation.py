import matplotlib.pyplot as plt
import seaborn as sns

sns.set_context('poster')  #Everything is larger
sns.set_context('paper')  #Everything is smaller
sns.set_context('talk')  #Everything is sized for a presentation

matplotlib.rcParams['font.family'] = "serif" # changes font family

# Styles
import matplotlib.style as style style.available
style.available

style.use('seaborn-poster') #sets the size of the charts
style.use('ggplot')

# ['seaborn-dark',
#  'seaborn-darkgrid',
#  'seaborn-ticks',
#  'fivethirtyeight',
#  'seaborn-whitegrid',
#  'classic',
#  '_classic_test',
#  'seaborn-talk',
#  'seaborn-dark-palette',
#  'seaborn-bright',
#  'seaborn-pastel',
#  'grayscale',
#  'seaborn-notebook',
#  'ggplot',
#  'seaborn-colorblind',
#  'seaborn-muted',
#  'seaborn',
#  'seaborn-paper',
#  'bmh',
#  'seaborn-white',
#  'dark_background',
#  'seaborn-poster',
#  'seaborn-deep']

sns.set_style("darkgrid")