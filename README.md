set b: 
💻 3. Compile Everything

Open terminal in VS Code:

javac *.java

If you see errors → fix them now, not during viva panic.

🚀 4. Start RMI Registry

This is where most people mess up.

Run:
rmiregistry

💡 If it crashes:

start rmiregistry   (Windows)

OR run in another terminal tab

🖥️ 5. Run Server

In a new terminal:

java Server

You should see:

Server ready...
💻 6. Run Client

Open another terminal:

java Client

Enter strings → boom, result.
