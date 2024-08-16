# Libraries
import pandas as pd
from bs4 import BeautifulSoup

# Scrape the tables data
url = 'https://www.bbc.co.uk/sport/football/european-championship/table'
tables = pd.read_html(url)

# Combine the tables
all_teams = pd.concat(tables[:6], ignore_index=True)

# Modify column names and sort by Points, GD and GF
columns={'Goals For': 'GF', 'Goals Against': 'GA', 'Goal Difference': 'GD',
    'Form, Last 6 games, Oldest first': 'Form'}
all_teams.rename(columns=columns, inplace=True)
all_teams = all_teams.sort_values(by=['Points', 'GD', 'GF'], ascending=False)

# Reset the index as the sorted positions
all_teams = all_teams.reset_index(drop=True)
all_teams.index = range(1, len(all_teams) + 1)

# Select and arrange the columns
columns = ['Team', 'Played', 'Won', 'Drawn', 'Lost', 'GF',
       'GA', 'GD', 'Points']
all_teams = all_teams[columns]
all_teams.columns = columns

# Create table HTML
table_html = all_teams.to_html(table_id='all-teams-table', classes=['display', 'nowrap'])

# Manipulate the HTML using Beautiful Soup
soup = BeautifulSoup(table_html, 'html.parser')

# Find the index column (first <th> in each row) and replace <th> with <td>
for row in soup.find_all('tr')[1:]:  # Exclude the top row
  first_th = row.find('th')
  if first_th:
    first_td = soup.new_tag('td')
    first_td.string = first_th.get_text()
    first_th.replace_with(first_td)

# Want to hide some of these columns on mobile devices
# Get table headers
table_headers = [th.get_text(strip=True) for th in soup.select('#all-teams-table thead th')]

# Define the columns to hide
columns_to_hide = ['Played', 'Won', 'Lost', 'Drawn', 'GF', 'GA']

# Function to find the column index by header name
def get_column_index(header_name):
  if header_name in table_headers:
    return table_headers.index(header_name)
  return None

# Add 'hide-on-mobile' class to the specified columns
for th in soup.find_all('th'):
  for col in columns_to_hide:
    if col in th.contents:
      th['class'] = th.get('class', []) + ['hide-on-mobile']
    
# Add class to all <td> elements in the column
for row in soup.find_all('tr')[1:]:  # Skip the header row
  tds = row.find_all('td')
  for col in columns_to_hide:
    col_index = table_headers.index(col)
    tds[col_index]['class'] = tds[col_index].get('class', []) + ['hide-on-mobile']

# Convert the modified BeautifulSoup object back to HTML
table_html = str(soup)

# Construct the complete HTML with jQuery Data tables
# You can enable or disable paging or enable y scrolling below
html = f"""
<html>
  <head>
    <link rel="stylesheet" href="https://cdn.datatables.net/2.0.8/css/dataTables.dataTables.css" />
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      body {{
        font-family: "Calibri", sans-serif;
        font-size: 12px;
      }}
      h1 {{
        font-family: "Calibri", sans-serif;
        text-align: center;
      }}
      .table-container {{
        max-width: 100%;
        overflow-x: auto;
      }}
      table {{
        font-size: 1em;
        width: 100%;
        border-collapse: collapse;
        border: 1px solid #ccc;

      }}
      th {{
        background-color: #f2f2f2;
        padding: 5px;
        border: 1px solid #ccc;
        text-align: center;
        width: auto;
      }}
      td {{
        padding: 5px;
        border: 1px solid #ccc;
        text-align: center;
        width: auto;
      }}
      /* CSS for hiding columns on mobile */
      @media only screen and (max-width: 768px) {{
        th, td {{
          padding: 6px; 
        }}
        .hide-on-mobile {{
          display: none;
        }}
      }}
    </style>
    <title>Euro 2024 Combined Group Stage Table</title>
  </head>
  <body>
    <h1>Euro 2024 Combined Group Stage Table</h1>
    <div class="table-container">
      {table_html}
    </div>
    <script type="text/javascript" src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.datatables.net/2.0.8/js/dataTables.js"></script>
    <script>
      $(document).ready( function () {{
      $('#all-teams-table').DataTable({{"paging": false}});
      }} );
    </script>
  </body>
</html>
"""

# Write HTML to file
text_file = open('index.html', 'w')
text_file.write(html)
text_file.close()