import nextcord
from nextcord import Interaction, SlashOption
from nextcord.ext import activities, commands

bot = commands.Bot(command_prefix="$")

token = "token here"

@bot.event
async def on_ready():
    print(f"Discord Bot - Dev. Info. "
          f"On NextCord, "
          f"Bot name = {str(bot.user)}, "
          f"Bot ID = {bot.user.id}, "
          f"Bot token = {token}, "
          f"By Not_JustFime")

@bot.slash_command(description="Ping command")
async def ping(interaction: Interaction):
    await interaction.response.send_message("Pong!")


class report(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Test Modal",
            timeout=5 * 60,  # 5 minutes
        )

        self.name = nextcord.ui.TextInput(
            label="Username of violator",
            min_length=2,
            max_length=50,
        )
        self.add_item(self.name)

        self.description = nextcord.ui.TextInput(
            label="Description",
            style=nextcord.TextInputStyle.paragraph,
            placeholder="Tell us more about rule`s violation. Don`t forget to include screenshots.",
            required=True,
            max_length=1800,
        )
        self.add_item(self.description)

    async def callback(self, interaction: nextcord.Interaction) -> None:
        channel = bot.get_channel(960200294703177799)
        response = f"Violator - {self.name.value}."
        if self.description.value != "":
            response += f"\nViolation - {self.description.value}\n By - {interaction.user}"
        await channel.send(response)


@bot.slash_command(
    name="report",
    description="Send report."
)
async def send(interaction: nextcord.Interaction):
    modal = report()
    await interaction.response.send_modal(modal)


bot.run("token here")