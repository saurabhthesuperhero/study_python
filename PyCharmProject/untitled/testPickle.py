import pickle

colors = ['red', 'green', 'black']

f = open('colors.pickle', 'wb')
pickle.dump(colors, f)
f.close()
