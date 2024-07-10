from tkinter import *

window = Tk()

fire_png = PhotoImage(file='fire.png')
fire = fire_png.subsample(10,10)
fire_label = Label(image=fire)
fire_label.pack()

def temperature():
    print('The temperature is: '+ str(scale.get()) + ' degrees C')

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=('Impact',30,'bold'),
              tickinterval=10,
              resolution=.5,
              )
scale.pack()

snow_flake = PhotoImage(file='snowflake.png')
snow = snow_flake.subsample(5,5)
snow_label = Label(image=snow)
snow_label.pack()

button = Button(window,
                text='submit',
                command=temperature)
button.pack()

window.mainloop()