docker stop tsanalyst
docker rm tsanalyst
docker run -it --name tsanalyst -v $HOME/project/tsdata_analyst:/opt -p 5000:5000 py123 bash
