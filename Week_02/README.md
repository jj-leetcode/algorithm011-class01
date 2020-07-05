##### second github account on Mac

###### step 1: 

​			Generate A new ssh key: ~/.ssh/id_rsa_xxx

###### step 2:  (redo needed if you restarted your mac)

​			Add the private-key to ssh-agent by command 

```bash
ssh-add ~/.ssh/id_rsa_xxx
```

​			check the modified ssh-agent

```bash
ssh-add-l
```

​			https://www.dribin.org/dave/blog/archives/2007/11/28/ssh_agent_leopard/

###### step 3:

​			change your github identity(user name, user email)

```bash
git config --local user.name "xxx"
git config --local user.email "xxx"
```

###### step 4:

​			push your code with specific ssh-key

```bash
GIT_SSH_COMMAND="ssh -i 'path to you ssh key'" git push
```



god job !!