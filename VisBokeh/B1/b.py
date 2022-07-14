from bokeh.plotting import figure, output_file, show
output_file('practice.html')

x1 = [1, 5, 8, 9, 78, 100, 142]
x2 = [5, 8, 58, 78, 65, 90, 120]

p = figure()

p.line(x1, x2, color='red', legend='دمای هوای کرج')
p.circle(x1, x2, color='green', legend='دمای هوای تهران')
p.scatter(x2, x1 ,color='blue', legend='دمای هوای لواسان')
p.line(x2, x1, color='yellow', legend='دمای هوای کرمان')

p.legend.click_policy = 'hide'

show(p)