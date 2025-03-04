import name = "Sign up"
    add.new(frame)
frame.color(grey)
frame.name("SignupFrame")
SignupFrame.transparency = 0.3
Signup.location = Middle
Signup.size(864, 642)

 add.new(text)
text.name  = "Title"
Title.color = blue
title.text = "Create your account."

add.new(textbox)
textbox.name = "ACC_NAME"
ACC_name.placeholder = "Your new account name."
ACC_NAME.color = white
required(True)

add.new(textbox)
textbox.name = "ACC_PASS"
ACC_PASS.placeholder = "Your account's password."
ACC_PASS.color = white
required(True)


add.new(button)
button.name = "CREATE_ACC"
CREATE_ACC.text = "Create Account"
if CREATE_ACC.pressed = True
new.database(
    name=ACC_NAME.input
    password=ACC_PASS.input
)

if ACC_NAME.used = True
add.new(text="Account name is used!")
if ACC_PASS = "Password", "1234"
add.new(text)
text.name = "ErrorHandeler"
ErrorHandeler.text = "Password is to plain."
wait(10)
destroy(ErrorHandeler)
