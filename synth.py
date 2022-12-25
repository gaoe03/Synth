import discord
import requests
from discord.ext import commands
from keys import discord_private_key, private_textsynth_api_key
import asyncio


# create a Bot instance with all intents enabled
bot = commands.Bot(command_prefix='@', intents=discord.Intents.all())
textsynth_engine = chosen_engine = 'gptneox_20B' #default engine is GPT3


textsynth_api_key = private_textsynth_api_key
textsynth_api_url = "https://api.textsynth.com"


def generate_text(input_text, chosen_engine):
  print("The chosen input was {} and the chosen engine was {}".format(input_text, chosen_engine))
  endpoint = f"{textsynth_api_url}/v1/engines/{chosen_engine}/completions"

  headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {textsynth_api_key}'
  }

  data = {
    "prompt": input_text,
    "max_tokens":500,
  }

  response = requests.post(endpoint, headers=headers, json=data)

  if response.status_code == 200:
    return response.json()['text']
  else:
    print("Error:", response.status_code, response.text)
    return "Something went wrong while compiling your response. Try again."


def creditsleft(theapi):
  endpoint = 'https://api.textsynth.com/v1/credits'
  response = requests.get(endpoint, headers={'Authorization': 'Bearer ' + theapi})
  if response.status_code == 200:
    credits = response.json()['credits']
    return (f'You have {credits} credits remaining.')
  else:
    print("Error:", response.status_code, response.text)
    return "Something went wrong while trying to get your balance. Try again."



timer = 0
lines = ["Current engines:", "**E1**: gptneox_20B. ``GPT-NeoX-20B`` is the largest publically available English language model with 20 billion parameters. It was trained on the same corpus as GPT-J.", 
        "**E2**: gptj_6B: ``GPT-J`` is a language model with 6 billion parameters trained on the Pile (825 GB of text data) published by EleutherAI. Its main language is English but it is also fluent in several other languages. It is also trained on several computer languages.",
        "**E3**: codegen_6B_mono: ``CodeGen-6B-mono`` is a 6 billion parameter model specialized to generate source code. It was mostly trained on Python code.",
        "**E4**: fairseq_gpt_13B: ``Fairseq GPT 13B`` is an English language model with 13 billion parameters. Its training corpus is less diverse than GPT-J but it has better performance at least on pure English language tasks.",
        "**E5**: m2m100_1_2B: ``M2M100 1.2B`` is a 1.2 billion parameter language model specialized for translation. It supports multilingual translation between 100 languages."]


@bot.event
async def on_message(message):
    global timer
    global lines
    
    #HELP COMMANDS
    if message.content.startswith('wwhelp'):
        lines = ["Current bot commands:", 
        "Send ``ping`` to find the bot latency", 
        "Send ``gen [text]`` for an AI to complete your text", 
        "Send ``wwengines`` to see the list of engines", 
        "Send ``wwcredits`` to view how many TextSynth credits you have left",
        "Send ``wwhelp`` to see the list of commands again", 
        "\nCreated by Alpha#9999"]
        await message.channel.send('\n'.join(lines))
    #ENGINE COMMAND
    if message.content.startswith('wwengines'):
      lines = ["Current engines:", "**E1**: gptneox_20B. ``GPT-NeoX-20B`` is the largest publically available English language model with 20 billion parameters. It was trained on the same corpus as GPT-J.", 
        "**E2**: gptj_6B: ``GPT-J`` is a language model with 6 billion parameters trained on the Pile (825 GB of text data) published by EleutherAI. Its main language is English but it is also fluent in several other languages. It is also trained on several computer languages.",
        "**E3**: codegen_6B_mono: ``CodeGen-6B-mono`` is a 6 billion parameter model specialized to generate source code. It was mostly trained on Python code.",
        "**E4**: fairseq_gpt_13B: ``Fairseq GPT 13B`` is an English language model with 13 billion parameters. Its training corpus is less diverse than GPT-J but it has better performance at least on pure English language tasks.",
        "**E5**: m2m100_1_2B: ``M2M100 1.2B`` is a 1.2 billion parameter language model specialized for translation. It supports multilingual translation between 100 languages."]
      await message.channel.send('\n\n'.join(lines))

    #PING
    if message.content.startswith('ping'):
        await message.channel.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

    #TEXTSYNTH
    
    if message.content.startswith('wwcredits'):
      await message.channel.send(creditsleft(textsynth_api_key))

    if message.content.startswith('gen'):
      
      #ENGINE CHECKER
      await message.channel.send("Which Engine? Default is E1. For more info, type ``wwengines``. ")
      # Wait for the user's response with a timeout of 60 seconds
      try:
        response = await bot.wait_for("message", check=lambda m: m.author == message.author, timeout=60.0)
      except asyncio.TimeoutError:
      # If the user does not respond within 60 seconds, return without generating text
         await message.channel.send("``Timed out.``")
      # Check the user's response and set the engine accordingly
      if response.content.lower() in ["e1", "e2", "e3", "e4", "e5"]:
        chosen_engine = {"e1": "gptneox_20B", "e2": "gptj_6B", "e3": "codegen_6B_mono", "e4": "fairseq_gpt_13B", "e5": "m2m100_1_2B"}[response.content.lower()]
      if response.content.lower() == "cancel":
        await message.channel.send("Operation cancelled.")
        return
      if response.content.lower() == "wwengines":
        await message.channel.send("``Operation cancelled. Try again by typing gen [query]``")
        return

      elif response.content.lower() != "wwengines":
        while response.content.lower() not in ["e1", "e2", "e3", "e4", "e5", "cancel"]:
           await message.channel.send("``Invalid option. Please choose a valid engine (E1, E2, E3, E4, or E5) or type 'cancel' to cancel the operation``")
           try: 
            response = await bot.wait_for("message", check=lambda m: m.author == message.author, timeout=60.0)
           except asyncio.TimeoutError:
            await message.channel.send("``Timed out.``")
            return
        if response.content.lower() in ["e1", "e2", "e3", "e4", "e5"]:
          chosen_engine = {"e1": "gptneox_20B", "e2": "gptj_6B", "e3": "codegen_6B_mono", "e4": "fairseq_gpt_13B", "e5": "m2m100_1_2B"}[response.content.lower()]
        if response.content.lower() == "cancel":
          await message.channel.send("``Operation cancelled.``")
          return


      
      
      timer= timer+1
      print("The generate text command was used for the {}{} time!".format(timer, (lambda x: "st" if x == 1 else "nd" if x == 2 else "rd" if x == 3 else "th")(timer % 10)))
      # Extract the text to be generated from the message
      text_to_generate = message.content[len('gen'):].strip()
      # Generate the text using your text generation function
      generated_text = generate_text(text_to_generate, chosen_engine)
      # Send the generated text back to the channel in 2000 character chunks
      for i in range(0, len(generated_text), 1999):
           await message.channel.send("```" + generated_text[i:i+1800] + "```")

bot.run(discord_private_key)
    