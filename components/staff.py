import staff_members(
  user_id(<STAFF_ID>)
)

import staff_commands(
  command.name("web ban")
  command.description("Ban a user from beacha.")
  command.option(
    label(user),
    type(user),
    required(True),

    label(reason),
    type(text),
    required(True),
  )
  if command.used = True,
  embed = embed(,
    title("Banned {user} from Beacha!"),
    description("You have banned {user} from Beacha."),
    embed.color.hex(FF0000),
),
wait(0.1)
remove.web.access({user})
import staff_ranks = [
"owner"(All_permissions),
"Admin"(All_permissions),
"Moderator" ("ban_users", "verify_users"),

"Partner" ("2 Free Boost")
]
