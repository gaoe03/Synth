<h1>TextSynth Discord Bot</h1>

<p>My code creates a Discord bot that integrates with the TextSynth API, a service that allows you to generate text using artificial intelligence. The bot has several commands that allow users to interact with it.</p>

<h2>Dependencies</h2>
<p>This project relies on the following libraries:</p>
<ul>
  <li>discord</li>
  <li>requests</li>
</ul>

<h2>Usage</h2>
<p>To use the project, follow these steps:</p>
<ol>
  <li>Set up a bot environment in Discord, and obtain the bot key.</li>
  <li>Modify the textsynth_api_key and discord_private_key variables in the keys.py file with your own keys.</li>
  <li>Run synth.py</li>
  <li>Type <code>wwhelp</code> for a list of supported commands.</li>
</ol>

<h2>Commands</h2>
<p>The discord bot has the following commands:</p>
<ul>
  <li><code>wwhelp</code>: displays a list of all available bot commands.</li>
  <li><code>wwengines</code>: lists the available engines that can be used to generate text.</li>
  <li><code>wwcredits</code>: displays how many TextSynth credits you have left.</li>
  <li><code>ping</code>: sends a message to the server with the current latency of the bot.</li>
  <li><code>gen</code>: generates text based on an input prompt using the TextSynth API.</li>
  
</ul>



<h2>Example Generate Usages</h2>
<p>The user types in gen [query] and enters the engine.</p>

<img src="https://user-images.githubusercontent.com/36996267/208317511-906f1b7d-0982-4b73-aedf-e2b41c7b8b02.png" alt="Screenshot of gen e1 command usage">
<img src="https://user-images.githubusercontent.com/36996267/208317798-e4318df6-bde5-41cc-afcd-a136612a52b0.png" alt="Screenshot of gen e3 command usage">

<h2>Additional Features</h2>
<p>Keep track of the number of gen commands used in the server with a summary of each text generation in the shell.</p>
<img src="https://user-images.githubusercontent.com/36996267/208317923-086d5e3c-bd2a-4cbb-8f26-7edb7e42b89f.png" alt="Screenshot of gen command usage summary">
