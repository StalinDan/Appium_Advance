import yaml

file = open('familyInfoYmal')
data = yaml.load(file)
print(data)

print('丈夫姓名：%s \n妻子姓名：%s \n第一个孩子姓名：%s \n第二个孩子姓名：%s'\
      %(data['name'],data['spouse']['name'],data['children'][0]['name'],data['children'][1]['name']))