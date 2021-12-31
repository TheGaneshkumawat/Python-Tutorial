import matplotlib.pyplot as plt, mpld3
import pandas as pd
  
  
# Initialize the lists for X and Y
data = pd.read_csv('D:\\Ganesh\\study\\Practice\\Python\\Python-Tutorial\\resources\\output.csv')
  
df = pd.DataFrame(data)
  
X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 2])
  
# Plot the data using bar() method
plt.bar(X, Y, color='g')
plt.title("Health Ping")
plt.xlabel("URLs")
plt.ylabel("Status")
  
# Show the plot
#plt.show()
my_html = mpld3.fig_to_html(plt.figure(), d3_url=None, mpld3_url=None, no_extras=False, template_type='general', figid=None, use_http=False, include_libraries=True)

with open('output.html', 'w') as html:
    html.write(my_html)

#mpld3.show()