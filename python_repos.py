
#GitHub API


import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


#make api call and store response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print 'status code:', r.status_code


#store response in variable
response_dict = r.json()
print "total repositories:", response_dict['total_count']


#explore information about repositories
repo_dicts = response_dict['items']
print "repositories returned:", len(repo_dicts)



#pull values for keys in repo_dict
#print '\nInformation about each repository:'
names, plot_dicts = [], []
for repo_dict in repo_dicts:
        names.append(repo_dict['name'])

        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink': repo_dict['html_url'],#turn each bar into active link
        }
        plot_dicts.append(plot_dict)



#make visualization
my_style = LS('#333366', base_style=LCS)

chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')


my_config = pygal.Config()#instance of pygals config class
my_config.x_label_rotation = 45
my_config.show_legend = False#plotting only one series on chart
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15#shorten longer names to 15 characters
my_config.show_y_guides = False#hide horizontal lines
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')



#each repository
repo_dict = repo_dicts[0]
print '\nkeys:', len(repo_dict)
for key in enumerate(sorted(repo_dict.keys())):
    print key

"""
print 'Name:', repo_dict['name']
print 'Owner:', repo_dict['owner']['login']
print 'Stars:', repo_dict['stargazers_count']
print 'Repository:', repo_dict['html_url']
print 'Created:', repo_dict['created_at']
print 'Updated:', repo_dict['updated_at']
print 'Description:', repo_dict['description']
"""