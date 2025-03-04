"name" = "Beacha"
"description" = "Chat with people around the world! An chat app professionaly made."
"version" = "1.0.0"

"DATABASE" = [
  name({ACC_NAME.input})
  password({ACC_PASS.input})
]

"Booster_LVL" = [
  "LVL_1" = [2],
"LVL_2" = [7],
"LVL_3" = [10]
]

"Booster_rewards" = [
  "LVL_1" = ["Animated Server Icon", "Server Invite Banner", "Bot with free status", "50 Roles", "150 Channels"]
  "LVL_2" = ["Server Banner", "Custom Role Icon", "More Permissions", "300 Channels", "100 Roles", "10 Free bots"]
  "LVL_3" = ["NSFW Channels", "Custom Invite", "Animated Role Icon", "Role Gradient", "100 free bots (50 with custom status)", "Infite Channels", "300 Roles", "Animated Invite banner", "Animated server banners"]
]
"Created_servers" = [
  name("Beacha General")
  description("The official Beacha support!")
  boost_lvl("LVL_3")
  verified(True)
  server_id = 1
]

"Verified_servers" = [
  server_id(1)
]
