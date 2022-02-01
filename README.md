# srl-salt-minion-agent
A sample Salt minion created using the NDK Dev Environment

## How to build an agent based on the NDK Dev Environment in ❼ easy steps

See also [this demo agent](https://github.com/jbemmel/srl-salt-minion-agent/tree/greeter-app-go)

1. Clone the git repo template at https://github.com/jbemmel/srl-salt-minion-agent.git

![image](https://user-images.githubusercontent.com/2031627/151860775-a68854c2-9411-41c8-a148-b1497ca75070.png)

2. Switch to the programming language branch of your choice (Python or Go), e.g. ```git branch python```
3. Initialize the application: ```make APPNAME=your-agent-name```
4. [Python] Update 'requirements.txt' with any application specific Python dependencies like ```salt```
5. Update ```lab/dev.clab.yml``` with any extra images and nodes like ```salt-master```
6. Update the agent's YANG model to include any configuration parameters your agent needs, like ```master```
7. Update the agent's application logic to do whatever it needs to do (like connect to the master)
