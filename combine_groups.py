# Libraries
import pandas as pd

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

# Construct the complete HTML with jQuery Data tables
# You can enable or disable paging or enable y scrolling below
html = f"""
<html>
  <head>
    <link rel="stylesheet" href="https://cdn.datatables.net/2.0.8/css/dataTables.dataTables.css" />
    <style>
      body {{
        font-family: "Calibri", sans-serif;
        font-size: 12px;
      }}
      h1 {{
        font-family: "Calibri", sans-serif;
        text-align: center;
      }}
      table {{
        width: 80%;
        border-collapse: collapse;
        border: 1px solid #ccc;

      }}
      th {{
        background-color: #f2f2f2;
        padding: 5px;
        border: 1px solid #ccc;
        text-align: center;
      }}
      td {{
        padding: 5px;
        border: 1px solid #ccc;
        text-align: center;
      }}
    </style>
    <title>Euro 2024 Combined Group Stage Table</title>
  </head>
  <body>
    <h1>Euro 2024 Combined Group Stage Table</h1>
    {table_html}
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