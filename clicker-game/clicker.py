import turtle

wn = turtle.Screen()
wn.title("Slug Clicker 3000!")
wn.bgcolor("black")

wn.register_shape("Slugger.gif")

slug = turtle.Turtle()
slug.shape("Slugger.gif")
slug.speed(0)

clicks = 0

click_count = turtle.Turtle()
click_count.hideturtle()
click_count.color("white")
click_count.penup()
click_count.goto(0, 200)
click_count.write(f"🐌 Slug Taps: {clicks} 🐌", align="center",
                  font=("Courier New", 32, "normal"))

title = turtle.Turtle()
title.hideturtle()
title.color("green")
title.penup()
title.goto(0, 325)
title.write("SLUG CLICKER 3000!", align="center",
            font=("Comic sans", 56, "bold"))

slogan = turtle.Turtle()
slogan.hideturtle()
slogan.color("yellow")
slogan.penup()
slogan.goto(0, 250)
slogan.write("Go Get'em SLUGGER!", align="center",
            font=("Courier New", 48, "bold", "italic"))


def clicked(x, y):
    global clicks
    clicks += 1
    click_count.clear()
    click_count.write(f"🐌 Slug Taps: {clicks} 🐌", align="center",
                      font=("Courier New", 32, "normal"))


slug.onclick(clicked)

wn.mainloop()
