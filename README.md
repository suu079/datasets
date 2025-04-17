The BirdWatching app requires the setup of three containers:

1. A vector database container 
2. A Python container for the API services
3. A web server container for the frontend

**Prerequisites**

A prerequisite is the installation of Docker. 

Each container will run in isolation but communicate with each other to create the complete BirdWatching application.

**Clone GitHub Repository**

Clone or download the github repository. 

**Create a Local Secrets Folder**

The secrets file is managed outside of GitHub since secure information should be maintained outside of GitHub. 

At the same level as the E115-BirdWatchingApp-Internal folder create a folder called secrets where you will add your service account. 

Your folder structure should look like this:
```
 |-E115-BirdWatchingApp-Internal
     |-images
     |-notebooks
     |-references
     |-reports
     |-src
       |---api-service
       |---frontend-react
       |---vector-db
  |-secrets
```
  
**Setup GCP Service Account**

1. To setup a service account you will need to go to GCP Console, search for "Service accounts" from the top search box or go to: "IAM & Admins" > "Service accounts" from the top-left menu and create a new service account called "ml-workflow". For "Service account permissions" select "Storage Admin", "AI Platform Admin", "Vertex AI Administrator", "Service Account User"
2. This will create a service account
3. On the right "Actions" column click the vertical ... and select "Manage keys". A prompt for Create private key for "ml-workflow" will appear select "JSON" and click create. This will download a Private key json file to your computer. Copy this json file into the secrets folder. Rename the json file to ml-workflow.json

**Vector DB Container**

We will set up and initialize our vector database with bird-related content for Retrieval Augmented Generation (RAG).

Set up the Vector Database:

1. Navigate to the vector-db directory:
   
cd E115—BirdWatchingApp—Internal/src/vector-db

2. Build and run the container:
   
sh docker-shell.sh

3. Initialize the database. Run this within the docker shell:
   
python cli.py --download --load --chunk_type recursive-split

This process will:

- Download the bird knowledge base (chunks + embeddings)
- Load everything into the vector database 

This step is crucial for enabling the bird assistant to provide accurate, knowledge-based responses.

Keep this container running while setting up the backend API service and frontend apps.

**API-Service Container** 

We create a container running a FastAPI-based REST API service.

Setup API-Service:

1. Navigate to API Service Directory
   
cd E115—BirdWatchingApp—Internal/src/api-service

2. Build & Run Container
   
sh docker-shell.sh

3. Review Container Configuration
   
-	Check docker-shell.sh:
-	Port mapping: -p 9000:9000
-	Development mode: -e DEV=1
-	Check docker-entrypoint.sh: Dev vs. Production settings

4. Start the API Service
   
- Run the following command within the docker shell:

uvicorn_server

- Verify the service is running at http://localhost:9000

- Enable API Routes

- Enable All Routes in api/service.py

**Additional routers here**

app.include_router(newsletter.router, prefix="/newsletters")
app.include_router(podcast.router, prefix="/podcasts")
app.include_router(llm_chat.router, prefix="/llm")
app.include_router(llm_cnn_chat.router, prefix="/llm-cnn")
app.include_router(llm_rag_chat.router, prefix="/llm-rag")
app.include_router(llm_agent_chat.router, prefix="/llm-agent")

•	Go to http://localhost:9000/docs and test the newsletters routes
 
**View API Docs**

Fast API gives interactive API documentation and an exploration tool for free.

- Go to http://localhost:9000/docs
- You can test APIs from this tool
 
Keep this container running while setting up the backend API service and frontend apps.

**React Frontend Container**

Setup React Frontend Container:

1. Navigate to the React frontend directory:
   
cd E115—BirdWatchingApp—Internal/src/frontend-react

2. Start the development container:
   
sh docker-shell.sh

3. First time only: Install the required Node packages

npm install

4. Launch Development Server

- Start the development server:
   
npm run dev

- View the app at: http://localhost:3000
   
Note: Make sure the API service container is running for full functionality

**Docker Cleanup**

Make sure you do not have any running containers and clear up an unused images. Complete the following steps: 

1. Run

docker container ls

2. Stop any container that is running

3. Run

docker system prune

4. Run

docker image ls
