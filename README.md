Simplified Spotify using FastAPI and AWS
                                                     

# CURRENT ADMIN FEATURES:

• You can add an Artist   
• Create genres  
• Create albums  
• Add songs 

# FEATURES FOR ALL USERS:
• Registration on JWT tokens  
• Adding songs to favorites  
• View your favorite songs  
• Generation of a selection by genre  
• Adding custom playlists  
• Adding songs to your playlists  
• Viewing songs in a playlist  
• Downloading songs  
• The songs are stored on the AWS cloud  

# PIP INSTALL   
• pip install -r requirements.txt  
# Installation
Clone the repo with

• git clone https://github.com/NikitaZhukovsky/Simple-Spotify.git

• In the sync_db, async_db and alembic.ini files, specify your password for the database  

Create .env file inside the root directory and include the following variables

• AWS_ACCESS_KEY_ID=YOUR_KEY_ID  
• AWS_SECRET_ACCESS_KEY=YOUR_ACCESS_KEY  
• BUCKET_NAME=YOUR_BUCKET  
• ENDPOINT_URL=ENDPOINT_URL  
• REGION_NAME=ru-central1

# Alembic
• alembic revision -m "Initial"


Show your support by ⭐️ this project!
