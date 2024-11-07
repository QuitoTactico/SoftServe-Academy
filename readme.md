# SoftServe Academy

SoftServe Academy is a collaborative platform designed to create, evaluate, curate, organize, and share personalized learning paths tailored for the technology industry. In an era where continuous and autonomous learning is crucial, this platform bridges the gap by offering structured, curated, and user-specific educational resources that go beyond simple lists of links. By leveraging advanced algorithms, the platform generates customized learning paths based on individual users' knowledge, learning goals, time availability, and content preferences.

## Key Users
- Software Developers
- Programmers
- Technology Students
- Professors
- Mentors
- Content Curators

Users can explore personalized learning paths, consume high-quality content, and track their progress, while content curators ensure the relevance and quality of the educational materials. The platform is built using modern technologies such as a Python-based backend with Django and an intuitive UI using Django Template Language (DTL).

## Scope
The proposed system is a collaborative learning platform aimed at the creation, evaluation, curation, organization, and dissemination of learning paths in the technology sector. The system will allow users to access external educational resources, organize these resources into personalized learning paths, and assess their progress through interactive activities.

### Features Included in the Scope:
- **Creation of Learning Paths**: Users will be able to create personalized learning paths that integrate external content, such as videos and tutorials, through links or embedded content.
- **Content Curation**: Teachers, mentors, and content curators will be able to select, evaluate, and organize external educational resources, ensuring their relevance and quality.
- **Progress Evaluation**: Users will be able to perform interactive assessments to measure their understanding of the material and receive feedback based on their performance.
- **Recommendation Generation**: The platform will generate learning path recommendations based on the user's profile, preferences, and progress.
- **Intuitive User Interface**: The system will feature a user-friendly interface, developed with Django Template Language (DTL), allowing for easy navigation and use.

### System Boundaries:
- **Dependence on External Content**: The system will not host proprietary content but will rely entirely on links to tutorials, videos, and other external educational resources.
- **No Certification Integration**: External evaluation and certification platforms will not be included; however, their integration may be considered in future versions.

### Minimum Viable Product (MVP):
The MVP will include the basic functionalities necessary to allow users to create and follow personalized learning paths, curate and organize external content, and assess their progress through interactive activities. This first release will validate the system's viability and gather user feedback for future iterations.

## How to Run the Project

### Prerequisites
- Python 3.12.x
- SQLite (default database for Django)

### Installation

### Manually, just one instance

1. ** Download git and python:**
    ```bash
    sudo apt-get update
    sudo apt-get install -y git python3 python3-pip
    ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/softserve-academy.git
   cd softserve-academy
   ```

3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. **Install the dependencies:**
   ```bash
    pip install -r requirements.txt
    ```

5. **Run the Django migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

And that's it. Open your web browser and go to `http://localhost:8000/` if you have it locally, or `http://<instance-ip>:8000/` if you have it on a remote server.

### Dockerized, just one instance

1. **Install Docker and Docker Compose:**
    ```bash
    sudo apt-get update 
    sudo apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common 
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add - 
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian buster stable" 
    sudo apt-get update 
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io
    sudo apt update
    sudo apt install -y docker-compose-plugin
    ```

2. **Copy the docker-compose.yml on your PC:**
    ```bash
    curl -L -o docker-compose.yml https://github.com/QuitoTactico/SoftServe-Academy/raw/main/docker-compose.yml
    ```

3. **Run the Docker Compose:**
    ```bash
    sudo docker compose up -d --pull always
    ```

4. **Extra:**  
    You can check the status of the containers with:  
    ```bash
    sudo docker container ls
    ```  
    Check the logs with:  
    ```bash
    sudo docker container logs softserve_web_1
    sudo docker container logs softserve_db_1
    ```  
    And shut down the containers with:  
    ```bash
    sudo docker compose down
    ```

And that's it! You can now access the application opening your web browser and going to `http://localhost`, or `http://<instance-ip>` if you have it externally. This runs on the port 80 by default.

This creates `a container with the Django application` and another `container with the database (MySQL)`, but with the same migrations and data as the beta SQlite uploaded in this repository.

#### Dockerized, multiple instances with multiple django containers

1. **Install Docker and Docker Compose:**
    ```bash
    sudo apt-get update 
    sudo apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common 
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add - 
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian buster stable" 
    sudo apt-get update 
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io
    sudo apt update
    sudo apt install -y docker-compose-plugin
    ```

2. **Copy the docker-compose.yml on your PC:**
    ```bash
    curl -L -o docker-compose.yml https://github.com/QuitoTactico/SoftServe-Academy/raw/main/docker-compose.yml
    ```

3. **Run the Docker Swarm:**  
    The instance where you run this, will be the manager. It needs to have a public IP.
    ```bash
    sudo docker swarm init
    ```

4. **Copy the generated token and run the command on the worker instances:**  
    (Download docker for them too)
    ```bash
    sudo docker swarm join --token <token> <manager-ip>:2377
    ```

5. **Deploy the stack in the manager:**
    ```bash
    sudo docker stack deploy -c docker-compose-swarm.yml softserve
    ```

6. **Extra:**  
    You can check the status of the deployment with:  
    ```bash
    sudo docker node ls
    sudo docker service ls
    sudo docker service ps web
    sudo docker service ps db
    sudo docker container ls
    ```  
    Check the logs with:  
    ```bash
    sudo docker service logs web
    sudo docker service logs db
    ```
    And shut down the stack with:  
    ```bash
    sudo docker stack rm softserve
    ```
    And leave the swarm with:  
    ```bash
    sudo docker swarm leave --force
    ```

You can access the application opening your web browser and going to `http://<manager-ip>/`, this runs on the port 80 by default.

This will create a service with `5 replicas of the Django container`, and a service with `1 replica of the database container (MySQL)`.

## Contributors

| Name                      | Email                   | Role                   |
|---------------------------|-------------------------|------------------------|
| Esteban Vergara Giraldo   | evergarag@eafit.edu.co  | Developer, Architect   |
| Miguel Ángel Cock Cano    | macockc@eafit.edu.co    | Tester                 |
| Jonathan Betancur Espinosa| jbetancur3@eafit.edu.co | Developer              |
| Moises David Arrieta Hernandez | mdarrietah@eafit.edu.co | Analyst           |
| Pablo Baez Santamaria     | pbaezs@eafit.edu.co     | UX/UI, Scrum Master    |


