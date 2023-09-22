# <u>STORE MONITORING</u>

A project to create backend APIs that facilitate the monitoring of restaurant online statuses across the United States. The objective is to ensure that restaurants remain online during their operational hours. Occasionally, restaurants may go offline for brief periods due to unknown factors. To address this concern, restaurant owners require a historical report detailing the frequency of such occurrences. Our project aims to fulfill this need by developing a set of backend APIs that empower restaurant owners to obtain this valuable information.

## <u>Assumptions:</u>
* We're assuming that after the data in all three CSVs is entered, it won't be modified. However, during the hourly updates, new data will be added below the old data without changing the already existing data.

## <u>Installation:</u>
1. Clone the repository to your system.
2. Launch a new terminal and type ```bash setup.h```. This will create a virtual environment, activate it, and then install the required packages from the requirements.txt file.
3. Open a new terminal and type ```docker-compose up``` this will launch the container where the postgreql service is available, eliminating the need to install postgresql on your system.
4. Return to the previous terminal and type ```uvicorn main:app --reload```. This will run the fastapi server at port 8000 and allow you to make API calls using any API testing tool such as postman, thunder client, and so on.

## Commands
- uvicorn store_monitoring.main:app --reload
- docker-compose up