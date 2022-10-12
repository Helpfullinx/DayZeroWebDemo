(*MUST BUILD THE DATABASE FOR LOGIN PAGE TO WORK*)
Instructions to set up MySQL database :

    1. You must have docker installed for the container to install and load mysql

    2. You will need to run the "Docker_Build.sh" script to build the database container
       (If you are on Windows you will need to use WSL or something else to run the bash scripts)

    3. After building the container you will need to run the "Docker_Import.sh" script to load the
       pre-existing database (If the script is ran while the container is running you will need to restart it)
    
    4. If you would like to save the current volume being ran on the database, you will need to run the
       the "Docker_Export_Volume.sh" script and this will save the volume to a tar file in the backup folder