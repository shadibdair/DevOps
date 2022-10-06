# 🚧 Dockerize
*Process of packing, deploying, and running application using Docker containe.*

-----
## 👨🏻‍💻 **How it's works :** 

#### To get inside the folder that conatins the script :
- cd "Folder-Name"
#### Run this command to start the container :
- docker-compose up -d

![Screen Shot 2022-09-21 at 10 57 43](https://user-images.githubusercontent.com/43513994/191452599-3b28cd10-3238-4467-9adc-4faa5faf2d80.png)


##### Once It completed, You can go to "http://0.0.0.0:8081/"

<img width="1497" alt="Screen Shot 2022-09-21 at 11 00 23" src="https://user-images.githubusercontent.com/43513994/191456075-fcd2de50-3e43-4de8-ab54-46c3ac84f898.png">

##### And you can start with mongoDB localy

----

## 🐙 **With CLI :**

#### Run this command to start the container :
- docker-compose exec mongodb bash
#### To get inside the MongoDB
- mongo --authenticationDatabase "admin" -u admin -p
#### You can see the users that were added from the script :
- db.getUsers();

![Screen Shot 2022-09-21 at 11 47 17](https://user-images.githubusercontent.com/43513994/191459835-b0232eac-97fc-470b-a648-b74753584023.png)

----

### 🎏 **The Folder Contains :**
```
- docker-compose.yaml
- init.d
    - mongo-init.js
```
------

### 🤖 **Inside this folder :**

##### **There is a script that running inside the container once you "docker-compose up" :**
- **init.d**
    - **mongo-init.js**


💡 *Inside this script you can create the users that you want to be on the mongoDB as default like Users, etc..*


