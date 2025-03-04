import account_DataBase(
  "NAME" = {ACC_NAME}
  "PASSWORD" = {ACC_PASS}
)
import name(login)
  add.new(frame)
frame.name("BackGround")
BackGround.color(grey)
background.size(864, 642)
BackGround.location(middle)

add.new(text)
text.name("Title"),
title.location(top.BackGround),
title.text("Log into your account.")

add.new(textbox)
textbox.name(ACC_NAME)
ACC_NAME.placeholder("Enter your account's name.")
ACC_NAME.location(middle.BackGround)

add.new(textbox)
textbox.name(ACC_PASS)
ACC_PASS.placeholder("Enter your account's password.")
ACC_PASS.location(below.ACC_NAME)

add.new(button)
button.name("ACCOUNT_LOGIN")
ACCOUNT_LOGIN.text("Log into your account.")
ACCOUNT_LOGIN.text.color(white)
ACCOUNT_LOGIN.background.color(blue)

if ACCOUNT_LOGIN.pressed = True
new(account_database(
  "NAME" = {ACC_NAME}
  "PASSWORD" = {ACC_PASS}
))

if {ACC_NAME} = used
add.new(text)
text.name("ErrorHandeler")
ErrorHandeler.text("Could not create account. (Account name is used.)")
ErrorHandeler.color(red)
wait(5)
delete.ErrorHandeler = True
