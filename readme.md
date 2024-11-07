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

#### (Manually, just one instance)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/softserve-academy.git
   cd softserve-academy
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
    pip install -r requirements.txt
    ```

4. **Run the Django migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    Open your web browser and go to `http://localhost:8000/`

#### Dockerized version

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
    curl -L -o docker-compose.yml https://github.com/QuitoTactico/SoftServe-Academy/raw/main/scripts/docker-compose.yml
    ```

3. **Run the Docker Compose:**
    ```bash
    sudo docker compose up -d --pull always
    ```

And that's it! You can now access the application opening your web browser and going to `http://localhost/`, this runs on the port 80 by default.

## Contributors

| Name                      | Email                   | Role                   |
|---------------------------|-------------------------|------------------------|
| Esteban Vergara Giraldo   | evergarag@eafit.edu.co  | Developer, Architect   |
| Miguel Ángel Cock Cano    | macockc@eafit.edu.co    | Tester                 |
| Jonathan Betancur Espinosa| jbetancur3@eafit.edu.co | Developer              |
| Moises David Arrieta Hernandez | mdarrietah@eafit.edu.co | Analyst           |
| Pablo Baez Santamaria     | pbaezs@eafit.edu.co     | UX/UI, Scrum Master    |


